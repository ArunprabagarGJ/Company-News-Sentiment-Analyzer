# Company-News-Sentiment-Analyzer

## Objective
This project is a web-based application that extracts key details from multiple news articles related to a given company, performs sentiment analysis, conducts a comparative analysis, and generates a text-to-speech (TTS) output in Hindi. 

## Features
- **News Extraction**: Extracts and displays title, summary, and metadata from at least 10 unique news articles.
- **Sentiment Analysis**: Categorizes news articles as Positive, Negative, or Neutral.
- **Comparative Analysis**: Provides insights into how the company's news coverage varies.
- **Text-to-Speech (TTS)**: Converts summarized content into Hindi speech.
- **User Interface**: Simple web-based interface using Streamlit or Gradio.
- **API Development**: Frontend and backend communicate via APIs.
- **Deployment**: The application is deployed on Hugging Face Spaces.

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/ArunprabagarGJ/Company-News-Sentiment-Analyzer.git
   cd Company-News-Sentiment-Analyzer
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Run the application:
   ```sh
   python -m streamlit run app.py
   ```

## File Structure
```
📂 news-summarization-tts
├── 📄 app.py            # Main script for running the application
├── 📄 api.py            # API endpoints for handling requests
├── 📄 utils.py          # Utility functions for scraping and processing data
├── 📄 requirements.txt  # Dependencies
├── 📄 README.md         # Project documentation
```

## API Endpoints
- `GET /news?company={company_name}`: Fetches news articles for a given company.
- `POST /sentiment-analysis`: Performs sentiment analysis on extracted news.
- `POST /tts`: Generates Hindi text-to-speech output from the summary.

## Example Output
```json
{
    "Company": "Tesla",
    "Articles": [
        {
            "Title": "Tesla's New Model Breaks Sales Records",
            "Summary": "Tesla's latest EV sees record sales in Q3...",
            "Sentiment": "Positive",
            "Topics": ["Electric Vehicles", "Stock Market", "Innovation"]
        }
    ],
    "Final Sentiment Analysis": "Tesla’s latest news coverage is mostly positive.",
    "Audio": "[Play Hindi Speech]"
}
```

## Deployment
The application is deployed on Hugging Face Spaces.

## Assumptions & Limitations
- Only non-JavaScript-based websites are considered for scraping.
- The model used for sentiment analysis may have limitations in detecting nuances.
- The TTS model may not support all Hindi pronunciations perfectly.

## License
This project is licensed under the MIT License. Feel free to use and modify it as needed.

## Contributors
- Arunprabagar Ganesan
