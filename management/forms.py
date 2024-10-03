from django import forms
from django.forms import ModelForm
from django.forms.models import inlineformset_factory
# from patients.models import Patient, PatientDetail, LabData, LabThumor, LabThumor1
from patients.models import Patient, PatientDetail, LabData, LabThumor1


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ('hcc_number', 'pesel', 'name', 'phone', 'email', 'date', 'decision')
        widgets = {
            'hcc_number': forms.TextInput(attrs={'class':'form-control border border-warning', 'placeholder':'HCC'}),
            'name': forms.TextInput(attrs={'class':'form-control border border-warning', 'placeholder':'Imię i nazwisko'}),
            'phone': forms.TextInput(attrs={'class':'form-control border border-warning', 'placeholder':'+48 000 000 000'}),
            'pesel': forms.TextInput(attrs={'class':'form-control border border-warning', 'placeholder':'PESEL'}),
            'email': forms.EmailInput(attrs={'class':'form-control', 'placeholder':'mail@mail.com'}),
            'decision': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Dezyzja'}),
            'date': forms.NumberInput(attrs={'class':'form-control border border-warning', 'type': 'date'}),                 
        }

class PatientDeatilForm(ModelForm):
    class Meta:
        model = PatientDetail
        fields = ('age','grupa_krwi','patient_height','patient_weight', 'gender', 'ecog')
        widgets = {
            'age': forms.TextInput(attrs={'class':'form-control border border-warning', 'placeholder':'Wiek'}),
            'grupa_krwi': forms.Select(attrs={'class':'form-select border border-warning', 'placeholder':'Gr. krwi'}),
            'patient_height': forms.TextInput(attrs={'class':'form-control border border-warning', 'placeholder':'Wzrost'}),
            'patient_weight': forms.TextInput(attrs={'class':'form-control border border-warning', 'placeholder':'Waga'}),
            'gender': forms.Select(attrs={'class':'form-select border border-warning'}),
            'ecog': forms.TextInput(attrs={'class':'form-control border border-warning', 'placeholder':'ECOG'}),
        }

class PatientLabForm(ModelForm):
    class Meta:
        model = LabData
        fields = ('lab_date', 'albuminy', 'inr', 'kreatynina', 'sod_surowica', 'bilirubina_cal',
                  'li_rads_hcc', 'afp', 'plt', 'cea', 'ca19_9', 'cukrzyca',
                  'marskosc', 'wodobrzusze', 'encefalopatia', 'hbv', 'hcv',
                  'kommentarz', 'leczenie')
        widgets = {
            'lab_date': forms.NumberInput(attrs={'class':'form-control', 'type': 'date'}),
            'albuminy': forms.TextInput(attrs={'class':'form-control', 'placeholder':'3,5-5'}),  # norma 3,5-5
            'inr': forms.TextInput(attrs={'class':'form-control', 'placeholder':'0,8-1,2'}),  # norma 0,8-1,2
            'kreatynina': forms.TextInput(attrs={'class':'form-control', 'placeholder':'53–115 µmol/l'}), # norma 53–115 µmol/l (0,6–1,3 mg/dl)
            'sod_surowica': forms.TextInput(attrs={'class':'form-control', 'placeholder':'135-145 mmol/l'}), # norma 135-145 mmol/l
            'bilirubina_cal': forms.TextInput(attrs={'class':'form-control w-100', 'placeholder':'5.1-17.1 μmol/L'}),  # norma 5.1-17.1 μmol/L
            # 
            'li_rads_hcc': forms.Select(attrs={'class':'form-select', 'placeholder':'Li-rads'}),
            'afp': forms.TextInput(attrs={'class':'form-control', 'placeholder':'0-40 µg/l'}),
            'plt': forms.TextInput(attrs={'class':'form-control', 'placeholder':'150–400 tyś'}),
            'cea': forms.TextInput(attrs={'class':'form-control', 'placeholder':'2,5ng/ml|5ng/ml'}),
            'ca19_9': forms.TextInput(attrs={'class':'form-control', 'placeholder':'< 37 U/ml'}),
            'cukrzyca': forms.Select(attrs={'class':'form-control'}),
            # 
            'marskosc': forms.Select(attrs={'class':'form-control'}),
            'wodobrzusze': forms.Select(attrs={'class':'form-control'}),
            'encefalopatia': forms.Select(attrs={'class':'form-control'}),
            'hbv': forms.Select(attrs={'class':'form-control'}),
            'hcv': forms.Select(attrs={'class':'form-control'}), 
# 
            'kommentarz': forms.Textarea(attrs={'class':'form-control', 'rows':5, 'placeholder':'Dodaj dodatkowe uwagi'}),
            'leczenie': forms.Textarea(attrs={'class':'form-control', 'rows':5, 'placeholder':'Leczenie dotychczasowe:  1-Resekcja | 2-Ablacja(RFA/MWA) | 3-TACE | 4-OLTx | 5-Y90 | 6-Radioterapia | 7-Leczenie systemowe '}),
        }

