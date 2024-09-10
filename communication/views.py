from django.shortcuts import render

# Create your views here.


def home(request):
    """
    View function that views the home
    page
    """
    return render(
        request,
        'communication/home.html',
    )
