import streamlit as st
import requests

def fetch_trends(keyword, timeframe='now 1-H', geo=''):
    # Use localhost for local development
    url = f"http://localhost:5000/trends?keyword={keyword}&timeframe={timeframe}&geo={geo}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise exception for bad responses
        
        # Print raw response for debugging
        st.write("Raw Response:", response.text)
        
        return response.json()
    except requests.RequestException as e:
        st.error(f"Request Error: {e}")
        return None
    except ValueError as e:
        st.error(f"JSON Decode Error: {e}")
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