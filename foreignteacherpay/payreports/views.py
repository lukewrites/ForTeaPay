from django.shortcuts import render
from django.views import generic
from forms import EmployerForm

from .models import Employer

# Create your views here.
def index(request):
    if request.method=='POST':
        form = EmployerForm(request.POST)
        # form.teacher = 1
        if form.is_valid():
            form.save()
            return thanks(request)
        else:
            print(form.errors)
    else:
        form = EmployerForm()
    context_dict = {'form': form}
    return render(request, 'index.html', context_dict)


def thanks(request):
    return render(request, 'thanks.html')


class IndexView(generic.ListView):
    template_name = 'schools.html'
    context_object_name = 'school_list'

    def get_queryset(self):
        return Employer.objects.order_by('school_province')


def schools(request):
    context_dict = {''}
    return render(request, 'schools.html', context_dict)