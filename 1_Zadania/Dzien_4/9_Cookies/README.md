<img alt="Logo" src="http://coderslab.pl/svg/logo-coderslab.svg" width="400">

# Przekazywanie informacji między stronami: ciasteczka.

### Zadanie 1
W tym zadaniu stwórz trzy strony:
* Pierwszy widok, przypisany do adresu `/set-cookie/`, ma nastawiać ciasteczko o nazwie ```User``` na Twoje imię.
* Drugi widok, przypisany do adresu `/show-cookie/`, ma wyświetlać zawartość ciasteczka ```User```. Jeżeli nie ma takiego ciasteczka, to powinna wyświetlić odpowiednie informacje.
* Trzeci widok, przypisany do adresu `/delete-cookie/`, powinien kasować ciasteczko o nazwie ```User```. 

### Zadanie 2.
Napisz widok pod adresem `/add-to-cookie/` który wyświetli następujący formularz:  
```html
<form action="#" method="POST">
    <label>
        Klucz:
        <input type="text" name="key">
    </label>
    <label>
        Wartość:
        <input type="text" name="value">
    </label>
    <input type="submit" name="convertionType">
</form>
  ``` 
W przypadku wejścia na tą stronę metodą POST widok powinien dodawać do ciasteczek przesłaną wartość (pod odpowiedni nazwę).  
Następnie napisz widok pod adresem `/show-all-cookies/` który wyświetli w formie tabeli wszystkie dane znajdujące się w ciasteczkach do których masz dostep (zarówno nazwę ciasteczka jak i wartość). 

**Podpowiedź:** Widok będzie oczekiwał tokena CSRF i jeśli go nie znajdzie, zgłosi błąd i nie przepuści użytkownika dalej. Aby temu zapobiec (tylko na potrzeby ćwiczenia, CSRF to dość skuteczne zabezpieczenie przed włamaniami na stronę), należy użyć dekoratora:

```python
@csrf_exempt
def my_view(request):
    . . . 
```

**Dla chętnych:**
Kod **HTML** możesz umieścić w zewnętrznym pliku i przekazać dane za pomocą kontekstu. Więcej na ten temat znajdziesz w jednej z dodatkowych prezentacji **SZABLONY_WSTEP_DO_WARSZTATOW**.

### Zadanie 3(*).

Stwórz widok `set_as_favourite` (udostępnij go pod odpowiednim  URL-em), który przyjmie paramter ID metodą GET, po czym:
* sprawdzi, czy ID jest poprawną liczbą, jeśli nie -- wyświetli informację o błędzie,
* sprawdzi, czy identyfikator istnieje w bazie danych (czy istnieje klub o takim ID). Jeśli nie -- wyświetli błąd 404,
* jeśli id jest poprawny, ustaw ciasteczko, ważne przez rok, w którym zapiszesz informację, który klub jest ulubionym klubem użytkownika.

### Zadanie 4(*).

Zmodyfikuj widok `league_table` tak, aby:
* ulubiony klub wyświetlał się na czerwono (odczytaj wartość ciasteczka),
* przy każdym klubie był link "zaznacz, jako ulubiony", z wygenerowanym odpowiednim ID, prowadzący do widoku `/set-as-favourite/`.
