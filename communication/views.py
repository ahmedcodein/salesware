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


def contact(request):
    """
    View function that views the contact
    page
    """
    return render(
        request,
        'communication/contact.html'
    )


def error_404(request, exception):
    """
    View function that views the 404 error
    page
    """
    return render(request, 'communication/404.html')


def error_500(request):
    """
    View function that views the 500 error
    page
    """
    return render(request, 'communication/500.html')
