##__IMPORTS__##
from preprocessing import conversion_donnees, vectorisation, apply_smote
from model_SVM import train_and_evaluation as svm_train
from model_tree import train_and_evaluation as tree_train
from model_random_forest import train_and_evaluation as rf_train
from dico_repartition_rumour_non_rumour import data_to_dict
import pandas as pd
from sklearn.model_selection import train_test_split


def main(): 
    #Récupération des données 
    dico = data_to_dict()

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
    print(f"SVM result :\n {svm_result}")
    print(f"Tree Classifier result :\n {tree_result}")
    print(f"Random Forest result :\n {rf_result}")


if __name__ == "__main__":
    main()



