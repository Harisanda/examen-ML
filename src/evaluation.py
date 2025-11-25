def calculate_f1_score(y_true, y_pred):
    from sklearn.metrics import f1_score
    return f1_score(y_true, y_pred)

def calculate_confusion_matrix(y_true, y_pred):
    from sklearn.metrics import confusion_matrix
    return confusion_matrix(y_true, y_pred)

def calculate_classification_report(y_true, y_pred):
    from sklearn.metrics import classification_report
    return classification_report(y_true, y_pred)

def plot_confusion_matrix(cm, classes, title='Confusion Matrix', cmap=None):
    import matplotlib.pyplot as plt
    import numpy as np

    if cmap is None:
        cmap = plt.get_cmap('Blues')

    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)

    plt.ylabel('True label')
    plt.xlabel('Predicted label')
    plt.tight_layout()