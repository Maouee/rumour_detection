##__IMPORTS__##
from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

dico = {
  "post1" : {
    "text" : "Patrol cars still flood the streets in #ferguson more than 6 hours after police officer shot teenager @ksdknews http:\/\/t.co\/fCCGAfIRbG",
    "label" : "true_news"
  },
  "post2" : {
    "text" : "I'm very fit and very healthy,No truth in the internet rumours that I have contracted Ebola.",
    "label" : "fake_news"
  },
  "post3" : {
    "text" : "Charlie Hebdo became well known for publishing the Muhammed cartoons two years ago.",
    "label" : "fake_news"
  },
  "post4" : {
      "text" : "#Ferguson police have brought dogs into neighborhood. Residents protest with hands in the air. Tension is growing... http:\/\/t.co\/BxYIsHHjnE",
      "label" : "true_news"
  },
  "post5" : {
      "text" : "Police have brought cats into neighborhood. Residents protest with hands in the air. Tension is growing... http:\/\/t.co\/BxYIsHHjnE",
      "label" : "true_news"
  },
  "post9" : {
    "text" : "Patrol trucks still flood the streets in #NewYork more than 12 hours after police officer shot teenager @ksdknews http:\/\/t.co\/fCCGAfIRbG",
    "label" : "true_news"
  },
  "post6": {
        "text": "Scientists discovered a new planet that could potentially support life.",
        "label": "true_news"
    },
    "post7": {
        "text": "Eating chocolate every day helps you lose weight, says new study.",
        "label": "fake_news"
    },
    "post8": {
        "text": "Alien life found on Mars, claims controversial study.",
        "label": "fake_news"
    },
      "post9": {
        "text": "Breaking: Major earthquake strikes California, thousands feared dead.",
        "label": "true_news"
    },
    "post10": {
        "text": "President signs new law to increase minimum wage.",
        "label": "true_news"
    },
    "post11": {
        "text": "Study shows that using smartphones can improve memory.",
        "label": "true_news"
    },
    "post12": {
        "text": "New diet pill guarantees weight loss without exercise.",
        "label": "fake_news"
    },
    "post13": {
        "text": "Global warming is a hoax, claims new research.",
        "label": "fake_news"
    },
    "post14": {
        "text": "New species of dinosaur discovered in China.",
        "label": "true_news"
    },
    "post15": {
        "text": "Eating broccoli every day can cure cancer, says new study.",
        "label": "fake_news"
    },
    "post16": {
        "text": "New vaccine developed for Zika virus.",
        "label": "true_news"
    },
    "post17": {
        "text": "Moon landing was faked, new evidence suggests.",
        "label": "fake_news"
    },
    "post18": {
        "text": "Massive solar storm to hit Earth tomorrow, scientists warn.",
        "label": "true_news"
    },
    "post19": {
        "text": "New app can diagnose illnesses from a photo of your face.",
        "label": "fake_news"
    },
    "post20": {
        "text": "Government confirms existence of extraterrestrial life.",
        "label": "fake_news"
    },
    "post21": {
        "text": "New technology can make humans invisible, scientists claim.",
        "label": "fake_news"
    },
    "post22": {
        "text": "Breaking: Major breakthrough in cancer research.",
        "label": "true_news"
    },
    "post23": {
        "text": "Study finds that drinking wine can help you live longer.",
        "label": "true_news"
    },
    "post24": {
        "text": "Using garlic can protect against vampires, says expert.",
        "label": "fake_news"
    },
    "post25": {
        "text": "New research shows that exercise can boost mental health.",
        "label": "true_news"
    }
}

def main(): 
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