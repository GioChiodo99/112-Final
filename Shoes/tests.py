from django.test import TestCase
from django.contrib.auth.models import User
from .models import Shoe, Product, Review
import datetime
from django.urls import reverse_lazy, reverse

# Create your tests here.

class ShoeTest(TestCase):
    def setUp(self):
        self.type=Shoe(typename='Nike Air Max Dawn')

    def test_typestring(self):
        self.assertEqual(str(self.type), 'Nike Air Max Dawn')

    def test_tablename(self):
        self.assertEqual(str(Shoe._meta.db_table), 'Shoe')

#need to figure out whats wrong, something to do with the function itself

class ProductTest(TestCase):
    def setUp(self):
        self.type=Shoe(typename= 'Nike Air Max')
        self.user=User(username= 'user1')
        self.product=Product(productname= 'Nike Air Max Dawn', producttype=self.type, user=self.user, dateentered=datetime.date(2022, 1, 10), price=110.00, producturl= 'https://www.nike.com', description= "Nike Shoes" )

    def test_string(self):
        self.assertEqual(str(self.product), 'Nike Air Max Dawn')

    
    def test_discount(self):
        disc=self.product.price * .05
        self.assertEqual(self.product.discountPrice(), disc)
    
    def test_discountedAmount(self):
        disc=self.product.price * ( 1 -.05)
        self.assertEqual(self.product.discountPrice(), disc)    
