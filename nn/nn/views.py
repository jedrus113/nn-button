from django.http import HttpResponse

from nn import ai_tree


def ai_response(request):
    odp = ai_tree.predict(**request.GET)
    s = str(odp[0])
    for x in odp[1:]:
    	s += f",{x}"
    return HttpResponse(s)
