from django.shortcuts import render
from django.views.generic import ListView
from product.models import Product
#from django.apps import apps
#Product=apps.get_model('product','Product')

class SearchProductView(ListView):
    template_name = "searchproduct.html"


    def get_context_data(self, *args, **kwargs):
        context = super(SearchProductView, self).get_context_data(*args, **kwargs)
        query = self.request.GET.get('q')
        print(query)
        context['query'] = query
        # SearchQuery.objects.create(query=query)
        return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        method_dict = request.GET

        query = method_dict.get('q',None)  # method_dict['q']

        if query is not None:
            return Product.objects.filter(name__icontains=query)

        return Product.objects.none()



def search_query(request):
    query=request.GET.get('q')
    return render(request,'searchproduct.html',{'query':query})