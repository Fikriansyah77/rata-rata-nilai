def nilai_ratarata(jumlah_mahasiswa):
    daftar_nilai = []  # Membuat list untuk menyimpan nilai mahasiswa
    for i in range(1, jumlah_mahasiswa + 1):
        nilai = float(input(f"Masukkan nilai mahasiswa ke-{i}: "))
        daftar_nilai.append(nilai)  # Menambahkan nilai ke dalam list
    rata_rata = sum(daftar_nilai) / jumlah_mahasiswa  # Menghitung rata-rata dengan sum dan jumlah elemen list
    return rata_rata, daftar_nilai

def main():
    jumlah_mahasiswa = int(input("Masukkan jumlah mahasiswa: "))
    rata_rata, daftar_nilai = nilai_ratarata(jumlah_mahasiswa)
    print(f"\nNilai rata-rata dari {jumlah_mahasiswa} mahasiswa adalah: {rata_rata:.2f}")
    print("Daftar nilai mahasiswa:", daftar_nilai)

main()
