<img alt="Logo" src="http://coderslab.pl/svg/logo-coderslab.svg" width="400">

# Django &ndash; Snippety
> Krótkie kawałki kodu, które pokazują zależności, rozwiązują popularne problemy oraz pokazują jak używać niektórych funkcji.


#### 1. Jak utworzyć projekt?
```shell
django-admin startproject coderslab /home/yoda/workspace/
```

Syntax:
```shell
django-admin startproject <nazwa-projektu> <ścieżka-do-projektu>
```

Możesz też pominąć ścieżkę. Wtedy projekt zostanie utworzony w bieżącej lokalizacji w folderze o tej samej nazwie co podana przez Ciebie nazwa projektu

```shell
django-admin startproject coderslab
``` 

Syntax:
```shell
django-admin startproject <nazwa-projektu>
``` 
#### 2. Jak utworzyć aplikację w projekcie?
```shell
python manage.py startapp my_application
```

Syntax:
```shell
python manage.py startapp <app-name>
```

Hint:
Nie zapomnij o zarejestrowaniu aplikacji w pliku `settings.py`
#### 3. Jak ograniczyć dostępne wartości w polu modelu?
Wystarczy utworzyć specjalnie sformatowaną krotkę i użyć parametru `choices`, definiując pole w modelu:

```python
CAR_COLORS = (
    (1, "red"),
    (2, "blue"),
    (3, "white"),
    (4, "black")
)

class Car(models.Model):
    color = models.IntegerField(choices = CAR_COLORS)
    # reszta pól
```

Lub w bardziej elegancki sposób:
```python
class Car(models.Model):
    COLORS = (
        (1, "red"),
        (2, "blue"),
        (3, "white"),
        (4, "black")
)
    color = models.IntegerField(choices = CAR_COLORS)
    # reszta pól
```

#### 4. Jak odczytać opis z pola `choices`, mając do dyspozycji tylko jego wartość?
Musimy użyć dynamicznie tworzonej metody o nazwie `get_<nazwa_pola>_display()`.

Weźmy przykład z pktu 3:
```python
c = Car.objects.get(pk=1)  # pobieramy z bazy danych obiekt typu Car, o id=1
print(c.get_color_display())  # "blue"
```

#### 5. Ważniejsze polecenia `django-admin` / `manage.py`
```shell
python manage.py runserver              # uruchamia serwer deweloperski na porcie 8000
python manage.py runserver 8888         # uruchamia serwer deweloperski na porcie 8888
python manage.py runserver 0.0.0.0      # uruchamia serwer deweloperski i pozwala dostać się do strony z innuch komputerów

python manage.py makemigrations         # tworzy migracje dla wszystkich aplikacji
python manage.py makemigrations app     # tworzy migrację dla aplikacji app
python manage.py migrate                # wykonuje migrację

python manage.py shell                  # uruchamia interaktywną powłokę Pythona z podłączonymi wszystkimi aplikacjami
```
Wszystkie komendy:
https://docs.djangoproject.com/en/2.2/ref/django-admin/#available-commands

#### 6. Utworzenie ciasteczka
```python
HttpResponse.set_cookie(key, value="", max_age=None, expires=None, path="/", domain=None, secure=None, httponly=False)
```
**Przykłady:**

* utworzenie ciasteczka o nazwie **logged_as**, wartości: **admin**, wygasającego za 24h w widoku o nazwie `my_view`:
```python
def my_view(request):
    response = HttpResponse("Hello World!")
    response.set_cookie("logged_as", "admin", max_age=60*60*24)
```

* utworzenie ciasteczka o nazwie **voted**, wartości **1**, wygasa dopiero 1 stycznia 2100 roku. ;-)
```python
from datetime import datetime

def my_view(request):
    cookie_expires = datetime(2100, 1, 1)
    response = render("index.html", ctx)  # Wykorzystanie szablonu "index.html", jest to inny sposób na utworzenie obiektu HttpResponse
    response.set_cookie("voted", "1", expires=cookie_expires)
```

#### 7. Odczytywanie danych z ciasteczek
Ciasteczka znajdują się w obiekcie klasy **HttpRequest**, przekazyanym do widoku:
```python
def my_view(request):
    user_id = request.COOKIES.get("logged_in")
    if user_id:
        # dalsza część widoku
    else:
        # to wykonujemy, jeśli ciasteczka nie ma
```

#### 8. Sesje

* dodanie wartości do sesji:
```python
def my_view(request):
    request.session["nazwa_zmiennej_sesyjnej"] = "wartość"
```

* odczytanie wartości z sesji:
```python
def my_view(request):
    val = request.session.get("nazwa_zmiennej_sesyjnej")  # jeśli nie ma takiej zmiennej, zwróci nam None
    if val:
        # zrób coś ze zmienną sesyjną
    else:
        # zrób coś, jeśli w sesji nie ma zmiennej 
```

#### 9. Jak wyszukiwać w modelach z operatorem OR?
W modelu **User**, przechowującycym dane użytkowników chcemy znaleźć użytkowników o nazwiskach "Kowalski" **lub** "Nowak".

Należy użyć obiektu `Q`:
```python
from django.db.models import Q

data = User.objects.filter(
    Q(last_name="Nowak") | Q(last_name="Kowalski")
)
```
https://docs.djangoproject.com/en/2.2/topics/db/queries/#complex-lookups-with-q-objects
