# Integrating our code with OpenAI API

# Importing necessary libraries
import os
from constants import openai_key
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate # For Custom-Prompts
from langchain.chains import LLMChain # LLMChain is responsible to execute the Prompt Template(s)

from langchain.chains import SimpleSequentialChain
from langchain.chains import SequentialChain

# For memorizing the converstation🔻
from langchain.memory import ConversationBufferMemory

import streamlit as st

os.environ["OPENAI_API_KEY"] = openai_key

# Initializing Streamlit framework
st.title('Celebrity Search Application')

# Taking input into the streamlit application
input_text = st.text_input("Search about the celebrity you want")

# Prompt Template #1
first_input_prompt = PromptTemplate(
    input_variables = ['name'],
    template = "Tell me about the celebrity : {name}"
)

# Temperature [Value varies from 0 to 1]🔽
# How much control the agent will have when responding (when giving out response to us)

# "verbose" means generating a very detailed and expansive response, often 
# including extra information or explanations beyond what is strictly necessary 
# to answer a question, essentially providing a more "talkative" output.

# Memory
person_memory = ConversationBufferMemory(input_key = 'name', memory_key = 'chat_history')
dob_memory = ConversationBufferMemory(input_key = 'person', memory_key = 'chat_history')
descr_memory = ConversationBufferMemory(input_key = 'dob', memory_key = 'description_history')

# OpenAI LLMs
llm = OpenAI(temperature = 0.8)

chain = LLMChain(llm = llm, 
                 prompt = first_input_prompt, 
                 verbose = True, 
                 output_key = 'person', # 'person' will be passed to next Prompt Template
                 memory = person_memory) # Memorizing the output generated for Prompt Template #1

# Prompt Template #2
second_input_prompt = PromptTemplate(
    input_variables = ['person'],
    template = "When was {person} born ?"
)

# If using multiple Prompt Templates - the logic can be like this way 🔽
# We got some output from first Prompt Template via LLM, then we can pass on
# the response to the next Prompt template(s) - and it may keep on going

# For the second template too, you need to make another chain
chain2 = LLMChain(llm = llm, 
                  prompt = second_input_prompt, 
                  verbose = True, 
                  output_key = 'dob', # 'dob' will be obtained as the core-output (which may be passed on)
                  memory = dob_memory) # Memorizing the output generated for Prompt Template #2

# Prompt Template #3
third_input_prompt = PromptTemplate(
    input_variables = ['dob'],
    template = "Mention 5 major events that happened around {dob} in the world ?"
)

# Chain for 3rd Prompt Template
chain3 = LLMChain(llm = llm, 
                  prompt = third_input_prompt, 
                  verbose = True, 
                  output_key = 'description',
                  memory = descr_memory) # Memorizing the output generated for Prompt Template #3


# When having multiple Prompt Templates, we can either get outputs parallely from each of them,
# OR we can sequentially arrange them to get a sequential response.
parent_chain = SimpleSequentialChain(chains = [chain, chain2], verbose = True) # Sequence of 'Chains'

# When using 'SimpleSequentialChain' - it will only show the last chain's response
# SOLUTION : Use 'SequentialChain' (All in the form of JSON)
parent_chain_2 = SequentialChain(
    chains = [chain, chain2], 
    input_variables = ['name'],
    output_variables = ['person', 'dob'],
    verbose = True)

# Another parent chain
parent_chain_3 = SequentialChain(
    chains = [chain, chain2, chain3], 
    input_variables = ['name'],
    output_variables = ['person', 'dob', 'description'],
    verbose = True)

if input_text:
    # st.write(llm(input_text)) # Output (LLM response) will be shown in Streamlit Application
    # st.write(chain.run(input_text)) # Specific output from LLMCHain for the defined Prompt Template
    # st.write(parent_chain(input_text)) # Sequential Chains response
    # st.write(parent_chain_2({'name' : input_text})) # To get response (combined) from both the chains (1+2) (SequentialChain)
    st.write(parent_chain_3({'name' : input_text})) # For chains (1+2+3)

    # Memory (from all the chains) can be written somewhere
    with st.expander('Person Name'):
        st.info(person_memory.buffer)

    with st.expander('Major Events'):
        st.info(descr_memory.buffer)