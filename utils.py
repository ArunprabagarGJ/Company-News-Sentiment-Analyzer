import requests
from bs4 import BeautifulSoup
from transformers import pipeline
from gtts import gTTS
import os
import tempfile
import hashlib

class NewsAnalyzer:
    def __init__(self):
        self.sentiment_analyzer = pipeline("sentiment-analysis")
        self.summarizer = pipeline("summarization")

    def search_news_articles(self, company_name):
        if company_name.lower() == "tesla":
            return [
                {
                    "url": "https://example.com/article1",
                    "title": "Tesla's New Model Breaks Sales Records",
                    "content": "Tesla's latest EV sees record sales in Q3. The company reported a 30% increase in deliveries compared to the previous quarter. Analysts are optimistic about Tesla's market position."
                },
                {
                    "url": "https://example.com/article2",
                    "title": "Regulatory Scrutiny on Tesla's Self-Driving Tech",
                    "content": "Regulators have raised concerns over Tesla’s self-driving software. The National Highway Traffic Safety Administration is investigating several incidents involving Tesla vehicles in autonomous mode."
                }
            ]
        return []

    def extract_article_metadata(self, article_url):
        try:
            response = requests.get(article_url)
            soup = BeautifulSoup(response.content, 'html.parser')
            return {
                "title": soup.find('title').get_text(),
                "date": soup.find('meta', attrs={'property': 'article:published_time'})['content'] if soup.find('meta', attrs={'property': 'article:published_time'}) else "N/A",
                "author": soup.find('meta', attrs={'name': 'author'})['content'] if soup.find('meta', attrs={'name': 'author'}) else "N/A"
            }
        except Exception as e:
            print(f"Metadata extraction error: {str(e)}")
            return {"title": "N/A", "date": "N/A", "author": "N/A"}

    def analyze_sentiment(self, text):
        return self.sentiment_analyzer(text[:512])[0]["label"]

    def summarize_text(self, text):
        return self.summarizer(text[:1024], max_length=100, min_length=30, do_sample=False)[0]['summary_text']

    def extract_topics(self, text):
        keywords = ["Electric Vehicles", "Stock Market", "Innovation", "Regulations", 
                   "Autonomous Vehicles", "Self-Driving", "Sales", "Revenue"]
        return list({kw for kw in keywords if kw.lower() in text.lower()})

    def generate_comparative_analysis(self, articles):
        sentiment_distribution = {"Positive": 0, "Negative": 0, "Neutral": 0}
        for article in articles:
            sentiment = article["Sentiment"].capitalize()
            sentiment_distribution[sentiment] = sentiment_distribution.get(sentiment, 0) + 1

        topic_overlap = {
            "Common Topics": list(set.intersection(*[set(a["Topics"]) for a in articles])),
            "Unique Topics": {f"Article {i+1}": art["Topics"] for i, art in enumerate(articles)}
        }

        return {
            "Sentiment Distribution": sentiment_distribution,
            "Coverage Differences": [],
            "Topic Overlap": topic_overlap
        }

    def generate_final_analysis(self, sentiment_distribution):
        total = sum(sentiment_distribution.values())
        if total == 0: return "No analyzable sentiment data."
        
        positive = sentiment_distribution.get("Positive", 0)/total * 100
        negative = sentiment_distribution.get("Negative", 0)/total * 100
        
        if positive > 60: return "Predominantly positive news coverage indicating strong performance."
        elif negative > 60: return "Mostly negative coverage suggesting potential challenges."
        return "Mixed sentiment coverage with both positive and negative aspects."

    def text_to_speech_hindi(self, text):
        tts = gTTS(text=text, lang='hi')
        fp = os.path.join(tempfile.gettempdir(), f"tts_{hashlib.md5(text.encode()).hexdigest()}.mp3")
        tts.save(fp)
        return fp

    def analyze_company_news(self, company_name):
        articles = self.search_news_articles(company_name)
        if not articles:
            return {"error": "No articles found", "Company": company_name}
        
        analyzed_articles = []
        for article in articles:
            metadata = self.extract_article_metadata(article["url"])
            analyzed_articles.append({
                "Title": metadata["title"],
                "Summary": self.summarize_text(article["content"]),
                "Sentiment": self.analyze_sentiment(article["content"]),
                "Topics": self.extract_topics(article["content"])
            })
        
        return {
            "Company": company_name,
            "Articles": analyzed_articles,
            "Comparative Sentiment Score": self.generate_comparative_analysis(analyzed_articles),
            "Final Sentiment Analysis": self.generate_final_analysis(
                self.generate_comparative_analysis(analyzed_articles)["Sentiment Distribution"]
            ),
            "Audio": self.text_to_speech_hindi("कंपनी की समाचार रिपोर्ट विभिन्न प्रतिक्रियाओं के साथ आई है।")
        }