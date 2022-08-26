from django.urls import path
from . import views
from .views import * 

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('posts/',views.PostList.as_view(), name="post_list"),
    # path('posts/new/', views.PostCreate.as_view(), name="post_create"),
    path('accounts/signup/', views.Signup.as_view(), name="signup"),
    # path('posts/<int:pk>/', views.PostDetail.as_view(), name="post_detail"),
    # path('posts/<int:pk>/update', views.PostUpdate.as_view(), name="artist_update"),
    
]

# embed for pdf 

#/
# accounts/signup/
# momnpops/
# momnpops/<int:momnpopsId>
# accounts/<int:accountId>
# momnpops/category/<int:category_id>
# momnpops/neighborhood/<int:neighborhood_id>

# path('posts/upload/img/', views.upload, name='upload'),