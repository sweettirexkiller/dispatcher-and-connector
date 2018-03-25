# Dispatcher-and-connector


Klasa eventDispatcher to jest klasa ‘globalna’
niezalezna od Sklepu i Klienta
i ma on atrybuty eventów i listenerów
oraz funkcje listen oraz fire
najlepiej to zobaczyc na przykladzie
ktory jest na dole
1. tworze klienta czyil siebie
i daje sobie jako jeden argument obiekt dispatcher bym mogl sie do niego odwolywac wewnatrz obiektu
2. towrze random sklep
ktory rowniez ma dostep do dispatchera
potem robie cos takiego: 

![screen](screen1.png)

wewnatrz kontruktora sklepu ‘rejestruje’ event

![screen](screen2.png)


ktory potem wywoluje podczas dodawania produktu
i kończąc
wewntrz ‘mnie’ czyli kliena
tworze fukncje odpowiadającą eventowi.

![screen](screen3.png)
