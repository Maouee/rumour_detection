##__IMPORTS__##
from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from dico_repartition_rumour_non_rumour import data_to_dict

def main(): 
  dico = data_to_dict()
  fake_news_moyenne, true_news_moyenne = sentiment_analysis(dico)
  print(f"Moyenne du sous-corpus fake : {fake_news_moyenne:.2f}")
  print(f"Moyenne du sous-corpus true : {true_news_moyenne:.2f}")

def sentiment_analysis(dico) :
  """
  
  """

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


if __name__ == "__main__":
    main()