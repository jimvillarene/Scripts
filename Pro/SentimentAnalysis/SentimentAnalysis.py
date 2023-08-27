#! /usr/bin/env python3
from sentiment_analysis_spanish import sentiment_analysis

sentiment = sentiment_analysis.SentimentAnalysisSpanish()
print(sentiment.sentiment("mejor explicacion"))
