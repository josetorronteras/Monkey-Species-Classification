import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix

def pltResults(logdir, data1, data2, title, labelx, labely):
    plt.plot(data1)
    plt.plot(data2)
    plt.title(title)
    plt.xlabel(labelx)
    plt.ylabel(labely)
    plt.legend(['train', 'test'], loc='upper left')
    plt.savefig(logdir + '/' + labely + '.png')
    plt.close()

def confusionMatrix(y_test, y_pred):
    matrix = confusion_matrix(y_test, y_pred)
    plt.figure(figsize=(10, 10))
    ax = plt.subplot()
    sns.heatmap(matrix, annot=True, ax=ax);

    ax.set_xlabel('Predicted labels');
    ax.set_ylabel('True labels'); 
    ax.set_title('Matriz de confusión'); 
    ax.xaxis.set_ticklabels(['mantled_howler', 'patas_monkey', 'bald_uakari', 'japanese_macaque',\
                             'pygmy_marmoset', 'white_headed_capuchin', 'silvery_marmoset', \
                             'common_squirrel_monkey', 'black_headed_night_monkey', 'nilgiri_langur']); 
    ax.yaxis.set_ticklabels(['mantled_howler', 'patas_monkey', 'bald_uakari', 'japanese_macaque',\
                             'pygmy_marmoset', 'white_headed_capuchin', 'silvery_marmoset', \
                             'common_squirrel_monkey', 'black_headed_night_monkey', 'nilgiri_langur']);

    plt.show()