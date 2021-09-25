from django.urls import path
from . import views
urlpatterns=[
	path('',views.login,name='login'),
    path('panal',views.panal,name='panal'),
    path('verify',views.verify,name='verify'),
    path('add',views.add,name='add'),
    path('addproduct',views.addproduct,name='addproduct'),
    path('sales',views.sales,name='sales'),
    path('salesproduct',views.salesproduct,name='salesproduct'),
    path('cart',views.cart,name='cart'),
    path('order',views.order,name='order'),
    path('report',views.report,name='report'), 
    path('viewstock', views.viewstock, name="viewstock"),
]    
