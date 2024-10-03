import csv
import io
from datetime import datetime
# 
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
# 
# from patients.models import Patient, PatientDetail, LabData, LabThumor
from patients.models import Patient, PatientDetail, LabData, LabThumor1
from .forms import PatientForm, PatientDeatilForm, PatientLabForm, PatientThumorForm1
# from .forms import ThumorFormset, ThumorFormset1, ThumorFormset2, UploadCSVForm
from .forms import UploadCSVForm



# Patient flled up profile
def patient(request, patient_id):
    patient_user = Patient.objects.get(pk=patient_id)
    patient_base = PatientDetail.objects.get(pk=patient_id)
    patient_lab = LabData.objects.get(pk=patient_id)
    # patient_thumor = ThumorFormset2(instance=patient_user)
    patient_thumor = LabThumor1.objects.get(id=patient_id)

    specific_fields = [
        'thumor_number',
        'thumor1_segment1', 'thumor1_segment2', 'thumor1_segment3', 'thumor1_diameter',
        'thumor2_segment1', 'thumor2_segment2', 'thumor2_segment3', 'thumor2_diameter',
        'thumor3_segment1', 'thumor3_segment2', 'thumor3_segment3', 'thumor3_diameter',
        'thumor4_segment1', 'thumor4_segment2', 'thumor4_segment3', 'thumor4_diameter',
        'thumor5_segment1', 'thumor5_segment2', 'thumor5_segment3', 'thumor5_diameter',
        'thumor6_segment1', 'thumor6_segment2', 'thumor6_segment3', 'thumor6_diameter',
        'top_diameter',
    ]

    filled_fields = {field: getattr(patient_thumor, field)
                     for field in specific_fields
                     if getattr(patient_thumor, field)
        }

    context = {
        'patient_user': patient_user,
        'patient_base': patient_base,
        'patient_lab': patient_lab,
        'filled_fields': filled_fields,
        'patient_thumor': patient_thumor,
    }
    return render(request, 'patient_profile.html', context)


def patient_add(request):
    if request.user.is_authenticated:
            user_form = PatientForm(request.POST)
            base_form = PatientDeatilForm(request.POST)
            lab_form = PatientLabForm(request.POST)
            # thumor_formset = ThumorFormset(request.POST)
            thumor_form = PatientThumorForm1(request.POST)

            
            if all([user_form.is_valid(),base_form.is_valid(),lab_form.is_valid(), thumor_form.is_valid()]): # thumor_formset.is_valid()]):
                # patient = user_form.save()
                user_form.save()
                base_form.save()
                lab_form.save()
                thumor_form.save()
                # thumors = thumor_formset.save(commit=False)
                # for thumor in thumors:
                #     thumor.patient = patient
                #     thumor.save()

                messages.success(request, ("Dodano pomyślnie"))
                return redirect('home')

            user_form = PatientForm()
            base_form = PatientDeatilForm()
            lab_form = PatientLabForm()
            thumor_form = PatientThumorForm1()
                
            context = {'user_form': user_form,
                       'base_form': base_form,
                       'lab_form': lab_form,
                       'thumor_form': thumor_form
                    #    'thumor_formset': thumor_formset
                    }
            return render(request, 'patient_add.html', context)
    else:
        messages.success(request, ("Musisz się zalogować..."))
        return redirect('home')


def patient_update(request, patient_id):
    user_user = Patient.objects.get(pk=patient_id)
    user_base = PatientDetail.objects.get(pk=patient_id)
    user_lab = LabData.objects.get(pk=patient_id)
    user_thum = LabThumor1.objects.get(pk=patient_id)
    
    user_form = PatientForm(request.POST or None, instance=user_user)
    base_form = PatientDeatilForm(request.POST or None, instance=user_base)
    lab_form = PatientLabForm(request.POST or None, instance=user_lab)
    thumor_form = PatientThumorForm1(request.POST or None, instance=user_thum)
    # thumor_formset = ThumorFormset1(request.POST or None, instance=user_user)

    if request.user.is_authenticated:
        # if all([user_form.is_valid(), base_form.is_valid(), lab_form.is_valid(), thumor_formset.is_valid()]):     
        if all([user_form.is_valid(), base_form.is_valid(), lab_form.is_valid(), thumor_form.is_valid()]):           
            user_form.save()
            base_form.save()
            lab_form.save()
            thumor_form.save()
            # thumor_formset.save()
            messages.success(request, ('Zaktualizowano pomyślnie'))
            # return redirect('patient', patient_id=user_user.id) 
            return redirect('home') 

 
        user_form = PatientForm(instance=user_user)
        base_form = PatientDeatilForm(instance=user_base)
        lab_form = PatientLabForm(instance=user_lab)
        thumor_form = PatientThumorForm1(instance=user_thum)
        # thumor_formset = ThumorFormset1(instance=user_user)
        context = {
            'user_form_update': user_form,
            'base_form_update': base_form,
            'lab_form_update': lab_form,
            # 'thumor_update': thumor_formset
            'thumor_update': thumor_form
            }
        return render(request, 'patient_update.html', context)
    else:
        messages.success(request, ("Musisz się zalogować..."))
        return redirect('home')


