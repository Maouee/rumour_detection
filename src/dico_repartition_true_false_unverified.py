import glob
import json
import os

def data_to_dict():

    folders = [
        "prince-toronto-all-rnr-threads", "ottawashooting-all-rnr-threads", 
        "charliehebdo-all-rnr-threads", "ferguson-all-rnr-threads", 
        "gurlitt-all-rnr-threads", "putinmissing-all-rnr-threads", 
        "germanwings-crash-all-rnr-threads", "ebola-essien-all-rnr-threads", 
        "sydneysiege-all-rnr-threads"
    ]

    # folders = ["one_of_each"]

    dico_global = {}
    
    for folder in folders:
        print(f"\nTraitement du dossier : {folder}")

        dico_local = {}

        non_rumours_source_tweets_path = f'../../data/{folder}/non-rumours/*/source-tweets/*'
        dico_local = preprocess_non_rumours(non_rumours_source_tweets_path)

        rumours_source_tweets_path = f'../../data/{folder}/rumours/*/source-tweets/*'
        rumours_annotation_path = f'../../data/{folder}/rumours/*/annotation.json'
        dico_rumours = preprocess_rumours(rumours_source_tweets_path, rumours_annotation_path)
        dico_local.update(dico_rumours)
        
        summarize_results(dico_local)

        dico_global.update(dico_local)

    print("\nRésumé global :")
    summarize_results(dico_global)
    # print(dico_global)

    return dico_global

def preprocess_non_rumours(non_rumours_source_tweets_path):
    dico_local2 = {}
    for file in glob.glob(non_rumours_source_tweets_path):
        with open(file, 'r') as f:
            data = json.load(f)
            nr_tweet_text = data['text']
            nr_tweet_id = data['id']
            nr_tweet_label = "true_news"
            dico_local2[nr_tweet_id] = {'text': nr_tweet_text, 'label': nr_tweet_label}
    return dico_local2

def preprocess_rumours(rumours_source_tweets_path, rumours_annotation_path):
    # print("chemins source tweet", rumours_source_tweets_path)
    # print("chemins annotation", rumours_annotation_path)
    dico_local2 = {}
    for source_file in glob.glob(rumours_source_tweets_path):
        # print("source file", source_file)
        with open(source_file, 'r') as f:
            data = json.load(f)
            r_tweet_text = data['text']
            r_tweet_id = data['id']

            annotation_file = os.path.join(os.path.dirname(os.path.dirname(source_file)), "annotation.json")            
            # print("annotation file", annotation_file,"\n")
            with open(annotation_file, 'r') as af:
                annotations = json.load(af)
                # print("annotations", annotations)
                if 'misinformation' in annotations and 'true' in annotations:
                    # print("il y a misinformation et true")
                    if int(annotations['misinformation']) == 0 and int(annotations['true']) == 1:
                        r_tweet_label = "true_news"
                    elif int(annotations['misinformation']) == 1 and int(annotations['true']) == 0:
                        r_tweet_label = "fake_news"
                    elif int(annotations['misinformation']) == 0 and int(annotations['true']) == 0:
                        r_tweet_label = "unverified"
                    elif int(annotations['misinformation']) == 1 and int(annotations['true']) == 1:
                        r_tweet_label = "none"

                elif 'misinformation' in annotations and 'true' not in annotations:
                    # print("il y a misinformation et pas de true")
                    if int(annotations['misinformation']) == 1:
                        r_tweet_label = "fake_news"
                    elif int(annotations['misinformation']) == 0:
                        r_tweet_label = "unverified"
                elif 'misinformation' not in annotations and 'true' in annotations:
                    # print("il y a true et pas de misinformation")
                    r_tweet_label = "none"
                else:
                    # print("il n'y a ni misinformation ni true")
                    r_tweet_label = "none"
                dico_local2[r_tweet_id] = {'text': r_tweet_text, 'label': r_tweet_label}
    return dico_local2

def summarize_results(dico_global):
    # Calcul du nombre total de tweets
    total_tweets = len(dico_global)

    # Comptage des catégories
    nb_fake_news = len([tweet for tweet in dico_global.values() if tweet['label'] == 'fake_news'])
    nb_true_news = len([tweet for tweet in dico_global.values() if tweet['label'] == 'true_news'])
    nb_unverified = len([tweet for tweet in dico_global.values() if tweet['label'] == 'unverified'])
    nb_none = len([tweet for tweet in dico_global.values() if tweet['label'] == 'none'])

    # Calcul des pourcentages
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

resultat = data_to_dict()
# print(resultat)