class PatientThumorForm1(forms.ModelForm):
    class Meta:
        model = LabThumor1
        fields = [
            'thumor_number',
            'thumor1_segment1', 'thumor1_segment2', 'thumor1_segment3', 'thumor1_diameter',
            'thumor2_segment1', 'thumor2_segment2', 'thumor2_segment3', 'thumor2_diameter',
            'thumor3_segment1', 'thumor3_segment2', 'thumor3_segment3', 'thumor3_diameter',
            'thumor4_segment1', 'thumor4_segment2', 'thumor4_segment3', 'thumor4_diameter',
            'thumor5_segment1', 'thumor5_segment2', 'thumor5_segment3', 'thumor5_diameter',
            'thumor6_segment1', 'thumor6_segment2', 'thumor6_segment3', 'thumor6_diameter',
            'top_diameter',
        ]
        widgets = {
            'thumor_number': forms.TextInput(attrs={'class':'form-control','placeholder':'liczba'}),
            # 1
            'thumor1_segment1': forms.TextInput(attrs={'class':'form-control','placeholder':'segm. 1'}), 
            'thumor1_segment2': forms.TextInput(attrs={'class':'form-control','placeholder':'segm. 2'}), 
            'thumor1_segment3': forms.TextInput(attrs={'class':'form-control','placeholder':'segm. 3'}), 
            'thumor1_diameter': forms.TextInput(attrs={'class':'form-control','placeholder':'wymiar'}),
            # 2
            'thumor2_segment1': forms.TextInput(attrs={'class':'form-control','placeholder':'segm. 1'}),
            'thumor2_segment2': forms.TextInput(attrs={'class':'form-control','placeholder':'segm. 2'}), 
            'thumor2_segment3': forms.TextInput(attrs={'class':'form-control','placeholder':'segm. 3'}), 
            'thumor2_diameter': forms.TextInput(attrs={'class':'form-control','placeholder':'wymiar'}),
            # 3
            'thumor3_segment1': forms.TextInput(attrs={'class':'form-control','placeholder':'segm. 1'}), 
            'thumor3_segment2': forms.TextInput(attrs={'class':'form-control','placeholder':'segm. 2'}), 
            'thumor3_segment3': forms.TextInput(attrs={'class':'form-control','placeholder':'segm. 3'}),
            'thumor3_diameter': forms.TextInput(attrs={'class':'form-control','placeholder':'wymiar'}),
            # 4
            'thumor4_segment1': forms.TextInput(attrs={'class':'form-control','placeholder':'segm. 1'}), 
            'thumor4_segment2': forms.TextInput(attrs={'class':'form-control','placeholder':'segm. 2'}), 
            'thumor4_segment3': forms.TextInput(attrs={'class':'form-control','placeholder':'segm. 3'}), 
            'thumor4_diameter': forms.TextInput(attrs={'class':'form-control','placeholder':'wymiar'}),
            # 5
            'thumor5_segment1': forms.TextInput(attrs={'class':'form-control','placeholder':'segm. 1'}), 
            'thumor5_segment2': forms.TextInput(attrs={'class':'form-control','placeholder':'segm. 2'}), 
            'thumor5_segment3': forms.TextInput(attrs={'class':'form-control','placeholder':'segm. 3'}), 
            'thumor5_diameter': forms.TextInput(attrs={'class':'form-control','placeholder':'wymiar'}),
            # 6
            'thumor6_segment1': forms.TextInput(attrs={'class':'form-control','placeholder':'segm. 1'}), 
            'thumor6_segment2': forms.TextInput(attrs={'class':'form-control','placeholder':'segm. 2'}), 
            'thumor6_segment3': forms.TextInput(attrs={'class':'form-control','placeholder':'segm. 3'}),
            'thumor6_diameter': forms.TextInput(attrs={'class':'form-control','placeholder':'wymiar'}),
            # 
            'top_diameter': forms.TextInput(attrs={'class':'form-control','placeholder':'największy wymiar'}),
        }