def patient_delete(request, patient_id):
    if request.user.is_authenticated:
        user_user = Patient.objects.get(pk=patient_id)
        user_base = PatientDetail.objects.get(pk=patient_id)
        user_lab = LabData.objects.get(pk=patient_id)

        user_user.delete()
        user_base.delete()
        user_lab.delete()
        messages.success(request, ("Usunięto pomyślnie"))
        return redirect('home')
    else:
        messages.success(request, ("Musisz się zalogować..."))
        return redirect('home')

def patient_search(request):
    patient_count = Patient.objects.all().count()
    if request.method == 'POST':
        searched = request.POST['searched']
        patient = Patient.objects.all().order_by('-date', '-hcc_number').filter(pesel__contains=searched)[:10]
        return render(request, 'patient_search.html', {'searched':searched, 'patient':patient, 'patient_count':patient_count})
    else:
        return render(request, 'patient_search.html', {})


def patient_compare(request):
    patient_ids = request.POST.getlist('compare')
    if len(patient_ids) != 2:
        # Ensure that exactly two products are selected
        messages.success(request, ("Proszę zaznaczyć dokładnie minimum dwóch pacjentów z listy"))
        return redirect('home')
    
    # Fetch the products based on the selected ids
    patient_user = Patient.objects.filter(id__in=patient_ids)
    patient_count = Patient.objects.all().count()
    patient_base = PatientDetail.objects.all()
    patient_lab = LabData.objects.all()
    patient_thumor = LabThumor1.objects.filter(id__in=patient_ids)
    
    context = {
        'patient_user': patient_user,
        'patient_base': patient_base,
        'patient_lab': patient_lab,
        'patient_thumor': patient_thumor,
        'patient_count': patient_count,
        }
    
    if patient_user.count() == 2:
        
        return render(request, 'patient_compare.html', context)
    else:
        messages.success(request, ("Proszę zaznaczyć dokładnie minimum dwóch pacjentów z listy"))
        return redirect('home')

def export_csv(request):
    # Add models lines
    patient_user = Patient.objects.all()
    patient_base = PatientDetail.objects.all()
    patient_lab = LabData.objects.all()
    patient_thumor = LabThumor1.objects.all()
    
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachement; filename="patientlist.csv"'
    # CSV writer
    writer = csv.writer(response)
    # Add column in csv
    writer.writerow([
        # Patient
        'hcc_number', 'date', 'name', 'phone', 'pesel', 'email', 'decision',            
        # Patient base
        'age','grupa_krwi','patient_height','patient_weight', 'gender', 'ecog',         
        # Patient Lab
        'lab_date', 'albuminy', 'inr', 'kreatynina', 'sod_surowica', 'bilirubina_cal',  
        'li_rads_hcc', 'afp', 'plt', 'cea', 'ca19_9', 'cukrzyca',
        'marskosc', 'wodobrzusze', 'encefalopatia', 'hbv', 'hcv',
        'kommentarz', 'leczenie',
        # Patient Thumor
        'thumor_number',
        'thumor1_segment1', 'thumor1_segment2', 'thumor1_segment3', 'thumor1_diameter',
        'thumor2_segment1', 'thumor2_segment2', 'thumor2_segment3', 'thumor2_diameter',
        'thumor3_segment1', 'thumor3_segment2', 'thumor3_segment3', 'thumor3_diameter',
        'thumor4_segment1', 'thumor4_segment2', 'thumor4_segment3', 'thumor4_diameter',
        'thumor5_segment1', 'thumor5_segment2', 'thumor5_segment3', 'thumor5_diameter',
        'thumor6_segment1', 'thumor6_segment2', 'thumor6_segment3', 'thumor6_diameter',
        'top_diameter',
    ])

    for patient, base, lab, thum in zip(patient_user, patient_base, patient_lab, patient_thumor):
        # If no thumor info
                writer.writerow([
                # Patient
                patient.hcc_number, patient.date, patient.name, patient.phone, patient.pesel, patient.email, patient.decision,
                # Patient base
                base.age, base.grupa_krwi, base.patient_height, base.patient_weight, base.gender, base.ecog,         
                # Patient Lab
                lab.lab_date, lab.albuminy, lab.inr, lab.kreatynina, lab.sod_surowica, lab.bilirubina_cal,  
                lab.li_rads_hcc, lab.afp, lab.plt, lab.cea, lab.ca19_9, lab.cukrzyca,
                lab.marskosc, lab.wodobrzusze, lab.encefalopatia, lab.hbv, lab.hcv,
                lab.kommentarz, lab.leczenie,
                # Patient Thumor
                thum.thumor_number,
                thum.thumor1_segment1, thum.thumor1_segment2, thum.thumor1_segment3, thum.thumor1_diameter, 
                thum.thumor2_segment1, thum.thumor2_segment2, thum.thumor2_segment3, thum.thumor2_diameter,
                thum.thumor3_segment1, thum.thumor3_segment2, thum.thumor3_segment3, thum.thumor3_diameter,
                thum.thumor4_segment1, thum.thumor4_segment2, thum.thumor4_segment3, thum.thumor4_diameter,
                thum.thumor5_segment1, thum.thumor5_segment2, thum.thumor5_segment3, thum.thumor5_diameter,
                thum.thumor6_segment1, thum.thumor6_segment2, thum.thumor6_segment3, thum.thumor6_diameter,
                thum.top_diameter
                ])


    # # Write to csv file
    return response

