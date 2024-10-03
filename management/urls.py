from django.urls import path
from . import views


urlpatterns = [
    # User management
    path('patient/<patient_id>/', views.patient, name='patient'),
   
    path('patient_add/', views.patient_add, name='patient-add'),
    path('patient_update/<patient_id>', views.patient_update, name='patient-update'),
    path('patient_delete/<patient_id>', views.patient_delete, name='patient-delete'),
    
    path('patient_compare/', views.patient_compare, name='patient-compare'),
    path('patient_search/', views.patient_search, name='patient-search'),
    
    path('patient_csv/', views.export_csv, name='patient-csv'),
    # path('export_csv/<patient_id>', views.export_csv1, name='export-csv'),
    path('import_csv/', views.import_csv, name='import-csv'),
]