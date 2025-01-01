# Integrating our code with OpenAI API

# Importing necessary libraries
import os
from constants import openai_key
from langchain.llms import OpenAI

import streamlit as st

os.environ["OPENAI_API_KEY"] = openai_key

# Initializing Streamlit framework
st.title('LangChain Demo with OpenAI API')

# Taking input into the streamlit application
input_text = st.text_input("Seach the topic you want")

# OpenAI LLMs
llm = OpenAI(temperature = 0.8) # Temperature [Value varies from 0 to 1] : How much control the ganet will have when responding (giving out response to us)


if input_text:
    st.write(llm(input_text)) # Output (LLM response) will be shown in Streamlit Application