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

    for i, label in enumerate(y_pred):
      tweet = X_test.iloc[i] #.iloc car c'est un objet de type Series pandas
      if label == 1:
        true_news.append({"text": tweet, "label": 1})
      elif label == 2:
        fake_news.append({"text": tweet, "label": 2})
      elif label == 3:
        continue
    
    return true_news, fake_news

def sentiment_analysis_on_results(tweets): 
   #Initialisation de Vader
  analyzer = SentimentIntensityAnalyzer()

  fake_news_polarity = []
  true_news_polarity = []

  for tweet in tweets :
    texte = tweet["text"]
    label = tweet["label"]

    #Analyse polarité avec Blob
    blob = TextBlob(texte)
    blob_polarity = blob.sentiment.polarity
    
    #Analyse polarité avec Vader
    vader_polarity = analyzer.polarity_scores(texte)['compound']

    #Moyenne des scores de polarité obtenus avec les deux analyseurs
    combined_polarity = (blob_polarity + vader_polarity) / 2

    if label == 2 : # Fake news
        fake_news_polarity.append(combined_polarity)       
    elif label == 1 : # True news
        true_news_polarity.append(combined_polarity)

   #Calcul le score moyen de polarité pour fake_news et true_news
  if fake_news_polarity :
    fake_news_moyenne = sum(fake_news_polarity) / len(fake_news_polarity)
  else : 
     return 0 
  if true_news_polarity :
    true_news_moyenne = sum(true_news_polarity) / len(true_news_polarity)
  else : 
    return 0

  return fake_news_moyenne, true_news_moyenne