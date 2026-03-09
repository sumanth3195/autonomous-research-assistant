# import os
# from dotenv import load_dotenv
# from langchain_groq import ChatGroq

# load_dotenv()
# groq_api_key = os.getenv("GROQ_API_KEY")

# print(groq_api_key)






# llm = ChatGroq(
#     groq_api_key=os.getenv("GROQ_API_KEY"),
#     model_name="llama3-70b-8192",
#     temperature=0
# )

# #response = llm.invoke("Explain what RAG system is in simple terms.")

# #print(response.content)












import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()
# groq_api_key=os.getenv("GROQ_API_KEY")

llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama-3.1-8b-instant",
    temperature=0
)

response = llm.invoke("Explain what RAG system is in simple terms.")

print(response.content)
# print(groq_api_key)