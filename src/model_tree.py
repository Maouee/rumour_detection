##__IMPORTS__##
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt

def train_and_evaluation(X_train, X_test, y_train, y_test) : 
    """
    
    """
    #Initialisation du modèle
    tree_model = DecisionTreeClassifier(random_state=42)

    #Entraînement du modèle
    tree_model.fit(X_train, y_train)

    #Prédictions
    y_pred = tree_model.predict(X_test)

    #Calcul des métriques
    print("Classification Report :\n")
    print(classification_report(y_test, y_pred))

    #Matrice de confusion
    matrice = confusion_matrix(y_test, y_pred)
    disp = ConfusionMatrixDisplay(confusion_matrix=matrice, display_labels=tree_model.classes_)
    plt.figure(figsize = (12, 7))
    disp.plot(ax=plt.gca())
    plt.title('Matrice de Confusion Tree')
    plt.show()
    
    return classification_report(y_test, y_pred)