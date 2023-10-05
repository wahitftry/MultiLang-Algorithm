def hitung_pajak(gaji_tahunan, jumlah_tanggungan):
    if gaji_tahunan <= 50000000:
        pajak = 0.05 * gaji_tahunan
    elif gaji_tahunan <= 250000000:
        pajak = 0.1 * (gaji_tahunan - 50000000) + 2500000
    elif gaji_tahunan <= 500000000:
        pajak = 0.2 * (gaji_tahunan - 250000000) + 27500000
    elif gaji_tahunan <= 1000000000:
        pajak = 0.3 * (gaji_tahunan - 500000000) + 77500000
    else:
        pajak = 0.35 * (gaji_tahunan - 1000000000) + 227500000

    if jumlah_tanggungan == 0:
        pengurangan_pajak = 0
    elif jumlah_tanggungan == 1:
        pengurangan_pajak = 4000000
    elif jumlah_tanggungan == 2:
        pengurangan_pajak = 8000000
    elif jumlah_tanggungan == 3:
        pengurangan_pajak = 12000000
    else:
        pengurangan_pajak = 12000000 + (jumlah_tanggungan - 3) * 3000000

    pajak -= pengurangan_pajak

    return pajak

gaji_tahunan = int(input("Masukkan gaji tahunan: "))
jumlah_tanggungan = int(input("Masukkan jumlah tanggungan: "))

pajak = hitung_pajak(gaji_tahunan, jumlah_tanggungan)

print("Pajak yang harus dibayar: Rp", pajak)