from langchain_ollama import ChatOllama
import os
from dotenv import load_dotenv

load_dotenv()

# llama3.2 (With Tools)
llama3_2_tools=ChatOllama(
  model=os.getenv("OLLAMA_MODEL_1"),
  temperature=0.7,
  base_url=os.getenv("OLLAMA_LOCAL_URL")
)