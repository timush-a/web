from django.http import HttpResponse
from django.views.decorators.http import require_GET, require_POST


@require_GET
def simple_route(request):
    return HttpResponse(content='')


@require_GET
def slug_route(request):
    return HttpResponse(content=request.path.split('/')[3])


@require_GET
def sum_route(request):
    first_value = int(request.path.split('/')[3])
    second_value = int(request.path.split('/')[4])
    result = first_value + second_value
    return HttpResponse(content=result)


@require_GET
def sum_get_method(request):
    try:
        a = int(request.GET.get('a'))
    except (TypeError, ValueError):
        a = None

    try:
        b = int(request.GET.get('b'))
    except (TypeError, ValueError):
        b = None

    if not (a and b):
        return HttpResponse(content='', status=400)

    return HttpResponse(content=(a + b))


@require_POST
def sum_post_method(request):
    try:
        a = int(request.POST.get('a'))
    except (TypeError, ValueError):
        a = None

    try:
        b = int(request.POST.get('b'))
    except (TypeError, ValueError):
        b = None

    if not (a and b):
        return HttpResponse(content='', status=400)

    return HttpResponse(content=(a + b))
