from django.shortcuts import render


def home(request):
    """
    The view handles the presentation
    of the home page
    """
    return render(
        request,
        'home.html'
    )
