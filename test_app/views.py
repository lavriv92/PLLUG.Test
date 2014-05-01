from django.shortcuts import render

from .models import Student


def test(request):
    data = Student.objects.all()
    return render(request, 'test.html', {'data': data})
