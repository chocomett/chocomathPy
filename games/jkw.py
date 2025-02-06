import libs 

def hitung_jarak(kecepatan, waktu):
    """Menghitung jarak jika diketahui kecepatan dan waktu."""
    return kecepatan * waktu

def hitung_kecepatan(jarak, waktu):
    """Menghitung kecepatan jika diketahui jarak dan waktu."""
    return jarak / waktu

def hitung_waktu(jarak, kecepatan):
    """Menghitung waktu jika diketahui jarak dan kecepatan."""
    return jarak / kecepatan

def start():    
    while True:
        print("\nPilih jenis perhitungan:")
        print("1. Hitung Jarak")
        print("2. Hitung Kecepatan")
        print("3. Hitung Waktu")
        print("4. Keluar")

        pilihan = input("Masukkan pilihan (1/2/3/4): ")

        if pilihan == '4':
            libs.wellcome_message()   
            libs.menu()

        try: #mencegah user salah memasukan inputan
            if pilihan == '1':
                kecepatan = float(input("Masukkan kecepatan: "))
                waktu = float(input("Masukkan waktu: "))
                jarak = hitung_jarak(kecepatan, waktu)
                print("Jarak:", jarak)
            elif pilihan == '2':
                jarak = float(input("Masukkan jarak: "))
                waktu = float(input("Masukkan waktu: "))
                kecepatan = hitung_kecepatan(jarak, waktu)
                print("Kecepatan:", kecepatan)
            elif pilihan == '3':
                jarak = float(input("Masukkan jarak: "))
                kecepatan = float(input("Masukkan kecepatan: "))
                waktu = hitung_waktu(jarak, kecepatan)
                print("Waktu:", waktu)
            else:
                print("Pilihan tidak valid.")
        except ValueError:
            print("Input tidak valid. Masukkan angka.")
        
        
if __name__ == "__main__":
    start()