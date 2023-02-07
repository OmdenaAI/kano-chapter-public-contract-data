from django.urls import path
from .views import projects_view
from .views import projects_view, export_csv,  export_json,csv 
from . import views




urlpatterns = [
    path("",views.index,name='index'),
    path('chart/',views.chart, name='chart'),
    path('project/', views.project, name='projects'),
    path('projects/', projects_view, name='projects_view'),
    path('export/csv/', export_csv, name='download_csv'),
    # path('export/pdf/', export_pdf, name='export_pdf'),
    path('export/json/', export_json, name='download_json'),
]


