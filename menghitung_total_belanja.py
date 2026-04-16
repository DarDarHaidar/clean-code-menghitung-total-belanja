DISCOUNT_THRESHOLD = 100000
HIGH_DISCOUNT = 0.10
LOW_DISCOUNT = 0.05

def calculate_total_price(price, quantity):
    """
    Menghitung total harga setelah diskon.

    Parameter:
    price (int/float): Harga satuan barang
    quantity (int): Jumlah barang yang dibeli

    Returns:
    float: Total harga setelah diskon
    """
    total = price * quantity
    discount = get_discount(total)
    return total - discount


def get_discount(total):
    """
    Menentukan besar diskon berdasarkan total belanja.

    Jika total lebih dari DISCOUNT_THRESHOLD,
    maka menggunakan HIGH_DISCOUNT, jika tidak LOW_DISCOUNT.

    Parameter:
    total (int/float): Total harga sebelum diskon

    Returns:
    float: Nilai diskon
    """
    if total > DISCOUNT_THRESHOLD:
        return total * HIGH_DISCOUNT
    return total * LOW_DISCOUNT


def print_total(total_price):
    """
    Menampilkan total harga ke layar.

    Parameter:
    total_price (float): Total harga setelah diskon
    """
    print(f"Total belanja: {total_price}")


def main():
    """
    Fungsi utama program.
    Mengatur alur input dan output program.
    """
    price = 50000
    quantity = 3

    total_price = calculate_total_price(price, quantity)
    print_total(total_price)


# Menjalankan program
if __name__ == "__main__":
    main()
