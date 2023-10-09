from django.urls import path
from . import views

urlpatterns = [
    path('degreechecklist/', views.degreechecklist, name='degreechecklist'),
]
