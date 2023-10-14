from django.contrib import admin
from django.urls import path
from .views import *
from . import views


urlpatterns = [
    # path("admin/", admin.site.urls),
    path("", PostListView.as_view(), name='blog-home'),
     path("user/<str:username>", UserPostListView.as_view(), name='user-post'),
    path("post/<int:pk>/", PostDetailView.as_view(), name='post_detail'),
    path("post/new/", PostCreateView.as_view(), name='post_create'),
    path("post/<int:pk>/update", PostUpdateView.as_view(), name='post_update'),
    path("post/<int:pk>/delete", PostDeleteView.as_view(), name='post_delete'),
    path("about/", views.about, name='blog-about')
]

## naming convention of template file the browser is looking for
## <app>/<model>_<viewtype>.html 