def format_date(date_str):
    if date_str:
        try:
            date_obj = datetime.strptime(date_str, '%Y-%M-%D')
            return date_obj.strftime('%Y-%M-%D')
        except ValueError:
            return ''
    return''
            

def import_csv(request):
    if request.method == 'POST':
        form = UploadCSVForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['csv_file']

            # Check if the file is a CSV
            if not csv_file.name.endswith('.csv'):
                messages.error(request, 'This is not a CSV file.')
                return redirect('import-csv')

            # Read the CSV file
            data_set = csv_file.read().decode('UTF-8')
            io_string = io.StringIO(data_set)
            csv_reader = csv.reader(io_string, delimiter=',', quotechar='"')

            # Skip the header row
            next(csv_reader)

            # Process CSV rows
            for row in csv_reader:
                # You can process each row here and save it to your model
                # Assuming the order of fields matches the CSV file structure
                Patient.objects.create(hcc_number=row[0], date=row[1], name=row[2], phone=row[3], pesel=row[4], email=row[5], decision=row[6])
                PatientDetail.objects.create(age=row[7],grupa_krwi=row[8], patient_height=row[9],patient_weight=row[10], gender=row[11], ecog=row[12])
                LabData.objects.create(lab_date=row[13], albuminy=row[14], inr=row[15], kreatynina=row[16], sod_surowica=row[17], bilirubina_cal=row[18],
                                       li_rads_hcc=row[19], afp=row[20], plt=row[21], cea=row[22], ca19_9=row[23], cukrzyca=row[24],
                                       marskosc=row[25], wodobrzusze=row[26], encefalopatia=row[27], hbv=row[28], hcv=row[29],
                                       kommentarz=row[30], leczenie=row[31])
                LabThumor1.objects.create(
                    thumor_number=row[32],
                    thumor1_segment1=row[33], thumor1_segment2=row[34], thumor1_segment3=row[35], thumor1_diameter=row[36],
                    thumor2_segment1=row[37], thumor2_segment2=row[38], thumor2_segment3=row[39], thumor2_diameter=row[40],
                    thumor3_segment1=row[41], thumor3_segment2=row[42], thumor3_segment3=row[43], thumor3_diameter=row[44],
                    thumor4_segment1=row[45], thumor4_segment2=row[46], thumor4_segment3=row[47], thumor4_diameter=row[48],
                    thumor5_segment1=row[49], thumor5_segment2=row[45], thumor5_segment3=row[46], thumor5_diameter=row[47],
                    thumor6_segment1=row[48], thumor6_segment2=row[49], thumor6_segment3=row[50], thumor6_diameter=row[51],
                    top_diameter=row[52] 
                    )

            messages.success(request, 'CSV file successfully imported.')
            return redirect('import-csv')
    else:
        form = UploadCSVForm()

    return render(request, 'csv/import_csv.html', {'form_csv':form})
