from django.shortcuts import render

# Create your views here.
def bottles(request):
    context = {'drink' : 'pop' }
    return render(request, 'dtl/song.html', context)
