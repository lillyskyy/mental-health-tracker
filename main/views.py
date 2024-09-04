from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2306165572',
        'name': 'Ananda Dwi Hanifa',
        'class': 'PBP F'
    }

    return render(request, "main.html", context)