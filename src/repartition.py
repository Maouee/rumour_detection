import glob
import json

def calculate_veracity_distribution(rumour_path, non_rumour_path, global_counts):
    # Initialisation des compteurs locaux
    true_count = 0
    false_count = 0
    unverified_count = 0
    none_count = 0

    # Fonction pour analyser les fichiers *rumours*
    def process_rumours(annotation_files):
        nonlocal true_count, false_count, unverified_count, none_count
        for file in glob.glob(annotation_files):
            with open(file, 'r') as f:
                annotation = json.load(f)

                # Vérifie les annotations pour déterminer la véracité
                if 'misinformation' in annotation and 'true' in annotation:
                    if int(annotation['misinformation']) == 0 and int(annotation['true']) == 1:
                        true_count += 1
                    elif int(annotation['misinformation']) == 1 and int(annotation['true']) == 0:
                        false_count += 1
                    elif int(annotation['misinformation']) == 0 and int(annotation['true']) == 0:
                        unverified_count += 1                
                    elif int(annotation['misinformation']) == 1 and int(annotation['true']) == 1:
                        none_count += 1
                elif 'misinformation' in annotation and "true" not in annotation:
                    if int(annotation['misinformation']) == 1:
                        false_count += 1
                    elif int(annotation['misinformation']) == 0:
                        unverified_count += 1
                elif 'misinformation' not in annotation and 'true' in annotation:
                    none_count += 1
                else:
                    none_count += 1

    # Fonction pour analyser les fichiers *non-rumours*
    def process_non_rumours(annotation_files):
        nonlocal true_count
        for file in glob.glob(annotation_files):
            # Tous les fichiers dans *non-rumours* sont considérés comme `true`
            true_count += 1

    # Analyse des *rumours* et *non-rumours*
    process_rumours(rumour_path)
    process_non_rumours(non_rumour_path)

    # Mise à jour des compteurs globaux
    global_counts['true'] += true_count
    global_counts['false'] += false_count
    global_counts['unverified'] += unverified_count
    global_counts['none'] += none_count

    # Affiche les résultats pour le dossier
    total = true_count + false_count + unverified_count + none_count
    print(f"\nRépartition des annotations (local) :")
    print(f"True: {true_count} ({true_count / total * 100:.2f}%)")
    print(f"False: {false_count} ({false_count / total * 100:.2f}%)")
    print(f"Unverified: {unverified_count} ({unverified_count / total * 100:.2f}%)")
    print(f"None: {none_count} ({none_count / total * 100:.2f}%)\n")

# Liste des noms de dossiers
folders = [
    "prince-toronto-all-rnr-threads", "ottawashooting-all-rnr-threads", 
    "charliehebdo-all-rnr-threads", "ferguson-all-rnr-threads", 
    "gurlitt-all-rnr-threads", "putinmissing-all-rnr-threads", 
    "germanwings-crash-all-rnr-threads", "ebola-essien-all-rnr-threads", 
    "sydneysiege-all-rnr-threads"
]

# Initialisation des compteurs globaux
global_counts = {'true': 0, 'false': 0, 'unverified': 0, 'none': 0}

# Parcours de la liste des dossiers
for folder in folders:
    # Chemins pour *rumours* et *non-rumours*
    rumour_annotations_path = f'../data/{folder}/rumours/*/annotation.json'
    non_rumour_annotations_path = f'../data/{folder}/non-rumours/*/annotation.json'

    print(f"Traitement du dossier : {folder}")
    print(f"Chemin des annotations (rumours) : {rumour_annotations_path}")
    print(f"Chemin des annotations (non-rumours) : {non_rumour_annotations_path}")
    
    # Appel de la fonction pour ce dossier
    calculate_veracity_distribution(rumour_annotations_path, non_rumour_annotations_path, global_counts)

# Affichage des résultats globaux
total_global = global_counts['true'] + global_counts['false'] + global_counts['unverified'] + global_counts['none']
print("\nRépartition des annotations (global) :")
print(f"True: {global_counts['true']} ({global_counts['true'] / total_global * 100:.2f}%)")
print(f"False: {global_counts['false']} ({global_counts['false'] / total_global * 100:.2f}%)")
print(f"Unverified: {global_counts['unverified']} ({global_counts['unverified'] / total_global * 100:.2f}%)")
print(f"None: {global_counts['none']} ({global_counts['none'] / total_global * 100:.2f}%)\n")
