from django.http import HttpResponse

from nn import ai_tree


def ai_response(request):
    odp = ai_tree.predict(**request.GET)
    return HttpResponse(odp)
