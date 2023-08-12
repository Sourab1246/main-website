from django.urls import path,include
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home,name='home'),
    path('register/',views.register,name='register'),

    path('login/',views.login,name='login'),

    path('profile/',views.profile,name='profile'),

    path('product_detail/',views.product_detail,name='product_detail'),

    path('cart/',views.view_cart,name='view_cart'),
 
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),

    path('checkout/',views.checkout,name='checkout'),
    
    path('order_confirmation/',views.order_confirmation,name='order_confirmation'),
   
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
