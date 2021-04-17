print("===== Program Latihan Menghitung Diagonal Bidang dan Diagonal Ruang Kubus =====")
import random
rusuk = [7, 4.11 , 11, 23.133 , 33.66 , 41, 57.1 , 61]
print("Telah disediakan berbagai macam angka acak sebagai panjang rusuk kubus"
      "\nKetik P untuk memulai proses pengacakan angka")
variabel = input("Masukkan p : " ).upper()
if variabel == 'P' :
    acak = random.choice(rusuk)
    print("Panjang rusuk kubus :", acak)
    print("Hitunglah Diagonal Ruang dan Diagonal Bidang dengan Panjang Rusuk", acak, "cm" )
    print("====================================================================")
    import math
    bidang = acak * math.sqrt(2)
    print("Diagonal Bidang dari kubus dengan panjang rusuk", acak, "cm adalah", bidang, "cm ~", math.ceil(bidang), "cm.")
    ruang = acak * math.sqrt(3)
    print("Diagonal Ruang dari kubus dengan panjang rusuk", acak, "cm adalah", ruang, "cm ~", math.ceil(ruang), "cm.")
else:
    print("Ulang program dan ketik 'P' untuk mendapatkan sebuah angka.")