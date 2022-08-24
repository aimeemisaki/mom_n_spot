from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('accounts/signup/', views.Signup.as_view(), name="signup"),
    path('momnpops/', views.MomNPopsList.as_view(), name="momnpops_list"),
]

#/
# accounts/signup/
# momnpops/
# momnpops/<int:momnpopsId>
# accounts/<int:accountId>
# momnpops/category/<int:category_id>
# momnpops/neighborhood/<int:neighborhood_id>