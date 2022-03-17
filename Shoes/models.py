from django.db import models
from django.contrib.auth.models import User 

# Create your models here.

# In /admin all text fields need ()
class Shoe(models.Model):
    typename=models.CharField(max_length=255)
    typedescription=models.TextField(null=True, blank=True)

    def __str__(self):
        return self.typename

    class Meta:
        db_table='Shoe'

# In /admin all text fields need ()
class Product(models.Model):
    productname=models.CharField(max_length=255)
    producttype=models.ForeignKey(Shoe, on_delete=models.DO_NOTHING)
    user=models.ForeignKey(User, on_delete=models.DO_NOTHING)
    dateentered=models.DateField()
    price=models.DecimalField(max_digits=6, decimal_places=2)
    producturl=models.URLField(null=True, blank=True)
    description=models.TextField(null=True, blank=True)

    def discountAmount(self):
        self.discount=self.price * .05
        return self.discount

    def discountPrice(self):
        disc=self.discountAmount()
        self.discountedPrice=self.price-disc

    def __str__(self):
        return self.productname

    class Meta:
        db_table='product'

# In /admin all text fields need ()
class Review(models.Model):
    title=models.CharField(max_length=255)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    reviewdate=models.DateField()
    reviewtext=models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        db_table='review'