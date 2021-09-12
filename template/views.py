from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods


@require_http_methods(['GET', 'POST'])
def echo(request):
    if request.method == 'GET':
        params = request.GET
        x_print_statement = request.META.get('HTTP_X_PRINT_STATEMENT')
    elif request.method == 'POST':
        params = request.POST
        x_print_statement = request.POST.get('HTTP_X_PRINT_STATEMENT')

    method = request.method.lower()
    result_string = ''

    for a in params.items():
        result_string += f'{a[0]}: {a[1]} '

    if x_print_statement:
        body = f'{method} {result_string}{x_print_statement}'
    else:
        body = f'{method} {result_string}statement is empty'

    return HttpResponse(status=200, content=body)


def filters(request):
    return render(request, 'filters.html', context={
        'a': request.GET.get('a', 1),
        'b': request.GET.get('b', 1)
    })


def extend(request):
    return render(request, 'extend.html', context={
        'a': request.GET.get('a'),
        'b': request.GET.get('b')
    })
