from .nkanyezi_tools import nkanyezi_toolkit
from src.config.llm_config import llama3_2_tools


# Primary agent established
nkanyezi_engine=llama3_2_tools.bind_tools(nkanyezi_toolkit)
