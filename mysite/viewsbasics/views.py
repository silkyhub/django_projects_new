from django.http import HttpResponse


def danger(request) :
    f = open('viewsbasics/templates/viewsbasics/top.html', 'r')
    top = f.read()
    f.close()
    f = open('viewsbasics/templates/viewsbasics/bottom.html', 'r')
    bottom = f.read()
    f.close()
    response = top + request.GET['thing'] + bottom
    return HttpResponse(response)