class UploadCSVForm(forms.Form):
    csv_file = forms.FileField()
    
# class PatientThumorForm(forms.ModelForm):
#     class Meta:
#         model = LabThumor
#         fields = ['thumor_number', 'thumor_segment1', 'thumor_segment2', 'thumor_segment3', 'thumor_diameter', 'top_diameter']
#         widgets = {
#             'thumor_number': forms.TextInput(attrs={
#                 'style': 'display: inline; background-color: #212529;margin-bottom: 5px; padding: 0.375rem 0.75rem; font-color: white; line-height: 1.5; font-size: inherit; font-weight: 400; font-family: inherit; border: solid #495057 1px; border-radius: 0.375rem;',
#                 'placeholder':'liczba',
#                 }),
#             'thumor_segment1': forms.TextInput(attrs={
#                 'style': 'display: inline; background-color: #212529; padding: 0.375rem 0.75rem; font-color: white; line-height: 1.5; font-size: inherit; font-weight: 400; font-family: inherit; border: solid #495057 1px; border-radius: 0.375rem;',
#                 'placeholder':'segment 1'
#                 }),
#             'thumor_segment2': forms.TextInput(attrs={
#                 'style': 'display: inline; background-color: #212529; padding: 0.375rem 0.75rem; font-color: white; line-height: 1.5; font-size: inherit; font-weight: 400; font-family: inherit; border: solid #495057 1px; border-radius: 0.375rem;',
#                 'placeholder':'segment 2'
#                 }),
#             'thumor_segment3': forms.TextInput(attrs={
#                 'style': 'display: inline; background-color: #212529; padding: 0.375rem 0.75rem; font-color: white; line-height: 1.5; font-size: inherit; font-weight: 400; font-family: inherit; border: solid #495057 1px; border-radius: 0.375rem;',
#                 'placeholder':'segment 3'
#                 }),                
#             'thumor_diameter': forms.TextInput(attrs={                
#                 'style': 'display: inline; background-color: #212529; padding: 0.375rem 0.75rem; font-color: white; line-height: 1.5; font-size: inherit; font-weight: 400; font-family: inherit; border: solid #495057 1px; border-radius: 0.375rem;',
#                 'placeholder':'wymiar'
#                 }),
#             'top_diameter': forms.TextInput(attrs={
#                 'style': 'display: inline; background-color: #212529; padding: 0.375rem 0.75rem; font-color: white; line-height: 1.5; font-size: inherit; font-weight: 400; font-family: inherit; border: solid #495057 1px; border-radius: 0.375rem;',
#                 'placeholder':'największy wymiar'
#                 }),
#         }



# ThumorFormset = inlineformset_factory(
#     Patient, LabThumor,
#     form=PatientThumorForm,
#     extra=3,
#     can_delete=False
# )

# ThumorFormset1 = inlineformset_factory(
#     Patient, LabThumor,
#     form=PatientThumorForm,
#     extra=3,
#     can_delete=False
# )

# ThumorFormset2 = inlineformset_factory(
#     Patient, LabThumor,
#     form=PatientThumorForm,
#     extra=0,
#     can_delete=False
# )
