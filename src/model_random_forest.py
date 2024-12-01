##__IMPORTS__##
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt

def train_and_evaluation(X_train, X_test, y_train, y_test):
    """
    
    """
    # Initialiser le modèle Random Forest
    rf_model = RandomForestClassifier(random_state=42)

    #Entraînement du modèle
    rf_model.fit(X_train, y_train)

    #Prédictions
    y_pred = rf_model.predict(X_test)

    #Calcul des métriques
    report = classification_report(y_test, y_pred, output_dict=True)

    #Matrice de confusion
    matrice = confusion_matrix(y_test, y_pred)
    disp = ConfusionMatrixDisplay(confusion_matrix=matrice, display_labels=rf_model.classes_)
    # plt.figure(figsize = (12, 7))
    # disp.plot(ax=plt.gca())
    # plt.title('Matrice de Confusion RandomForest')
    # plt.show()
    
    return {'label_pred': y_pred,'classification_report': report, 'confusion_matrix': matrice}