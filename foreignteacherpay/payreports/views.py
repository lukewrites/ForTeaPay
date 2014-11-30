from django.shortcuts import render
from django.views import generic
from forms import EmployerForm

# Create your views here.
def index(request):
    if request.method=='POST':
        form = EmployerForm(request.POST)
        if form.is_valid():
            form.save()
            return index(request)
        else:
            print(form.errors)
    else:
        form = EmployerForm()
    context_dict = {'form': form}
    return render(request, 'index.html', context_dict)


def thanks(request):
    return render(request, 'thanks.html')