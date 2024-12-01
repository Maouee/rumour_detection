import glob
import json
import os

def data_to_dict():
    """
    Fonction principale pour traiter les tweets, leur ajouter une étiquette de véracité 
    et les ré-organiser dans un dictionnaire global.
    Parcourt plusieurs dossiers contenant des tweets rumeurs et non-rumeurs,
    calcule la véracité et stocke chaque tweet, son contenu textuel et son étiquette de 
    véracité dans un dictionnaire.
    """
    # Liste des dossiers contenant les tweets
    folders = [
        "prince-toronto-all-rnr-threads", "ottawashooting-all-rnr-threads", 
        "charliehebdo-all-rnr-threads", "ferguson-all-rnr-threads", 
        "gurlitt-all-rnr-threads", "putinmissing-all-rnr-threads", 
        "germanwings-crash-all-rnr-threads", "ebola-essien-all-rnr-threads", 
        "sydneysiege-all-rnr-threads"
    ]
    
    # Dictionnaire global pour stocker tous les tweets traités
    dico_global = {}

    for folder in folders:
        print(f"\nTraitement du dossier : {folder}")

        # Dictionnaire local pour stocker les tweets traités dans un dossier
        dico_local = {}

        # Traitement des tweets non-rumeurs
        non_rumours_source_tweets_path = f'../../data/{folder}/non-rumours/*/source-tweets/*'
        dico_local = preprocess_non_rumours(non_rumours_source_tweets_path)

        # Traitement des tweets rumeurs
        rumours_source_tweets_path = f'../../data/{folder}/rumours/*/source-tweets/*'
        rumours_annotation_path = f'../../data/{folder}/rumours/*/annotation.json'
        dico_rumours = preprocess_rumours(rumours_source_tweets_path, rumours_annotation_path)
        
        # Fusion des résultats locaux des rumeurs et non-rumeurs
        dico_local.update(dico_rumours)
        
        # Résumé des résultats pour le dossier en cours
        summarize_results(dico_local)

        # Mise à jour du dictionnaire global avec les résultats locaux
        dico_global.update(dico_local)

    # Résumé global pour tous les dossiers
    print("\nRésumé global :")
    summarize_results(dico_global)

    return dico_global

def preprocess_non_rumours(non_rumours_source_tweets_path):
    """
    Traite les tweets non-rumeurs à partir des fichiers sources.
    Retourne un dictionnaire contenant l'ID, le texte et l'étiquette des tweets.
    """
    dico_local2 = {}
    for file in glob.glob(non_rumours_source_tweets_path):
        with open(file, 'r') as f:
            # Charger les données JSON du fichier
            data = json.load(f)
            nr_tweet_text = data['text']  # Texte du tweet
            nr_tweet_id = data['id']      # ID du tweet
            nr_tweet_label = "true_news"  # Étiquette par défaut pour les non-rumeurs
            # Ajouter les données au dictionnaire local
            dico_local2[nr_tweet_id] = {'text': nr_tweet_text, 'label': nr_tweet_label}
    return dico_local2

def preprocess_rumours(rumours_source_tweets_path, rumours_annotation_path):
    """
    Traite les tweets rumeurs en utilisant les fichiers sources et les annotations.
    Retourne un dictionnaire contenant l'ID, le texte et l'étiquette des tweets.
    """
    dico_local2 = {}
    for source_file in glob.glob(rumours_source_tweets_path):
        with open(source_file, 'r') as f:
            # Charge les données JSON du fichier source
            data = json.load(f)
            r_tweet_text = data['text']  # Texte du tweet
            r_tweet_id = data['id']      # ID du tweet

            # Construis le chemin vers le fichier d'annotations
            annotation_file = os.path.join(os.path.dirname(os.path.dirname(source_file)), "annotation.json")
            with open(annotation_file, 'r') as af:
                annotations = json.load(af)  # Charger les annotations JSON

                # Détermine l'étiquette en fonction des annotations
                if 'misinformation' in annotations and 'true' in annotations:
                    if int(annotations['misinformation']) == 0 and int(annotations['true']) == 1:
                        r_tweet_label = "true_news"
                    elif int(annotations['misinformation']) == 1 and int(annotations['true']) == 0:
                        r_tweet_label = "fake_news"
                    elif int(annotations['misinformation']) == 0 and int(annotations['true']) == 0:
                        r_tweet_label = "unverified"
                    elif int(annotations['misinformation']) == 1 and int(annotations['true']) == 1:
                        r_tweet_label = "none"
                elif 'misinformation' in annotations and 'true' not in annotations:
                    if int(annotations['misinformation']) == 1:
                        r_tweet_label = "fake_news"
                    elif int(annotations['misinformation']) == 0:
                        r_tweet_label = "unverified"
                elif 'misinformation' not in annotations and 'true' in annotations:
                    r_tweet_label = "none"
                else:
                    r_tweet_label = "none"

                # Ajoute les données au dictionnaire local
                dico_local2[r_tweet_id] = {'text': r_tweet_text, 'label': r_tweet_label}
    return dico_local2

def summarize_results(dico_global):
    """
    Résume les résultats d'un dictionnaire contenant des tweets par catégorie.
    Affiche le total des tweets et les proportions de chaque catégorie.
    """
    # Calcul du nombre total de tweets
    total_tweets = len(dico_global)

    # Comptage des tweets par catégorie
    nb_fake_news = len([tweet for tweet in dico_global.values() if tweet['label'] == 'fake_news'])
    nb_true_news = len([tweet for tweet in dico_global.values() if tweet['label'] == 'true_news'])
    nb_unverified = len([tweet for tweet in dico_global.values() if tweet['label'] == 'unverified'])
    nb_none = len([tweet for tweet in dico_global.values() if tweet['label'] == 'none'])

    # Calcul des pourcentages pour chaque catégorie
    percent_fake_news = (nb_fake_news / total_tweets * 100) if total_tweets > 0 else 0
    percent_true_news = (nb_true_news / total_tweets * 100) if total_tweets > 0 else 0
    percent_unverified = (nb_unverified / total_tweets * 100) if total_tweets > 0 else 0
    percent_none = (nb_none / total_tweets * 100) if total_tweets > 0 else 0

    # Affichage des résultats
    print(f"Total tweets : {total_tweets}")
    print(f"Fake news : {nb_fake_news} ({percent_fake_news:.2f}%)")
    print(f"True news : {nb_true_news} ({percent_true_news:.2f}%)")
    print(f"Unverified : {nb_unverified} ({percent_unverified:.2f}%)")
    print(f"None : {nb_none} ({percent_none:.2f}%)")

# Exécution de la fonction principale et stockage du résultat final
resultat = data_to_dict()