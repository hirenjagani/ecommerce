from django.http import Http404
from .models import Product
from django.views.generic import ListView,DetailView
from django.shortcuts import render, get_object_or_404
from cart.forms import CartAddProductForm


# Create your views here.
def productlist(request):
    prod_list = Product.objects.all()
    context = {
        'object_list': prod_list
    }
    return render(request, 'product.html', context)


def productdetail(request, pk=None, *args, **kwargs):
    prod_detail=get_object_or_404(Product,pk=pk)
    #  try:
    #      prod_detail=Product.objects.get(id=pk)
    #  except Product.DoesNotExist:
    #      print("no product here")
    #      raise Http404("product doesnot exist")
    #  except:
    #      print("hey")
    #----------
    # prod_detail = Product.objects.get_by_id(pk)
    # if prod_detail is None:
    #     raise Http404("product doesnot exist")
    #-------
    cart_product_form=CartAddProductForm()
    context = {
        'product_detail': prod_detail,
        'cart_product_form':cart_product_form
    }

    return render(request, 'productdetail.html', context)

class ProductFeaturedList(ListView):
    template_name="product.html"

    def get_queryset(self,*args,**kwargs):
        request=self.request
        return Product.objects.featured()

# class ProductFeaturedDetail(DetailView):
#     prod_detail = Product.objects.featured()
#     template="productfeatureddetail.html"

    # def get_queryset(self,*args,**kwargs):
    #     request=self.request
    #     return Product.objects.featured()


# class ProductDetailSlugView(DetailView):
#     prod_detail = Product.objects.all()
#     template_name = "productdetail.html"
#
#     def get_object(self, *args, **kwargs):
#         request = self.request
#         slug = self.kwargs.get('slug')
#         #instance = get_object_or_404(Product, slug=slug, active=True)
#         try:
#             instance = Product.objects.get(slug=slug, active=True)
#         except Product.DoesNotExist:
#             raise Http404("Not found..")
#         except Product.MultipleObjectsReturned:
#             qs = Product.objects.filter(slug=slug, active=True)
#             instance = qs.first()
#         except:
#             raise Http404("Uhhmmm ")
#         return instance