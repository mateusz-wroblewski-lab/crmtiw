from django.contrib import admin
from patients.models import Patient, PatientDetail, LabData, LabThumor1


@admin.register(Patient)
class Patient(admin.ModelAdmin):
    list_display = ['hcc_number',  'name',  'pesel', 'phone', 'email', 'date', 'decision']

@admin.register(PatientDetail)
class PatientDetail(admin.ModelAdmin):
    list_display = ['patient', 'age','grupa_krwi','patient_height','patient_weight', 'gender', 'ecog']

@admin.register(LabData)
class LabData(admin.ModelAdmin):
    list_display = ['patient','lab_date', 'albuminy', 'inr', 'kreatynina', 'sod_surowica', 'bilirubina_cal', 'li_rads_hcc', 'afp', 'plt', 'cea', 'ca19_9', 'cukrzyca', 'marskosc', 'wodobrzusze', 'encefalopatia', 'hbv', 'hcv', 'kommentarz', 'leczenie']

@admin.register(LabThumor1)
class LabThumor(admin.ModelAdmin):
    list_display = [
        'patient', 
        'thumor_number',
        'thumor1_segment1', 'thumor1_segment2', 'thumor1_segment3', 'thumor1_diameter',
        'thumor2_segment1', 'thumor2_segment2', 'thumor2_segment3', 'thumor2_diameter',
        'thumor3_segment1', 'thumor3_segment2', 'thumor3_segment3', 'thumor3_diameter',
        'thumor4_segment1', 'thumor4_segment2', 'thumor4_segment3', 'thumor4_diameter',
        'thumor5_segment1', 'thumor5_segment2', 'thumor5_segment3', 'thumor5_diameter',
        'thumor6_segment1', 'thumor6_segment2', 'thumor6_segment3', 'thumor6_diameter',
        'top_diameter',
        ]