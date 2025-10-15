a=3.5
print(type(a))

nama="ade"
print(type(nama))

angka=[1,2,3,4,5]
print(type(angka))

Belanjaan=["Beras","Minyak","Telur"]
Belanjaan.append("Gula")
Belanjaan.append("Kopi")
print("Daftar belanjaan")
for x in Belanjaan:
    print("-", x)

Dictionary={'Beras':12000,'Minyak':17000,'Telur':24000,'Gula':15000,'Kopi':20000}
list=[Dictionary[x] for x in Belanjaan]
total=sum(list)
print("Total belanjaan: Rp", total)

def luasPersegiPanjang(panjang, lebar):
    luas= panjang * lebar
    keliling= 2 * (panjang + lebar)
    return ('Luas :' , luas , 'Keliling  :' , keliling)
print (luasPersegiPanjang(11, 12))

percabangan=int(input("Masukkan Usia: "))
if percabangan >= 0 and percabangan < 13:
    print("Anak")
if percabangan >= 14 and percabangan < 24:
    print("Remaja")
if percabangan >= 25 and percabangan < 49:
    print("Dewasa")
if percabangan >= 50:
    print("Lansia")

