from django.db import models


class Patient(models.Model):
    hcc_number = models.CharField(max_length=5, null=True, blank=False)
    name = models.CharField(max_length=50, null=True, blank=False)
    phone = models.CharField(max_length=15, null=True, blank=False)
    pesel = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(max_length=20, null=True, blank=True)
    decision = models.CharField(max_length=50, null=True, blank=True)
    date = models.DateField(max_length=20, null=True, blank=True)


class PatientDetail(models.Model):
    GENDER_SEL = (
        ('M','Męska'),
        ('K', 'Żeńska'),
    )
    
    GR_KRWI = (
        ('A', 'A'), 
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B', 'B'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB', 'AB'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O', 'O'),
        ('O+', 'O+'),
        ('O-', 'O-'),
    )
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True)
    age = models.CharField(max_length=5, null=True, blank=True)
    grupa_krwi = models.CharField(choices=GR_KRWI, max_length=20, null=True, blank=True)
    patient_height = models.CharField(max_length=50, null=True, blank=True)
    patient_weight = models.CharField(max_length=50, null=True, blank=True)
    gender = models.CharField(max_length=5, choices=GENDER_SEL, null=True, blank=True)
    ecog = models.CharField(max_length=5, null=True, blank=True)

class LabData(models.Model):
    LIRADS_SEL = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    )

    NASH_SEL = (
        ('1', 'tak'),
        ('0', 'nie'),
    )

    CUKR_SEL = (
        ('1', 'tak'),
        ('0', 'nie'),
    )

    MARSK_SEL = (
        ('1', 'tak'),
        ('0', 'nie'),
    )

    ENCEFAL_SEL = (
        ('1', '1/2 stopień'),
        ('2', '3/4 stopień'),
    )

    WODOBRZ_SEL = (
        ('1', '1/2 stopień'),
        ('2', '3/4 stopień'),
    )

    HCV_SEL = (
        ('0', 'ujemne'),
        ('1', 'wyleczone'),
        ('2', 'dodatnie'),
    )

    HBV_SEL = (
        ('0', 'ujemne'),
        ('1', 'wyleczone'),
        ('2', 'dodatnie'),
    )
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True)
    lab_date = models.DateField(max_length=20, null=True, blank=True)
    albuminy = models.CharField(max_length=20, null=True, blank=True) # norma 3,5-5
    inr = models.CharField(max_length=5, null=True, blank=True) # norma 0,8-1,2
    kreatynina = models.CharField(max_length=5, null=True, blank=True)# norma 53–115 µmol/l (0,6–1,3 mg/dl)
    sod_surowica = models.CharField(max_length=5, null=True, blank=True) # norma 135-145 mmol/l
    bilirubina_cal = models.CharField(max_length=5, null=True, blank=True) # norma 5.1-17.1 μmol/L
    li_rads_hcc = models.CharField(choices=LIRADS_SEL, max_length=10, blank=True)
    afp = models.CharField(max_length=5, null=True, blank=True) # norma od 0 do 40 µg/l
    plt = models.CharField(max_length=5, null=True, blank=True) # norma 150 tys. –400 tys
    cea = models.CharField(max_length=5, null=True, blank=True) # norma 2,5ng/ml niepalących i < 5ng/ml palących papierosy
    ca19_9 = models.CharField(max_length=5, null=True, blank=True) # < 37 U/ml
    cukrzyca = models.CharField(choices=CUKR_SEL, max_length=20, null=True, blank=True)
    marskosc = models.CharField(choices=MARSK_SEL, max_length=20, null=True, blank=True)
    wodobrzusze = models.CharField(choices=WODOBRZ_SEL, max_length=20, null=True, blank=True)
    encefalopatia = models.CharField(choices=ENCEFAL_SEL, max_length=20, null=True, blank=True)
    hbv = models.CharField(choices=HBV_SEL, max_length=20, null=True, blank=True)
    hcv = models.CharField(choices=HCV_SEL, max_length=20, null=True, blank=True)
    kommentarz = models.TextField(max_length=300, null=True, blank=True)
    leczenie = models.TextField(max_length=300, null=True, blank=True)

class LabThumor1(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True)
    thumor_number = models.CharField(max_length=5, null=True, blank=True)
    # 1
    thumor1_segment1 = models.CharField(max_length=5, null=True, blank=True)
    thumor1_segment2 = models.CharField(max_length=5, null=True, blank=True)
    thumor1_segment3 = models.CharField(max_length=5, null=True, blank=True)
    thumor1_diameter = models.CharField(max_length=5, null=True, blank=True)
    # 2
    thumor2_segment1 = models.CharField(max_length=5, null=True, blank=True)
    thumor2_segment2 = models.CharField(max_length=5, null=True, blank=True)
    thumor2_segment3 = models.CharField(max_length=5, null=True, blank=True)
    thumor2_diameter = models.CharField(max_length=5, null=True, blank=True)
    # 3
    thumor3_segment1 = models.CharField(max_length=5, null=True, blank=True)
    thumor3_segment2 = models.CharField(max_length=5, null=True, blank=True)
    thumor3_segment3 = models.CharField(max_length=5, null=True, blank=True)
    thumor3_diameter = models.CharField(max_length=5, null=True, blank=True)
    # 4
    thumor4_segment1 = models.CharField(max_length=5, null=True, blank=True)
    thumor4_segment2 = models.CharField(max_length=5, null=True, blank=True)
    thumor4_segment3 = models.CharField(max_length=5, null=True, blank=True)
    thumor4_diameter = models.CharField(max_length=5, null=True, blank=True)
    # 5
    thumor5_segment1 = models.CharField(max_length=5, null=True, blank=True)
    thumor5_segment2 = models.CharField(max_length=5, null=True, blank=True)
    thumor5_segment3 = models.CharField(max_length=5, null=True, blank=True)
    thumor5_diameter = models.CharField(max_length=5, null=True, blank=True)
    # 6
    thumor6_segment1 = models.CharField(max_length=5, null=True, blank=True)
    thumor6_segment2 = models.CharField(max_length=5, null=True, blank=True)
    thumor6_segment3 = models.CharField(max_length=5, null=True, blank=True)
    thumor6_diameter = models.CharField(max_length=5, null=True, blank=True)
    # 
    top_diameter = models.CharField(max_length=5, null=True, blank=True)