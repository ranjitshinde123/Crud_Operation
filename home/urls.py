from django.urls import path
from . import views

urlpatterns=[
    path('',views.signup,name='signup'),
    path('showdata/',views.showdata,name='showdata'),
    path('updatedata/<int:id>',views.update,name='updatedata'),
    path('deletedata/<int:id>',views.deletedata,name='deletedata'),
]