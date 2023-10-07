def hitung_pajak(gaji_in, tanggungan_in):
    if gaji_in <= 50000000:
        pajak = 0.05 * gaji_in
    elif gaji_in <= 250000000:
        pajak = 0.1 * (gaji_in - 50000000) + 2500000
    elif gaji_in <= 500000000:
        pajak = 0.2 * (gaji_in - 250000000) + 27500000
    elif gaji_in <= 1000000000:
        pajak = 0.3 * (gaji_in - 500000000) + 77500000
    else:
        pajak = 0.35 * (gaji_in - 1000000000) + 227500000

    if tanggungan_in == 0:
        pengurangan_pajak = 0
    elif tanggungan_in == 1:
        pengurangan_pajak = 4000000
    elif tanggungan_in == 2:
        pengurangan_pajak = 8000000
    elif tanggungan_in == 3:
        pengurangan_pajak = 12000000
    else:
        pengurangan_pajak = 12000000 + (tanggungan_in - 3) * 3000000

    pajak -= pengurangan_pajak

    return pajak

gaji_input = int(input("Masukkan gaji tahunan: "))
tanggungan_input = int(input("Masukkan jumlah tanggungan: "))

pajak_result = hitung_pajak(gaji_input, tanggungan_input)

print("Pajak yang harus dibayar: Rp", pajak_result)