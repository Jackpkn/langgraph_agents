from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()
from langchain_google_genai import GoogleGenerativeAI
model=ChatOpenAI(model="gpt-4",temperature=1) # temperature is a parameter that controls the randomness of a language model's output. it affects how creative or deterministic the responses are
# lower value (0.0 - 0.3 ) - more deterministic and predictable
# Higher values (0.7 - 1.5) - more random creative, and diverse
result = model.invoke("what is the capital of india")

print(result.content)