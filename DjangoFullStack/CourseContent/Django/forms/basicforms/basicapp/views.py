from django.shortcuts import render
from django.views.generic import CreateView
from basicapp.forms import NewUserForm
# Create your views here.
def index(request):
    return render(request,'basicapp/index.html')

def users(request):
    form = NewUserForm()

    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('Error: Form Inavalid')
    return render(request, 'basicapp/form_page.html',{'form':form})
