# program menghitung total belanja

def h(a, b, c):
    # a = harga, b = jumlah, c = diskon
    t = a * b
    if t > 100000:
        t = t - (t * 0.1)
    else:
        t = t - (t * 0.05)
    print("Total:", t)

h(50000, 3, 0)
