from time import sleep

sayı = input("Süreyi verin (saniye cinsinden): ")

try:
    sayı = int(sayı)
    while sayı > 0:
        print(f"{sayı} saniye kaldı")
        sayı -= 1
        sleep(1)
    print("\nSüre doldu")
except:
    print("Hata, sayı yazdığınızdan emin olun.")
