
# 📊 Live News Scraper Dashboard

A **Streamlit-based web application** that scrapes live headlines from any public news website and visualizes them using an interactive dashboard with word clouds, keyword analytics, and auto-categorization. Built to demonstrate skills in **web scraping**, **data visualization**, **natural language processing**, and **dashboard development**.

---

## 🧠 Features

| Feature | Description |
|--------|-------------|
| 🌐 Live Web Scraping | Enter any public news website URL and instantly fetch headlines. |
| 📋 Headline Extraction | Extracts headlines from tags like `<h1>`, `<h2>`, `<a>` and filters out short/noise text. |
| 📊 Dashboard Metrics | Visualize the total number of headlines, most common word, and inferred categories. |
| ☁️ Word Cloud | Displays a word cloud based on scraped headlines to highlight trending topics. |
| 🧠 Topic Detection | Automatically detects general news categories like Politics, Tech, Sports, etc. |
| 🗒️ Interactive Table | View all cleaned and unique headlines in a scrollable, responsive table. |

---

## 🔧 Tech Stack

- **Frontend & Dashboard**: [Streamlit](https://streamlit.io/)
- **Backend**: Python
- **Libraries**:
  - `requests` & `beautifulsoup4` for web scraping
  - `pandas` for data manipulation
  - `matplotlib` & `wordcloud` for visualizations
  - `re` for text cleaning

---

## 🛠️ Installation & Setup

1. **Clone the repository**

```bash
git clone https://github.com/Rishita-Garg/live-news-dashboard.git
cd live-news-dashboard
````

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

If you don't have a `requirements.txt`, use:

```bash
pip install streamlit requests beautifulsoup4 pandas wordcloud matplotlib
```

3. **Run the Streamlit app**

```bash
streamlit run app.py
```

4. **Open in Browser**

It will open at: [http://localhost:8501](http://localhost:8501)

---

## 🚀 Usage

1. Enter a valid news website URL (e.g. `https://www.bbc.com/news/world`)
2. Click **"Scrape Website"**
3. View:

   * Headline count and top word
   * Word cloud of scraped news
   * Auto-detected categories (based on keywords)
   * Complete headline table

---

## 🧪 Example URLs

| Site                  | URL                                                                              |
| --------------------- | -------------------------------------------------------------------------------- |
| BBC News              | [https://www.bbc.com/news](https://www.bbc.com/news)                             |
| Al Jazeera            | [https://www.aljazeera.com/news](https://www.aljazeera.com/news)                 |
| Reuters World         | [https://www.reuters.com/world/](https://www.reuters.com/world/)                 |
| NYTimes International | [https://www.nytimes.com/international/](https://www.nytimes.com/international/) |

---
![6985101b-0243-4ae1-a946-4f93050f7f04](https://github.com/user-attachments/assets/7d571030-54ff-4a6a-a213-c02ed82d6e55)

