##__IMPORTS__##
from preprocessing import conversion_donnees, vectorisation, apply_smote
from model_SVM import train_and_evaluation as svm_train
from model_tree import train_and_evaluation as tree_train
from model_random_forest import train_and_evaluation as rf_train
import pandas as pd
from sklearn.model_selection import train_test_split

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
    #Chargement des données 
    y, X = conversion_donnees(dico)
    
    #Division du jeu de données
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    
    #Vectorisation des textes
    X_train_vect, X_test_vect = vectorisation(X_train, X_test)

    #Génération d'exemples synthétiques de la classe minoritaire avec SMOTE
    X_train_resampled, y_train_resampled = apply_smote(X_train_vect, y_train)
    
    #Entraînement et évaluation des modèles
    svm_result = svm_train(X_train_resampled, X_test_vect, y_train_resampled, y_test)
    tree_result = tree_train(X_train_resampled, X_test_vect, y_train_resampled, y_test)
    rf_result = rf_train(X_train_resampled, X_test_vect, y_train_resampled, y_test)

    # Afficher les résultats
    print(f"SVM result : {svm_result}")
    print(f"Tree Classifier result : {tree_result}")
    print(f"Random Forest result : {rf_result}")


if __name__ == "__main__":
    main()



