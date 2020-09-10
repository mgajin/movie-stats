from django.shortcuts import render
from django.views import View


class HomeView(View):
    def get(self, request):
        return render(request, 'pages/index.html')


class NotFoundView(View):
    def get(self, request):
        return render(request, 'pages/not_found.html')
