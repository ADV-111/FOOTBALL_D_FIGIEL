<img alt="Logo" src="http://coderslab.pl/svg/logo-coderslab.svg" width="400">

# Przekazywanie informacji między stronami: sesje.
Upewnij się, czy frameworki sesji są podłączone do aplikacji (plik **settings.py**),

### Zadanie 1.
W zadaniu stwórz trzy widoki, które mają mieć następującą funkcjonalność:
* Pierwszy widok ma być przypisany pod adres `/set-session/` ma nastawiać informacje w sesji pod kluczem ```counter``` na **0**.
* Drugi widok ma być przypisany pod adres `/show-session/`  wyświetlać zawartość sesji pod kluczem ```counter``` i zwiększać ją o **1**. Jeżeli nie ma takich danych w sesji, to strona powinna wyświetlić odpowiednie informacje.
* Trzeci widok ma być przypisany pod adres `/delete-session/`  kasować dane z sesji (tylko te trzymane pod kluczem ```counter```).

### Zadanie 2.
Napisz widok przypisany pod adres `/login/`. Widok ten powinien:
* W przypadku w którym wejdziemy na niego metodą GET wyświetlić formularz do logowania:  
```html
<form action="" method="POST">
    <label>
        Imię:
        <input type="text" name="name">
    </label>
    <input type="submit">
</form>
``` 
* W przypadku przesłania danych POST do sesji pod kluczem `loggedUser` wpisz przesłane imię.
* W przypadku w którym wejdziemy na niego metodą GET, a sesji są informacji pod kluczem `loggedUser` wyświetl komunikat `Witaj <imię>` - ta część polecenia wymaga modyfikacji kodu napisanego w pierwszym punkcie.

**Podpowiedź:** Widok będzie oczekiwał tokena CSRF i jeśli go nie znajdzie, zgłosi błąd i nie przepuści użytkownika dalej. Aby temu zapobiec (tylko na potrzeby ćwiczenia, CSRF to dość skuteczne zabezpieczenie przed włamaniami na stronę), należy użyć dekoratora:

```python
@csrf_exempt
def my_view(request):
    . . . 
```

**Dla chętnych:**
Kod **HTML** możesz umieścić w zewnętrznym pliku i przekazać dane za pomocą kontekstu. Więcej na ten temat znajdziesz w jednej z dodatkowych prezentacji **SZABLONY_WSTEP_DO_WARSZTATOW**.

### Zadanie 3.
Napisz widok pod adresem `/add-to-session/` który wyświetli następujący formularz:  
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
    <input type="submit">
</form>
  ``` 
W przypadku wejścia na tą stronę metodą POST widok powinien dodawać do sesji przesłaną wartość (pod odpowiedni klucz).  
Następnie napisz widok pod adresem `/show-all-session/` który wyświetli w formie tabeli wszystkie dane znajdujące się w sesji (zarówno klucz jak i wartość). 

**Podpowiedź:** Widok będzie oczekiwał tokena CSRF i jeśli go nie znajdzie, zgłosi błąd i nie przepuści użytkownika dalej. Aby temu zapobiec (tylko na potrzeby ćwiczenia, CSRF to dość skuteczne zabezpieczenie przed włamaniami na stronę), należy użyć dekoratora:

```python
@csrf_exempt
def my_view(request):
    . . . 
```

**Dla chętnych:**
Kod **HTML** możesz umieścić w zewnętrznym pliku i przekazać dane za pomocą kontekstu. Więcej na ten temat znajdziesz w jednej z dodatkowych prezentacji **SZABLONY_WSTEP_DO_WARSZTATOW**.

### Zadanie 4 (*).

* zmodyfikuj widok `add_game` tak, aby zapamiętać w sesji, który zespół był ostatnio edytowany (jako gospodarz),
* podczas ponownego wejścia na stronę odczytać zmienną sesyjną i ustawić listę HTML na pozycji odpowiadającej ostatnio edytowanemu klubowi (`<option ... selected>`)
