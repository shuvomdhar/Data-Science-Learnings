from dotenv import load_dotenv

load_dotenv()

# ChatGPT
from langchain.chat_models import init_chat_model
from langchain_openai import ChatOpenAI

# model_openai = init_chat_model("gpt-4.1")
# model_openai = ChatOpenAI("gpt-4.1")

# print(model_openai)

# response_openai = model_openai.invoke("Why do parrots talk?")

# print(response_openai)



# Gemini
from langchain.chat_models import init_chat_model

model_gemini = init_chat_model("google_genai:gemini-2.5-flash")
# print("model_gemini:\n", model_gemini)

print("\n")

response_gemini = model_gemini.invoke("Write a paragraph upon machine learning")
print("response_gemini: \n", response_gemini.content)



# Groq
from langchain_mistralai import ChatGroq

model_groq = ChatGroq(model = "openai/gpt-oss-120b")

response_groq = model_groq.invoke("write a poem on AI")

print(response_groq.content)



# Mistral
from langchain_mistralai import ChatMistralAI

model_mistral = ChatMistralAI(model = "mistral-small-2506",temperature=0.9)

response_mistral = model_mistral.invoke("write a poem on AI")

print(response_mistral.content)