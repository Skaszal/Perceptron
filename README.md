# Perceptron –  klasyfikacja liniowa w Pythonie (implementacja własna)

Ten projekt zawiera własną implementację perceptronu w Pythonie. Model uczy się wag metodą iteracyjnych poprawek (reguła delta) na danych z pliku `training.txt`, a następnie pozwala przewidywać klasę dla nowych obserwacji podanych w konsoli.

Do obliczeń używany jest `numpy`. Reszta logiki (uczenie, predykcja, wczytywanie danych) jest napisana ręcznie.

## Jak działa program

Program składa się z dwóch części:
- `Perceptron.py` zawiera klasę `Perceptron` z implementacją uczenia i predykcji.
- `main.py` uruchamia trening modelu, a potem w pętli pozwala wpisywać nowe obserwacje i odczytywać przewidywaną etykietę.

Po uruchomieniu programu w konsoli podawana jest wartość stałej uczenia (learning rate). Następnie model trenowany jest przez ustaloną liczbę epok (3000). W trakcie procesu uczenia program wypisuje dokładność po każdej epoce. Po zakończeniu treningu możliwe jest wprowadzanie nowych obserwacji (samych cech) w konsoli oraz uzyskanie przewidywanej etykiety klasy.

## Format danych treningowych

Plik `training.txt` powinien mieć format CSV:
- każda linia to jedna obserwacja,
- wartości są rozdzielone przecinkami,
- ostatnia kolumna to etykieta (label),
- pozostałe kolumny to cechy numeryczne (float).

Etykiety są mapowane na wartości liczbowe wewnątrz programu (pierwsza napotkana etykieta -> 0, druga -> 1, itd.). W obecnej wersji perceptron działa jako klasyfikator binarny (z funkcją progową 0/1), więc najlepiej używać dwóch klas w danych.

## Implementacja (skrót)

Perceptron oblicza wartość skalarna `w · x + bias`, a następnie stosuje funkcję progową (Heaviside), która zwraca 0 albo 1. Gdy wynik nie zgadza się z oczekiwaną klasą, wagi i bias są aktualizowane regułą delta.

Bias ma wartość początkową 0.1, a wagi są inicjalizowane stałą wartością 0.05 dla każdej cechy.
