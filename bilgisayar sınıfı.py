import random
import time
class Bilgisayar():

    def __init__(self,pc_durumu = "Kapalı", pc_ses = 0, pc_parlaklık = 0,internet = "Bağlı değil", bluetooth = "Kapalı",program_listesi=["python"]):
        self.pc_durumu = pc_durumu
        self.pc_ses = pc_ses
        self.pc_parlaklık = pc_parlaklık
        self.internet = internet
        self.bluetooth = bluetooth
        self.program_listesi = program_listesi

    def bilgisayarı_ac(self):
        if self.pc_durumu == "Açık":
            print("Bilgisayar zaten açık.")
        else:
            print("Bilgisayar aciliyor....")
            self.pc_durumu = "Açık"

    def bilgisayarı_kapat(self):
        if self.pc_durumu =="Kapalı":
            print("Bilgisayar zaten kapalı.")
        else:
            print("Bilgisayar kapatılıyor....")
            self.pc_durumu = "Kapalı"

    def bilgisayar_ses(self):
        while True:
            cevap = input("Sesi arttırmak icin '>'\nSesi azaltmak icin '<'\nSes ayarından çıkmak için 'q' giriniz: ")
            if cevap == ">":
                if self.pc_ses != 20:
                    self.pc_ses +=1
                    print("Ses: ",self.pc_ses)
            elif cevap == "<":
                if self.pc_ses != 0:
                    self.pc_ses -=1
                    print("Ses: ",self.pc_ses)
            else:
                print("Sesiniz güncellendi:",self.pc_ses)
                break

    def bilgisayar_parlaklığı(self):
        while True:
            cevap1 = input("Parlaklıgı arttırmak icin '>'\nParlaklıgı azaltmak icin '<'\nParlaklık ayarından çıkmak için 'q' giriniz: ")
            if cevap1 == ">":
                if self.pc_parlaklık != 10:
                    self.pc_parlaklık +=1
                    print("Parlaklık: ",self.pc_parlaklık)
            elif cevap1 == "<":
                if self.pc_parlaklık != 0:
                    self.pc_parlaklık -= 1
                    print("Parlaklık: ",self.pc_parlaklık)
            else:
                print("Ekran parlaklığı güncellendi:",self.pc_parlaklık)
                break

    def wifiac(self):
        if self.internet == "Bağlı":
            print("İnternete zaten bağlısınız.")
        else:
            print("İnternete bağlanılıyor...")
            time.sleep(1)
            rastgele1 = random.randint(10,100)
            self.internet = "Bağlı"
            print("İnternete bağlandı.\nHızınız: {} mbps".format(rastgele1))

    def wifikapat(self):
        if self.internet == "Bağlı değil":
            print("İnternete zaten bağlı değilsiniz.")
        else:
            print("İnternet bağlantısı kesiliyor...")
            self.internet = "Bağlı değil"

    def bluetoothac(self):
        if self.bluetooth == "Açık":
            print("Bluetooth zaten açık.")
        else:
            print("Bluetooth açılıyor....")
            self.bluetooth = "Açık"

    def bluetooth_kapat(self):
        if self.bluetooth =="Kapalı":
            print("Bluetooth zaten kapalı.")
        else:
            print("Bluetooth kapatılyor....")
            self.bluetooth = "Kapalı"

    def program_indir(self,indirilecek_programlar):
        print("Program indiriliyor...")
        time.sleep(1)
        self.program_listesi.append(indirilecek_programlar)
        print("Program indirildi.")

    def __len__(self):
        return len(self.program_listesi)

    def __str__(self):
        return "PC durumu: {}\nSes seviyesi: {}\nParlaklık seviyesi: {}\nWifi: {}\nBluetooth: {}\nPC'deki programlar: {}  ".format(self.pc_durumu,self.pc_ses,self.pc_parlaklık,self.internet,self.bluetooth,self.program_listesi)

bilgisayar1 = Bilgisayar()

print("""
************************************
     Bilgisayar Uygulaması

     1-) PC aç
     2-) PC kapat
     3-) Ses ayarları
     4-) Parlaklık ayarları
     5-) Wifi ac
     6-) Wifi kapat
     7-) Bluetooth ac
     8-) Bluetooth kapat
     9-) Program indir
    10-) Program sayısı
    11-) PC'nin durumu
     
     Çıkmak için 'q' ya basınız..
***************************************

""")
while True:
    cevap = input("İşlem seçiniz: ")
    if cevap == "1":
        bilgisayar1.bilgisayarı_ac()
    elif cevap == "2":
        bilgisayar1.bilgisayarı_kapat()
    elif cevap == "3":
        bilgisayar1.bilgisayar_ses()
    elif cevap == "4":
        bilgisayar1.bilgisayar_parlaklığı()
    elif cevap == "5":
        bilgisayar1.wifiac()
    elif cevap == "6":
        bilgisayar1.wifikapat()
    elif cevap == "7":
        bilgisayar1.bluetoothac()
    elif cevap == "8":
        bilgisayar1.bluetooth_kapat()
    elif cevap == "9":
        indirilecek_programlar = input("İndirilecek programları arasında ',' olacak şekilde giriniz:")
        program_listesi = indirilecek_programlar.split(",") #indirilecek_programlar stringi split metoduyla virgüllerin olduğu yerden parçalanır ve liste oluşturur.

        for eklenecek_program in program_listesi:
            bilgisayar1.program_indir(eklenecek_program)
    elif cevap == "10":
        print("Program sayısı: ",len(bilgisayar1))
    elif cevap == "11":
        print(bilgisayar1)
    elif cevap == "q":
        print("Program kapatılıyor")
        break
    else:
        print("Geçersiz işlem")






















