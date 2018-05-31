# BY sklonley

import time
from sklearn import datasets
from sklearn.cross_validation import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score


def main():
    iris = datasets.load_iris()

    X = iris.data
    Y = iris.targer

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.5)

    my_classifier = KNeighborsClassifier()
    my_classifier.fit(X_train, Y_train)

    predicitions = my_classifier.predict(X_test)

    # print accuracy_score(Y_test,predicitions)

    # st=input (u"�Ы���@���~��")
    # time.sleep(4)


main()
