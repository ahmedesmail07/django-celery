from django.contrib import admin
from django.urls import path, include
from app2.views import ReviewEmailView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("review/", ReviewEmailView.as_view(), name='review')
]
