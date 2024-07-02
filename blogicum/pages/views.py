from django.shortcuts import render


def about(request):

    template = 'pages/about.html'
    """View-функция для просмотра информации о странице"""
    return render(request, template)


def rules(request):
    """View-функция для просмотра правил сайта"""
    template = 'pages/rules.html'
    return render(request, template)
