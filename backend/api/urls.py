from django.contrib import admin
from django.urls import path, include
from notes import views
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register(r'notes', views.NotesViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
