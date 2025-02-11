from django.shortcuts import render

# Create your views here.
def bottles(request, drink='pop', num_bottles=100):
    context = {
        'drink': drink,
        'num_bottles': str(num_bottles),
        'n': range(num_bottles, 1, -1)
    }
    return render(request, 'dtl/song.html', context)
