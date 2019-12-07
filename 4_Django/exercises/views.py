from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

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


@csrf_exempt
def start_end(request):
    result = []
    start_get = int(request.GET.get('start'))
    end_get = int(request.GET.get('end'))
    if start_get is not None and end_get is not None:
        for i in range(start_get, end_get + 1):
            result.append(i)
        return HttpResponse(f'''{result}''')
    else:
        return HttpResponse('Podaj poprawne parametry!!')


@csrf_exempt
def width_height(request):
    result = ''
    width_get = int(request.GET.get('width'))
    height_get = int(request.GET.get('height'))
    if width_get is not None and height_get is not None:
        for i in range(1, width_get + 1):
            for n in range(1, height_get + 1):
                result += f' {i * n} '
            result += '<br>'
        return HttpResponse(result)
    else:
        return HttpResponse('Podaj poprawne parametry!!')
