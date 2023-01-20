print('=====CONDITION=====') 
print('===IF===')

visit_volume = 13
if visit_volume > 10:
    print("mobil berjalan...")
if visit_volume < 10:
    print("mobil menunggu penumpang lain...")

print("Di luar condition")
print('\n===IF ELSE===')

score = 78

if score > 75:
    print('lulus')
else : 
    print('Tidak lulus')
print('\n===IF ELIF ELSE===')

score = 78
if score >=85:
    print('predikat A/Memuaskan')
elif score >= 75:
    print('predikat B/Bagus')
else:
    print('tidak lulus')

kelas = 3
score = 90

if kelas > 1:
    if score >= 85:
        print('predikat A/Memuaskan')
    elif score >= 75:
        print('predikat B/Bagus')
    else:
        print('Tidak Lulus')

else:
    if score >= 80:
        print('Predikat A/Bagus')
    else:
        print('Tidak Lulus')
num = float(input("masukan angka : "))
if num >= 0:
    if num == 0:
        print("Nol")
    else:
        print("angka positif")