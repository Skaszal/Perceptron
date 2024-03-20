def init():
    pass


if __name__ == "__main__":

    init()

    while True:
        print('''
        Wybierz opcje:
        a) wprowadź nowe obserwacje z wiersza poleceń i przewiduj klasę
        b) wyjdz''')
        inp = input("> ").lower()

        if inp == "a":
            pass
        if inp == "b":
            break
