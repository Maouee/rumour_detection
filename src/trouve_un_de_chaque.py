import glob
import json

def find_files_by_annotations(annotation_path):
    # Dictionnaire pour stocker les fichiers correspondants
    files_by_condition = {
        "misinfo_1_true_0": None,
        "misinfo_0_true_0": None,
        "misinfo_0_true_1": None
    }

    # Parcourt tous les fichiers d'annotation dans le chemin donné
    for file in glob.glob(annotation_path):
        with open(file, 'r') as f:
            annotation = json.load(f)

            # Vérifie les combinaisons d'annotations
            if 'misinformation' in annotation and 'true' in annotation:
                misinfo = int(annotation['misinformation'])
                true = int(annotation['true'])

                if misinfo == 1 and true == 0 and files_by_condition["misinfo_1_true_0"] is None:
                    files_by_condition["misinfo_1_true_0"] = file
                elif misinfo == 0 and true == 0 and files_by_condition["misinfo_0_true_0"] is None:
                    files_by_condition["misinfo_0_true_0"] = file
                elif misinfo == 0 and true == 1 and files_by_condition["misinfo_0_true_1"] is None:
                    files_by_condition["misinfo_0_true_1"] = file

            # Arrête la recherche si tous les fichiers ont été trouvés
            if all(value is not None for value in files_by_condition.values()):
                break

    # Affiche les fichiers trouvés
    print("Fichiers trouvés :")
    for condition, file in files_by_condition.items():
        print(f"{condition}: {file if file else 'Aucun fichier trouvé'}")

# Liste des noms de dossiers
folders = [
    "prince-toronto-all-rnr-threads", "ottawashooting-all-rnr-threads", 
    "charliehebdo-all-rnr-threads", "ferguson-all-rnr-threads", 
    "gurlitt-all-rnr-threads", "putinmissing-all-rnr-threads", 
    "germanwings-crash-all-rnr-threads", "ebola-essien-all-rnr-threads", 
    "sydneysiege-all-rnr-threads"
]

# Parcours de la liste des dossiers
for folder in folders:
    print(f"\nTraitement du dossier : {folder}")
    annotations_path = f'../../data/{folder}/rumours/*/annotation.json'

    # Appel de la fonction pour trouver les fichiers
    find_files_by_annotations(annotations_path)
