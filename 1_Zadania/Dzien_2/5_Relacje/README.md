<img alt="Logo" src="http://coderslab.pl/svg/logo-coderslab.svg" width="400">

# Relacje &ndash; zadania

##### Wszystkie zadania wykonuj używając Django ORM.

#### Zadanie 1 &ndash; wykonywane razem z wykładowcą.
* W jednym z poprzednich zadań, utworzyliśmy model `Album`. Teraz dodaj odpowiednią relację z modelem `Band`, tak by jeden zespół mógł mieć wiele albumów.

* Dodaj kilka albumów do kilku zespołów (nie szukaj ich w internecie, możesz coś wymyślić). 

* Wypisz w konsoli wszystkie albumy dowolnego zespołu.

---

#### Zadanie 2.

Dodaj do modeli kolejny: `Song`. Powinien mieć następujące pola:
* `title`: string, max długość 128 znaków,
* `duration`: czas (TimeField), może przyjmować null,
* dodaj relację wiele-do-jednego tak, aby jeden album mógł mieć wiele piosenek.

Uzupełnij dane, tworząc albumy grup i uzupełniając je piosenkami (nie przejmuj się, czy piosenki są prawdziwe, po prostu je dodaj).

#### Zadanie 3.

Wyciągnij z bazy danych (i wypisz na konsoli), używając modeli:

* wszystkie albumy dowolnego zespołu,
* wszystkie piosenki z każdego albumu.

#### Zadanie 4.

* Połącz modele `Article` i `Category` tak, aby jeden artykuł mógł mieć wiele kategorii, a każda kategoria mogła być przypisana do wielu artykułów.
* Dodaj kilka kategorii do każdego artykułu.

Podpowiedź: Relaję wiele do wielu możesz zaczepić w dowolnym modelu:
* Możesz dodać pole categpories w modelu Article
* Możesz dodać pole articles w modelu Category
#### Zadanie 5.

* Wybierz kategorię. Następnie wybierz (i wypisz na konsoli) wszystkie artykuły należące do tej kategorii.
* Wybierz dwie kategorie. Następnie wybierz i wypisz na konsoli wszystkie artykuły należące *jednocześnie* do obu kategorii.

#### Zadanie 6.
* Napisz model `Person`, który będzie miał następującą właściwość:
    * `name`,
* Napisz model `Position`, który będzie miał następujące właściwości:
    * `position_name`,
    * `salary`,
* Połącz oba modele relacją tak, aby jedna osoba mogła być przypisana dokładnie do jednego stanowiska, a każde stanowisko miało tylko jednego pracownika. Zadbaj o to, by wraz z usunięciem stanowiska, usuwana była też przyporządkowana do niego osoba.
Hint:
Masz dwa sposoby:
- albo dodajesz pole `person` w modelu `Position`
- albo dodajesz pole `position` w modelu `Person`

* Dodaj kilka osób i stanowisk.


#### Zadanie 7.

Napisz widok i udostępnij go pod adresem `/show-band/{id}/`, gdzie **id** to identyfikator zespołu. Widok powinien wyświetlić informacje o zespole muzycznym: jego nazwę, gatunek i rok założenia oraz informację, czy wciąż jest aktywny. 

W tym celu w widoku musisz pobrać parametrem z URL-a id zespołu, wyciągnąć przy użyciu modelu dane zespołu i przekazać je  za pomocą instrukcji `format` do stringa z kodem HTML. 

Zwróć uwagę, że jeśli w zadaniu 1 dodałeś klucz obcy Band - Album, to w modelu `Band` masz pole, które przechowuje listę albumów danego zespołu. Pokaż albumy w szablonie. 

**Hint:** użyj następującego wyrażenia regularnego, do zdefiniowania URL-a: 
```
^/show-band/(?P<id>\d+)/$
```

Możesz też użyć instrukcji **path** podając ścieżkę w prostszy sposób:
```
/show-band/<int:id>/
```

**Dla chętnych:**
Kod **HTML** możesz umieścić w zewnętrznym pliku i przekazać dane za pomocą kontekstu. Więcej na ten temat znajdziesz w jednej z dodatkowych prezentacji **SZABLONY_WSTEP_DO_WARSZTATOW**.


## Zadanie 8 (*).
1. Zapoznaj się z aplikacją **football** i sprawdź, czy jest zarejestrowana w projekcie.
2. Zapoznaj się ze strukturą bazy danych, znajdującą się w pliku **models.py**.
3. Wykonaj migrację, aby dodać odpowiednie tabele do bazy danych.
4. W katalogu `management` znajduje się komenda ładująca przykładowe dane do bazy. 
Możesz zapoznać się z zawartością tego katalogu. Uruchom komendę `python manage.py insert_football_data`.
5. Utwórz widok `league_table`, który:
    * wyciągnie z bazy danych ligową tabelę posortowaną wg liczby zdobytych punktów,
    * utworzy HTML, w którym znajdą się następujące dane:
        * pozycja w tabeli,
        * nazwa klubu,
        * liczba punktów,
    * zwróci wynik do przeglądarki.
6. utwórz wpis w pliku **urls.py**, który udostępni aplikacji widok `league_table` pod URL-em `/table/`.

**Podpowiedź:**

Aby zobaczyć informacje o dostępnych komendach wpisz:
```
python manage.py help
```
Aby załadować dane uruchom komendę:
```
python manage.py insert_football_data
```
Więcej o własnych komendach django możesz doczytać tutaj: https://docs.djangoproject.com/en/2.2/howto/custom-management-commands/



## Zadanie 9 (*).
1. Wybierz swój ulubiony klub piłkarski z tabeli (np. Naprzód Brwinów).
2. Utwórz widok `games_played`, który:
    * wyciągnie z tabeli wszystkie mecze, które rozegrał klub (zarówno te w domu, jak i na wyjeździe),
    * utworzy HTML, w którym znajdą się następujące dane:
        * nazwa klubu gospodarza,
        * nazwa klubu gościa,
        * wynik (np. 2:0),
    * zwróci wynik do przeglądarki.
3. Utwórz wpis w pliku **urls.py**, który udostępni aplikacji widok `games_played` pod URL-em `/games/`.

### Podpowiedzi do zadań 8 i 9

* Do operacji na bazach danych użyj modeli.

* Możesz zapoznać się z materiałami pod poniższymi linkami. Dowiesz się, jak poradzić sobie z tworzeniem modeli do istniejących już baz danych:
    * https://docs.djangoproject.com/en/2.2/ref/django-admin/#inspectdb
    * https://docs.djangoproject.com/en/2.2/howto/legacy-databases/

* Aby przećwiczyć import danych powyższym sposobem, możesz wykorzystać plik `football.sql`. 
Efekt powinien być podobny, jak przy uruchomieniu migracji i użyciu komendy `insert_football_data`.
Możesz w tym celu utworzyć nowy projekt django i spróbować zaimportować bazę z istniejącego pliku. 