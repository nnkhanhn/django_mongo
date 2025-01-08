from django.urls import re_path
from posts import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    re_path(r'^product$',views.ProductApi),
    re_path(r'^product/([0-9]+)$',views.ProductApi),

]