print("\n======ERROR HANDLING======")
print("===SYNTAX ERROR===")
# syntax error

# for fruit in fruit_list
#    print(fruit)

print("===LOGICAL ERROR===")
# Logical error


class ValueTooSmallError(Exception):
    pass


class ValueTooLargeError(Exception):
    pass


number = 10

while True:
    try:
        i_num = int(input("masukan angka: "))

        if i_num < number:
            raise ValueTooSmallError
        elif i_num > number:
            raise ValueTooLargeError
        break

    except ValueTooSmallError:
        print("Angka yang kamu tebak terlalu kecil, coba lagi")
    except ValueTooLargeError:
        print("angka yang kamu tebak terlalu besar, coba lagi")

print("betul! kamuu berhasil menebak dengan tepat")

# kita tetap bisa mengatasi error dengan Error Handling yang berguna sehingga tidak sampai break aplikasi yang kita jalankan
