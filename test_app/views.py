from django.shortcuts import render

from .models import Student
from .forms import GroupForm


def test(request):
    form = GroupForm(request.POST or None)
    data = Student.objects.all()
    if request.method == 'POST' and form.is_valid():

        print "is valid"

    else:
        print form.errors
    obj = {
        'data': data,
        'form': form
    }
    return render(request, 'test.html', obj)
