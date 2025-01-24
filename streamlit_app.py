import streamlit as st
import requests

def fetch_trends(keyword, timeframe='now 1-H', geo=''):
    url = f"https://your-flask-api-endpoint.com/trends?keyword={keyword}&timeframe={timeframe}&geo={geo}"
    try:
        response = requests.get(url)
        return response.json()
    except Exception as e:
        st.error(f"Error fetching trends: {e}")
        return None

def main():
    st.title('Google Trends Visualizer')
    
    keyword = st.text_input('Enter Keyword')
    timeframe = st.selectbox('Timeframe', ['now 1-H', 'now 1-d', 'now 7-d'])

    if st.button('Fetch Trends'):
        if keyword:
            trends = fetch_trends(keyword, timeframe)
            if trends:
                st.json(trends)
        else:
            st.warning('Please enter a keyword')

if __name__ == '__main__':
    main()