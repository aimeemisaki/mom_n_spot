from django.urls import path
from . import views
from .views import * 

urlpatterns = [
    path('', views.Start.as_view(), name="start"),
    path('home/', views.Home.as_view(), name="post_list_all"),
    path('myposts/',views.PostList.as_view(), name="post_list"),
    path('accounts/signup/', views.Signup.as_view(), name="signup"),
    path('myposts/<int:pk>/', views.PostDetail.as_view(), name="post_detail"),
    path('myposts/<int:pk>/delete', views.PostDelete.as_view(), name="post_delete"),
    path('tags/<int:pk>/posts/<int:post_pk>', views.TagPostAssoc.as_view(), name="tag_post_assoc"),
]

