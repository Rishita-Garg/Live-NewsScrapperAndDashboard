import streamlit as st
import requests
from bs4 import BeautifulSoup
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import re

st.set_page_config(page_title="Live News Dashboard", layout="wide")
st.title("📰 Live News Scraper Dashboard")

# Sidebar input
st.sidebar.header("Scrape Settings")
url = st.sidebar.text_input("Enter a news website URL", "https://www.bbc.com/news/world")
scrape_btn = st.sidebar.button("Scrape Website")

def clean_text(text):
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def extract_headlines(url):
    response = requests.get(url, timeout=10)
    soup = BeautifulSoup(response.content, "html.parser")

    headlines = []
    for tag in soup.find_all(["h1", "h2", "h3", "a"]):
        text = tag.get_text(strip=True)
        if text and len(text.split()) > 4:  # skip short texts
            headlines.append(clean_text(text))

    return list(set(headlines))

def display_wordcloud(texts):
    wordcloud = WordCloud(width=800, height=400, background_color="white").generate(" ".join(texts))
    plt.figure(figsize=(12, 6))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    st.pyplot(plt)

if scrape_btn:
    try:
        with st.spinner("Scraping headlines..."):
            headlines = extract_headlines(url)
            if headlines:
                df = pd.DataFrame({"Headline": headlines})

                st.success(f"✅ Scraped {len(df)} unique headlines from the website.")

                # Dashboard: Metrics
                st.subheader("📊 Dashboard Overview")
                col1, col2 = st.columns(2)
                col1.metric("Total Headlines", len(df))
                common_words = pd.Series(" ".join(headlines).lower().split()).value_counts()
                col2.metric("Top Word", common_words.index[0])

                # Word Cloud
                st.subheader("☁️ Word Cloud of Headlines")
                display_wordcloud(headlines)

                # Category Guess (Optional simple keyword match)
                st.subheader("🧠 Inferred Topics (guess based on keyword)")
                categories = {
                    "Politics": ["election", "president", "minister", "parliament"],
                    "Technology": ["tech", "ai", "data", "robot", "gadget", "device"],
                    "Sports": ["cricket", "football", "olympic", "player", "match"],
                    "Health": ["health", "virus", "covid", "doctor", "hospital"],
                    "Finance": ["stocks", "market", "inflation", "economy", "bank"]
                }

                text_blob = " ".join(headlines).lower()
                detected = []
                for cat, keywords in categories.items():
                    for word in keywords:
                        if word in text_blob:
                            detected.append(cat)
                            break

                detected = list(set(detected))
                st.write("Detected Categories:", ", ".join(detected) if detected else "Uncategorized")

                # Data Table
                st.subheader("🗒️ All Extracted Headlines")
                st.dataframe(df, use_container_width=True)
            else:
                st.warning("No valid headlines found on this page.")
    except Exception as e:
        st.error(f"❌ Failed to scrape: {e}")
