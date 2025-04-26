import streamlit as st
from agents.ta_agent import TechnicalAnalysisAgent
from agents.news_agent import NewsSentimentAgent
import time

# Config
st.set_page_config(page_title="CryptoGecko 🦎", layout="wide")

# Initialize agents
@st.cache_resource
def load_agents():
    return {
        'ta': TechnicalAnalysisAgent(),
        'news': NewsSentimentAgent()
    }

agents = load_agents()

# Your existing app code here...
# [PASTE THE FULL APP CODE FROM OUR PREVIOUS CHATS]