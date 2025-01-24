from flask import Flask, request, jsonify
from pytrends.request import TrendReq
import pandas as pd
import os

app = Flask(__name__)
pytrends = TrendReq(hl='en-US', tz=360)

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