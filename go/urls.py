from django.urls import path

from . import views
from go.views import WebURLFormView,ShowExcelView

urlpatterns = [
    path('test', views.index, name='index0'),
    path('',WebURLFormView.index,name='index'),
    path('form_action', WebURLFormView.FormToDB, name='form_action'),
    path('showExcel',ShowExcelView.as_view(),name='showExcel')
]
