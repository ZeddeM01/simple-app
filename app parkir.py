"""
Pada tugas besar ini anda akan membuat sebuah aplikasi parkir yang berfungsi untuk 
mencatat kendaraan yang masuk dan keluar dari area parkir. Aplikasi ini juga akan 
menghitung biaya parkir berdasarkan tarif parkir yang berlaku dan lamanya waktu parkir.
Berikut ini adalah proses yang terjadi ketika kendaraan akan memasuki area parkir:
1. Pengendara akan memasukan nomor/plat kendaraan (contoh: D1234AF)
2. Waktu masuk kendaraan akan dicatat
3. Gerbang masuk akan terbuka (Tampilkan teks: Silahkan masuk)

Berikut ini adalah proses yang terjadi ketika kendaraan akan keluar dari area parkir:
1. Pengendara akan memasukan nomor/plat kendaraan (contoh: D1234AF)
2. Waktu keluar kendaraan akan dicatat
3. Melakukan perhitungan biaya parkir berdasarkan tarif parkir yang berlaku dan
lamanya waktu parkir.
4. Menampilkan biaya parkir
5. Memasukan nominal pembayaran (sebagai pengganti melakukan pembayaran)
6. Gerbang keluar akan terbuka (Tampilkan teks: Terima Kasih)

Berikut ini adalah tarif parkir dan perhitungan biaya parkir yang berlaku:
1. Tarif parkir per 60 detik adalah Rp 10.000

2. Pembulatan waktu parkir
a. Parkir dibawah 60 detik akan dibulatkan atau dianggap atau sama dengan parkir 60 detik
b. Parkir 75 detik akan akan dibulatkan atau dianggap atau sama dengan parkir 120 detik, 
begitu juga seterusnya hingga maksimal waktu parkir adalah 4 menit (240 detik)

3. Denda Parkir
a. Kendaraan yang parkir lebih dari 4 menit akan dikenakan denda 10% dari total
biaya parkir
b. Kendaraan yang parkir lebih dari 6 menit akan dikenakan denda 25% dari total
biaya parkir

Berikut ini adalah batasan yang perlu diterapkan pada aplikasi parkir:
1. Perhitungan biaya parkir hanya dapat dilakukan jika kendaraan masuk terlebih dahulu
ke area parkir lalu keluar dari area parkir. Tampilkan pesan error jika ada yang memilih
menu Keluar Area Parkir tetapi tidak pernah memasuki area parkir sebelumnya
2. Menu Admin Parkir hanya dapat diakses dengan memasukan PIN terlebih dahulu
"""




# Konstanta
TARIF_PER_MENIT = 10000 
DENDA_THRESHOLD_1 = 4
DENDA_THRESHOLD_2 = 6

# Data parkir
parkir = []

# Admin parkir
PIN_ADMIN = "1234"


def hitung_biaya_parkir(waktu_parkir):
    # Pembulatan waktu parkir
    waktu_parkir_bulat = max(60, (waktu_parkir + 59) // 60 * 60) / 60

    # Hitung biaya parkir
    biaya_parkir = TARIF_PER_MENIT * waktu_parkir_bulat 

    return int(biaya_parkir)

def hitung_denda(waktu_parkir, biaya_parkir):
    # Pembulatan waktu parkir
    waktu_parkir_bulat = max(60, (waktu_parkir + 59) // 60 * 60) / 60

    denda = 0
    # Hitung denda
    if waktu_parkir_bulat > DENDA_THRESHOLD_1 and waktu_parkir_bulat <= DENDA_THRESHOLD_2:
        denda += 0.10 * biaya_parkir
    elif waktu_parkir_bulat > DENDA_THRESHOLD_2:
        denda += 0.25 * biaya_parkir
    
    return int(denda)

def masuk_area_parkir():
    nomor_polisi = input("Masukkan nomor polisi: ")
    waktu_masuk = 0  # Waktu masuk diatur langsung saat kendaraan memasuki area parkir

    print("Silahkan masuk")

    data_kendaraan = {
        "nomor_polisi": nomor_polisi,
        "waktu_masuk": waktu_masuk,
        "waktu_keluar": 0,
        "biaya_parkir": 0,
        "denda": 0
    }

    parkir.append(data_kendaraan)


def keluar_area_parkir():
    nomor_polisi = input("Masukkan nomor polisi: ")
    data_kendaraan_keluar = [kendaraan for kendaraan in parkir if kendaraan["nomor_polisi"] == nomor_polisi]

    if not data_kendaraan_keluar:
        print("Kendaraan tidak ditemukan atau tidak pernah masuk.")
        return

    waktu_keluar = int(input("Masukkan waktu keluar (detik): "))
    data_kendaraan_keluar[0]["waktu_keluar"] = waktu_keluar
    waktu_parkir = waktu_keluar - data_kendaraan_keluar[0]["waktu_masuk"]
    data_kendaraan_keluar[0]["biaya_parkir"] = hitung_biaya_parkir(waktu_parkir)
    data_kendaraan_keluar[0]["denda"] = hitung_denda(waktu_parkir, data_kendaraan_keluar[0]["biaya_parkir"])

    # Cetak data kendaraan keluar
    print("\n\n=====Data Kendaraan Keluar=====")
    print("Nomor Polisi:", data_kendaraan_keluar[0]["nomor_polisi"])
    print("Waktu Masuk:", data_kendaraan_keluar[0]["waktu_masuk"], "detik")
    print("Waktu Keluar:", data_kendaraan_keluar[0]["waktu_keluar"], "detik")
    print("Biaya Parkir:", data_kendaraan_keluar[0]["biaya_parkir"])
    print("Denda:", data_kendaraan_keluar[0]["denda"])


def admin_menu():
    global PIN_ADMIN
    pin = input("Masukkan PIN admin: ")

    if pin == PIN_ADMIN:
        print("\n\nAdmin Menu")
        print("1. Ganti PIN Admin")
        print("2. Lihat Data Parkir")
        print("3. Kembali")

        try:
            admin_pilihan = int(input("Pilih menu: "))
        except ValueError:
            print("Input tidak valid. Harap masukkan angka.")
            return

        if admin_pilihan == 1:
            pin_baru = input("Masukkan PIN baru: ")
            PIN_ADMIN = pin_baru
            print("PIN Admin berhasil diubah.")

        elif admin_pilihan == 2:
            print("\n\nData Parkir\n")
            print("Nomor Polisi \t\t| Waktu Masuk \t| Waktu Keluar \t| Biaya Parkir \t| Denda")
            # Mencetak Laporan Kendaraan yang masuk dan keluar
            for i, kendaraan in enumerate(parkir):
                print(f"{i + 1}. {kendaraan['nomor_polisi']} \t| {kendaraan['waktu_masuk']} \t| {kendaraan['waktu_keluar']} \t| {kendaraan['biaya_parkir']} \t| {kendaraan['denda']}")
        
        elif admin_pilihan == 3:
            pass

# Main program
while True:
    print("\nAplikasi Parkir")
    print("1. Masuk Area Parkir")
    print("2. Keluar Area Parkir")
    print("3. Admin Parkir")
    print("4. Keluar")

    pilihan = input("Pilih menu: ")

    try:
        pilihan = int(pilihan)
        if pilihan == 1:
            masuk_area_parkir()
        elif pilihan == 2:
            keluar_area_parkir()
            print("Terima Kasih")
        elif pilihan == 3:
            admin_menu()
        elif pilihan == 4:
            break
        else:
            print("Menu tidak valid. Silakan pilih lagi.")
    except ValueError:
        print("Input tidak valid. Harap masukkan angka.")

