from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('posts/',views.PostList.as_view(), name="post_list"),
    path('posts/new/',views.PostCreate.as_view(), name="post_create"),
    path('accounts/signup/', views.Signup.as_view(), name="signup"),
]

#/
# accounts/signup/
# momnpops/
# momnpops/<int:momnpopsId>
# accounts/<int:accountId>
# momnpops/category/<int:category_id>
# momnpops/neighborhood/<int:neighborhood_id>