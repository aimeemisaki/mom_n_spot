from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('posts/upload/img/', views.upload, name='upload'),
    path('posts/',views.PostList.as_view(), name="post_list"),
    path('posts/new/',views.PostCreate.as_view(), name="post_create"),
    # path('posts/<int:pk>/', views.PostDetail.as_view(), name="post_detail"),
    # path('posts/<int:pk>/update', views.PostUpdate.as_view(), name="artist_update"),
    path('accounts/signup/', views.Signup.as_view(), name="signup"),
]

#/
# accounts/signup/
# momnpops/
# momnpops/<int:momnpopsId>
# accounts/<int:accountId>
# momnpops/category/<int:category_id>
# momnpops/neighborhood/<int:neighborhood_id>