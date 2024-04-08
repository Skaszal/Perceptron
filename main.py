from Perceptron import Perceptron

global perceptron


def init():
    tmp = float(input("stala uczenia> "))
    perceptron = Perceptron(tmp, "training.txt")
    perceptron.train(3000)


def guess():
    inp = input("> ")
    perceptron.guess(inp)


if __name__ == "__main__":
    init()

    while True:
        
        print('''
        Wybierz opcje:
        a) wprowadź nowe obserwacje z wiersza poleceń i przewiduj klasę
        b) wyjdz''')
        inp = input("> ").lower()

        if inp == "a":
            guess()
        if inp == "b":
            break

