from django.urls import path
from . import views

app_name = 'e_app'

urlpatterns = [
    path('', views.allProductsCategory, name='allProductsCategory'),
    path('category/<slug:c_slug>/', views.allProductsCategory, name='productByCategory'),
    path('category/<slug:c_slug>/<slug:product_slug>/', views.proDetail, name='prodCatdetail'),
]
