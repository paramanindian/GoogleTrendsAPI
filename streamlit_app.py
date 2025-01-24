import streamlit_app as st
import requests

def fetch_trends(keyword, timeframe='now 1-H', geo=''):
    url = f"https://your-flask-api.com/trends?keyword={keyword}&timeframe={timeframe}&geo={geo}"
    response = requests.get(url)
    return response.json()

st.title('Google Trends Visualizer')

keyword = st.text_input('Enter Keyword')
timeframe = st.selectbox('Timeframe', ['now 1-H', 'now 1-d', 'now 7-d'])

if st.button('Fetch Trends'):
    trends = fetch_trends(keyword, timeframe)
    st.json(trends)