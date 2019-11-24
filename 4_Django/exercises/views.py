from django.http import HttpResponse
from django.shortcuts import render

from exercises.models import Band


def hello_word(request):
    return HttpResponse("Hello word")


def show_number(request, number, number2, **kwargs):
    print(kwargs)
    print("numer is:", request.GET.get("numer"))
    answer = """<html>
<body>
<p>
The answer is {}!
<br/>
The answer2 is {}!
</p>
</body>
</html>""".format(number, number2)
    return HttpResponse(answer)


def show_the(request):
    bands_query_set = Band.objects.filter(name__contains="The")
    return HttpResponse(bands_query_set)


def show_all_bands(request):
    bands = Band.objects.all()
    print(bands)
    print(list(bands))
    first_band = bands.first()
    print(first_band)
    print(first_band.name)
    return render(request, 'exercises/bands.html',
                  context={'bands': bands})


def show_active_80s(request):
    b = Band.objects.filter(year__gte=1980, year__lt=1990, still_active=True)
    return render(request, 'exercises/bands.html',
                  context={'bands': b})


def show_the_70s(request):
    b = Band.objects.filter(year__gte=1970, year__lt=1980, name__contains="The")
    return render(request, 'exercises/bands.html',
                  context={'bands': b})


def show_inactive_80s(request):
    b = Band.objects.filter(year__gte=1980, year__lt=1990, still_active=False)
    return render(request, 'exercises/bands.html',
                  context={'bands': b})
