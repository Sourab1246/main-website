from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=30)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=128)
    confirm_password=models.CharField(max_length=120,default=True) 
    first_name=models.CharField(max_length=38)
    last_name=models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)


def __str__(self):
    return self.username  

class Category(models.Model):
    product_type=[('clothing','clothing'),
    ('shoes','shoes'),
    ('innerwear','innerwear'),
    ('men\'s gromming','men\'s gromming'),
    ('men\'s gromming','men\'s gromming'),
    ('Kids wear','kids wear'),
]  
    types=models.CharField(max_length=30,default=False,choices=product_type)
    
    def __str__(self):
      return self.types   
    

class Products(models.Model):
    name=models.CharField(max_length=30)
    price=models.FloatField()
    discount_percent=models.PositiveIntegerField(default=0)
    description=models.TextField()
    image=models.ImageField(upload_to='products/')
    category=models.ForeignKey('Category',on_delete=models.CASCADE,)

    def discounted_price(self):
        return self.price *     (1-self.discount_percent  /100)
    
    def __str__(self):
        return self.name
    
       



