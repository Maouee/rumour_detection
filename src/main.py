##__IMPORTS__##
from preprocessing import conversion_donnees, vectorisation, apply_smote
from model_SVM import train_and_evaluation as svm_train
from model_tree import train_and_evaluation as tree_train
from model_random_forest import train_and_evaluation as rf_train
from save_results import save_classif_report, save_matrix
from dico_repartition_true_false_unverified import data_to_dict
from sentiment_analysis import sentiment_analysis
import pandas as pd
from sklearn.model_selection import train_test_split


def main(): 
    ##Récupération des données 
    dico = data_to_dict()

    ##Analyse des sentiments
    fake_news_moyenne, true_news_moyenne = sentiment_analysis(dico)
    print(f"Moyenne du sous-corpus fake : {fake_news_moyenne:.5f}")
    print(f"Moyenne du sous-corpus true : {true_news_moyenne:.5f}")

    ##Chargement des données 
    y, X = conversion_donnees(dico)
    
    ##Division du jeu de données
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    
    ##Vectorisation des textes
    X_train_vect, X_test_vect = vectorisation(X_train, X_test)

    ##Génération d'exemples synthétiques de la classe minoritaire (fake_news) avec SMOTE
    X_train_resampled, y_train_resampled = apply_smote(X_train_vect, y_train)

    ##Afficher la taille avant et après SMOTE
    # print(f"Taille d'origine de X_train_vect : {X_train_vect.shape}")
    # print(f"Taille après SMOTE : {X_train_resampled.shape}")
    
    #Entraînement et évaluation des modèles
    svm_result = svm_train(X_train_resampled, X_test_vect, y_train_resampled, y_test)
    tree_result = tree_train(X_train_resampled, X_test_vect, y_train_resampled, y_test)
    rf_result = rf_train(X_train_resampled, X_test_vect, y_train_resampled, y_test)

    ##Afficher les résultats
    print(f"SVM Classification Report :\n {svm_result['classification_report']}")
    print(f"SVM Confusion Matrix :\n {svm_result['confusion_matrix']}")
    
    print(f"Tree Classification Report :\n {tree_result['classification_report']}")
    print(f"Tree Confusion Matrix :\n {tree_result['confusion_matrix']}")
    
    print(f"Random Forest Classification Report :\n {rf_result['classification_report']}")
    print(f"Random Forest Matrix :\n {rf_result['confusion_matrix']}")

    ##Enregistrer les résultats
    #Rapports de classification : 
    save_classif_report(y_test, svm_result['y_pred'], 'assets/classif_report/svm_classification_report.txt')
    save_classif_report(y_test, tree_result['y_pred'], 'assets/classif_report/tree_classification_report.txt')
    save_classif_report(y_test, rf_result['y_pred'], 'assets/classif_report/rf_classification_report.txt')

    #Matrices de confusion
    save_matrix(svm_result['confusion_matrix'], 'assets/matrice/svm_confusion_matrix.png')
    save_matrix(tree_result['confusion_matrix'], 'assets/matrice/tree_confusion_matrix.png')
    save_matrix(rf_result['confusion_matrix'], 'assets/matrice/rf_confusion_matrix.png')



if __name__ == "__main__":
    main()



