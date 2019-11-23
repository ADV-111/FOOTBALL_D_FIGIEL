<img alt="Logo" src="http://coderslab.pl/svg/logo-coderslab.svg" width="400">

# Klasy widoków

### Zadanie 1.

Napisz widok bazujący na klasie, który po wejściu metodą `GET` wyświetli formularz przyjmujący imię i nazwisko. 
Formularz ten ma przekierowywać na ten sam adres metodą `POST`.
Jeżeli strona została uruchomiona przez zapytanie POST, to ponad formularzem ma się wyświetlić napis `Witaj, <podane imię> <podane nazwisko>`. 
Możesz przerobić widok z zadania 1 z działu **POST formularze**
 
### Zadanie 2.

Analogicznie do poprzedniego zadania, przerób zadanie 2 z działu **POST formularze** tak, aby korzystało z **klasy** widoku.

### Zadanie 3.

Przypomnij sobie zadanie 2 z działu **Modele**.
Napisz widok z użyciem klasy. Po wejściu metodą `GET` użytkownik powinien zobaczyć formularz z danymi na temat zespołu:
* name - nazwa zespołu
* year - rok założenia
* still_active - czy dalej aktywny
* genre - gatunek (pole typu select)

Po kliknięciu **Submit** dane powinny zostać przekazane na ten sam widok metodą `POST`.
Po wejściu metodą **POST** przechwyć dane z formularza i dodaj nowy zespół do bazy danych. Następnie wyświetl użytkownikowi komunikat:

`Zespół <name> został pomyślnie zapisany w bazie danych!`,

gdzie `<name>` to zespołu, który został dodany do bazy.

### Zadanie 4 (*)

Popraw widoki w aplikacji football, tak aby bazowały na klasach. Pamiętaj o odpowiednich zmianach w pliku **urls.py**.

