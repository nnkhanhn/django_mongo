from django.urls import re_path
from django.urls import path
from posts import views

from django.conf.urls.static import static
from django.conf import settings

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('product', views.productApi, basename='data')
router.register('user', views.userApi, basename='user')
urlpatterns = router.urls
urlpatterns.append(path('function/', views.function_based))
# urlpatterns.append(user_router.urls)