from django.http import HttpResponse

def get_page(request):
	return HttpResponse('OK')


def ai_response(request):
	return HttpResponse('odp')
