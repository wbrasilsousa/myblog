from django.urls import path
from .views import blog_views, finance_views


urlpatterns = [
    path("", blog_views.blog_index, name="blog_index"),
    path("post/<slug:slug>/", blog_views.blog_detail, name="blog_detail"),
    path("category/<category>/", blog_views.blog_category, name="blog_category"),

    path("finance", finance_views.finance, name="finance"),
]