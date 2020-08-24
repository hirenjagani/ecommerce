from django.db import models

# class ActiveProductsManager(models.Manager):
#     def get_queryset(self):
#         return super().get_queryset().filter(active=True)
#
#
# class FeaturedProductsManager(models.Manager):
#     def get_queryset(self):
#         return super().get_queryset().filter(featured=True, active= True)


class ProductQuerySet(models.query.QuerySet):
    def featured(self):
        return self.filter(active=True)

    def active(self):
        return self.filter(featured=True,active=True)

class Product(models.Model):
    name = models.CharField(max_length=20)
    quantities=models.IntegerField(default=0,blank=True)
    description = models.TextField(max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=20, default=100.00)
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    featured = models.BooleanField(default=False)
    active=models.BooleanField(default=True)


    # objects = models.Manager() # The default manager.
    # active_products = ActiveProductsManager()
    # featured_products = FeaturedProductsManager()


    def __str__(self):
        return self.name


