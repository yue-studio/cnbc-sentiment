#!pip install feedparser
#!pip install requests
#!pip install vaderSentiment
#!pip3 install beautifulsoup4

import feedparser
import requests

from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from bs4 import BeautifulSoup

"""Next create a function to get sentiment scores (neg, pos, neu, & compound). The compound score is a metric that calculates the sum of all the lexicon ratings which have been normalized between -1(most extreme negative) and +1 (most extreme positive).

positive sentiment: compound score >= 0.05
neutral sentiment: (compound score > -0.05) and (compound score < 0.05)
negative sentiment: compound score <= -0.05

Pos is the positive percentage score, neg is the negative percentage score, and neu is the neutral percentage score.
"""

def getSIA(text):
  sia = SentimentIntensityAnalyzer()
  sentiment = sia.polarity_scores(text)
  return sentiment

"""The subjectivity shows how subjective or objective a statement is.
The polarity shows how positive/negative the statement is, a value equal to 1 means the statement is positive, a value equal to 0 means the statement is neutral and a value of -1 means the statement is negative.

"""

URL = "https://www.cnbc.com/id/10000664/device/rss/rss.html"

NewsFeed = feedparser.parse(URL)

for entry in NewsFeed.entries:
    print (entry.title)
    print (entry.summary)
    print (entry.link)
    page = requests.get(entry.link)
    soup = BeautifulSoup(page.content, 'html.parser')
    article = soup.find(id='MainContent')
    print('Subjectivity:', TextBlob(entry.summary).sentiment.subjectivity)
    print('Polarity    :',TextBlob(entry.summary).sentiment.polarity)
    print(getSIA(article.text.strip()))
    print('-------')
