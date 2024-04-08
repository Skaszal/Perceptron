import random
import numpy as np


def heaviside(z):
    return np.where(z < 0, 0, 1)


class Perceptron:
    def __init__(self, learningRate: float, trainingFilePath: str):
        if not (0 < learningRate < 1):
            raise ValueError("Learning rate must be between 0 and 1!")

        self.learningRate = learningRate
        self.weight = np.array([])
        self.trainingFile = open(trainingFilePath)
        self.trainingTplArr = []
        self.bias = 0.1

        self.labelsdict = dict()
        label_counter = 0

        for x in self.trainingFile:
            tmp = x.strip().split(',')
            label = tmp[-1]
            # Sprawdź, czy etykieta jest już w słowniku, jeśli nie, dodaj ją
            if label not in self.labelsdict:
                self.labelsdict[label] = label_counter
                label_counter += 1  # Zwiększ licznik dla następnej etykiety

            values = np.array([float(x) for x in tmp[:-1]])
            xtuple = (values, label)
            self.trainingTplArr.append(xtuple)

        for y in self.trainingTplArr[0][0]:
            self.weight = np.append(self.weight, 0.05)

    def train(self, epoch):
        for x in range(epoch):
            gitgut = 0
            random.shuffle(self.trainingTplArr)
            for y in self.trainingTplArr:
                scalar = np.dot(self.weight, y[0])
                result = heaviside(scalar + self.bias)
                if result == self.labelsdict[y[1]]:
                    gitgut += 1
                else:
                    pass
                    # regula delta
                    self.updateWeight(result, y)
                    self.updateBias(result, y)

            print("Dokladnosc dla epoki: " + str(x + 1) + " wynosi: " + str(gitgut / len(self.trainingTplArr)))

    def updateWeight(self, result, y):
        self.weight += (self.labelsdict[y[1]] - result) * self.learningRate * y[0]

    def updateBias(self, result, y):
        self.bias += (self.labelsdict[y[1]] - result) * self.learningRate

    def guess(self, line):
        tmp = line.strip().split(',')  # Rozdziel linię na wartości cech
        ar = [float(x) for x in tmp]
        print(ar)
        scalar = np.dot(self.weight, ar)
        result = heaviside(scalar + self.bias)

        for x in self.labelsdict.keys():
            if self.labelsdict[x] == result:
                print("Guess: " + str(x))
