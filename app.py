import streamlit as st
from utils import NewsAnalyzer

st.title("Company News Sentiment Analyzer")

# Initialize analyzer
analyzer = NewsAnalyzer()

# User input
company_name = st.text_input("Enter company name:", "Tesla")

if st.button("Analyze News"):
    with st.spinner("Analyzing news articles..."):
        analysis_results = analyzer.analyze_company_news(company_name)
        
    if "error" in analysis_results:
        st.error(f"{analysis_results['error']} - Company: {analysis_results['Company']}")
    else:
        st.success(f"Analysis complete for {analysis_results['Company']}")
        
        # Display articles
        st.subheader("Analyzed Articles")
        for idx, article in enumerate(analysis_results["Articles"], 1):
            with st.expander(f"Article {idx}: {article['Title']}"):
                col1, col2 = st.columns(2)
                with col1:
                    st.markdown(f"**Summary**: {article['Summary']}")
                with col2:
                    st.markdown(f"**Sentiment**: {article['Sentiment']}")
                    st.markdown(f"**Key Topics**: {', '.join(article['Topics'])}")
        
        # Display comparative analysis
        st.subheader("Comparative Analysis")
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### Sentiment Distribution")
            sentiment_data = analysis_results["Comparative Sentiment Score"]["Sentiment Distribution"]
            st.bar_chart(sentiment_data)
            
        with col2:
            st.markdown("### Topic Overlap")
            topic_data = analysis_results["Comparative Sentiment Score"]["Topic Overlap"]
            st.write("**Common Topics:**", ", ".join(topic_data["Common Topics"]))
            for article, topics in topic_data["Unique Topics"].items():
                st.write(f"**{article}:**", ", ".join(topics))
        
        # Display final analysis
        st.subheader("Final Sentiment Analysis")
        st.write(analysis_results["Final Sentiment Analysis"])
        
        # Audio output
        st.markdown("### Hindi Audio Summary")
        st.audio(analysis_results["Audio"])