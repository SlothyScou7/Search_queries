from django.shortcuts import render
from django.db.models import Q
from django.http import HttpResponse
from .models import City
# Create your views here.
from django.views.generic import TemplateView, ListView

from .models import City


class HomePageView(TemplateView):
    template_name = 'home.html'

class SearchResultsView(ListView):
    model = City
    template_name = 'search_results.html'

    def get_queryset(self): # new
        query = self.request.GET.get('q')
        return City.objects.filter(Q(name__icontains=query) | Q(state__icontains=query)
        )
import pandas as pd
def dataBase(request):
    dataset = pd.read_excel('uscities.xlsx')
    print(len(dataset))
    for i in range(0,1000): # selecting 4 values for now
        flag = 0
        c = City(name=dataset.name[i],state=dataset.state[i])
        var = City.objects.all().values_list() # this is a list of tuples now
        for j in range(len(var)):
            # for not having duplicates in the database
            # now we are searching for same name cities
            if var[j][1]== c.name and var[j][2] == c.state:# this gives us the city name
                flag = 1
        print("the value of flag is:",flag)
        if flag == 0:
            c.save()
        
        
            
    return HttpResponse("<h1>If You are reading this then your database is updated...</h1>")