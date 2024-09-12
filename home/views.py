from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime

def credits(_request):
    content = "Nicky\nUrch"

    return HttpResponse(content, content_type="text/plain")

def about(_request):
    content = "<h1>About Page</h1>"

    return HttpResponse(content, content_type="text/HTML")


def news(request):
    data = {
        'news': [
            "RiffMate now has a news page!",
            "RiffMate has its first web page.",
        ],
    }

    return render(request, "news2.html", data)

def news_advanced(request):
    """Example of news data: list of tuples (date, subject)"""
    news_items = [
        (datetime(2023, 9, 1), 'New Django Version Release'),
        (datetime(2023, 8, 25), "DjangoCon Us 2023 Recap"),
        (datetime(2023, 8, 15), "Python 3.11 Features Overview"),
        (datetime(2023, 7, 30), "Django Security Update Release"),
        (datetime(2023, 6, 10), "Django 4.2 Release with New Features"),
    ]

    return render(request, 'news_adv.html', {'news_items': news_items})
