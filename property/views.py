from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView , CreateView
from django.views.generic.edit import FormMixin
from .models import Property
from .forms import PropertyBookForm
from .filters import PropertyFilter
from django_filters.views import FilterView
# Create your views here.


class PropertyList(FilterView):
    model = Property
    paginate_by = 1
    filterset_class = PropertyFilter
    template_name = 'property/property_list.html'


class PropertyDetail(FormMixin,DetailView):
    model = Property
    form_class = PropertyBookForm
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['related'] = Property.objects.filter(category=self.get_object().category)[:2]
        return context
        
    def post(self,request,*args,**kwargs):
        form = self.get_form()
        if form.is_valid():
            myform = form.save(commit=False)
            myform.property = self.get_object()
            myform.user = request.user
            myform.save()
            
            return redirect('/property')
            
class AddListing(CreateView):
    pass