""" 
Problem:
Anda adalah seorang Programmer di Daspro Laboratory. Daspro membutuhkan 
suatu program kalkulator pintar yang memungkinkan pengguna melakukan 
operasi matematika sederhana antara dua angka. Program ini menggunakan 
function untuk setiap operasi matematika (penjumlahan, pengurangan, 
perkalian, dan pembagian), menggunakan exception handling untuk memastikan 
bahwa input yang dimasukkan oleh pengguna adalah angka, dan memberikan 
pesan khusus jika terjadi pembagian oleh nol.

Requirements:
● Program meminta 2 angka
● Buatkan function untuk masing-masing operasi (penjumlahan, pengurangan,
perkalian, pembagian)
● Gunakan exception ZeroDivisionError jika angka kedua yang dimasukkan
adalah 0 dan operasi yang dipilih adalah pembagian. Berikan pesan 
"Tidak dapat melakukan pembagian dengan bilangan 0" jika error terjadi 
(Hint: Gunakan raise)
● Gunakan exception ValueError jika user memasukkan data selain integer
● Gunakan syntax finally untuk menampilkan pesan “Terima kasih sudah 
menggunakan kalkulator pintar!”
"""


def penjumlahan(a,b):
    return a+b

def pengurangan(a,b):
    return a-b

def perkalian(a,b):
    return a*b

def pembagian(a,b):
    if b == 0:
        raise ZeroDivisionError("pembagi bernilai 0, operasi dihentikan") 
    return  a/b

def main_menu():
    try:
        print("\n===========KALKULATOR PINTAR===========\n")
        a = int(input(f'masukkan angka pertama : '))
        b = int(input(f'masukkan angka kedua   : '))
        print("menu operasi : \n1.Penjumlahan \n2.Pengurangan \n3.Perkalian \n4.Pembagian\n")
        opsi = input(f'pilih operasi yang diinginkan')

        if not opsi.isdigit() or int(opsi) not in [1, 2, 3, 4]:
            raise ValueError("operasi tidak tersedia")
        else:
            opsi = int(opsi)
        
        if opsi == 1:
            hasil = penjumlahan(a,b)
            print(f"hasil penjumlahannya {hasil}")
        elif opsi ==2:
            hasil = pengurangan(a,b)
            print(f"hasil pengurangannya {hasil}")
        elif opsi ==3:
            hasil = perkalian(a,b)
            print(f"hasil perkaliannya {hasil}")
        elif opsi ==4:
            hasil = pembagian(a,b)
            print(f"hasil pembagiannya {hasil}")

    except ValueError as err:
        print(err)
    except ZeroDivisionError as err:
        print(err)
    finally:
        print("\nterima kasih sudah menggunakan aplikasi ini!!")
    
if __name__ == "__main__":
    main_menu()