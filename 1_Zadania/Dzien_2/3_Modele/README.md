<img alt="Logo" src="http://coderslab.pl/svg/logo-coderslab.svg" width="400">

# Modele &ndash; zadania

Pamiętaj, aby wszystkie modele definiować w pliku **models.py**!

## Zadanie 1 – rozwiązywane z wykładowcą

Zajrzyj do katalogu 4_Django. Znajdziesz tam projekt o nazwie **coderslab**. 
* Sprawdź plik **settings.py**, czy wszystko jest skonfigurowane poprawnie. 
* Utwórz wirtualne środowisko.
* Zainstaluj potrzebne biblioteki. (Możesz skorzystać z pliku **requirements.txt**: `pip install -r requirements.txt`)
* Załóż bazę danych o odpowiedniej nazwie. 
* Wykonaj migrację i uruchom projekt.

## Zadanie 2 – rozwiązywane z wykładowcą

Zajrzyj do aplikacji **exercises** w projekcie **coderslab**. Znajdziesz tam model `Band`, który zawiera informację o zespołach rockowych. Znajdziesz tam zdefiniowane dwa pola: `name` – nazwę zespołu i `year` – rok założenia zespołu.

Dodaj tam pola:
* `still_active`: czy zespół jest jeszcze aktywny. Pole powinno przyjmować typ boolean, domyślna wartość `True`.
* `genre`: pole typu integer, które powinno przyjmować wartości:
  * -1: not defined,
  * 0: rock,
  * 1: metal,
  * 2: pop,
  * 3: hip-hop,
  * 4: electronic,
  * 5: reggae,
  * 6: other.

Pole powinno domyślnie przyjąć wartość -1.

Hint: Skorzystaj z parametru **choices**. Więcej znajdziesz w sekcji **3_Snippets** w tym repozytorium

---

## Zadanie 3.

Utwórz model `Category`, który będzie przechowywał listę wszystkich kategorii w CMS-ie. Model powinien mieć pola:
* `name`: string, max 64 znaki,
* `description`: nielimitowanej długości string. Może przyjmować wartość `null`.


>CMS (Content Management System) - system zarządzania treścią.
>https://pl.wikipedia.org/wiki/System_zarz%C4%85dzania_tre%C5%9Bci%C4%85

## Zadanie 4.

a. Utwórz model `Article`, który będzie przechowywał dane nt. artykułów w CMS-ie. Model powinien mieć następujące pola:

* `title`: string, max. 128 znaków,
* `author`: string, max. 64 znaki, może przyjmować wartość `null`,
* `content`: nielimitowanej długości string,
* `date_added`: pole typu datetime, wartość ma być automatyczniee dodawana podczas pierwszego zapisu (podpowiedź: `auto_now_add=True`).

b. Model `Article` potrzebuje jeszcze kilku pól:

* statusu, który będzie przyjmował następujące wartości:
    * w trakcie pisania,
    * czeka na akceptację redaktora,
    * opublikowany
    (podpowiedź: atrybut **choices**),
* daty początku emisji (pole może przyjmować wartość null),
* daty końca emisji (pole może przyjmować wartość null).

Zdefiniuj te właściwości, odpowiednio dobierając typy pól.

## Zadanie 5.

Utwórz model `Album`, który będzie przechowywał następujące wartości:
* tytuł albumu,
* rok wydania,
* ocenę (w skali 0-5 gwiazdek) (podpowiedź: **choices**).

Zdefiniuj te właściwości, odpowiednio dobierając typy pól.
