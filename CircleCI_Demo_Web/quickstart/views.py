from django.http import HttpResponse


def home_view(request, **kwargs):
    return HttpResponse("CICD Demo", status=200)