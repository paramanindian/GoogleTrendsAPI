from flask import Flask, request, jsonify
from pytrends.request import TrendReq
import pandas as pd
import os

app = Flask(__name__)
pytrends = TrendReq(hl='en-US', tz=360)


@app.route('/google-trends', methods=['POST'])
def run_get_trends():
    try:
        data = request.get_json()  # This will read the JSON body of the request
        print(f"Received data: {data}")  # Log the data to verify it's coming through
        # Start the long-running task in a separate thread
        trending_searches = pytrends.trending_searches(pn='united_states')
        dl1 = trending_searches[0].to_list()

        # Immediately respond with a message
        return jsonify({
            'message': dl1
        }), 200
    except subprocess.CalledProcessError as e:
        return f"Error executing Python script: {str(e)}", 500


@app.route('/trends', methods=['GET'])
def get_trends():
    try:
        keyword = request.args.get('keyword', '')
        timeframe = request.args.get('timeframe', 'now 1-H')
        geo = request.args.get('geo', '')

        if not keyword:
            return jsonify({"error": "Keyword is required"}), 400

        pytrends.build_payload([keyword], timeframe=timeframe, geo=geo)
        trend_df = pytrends.interest_over_time()
        trend_data = trend_df.to_dict(orient='records')
        
        return jsonify({
            "keyword": keyword,
            "timeframe": timeframe,
            "geo": geo,
            "data": trend_data
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)