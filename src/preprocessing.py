##__IMPORTS__##
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from imblearn.over_sampling import SMOTE

def conversion_donnees(dico) : 
    #Conversion du dictionnaire en dataframe
    df = pd.DataFrame.from_dict(dico, orient='index')

    #Conversion des étiquettes du df en valeurs numériques
    df['label'] = df['label'].map({"true_news": 1, "fake_news": 2, "unverified" : 3})
    y = df['label']
    X = df['text']

    return y, X


def vectorisation(X_train, X_test): 
    # Vectorisation des textes avec TF-IDF
    vectorizer = TfidfVectorizer(stop_words='english')
    X_train_vect = vectorizer.fit_transform(X_train)
    X_test_vect = vectorizer.transform(X_test)

    return X_train_vect, X_test_vect


def apply_smote(X_train, y_train):
    #Application de SMOTE pour rééquilibrer les classes
    smote = SMOTE(random_state=42, sampling_strategy= "minority")
    X_resampled, y_resampled = smote.fit_resample(X_train, y_train)
    
    return X_resampled, y_resampled
