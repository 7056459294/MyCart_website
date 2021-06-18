

from django.urls import path
from .import views



        

urlpatterns = [
        path("",views.index,name="ShopHome"),
        path("about",views.about,name="about"),
        path("contact",views.contact,name="contact"),
        path("tracker",views.tracker,name="tracker"),
        path("products/<int:myid>",views.products,name="contactview"),
        path("checkout",views.checkout,name="checkout"),
        path("search",views.search,name="src")
    
       ]



