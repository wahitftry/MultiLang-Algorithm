# Mendefinisikan matriks koefisien dan vektor hasil
A = [[3, 2, -1], [2, -2, 4], [-1, 0.5, -1]]
b = [1, -2, 0]

# Mencari solusi dengan metode eliminasi Gauss
for i, item in enumerate(A):
    # Mencari elemen dengan nilai absolut terbesar di kolom i
    maxElem = abs(item[i])
    maxRow = i
    for k in range(i + 1, len(A)):
        if abs(A[k][i]) > maxElem:
            maxElem = abs(A[k][i])
            maxRow = k

    # Menukar baris dengan elemen terbesar ke baris i
    for k in range(i, len(A) + 1):
        tmp = A[maxRow][k]
        A[maxRow][k] = item[k]
        item[k] = tmp
    tmp = b[maxRow]
    b[maxRow] = b[i]
    b[i] = tmp

    # Membuat elemen di bawah diagonal menjadi nol
    for k in range(i + 1, len(A)):
        c = -A[k][i] / item[i]
        for j in range(i, len(A) + 1):
            if i == j:
                A[k][j] = 0
            else:
                A[k][j] += c * item[j]
        b[k] += c * b[i]

# Mencari solusi dari persamaan
x = [0 for i in range(len(A))]
for i in range(len(A) - 1, -1, -1):
    x[i] = b[i] / A[i][i]
    for k in range(i - 1, -1, -1):
        b[k] -= A[k][i] * x[i]

# Menampilkan solusi
print("Solusi dari persamaan:")
for i, item in enumerate(x):
    print(f"x{i+1} = {item}")