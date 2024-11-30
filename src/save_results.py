##__IMPORTS__##
import matplotlib.pyplot as plt
from sklearn.metrics import classification_report, confusion_matrix, ConfusionMatrixDisplay

def save_classif_report(y_test, y_pred, path): 
    report = classification_report(y_test, y_pred)
    with open (path, "w") as f : 
        f.write(report)

def save_matrix(y_test, y_pred, path) : 
    matrice = confusion_matrix(y_test, y_pred)
    disp = ConfusionMatrixDisplay(confusion_matrix=matrice)
    plt.figure(figsize = (12, 7))
    disp.plot(ax=plt.gca())
    plt.title('Matrice de Confusion SVM')
    plt.savefig(path)
    plt.close()