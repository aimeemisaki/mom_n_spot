from django.urls import path
from . import views
from .views import * 

urlpatterns = [
    path('', views.Home.as_view(), name="post_list_all"),
    path('myposts/',views.PostList.as_view(), name="post_list"),
    path('accounts/signup/', views.Signup.as_view(), name="signup"),
    path('myposts/<int:pk>/', views.PostDetail.as_view(), name="post_detail"),
    path('myposts/<int:pk>/delete', views.PostDelete.as_view(), name="post_delete"),
    path('tags/<int:pk>/posts/<int:post_pk>', views.TagPostAssoc.as_view(), name="tag_post_assoc"),
    # path('posts/', views.PostListAll.as_view(), name="post_list_all")
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