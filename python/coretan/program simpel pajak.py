def hitung_pajak(gaji, tanggungan):
    if gaji <= 50000000:
        pajak = 0.05 * gaji
    elif gaji <= 250000000:
        pajak = 0.1 * (gaji - 50000000) + 2500000
    elif gaji <= 500000000:
        pajak = 0.2 * (gaji - 250000000) + 27500000
    elif gaji <= 1000000000:
        pajak = 0.3 * (gaji - 500000000) + 77500000
    else:
        pajak = 0.35 * (gaji - 1000000000) + 227500000

    if tanggungan == 0:
        pengurangan_pajak = 0
    elif tanggungan == 1:
        pengurangan_pajak = 4000000
    elif tanggungan == 2:
        pengurangan_pajak = 8000000
    elif tanggungan == 3:
        pengurangan_pajak = 12000000
    else:
        pengurangan_pajak = 12000000 + (tanggungan - 3) * 3000000

    pajak -= pengurangan_pajak

    return pajak

gaji = int(input("Masukkan gaji tahunan: "))
tanggungan = int(input("Masukkan jumlah tanggungan: "))

pajak = hitung_pajak(gaji, tanggungan)

print("Pajak yang harus dibayar: Rp", pajak)