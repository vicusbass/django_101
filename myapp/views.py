from django.shortcuts import render
from django.views.generic import View
from .forms import ContactForm

# Create your views here.
def fbv(request):
    if request.method=='POST':
        form=ContactForm(request.POST)
    return render(request, 'myapp/fbv.html')


class CBV(View):
    def get(self, request):
        return render(request, 'myapp/cbv.html')

