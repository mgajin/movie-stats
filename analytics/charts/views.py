from django.shortcuts import render
from django.http import JsonResponse


def index(request):
    return render(request, 'charts.html')


def get_data(request):
    labels = ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange']
    data = [12, 19, 3, 5, 2, 3]

    response = {
        'data': data,
        'labels': labels
    }

    return JsonResponse(response)
