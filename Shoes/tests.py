from django.test import TestCase
from django.contrib.auth.models import User
from .models import Shoe, Product, Review
import datetime
from .forms import ProductForm
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
        disc=self.product.price * (1 -.05)
        self.assertEqual(self.product.discountPrice(), disc) 

class NewProductForm(TestCase):
    def test_productform(self):
        data[
            'productname': 'Nike Air Max Dawn',
            'producttype': 'Nike Air Max',
            'user': 'Giochiodo99',
            'dateentered': '2022-03-18',
            'price': '110',
            'producturl': ' https://www.nike.com/t/air-max-dawn-mens-shoes-Rg69GM/DJ3624-400',
            'description': 'RETRO DELIGHT. Rooted to track DNA, the Air Max Dawn is made with at least 20% recycled material by weight. Synthetic suede and other materials blend vintage running vibes with fresh details. Nike Air cushioning delivers a feel-good forecast for the day. Benefits Design lines echo the heritage look you love while the last brings you a top-down appearance. Low-profile Air-sole unit with retro pill-shaped window pairs with a plush foam midsole for cushioning. Outsole with seesaw pattern adds traction and durability Product Details Pull tab on heel Heel clip Shown: Team Royal/Red Clay/Light Bone/Summit White Style: DJ3624-400',
        ]   

        form=ProductForm (data)
        self.assertTrue(form.is_valid)

class New_Product_Authentication_Test(TestCase):
    def setUp(self):
        self.test_user=User.objects.create_user(username='testuser1', password='P@ssw0rd1')
        self.type=Shoe.objects.create(typename='Nike Air Max Dawn')
        self.product=Product(productname= 'Nike Air Max Dawn', producttype=self.type, user=self.user, dateentered=datetime.date(2022, 1, 10), price=110.00, producturl= 'https://www.nike.com', description= "Nike Shoes" )

    def test_redirect_if_not_logged_in(self):
         response=self.client.get(reverse('newproduct'))
         self.assertRedirects(response, '/accounts/login/?next=/Shoes/newproduct/')  
