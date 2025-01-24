import streamlit as st
import requests
import os

base_url = os.environ.get('FLASK_API_ENDPOINT', 'default_fallback_url')

def fetch_trends(keyword, timeframe='now 1-H', geo=''):
    url = f"https://your-flask-api-endpoint.com/trends?keyword={keyword}&timeframe={timeframe}&geo={geo}"
    response = requests.get(url)
    return response.json()

def main():
    st.title('Google Trends Visualizer')
    
    keyword = st.text_input('Enter Keyword')
    timeframe = st.selectbox('Timeframe', ['now 1-H', 'now 1-d', 'now 7-d'])
    st.write(base_url)
    if st.button('Fetch Trends'):
        if keyword:
            try:
                trends = fetch_trends(keyword, timeframe)
                st.json(trends)
            except Exception as e:
                st.error(f"Error: {e}")
        else:
            st.warning('Please enter a keyword')

if __name__ == '__main__':
    main()