import streamlit as st
from agents.ta_agent import TechnicalAnalysisAgent
from agents.news_agent import NewsSentimentAgent
import time

# Initialize agents (with error handling)
@st.cache_resource
def init_agents():
    try:
        return {
            'ta': TechnicalAnalysisAgent(),
            'news': NewsSentimentAgent()
        }
    except Exception as e:
        st.error(f"Agent initialization failed: {str(e)}")
        return None

# Main app function
def main():
    st.set_page_config(
        page_title="CryptoGecko 🦎",
        page_icon="🦎",
        layout="wide"
    )
    
    st.title("🦎 CryptoGecko Dashboard")
    
    agents = init_agents()
    if not agents:
        return
    
    # Coin selector
    coin = st.selectbox(
        "Select Cryptocurrency", 
        ["BTC", "ETH", "SOL", "BNB", "XRP"],
        index=0
    )
    
    # Display data
    with st.spinner("Fetching data..."):
        try:
            ta_data = agents['ta'].analyze(coin)
            news_data = agents['news'].analyze(coin)
            
            st.subheader(f"{coin} Technical Indicators")
            st.json(ta_data)  # Replace with your visualization
            
            st.subheader("News Sentiment")
            st.json(news_data)  # Replace with your visualization
            
        except Exception as e:
            st.error(f"Data fetch failed: {str(e)}")

if __name__ == "__main__":
    main()