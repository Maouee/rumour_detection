##__IMPORTS__##
from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from dico_repartition_true_false_unverified import data_to_dict

def sentiment_analysis(dico) :
  #Initialisation de Vader
  analyzer = SentimentIntensityAnalyzer()

  fake_news_polarity = []
  true_news_polarity = []

  for posts, infos in dico.items() : 
    texte = infos["text"]
    label = infos["label"]

    #Analyse polarité avec Blob
    blob = TextBlob(texte)
    blob_polarity = blob.sentiment.polarity
    
    #Analyse polarité avec Vader
    vader_polarity = analyzer.polarity_scores(texte)['compound']

    #Moyenne des scores de polarité obtenus avec les deux analyseurs
    combined_polarity = (blob_polarity + vader_polarity) / 2

    if label == "fake_news" : 
        fake_news_polarity.append(combined_polarity)       
    elif label == "true_news" : 
        true_news_polarity.append(combined_polarity)

  fake_news_moyenne = sum(fake_news_polarity) / len(fake_news_polarity)
  true_news_moyenne = sum(true_news_polarity) / len(true_news_polarity)

  return fake_news_moyenne, true_news_moyenne

def classify_tweets(X_test, y_pred):
    true_news = []
    fake_news = []

    for tweet, label in zip(X_test, y_pred):
      if label == 1:
        true_news.append(tweet)
      elif label == 2:
        fake_news.append(tweet)
      elif label == 3:
        continue

    return true_news, fake_news

def sentiment_analysis_on_results(X_test): 
   #Initialisation de Vader
  analyzer = SentimentIntensityAnalyzer()

  fake_news_polarity = []
  true_news_polarity = []

  for tweet in X_test : 
    texte = tweet["text"]
    label = tweet["label"]

    #Analyse polarité avec Blob
    blob = TextBlob(texte)
    blob_polarity = blob.sentiment.polarity
    
    #Analyse polarité avec Vader
    vader_polarity = analyzer.polarity_scores(texte)['compound']

    #Moyenne des scores de polarité obtenus avec les deux analyseurs
    combined_polarity = (blob_polarity + vader_polarity) / 2

    if label == 0 : 
        fake_news_polarity.append(combined_polarity)       
    elif label == 1 : 
        true_news_polarity.append(combined_polarity)

  if len(fake_news_polarity) > 0:
    fake_news_moyenne = sum(fake_news_polarity) / len(fake_news_polarity)
  if len(true_news_polarity) > 0:
    true_news_moyenne = sum(true_news_polarity) / len(true_news_polarity)
  
  return fake_news_moyenne, true_news_moyenne