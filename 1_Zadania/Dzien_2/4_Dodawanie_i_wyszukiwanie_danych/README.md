<img alt="Logo" src="http://coderslab.pl/svg/logo-coderslab.svg" width="400">

# Dodawanie i wyszukiwanie danych &ndash; zadania

##### Wszystkie zadania wykonuj używając Django ORM.

#### Zadanie 1 &ndash; wykonywane razem z wykładowcą.

W aplikacji **exercises**, w modelu `Band` znajduje się kilkanaście zespołów. 

* Wyciągnij dane wszystkich zespołów.
* Posortuj je alfabetycznie.
* Dodaj dane zespołu Rage Against The Machine, rok założenia 1991.

Zadania roziąż w konsoli interaktywnej (`python manage.py shell`)

Hint: Jak doinstalujesz **ipython** (`pip install ipython`) shell będzie kolorował składnię, oraz podpowiadał komendy przy użyciu przycisku **tab**

---

#### Zadanie 2.

* Znajdź wszystkie zespoły, które nie mają zdefinowanego roku założenia. Wypisz w konsoli ich nazwy i identyfikator nadany przez bazę danych.
* Znajdź informacje o zespołach, które nie mają w naszej bazie podanego roku założenia. Uzupełnij informacje (może być losowo) i zapisz je w bazie danych.

##### Skorzystaj z powłoki interaktywnej **django** (`python manage.py shell`)

Hint: Możesz napisać funkcję, którą następnie zaimportujesz i wywołasz w powłoce django.
Zwykły skrypt nie zadziała, ponieważ nie będzie miał skonfigurowanej bazy danych oraz aplikacji django.

**Dla chętnych**: Możesz napisać własną komendę, która będzie uruchamiana z poziomu **manage.py**

https://docs.djangoproject.com/en/dev/howto/custom-management-commands/

#### Zadanie 3.

* Uzupełnij gatunki zespołów oraz informację, czy są nadal aktywne. 

##### Skorzystaj z powłoki interaktywnej **django** (`python manage.py shell`)

Hint: Możesz napisać funkcję, którą następnie zaimportujesz i wywołasz w powłoce django.
Zwykły skrypt nie zadziała, ponieważ nie będzie miał skonfigurowanej bazy danych oraz aplikacji django.

**Dla chętnych**: Możesz napisać własną komendę, która będzie uruchamiana z poziomu **manage.py**

https://docs.djangoproject.com/en/dev/howto/custom-management-commands/

#### Zadanie 4.

Znajdź i wypisz na konsoli wszystkie zespoły, które:

* Mają w nazwie "The",
* założone zostały w latach 1980-tych i są wciąż aktywne,
* założone zostały w latach 1970-tych oraz mają w nazwie "The",
* założone zostały w latach 1980-tych, oraz są już nieaktywne. 

#### Zadanie 5.

* Do modelu `Category` z poprzedniej części, dodaj kilka wybranych kategorii,
* Dodaj kilka artykułów do modelu `Article`.

Nie dodawaj tytułu ani zawartości losowo, skorzystaj z http://randomtextgenerator.com/

#### Zadanie 6.

Napisz widok, który udostępnisz pod adresem `/articles`, w którym pokażesz listę artykułów. Na liście powinien pojawić się tytuł, autor (jeśli jest) i data dodania artykułu do bazy. Wybierz tylko artykuły ze statusem "opublikowany".

W tym celu w widoku wyciągnij wszystkie opublikowane artykuły z bazy danych, i przekaż je przy użyciu metody `format`, do stringa z kodem **html**, który wyświetli odpowiednio dane.

**Dla chętnych**:
Zamiast pisać kod **html** w zmiennej w widoku, możesz użyć zewnętrznego pliku **html** (tak zwanego szablonu). 
Więcej na ten temat znajdziesz w jednej z prezentacji z tego modułu, lub w oficjalnej dokumentacji:
https://docs.djangoproject.com/en/2.2/ref/templates/