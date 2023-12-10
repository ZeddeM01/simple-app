""" 
Andika adalah seorang karyawan baru di Puskesmas DASPRO. Untuk tugas 
pertamanya, Andika diminta untuk membuat program yang bisa menghitung 
BMI (Body Mass Index) dari pasien puskesmas. Program yang dibuat harus 
bisa input dan menyimpan data pasien puskesmas dalam list, kemudian 
bisa menghitung BMI dari pasien yang dipilih. Karena dokter di puskesmas 
sangat perfeksionis, program yang diminta harus bisa mengatasi kesalahan 
apapun yang mungkin terjadi. Sebagai Andika, tugas mu cukup membuat 
program python yang dapat:
a) Input Nama, Berat Badan dan Tinggi Badan pasien
b) Input angka untuk memilih data pasien dalam list
c) Menampilkan hasil nilai BMI pasien dan kategorinya
d) Menampilkan program telah berakhir jika memilih menu exit

Gunakan fungsi untuk menghitung BMI dan menentukan kategori BMI yang 
sesuai dari hasil perhitungan. Jangan lupa untuk menggunakan exception 
handling untuk mengatasi error yang mungkin terjadi.

Kategori BMI yang bisa digunakan : 
Kurang dari 18.5 (Underweight) 
18.5 - 24.9 (Normal)
25 - 29.9 (Overweight)
Lebih dari 30 (Obesitas)

Rumus menghitung BMI : 
BMI = Berat Badan (Kg)/(Tinggi(m))**2
 """

## buat array untuk menyimpan data pasien yang diinputkan
pasien = []

## Fungsi Input data Pasien
def user_input():

    nama = input(f'masukkan nama pasien :')
    berat = float(input(f'masukkan berat badan pasien (Kg): '))
    tinggi_cm = int(input(f'masukkan tinggi badan pasien (cm): '))
    tinggi = tinggi_cm/100
    print('data berhasil diinputkan')
    
    data_pasien = {
        "Nama":nama,
        "Berat":berat,
        "Tinggi":tinggi
    }
    ## Menambahkan dict data_pasien ke dalam array pasien 
    pasien.append(data_pasien)

    return pasien

## Fungsi perhitungan BMI
def bmi_calc(pasien_dipilih):
    try:
        pasien_dipilih = pasien_dipilih
        ## akses Berat dan Tinggi dari dict 
        berat, tinggi = pasien_dipilih["Berat"], pasien_dipilih["Tinggi"] 
        ## rumus BMI
        bmi = berat / (tinggi**2)
        return bmi
    ## Error Handling untuk pembagi bernilai 0
    except ZeroDivisionError:
        print("Error: Tinggi bernilai 0, tidak bisa dibagi.")
        return None

## Fungsi Kategori BMI
def kategori_bmi(bmi):
    if bmi is None:
        return None
    elif bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi <= 24.9:
        return "Normal"
    elif 25 <= bmi <= 29.9:
        return "Overweight"
    else:
        return "Obesitas"

def main_menu():
    while True:
        print ("\n================Kalkulator BMI================\n")
        print("Menu :\n 1.Input Data User\n 2.Hitung BMI Pasien\n 3.Exit")
    
        mm_option = input(f'masukkan pilihan anda :')

        ## Case handling untuk menu pilihan user
        if mm_option == "1":
            print("\n----------Input Data Pasien----------")
            user_input()

        elif mm_option == "2":
            print("\n----------Perhitungan BMI----------")
            if not pasien:
                print("tidak ada data pasien yang tedaftar")
            else:
                print("Pilih data pasien:")
                print("nama Pasien \t\t| Berat(Kg)\t| Tinggi(m)")
                
                ## perulangan untuk mengambil value dari pasien berdasarkan key
                for i, pas in enumerate(pasien):
                    print(f"{i + 1}. {pas['Nama']} \t\t| {pas['Berat']} \t\t| {pas['Tinggi']}")

                try:
                    index = int(input()) - 1 ## input opsi nomor pasien 
                    pasien_dipilih = pasien[index]
                    bmi_value = bmi_calc(pasien_dipilih)
                    kategori = kategori_bmi(bmi_value)

                    print(f"BMI Pasien {pasien_dipilih['Nama']}: {bmi_value:.2f}")
                    print(f"Kategori BMI: {kategori}")
                ## error handling untuk input yang tidak ada/ tidak sesuai dengan format
                except (ValueError, IndexError):
                    print("Input tidak valid. Masukkan nomor yang sesuai.")
            
        elif mm_option =="3":
            print("\nprogram telah berakhir")
            break
        else:
            print('\nopsi tidak tersedia')

## Run Code
if __name__ == '__main__':
    main_menu() 
