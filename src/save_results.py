##__IMPORTS__##
import matplotlib.pyplot as plt
import os
from sklearn.metrics import classification_report, confusion_matrix, ConfusionMatrixDisplay

def save_classif_report(y_test, y_pred, path): 
    ##Vérification de si le dossier existe, sinon le créer
    dossier = os.path.dirname(path)
    if not os.path.exists(dossier):
        os.makedirs(dossier)

    report = classification_report(y_test, y_pred)
    with open (path, "w") as f : 
        f.write(report)

def save_matrix(matrix, path) :
    ##Vérification de si le dossier existe, sinon le créer 
    folder = os.path.dirname(path)
    if not os.path.exists(folder):
        os.makedirs(folder)

    disp = ConfusionMatrixDisplay(confusion_matrix=matrix)
    plt.figure(figsize = (12, 7))
    disp.plot(ax=plt.gca())
    plt.title('Matrice de Confusion')
    plt.savefig(path)
    plt.close()