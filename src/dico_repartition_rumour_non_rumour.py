import glob
import json

def data_to_dict():

    # Liste des noms de dossiers
    folders = [
        "prince-toronto-all-rnr-threads", "ottawashooting-all-rnr-threads", 
        "charliehebdo-all-rnr-threads", "ferguson-all-rnr-threads", 
        "gurlitt-all-rnr-threads", "putinmissing-all-rnr-threads", 
        "germanwings-crash-all-rnr-threads", "ebola-essien-all-rnr-threads", 
        "sydneysiege-all-rnr-threads"
    ]

    # Dictionnaire global
    dico_global = {}

    # Parcours de la liste des dossiers
    for folder in folders:
        print(f"\nTraitement du dossier : {folder}")

        # Réinitialisation du dictionnaire pour ce dossier
        dico_theme = {}

        # Chemin vers les tweets classifiés comme "non-rumeurs"
        non_rumours_source_tweets_path = f'../../data/{folder}/non-rumours/*/source-tweets/*'
        dico_theme = preprocess_non_rumours(non_rumours_source_tweets_path, dico_theme)

        # Chemin vers les tweets classifiés comme "rumeurs" et leurs annotations
        rumours_source_tweets_path = f'../../data/{folder}/rumours/*/source-tweets/*'
        dico_theme = preprocess_rumours(rumours_source_tweets_path, dico_theme)

        # Affichage du résumé pour le dossier
        summarize_results(dico_theme)

        # Ajouter les données de ce dossier au dictionnaire global
        dico_global.update(dico_theme)

    # Résumé global
    print("\nRésumé global :")
    summarize_results(dico_global)

    return dico_global

# Traitement des "non-rumeurs"
def preprocess_non_rumours(non_rumours_source_tweets_path, dico):
    for file in glob.glob(non_rumours_source_tweets_path):
        with open(file, 'r') as f:
            data = json.load(f)
            nr_tweet_text = data['text']
            nr_tweet_id = data['id']
            nr_tweet_label = "true_news"
            dico[nr_tweet_id] = {'text': nr_tweet_text, 'label': nr_tweet_label}
    return dico

# Traitement des "rumeurs"
def preprocess_rumours(rumours_source_tweets_path, dico):
    for file in glob.glob(rumours_source_tweets_path):
        with open(file, 'r') as f:
            data = json.load(f)
            r_tweet_text = data['text']
            r_tweet_id = data['id']
            r_tweet_label = "fake_news"
            dico[r_tweet_id] = {'text': r_tweet_text, 'label': r_tweet_label}
    return dico

# Affichage du résumé pour le dictionnaire
def summarize_results(dico):
    nb_fake_news = len([tweet for tweet in dico.values() if tweet['label'] == 'fake_news'])
    nb_true_news = len([tweet for tweet in dico.values() if tweet['label'] == 'true_news'])
    print(f"nb fake news : {nb_fake_news}")
    print(f"nb true news : {nb_true_news}")

# Exécution principale
dico = data_to_dict()
