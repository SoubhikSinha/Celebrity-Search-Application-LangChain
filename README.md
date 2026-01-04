# Celebrity Search (Results) Application - LangChain

About the Project
---
This is a basic LangChain project that helped me understand how to use LLM (Large Language Model) responses to create my own applications, thanks to LangChain tools. The web application is built using Streamlit. It takes the input of a celebrity's name and provides information about them, including their date of birth (DOB) and five major events that occurred around the world on that date. Additionally, the web application attempts to memorize the responses.

<br>
<br>

How to Run the Project ?
---
 ### **1. Clone the Repository**
Clone the repository to your local machine :<br>
```bash
git clone https://github.com/SoubhikSinha/Celebrity-Search-Application-LangChain.git
```

### **2. Create a Virtual Environment**
Navigate to the repository's root directory and create a Conda virtual environment :<br>
```bash
conda create --prefix ./venv python==3.11 -y
```

### **3. Activate the Conda Environment**
Activate the newly created environment :<br>
```bash
conda activate venv/
```

### **4. Install Required Libraries**
Install all the necessary dependencies :<br>
```bash
pip install -r requirements.txt
```

### **5. Create OpenAI API Secret Key**
To use the LLMs provided by OpenAI, you need a secret API key. You can generate one by visiting this link ▶️ [https://platform.openai.com/api-keys](https://platform.openai.com/api-keys)
<br>

After generating the secret key, copy and paste it into the `constants.py` file (a variable has already been declared for this purpose) and save the file.

### **6. Run the Project**
Run the Streamlit command below to open the web application :<br>
```bash
streamlit run example1.py
```
<br>
<br>

## References
[Krish Naik](https://github.com/krishnaik06)
