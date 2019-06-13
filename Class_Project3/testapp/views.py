from django.shortcuts import render
from testapp.models import company
from django.views.generic import DeleteView, ListView,DetailView,UpdateView,CreateView
from django.core.urlresolvers import reverse_lazy

# Create your views here.

class companylist(ListView):
    model = company

class companydetail(DetailView):
    model = company

class companycreateview(CreateView):
    model = company
    fields = ('name','ceo','city')

class companyupdateview(UpdateView):
    model = company
    fields = ('name','ceo','city')

class companydeleteview(DeleteView):
    model = company
    success_url = reverse_lazy('company')
