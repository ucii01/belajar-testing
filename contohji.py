def hitung_total(angka1:int, angka2:int)->int:
    if not isinstance(angka1, int) or not isinstance(angka2, int):
        raise TypeError("Parameter harus bertipe integer!")
    return angka1 + angka2

if __name__=="__main__":
    a=int(input("masukkan angka pertama: "))
    b=int(input("masukkan angka kedua: "))
    hasil = hitung_total(a,b)
    print(f"Hasil penjumlahan: {hasil}")