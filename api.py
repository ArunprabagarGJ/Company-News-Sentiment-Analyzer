from flask import Flask, request, jsonify
from utils import NewsAnalyzer  # Corrected import
from flask_cors import CORS  # Add CORS support if needed

app = Flask(__name__)
CORS(app)  # Enable CORS if consuming from web frontend
analyzer = NewsAnalyzer()

@app.route('/analyze', methods=['POST'])
def analyze_news():
    # Get and validate input
    data = request.get_json()
    if not data or 'company_name' not in data:
        return jsonify({
            "error": "Missing required parameter: company_name",
            "status": 400
        }), 400

    # Process request
    company_name = data['company_name']
    result = analyzer.analyze_company_news(company_name)

    # Handle error cases
    if 'error' in result:
        return jsonify({
            "error": result['error'],
            "company": result.get('Company', company_name),
            "status": 404
        }), 404

    # Return successful response
    return jsonify({
        "company": result['Company'],
        "analysis": {
            "articles": result['Articles'],
            "sentiment_distribution": result['Comparative Sentiment Score']['Sentiment Distribution'],
            "topic_analysis": result['Comparative Sentiment Score']['Topic Overlap'],
            "final_summary": result['Final Sentiment Analysis']
        },
        "status": 200
    }), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)