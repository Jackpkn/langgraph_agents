import os
from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv;

load_dotenv()

llm = GoogleGenerativeAI(model='gemini-2.0-flash')

result = llm.invoke("what is the the capital of india")
print(result)