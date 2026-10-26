# # input
# nilai = int(input("masukkan nilai:"))
# # proses 
# if  nilai >=80 and nilai <=100:
#     print("anda mendapatkan nilai A")
# elif nilai >=70 and nilai <=80:
#     print("anda mendapatkan nilai B")
# elif nilai >=50 and nilai <=70:
#     print("anda mendapatkan nilai C")
# elif nilai >=30 and nilai <=50:
#     print("anda mendapatkan nilai D")
# elif nilai >=0 and nilai <=20:
#     print("anda mendapatkan nilai E")
# else:
#      print("data tidak valid") 




barang = input("masukkan nama barang ")
harga = int(input("masukkan harga barang1:"))

if barang == "kulkas": 
    print (barang)
    print (harga - (harga * 0.10))
elif barang == "TV":
    print (barang)
    print (harga - (0.05 * harga))
else:
    print (barang)
    print (harga)


 



