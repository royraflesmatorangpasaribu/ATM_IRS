import datetime
import time
import random

user = {
        "id" : "1037", 
	"nama" : "Ikhsan Saputra",
        "pin" : "250803",
        "norek" : "2117051037",
        "saldo" : 500000
        },{
        "id" : "1058",
        "nama" : "Roy Rafles",
        "pin" : "050503",
        "norek" : "2117051058",
        "saldo" : 1000000
        },{
        "id" : "1068",
        "nama" : "Siti Ayuni",
        "pin" : "251002",
        "norek" : "2117051068",
        "saldo" : 1500000      
	}
    	
ewallet = {1 : 'Dana', 2 : 'Shopeepay', 3 : 'Gopay'}
nohp ={1:['081234567890','Ayuni'],2: ['085678901234', 'Roy Rafles'], 3:['087890123456','Ikhsan']}
admin = [0,2500,2000]
login = False
id_user = 0
waktu = 0
waktu = datetime.datetime.now()

def splash():
    print("")
    print("================================================")
    print("|	    --	      ATM IRS      --          |")
    print("================================================")
    print("")
    print("----    Selamat Datang di IRS BANK    ----  ")
    print("\tTransaksi Menjadi Lebih Mudah\t")
    print("================================================")

def cekpin(cpin):
    for usr in user:
        if usr['pin'] == cpin:
            return usr
    return False

def cek_user(id):
    for i in range(len(user)):
        if user[i]['id'] == str(id):
            return int(i)
    return 0

def cek_norek(cno):
    for i in range(len(user)):
        if str(user[i]['norek']) == str(cno):
            return int(i)
    return -1

def transfer(nominal, norek):
    inisial1 = cek_user(id_user)
    inisial2 = cek_norek(norek)
    if inisial1 >=0:
        if  user[inisial1]['saldo'] >= int(nominal):
            user[inisial1]['saldo'] = user[inisial1]['saldo'] - int(nominal)
            user[inisial2]['saldo'] = user [inisial2]['saldo'] + int(nominal)
            print("Anda berhasil transfer uang sebesar Rp. " + str(nominal) + " ke nomor rekening " + norek)
            print("Sisa Saldo Anda adalah Rp. ", user[inisial1]['saldo'])

            
            print("")
            time.sleep(3)
            print("=================================================")
            print("|		RESI TRANSAKSI		        |")
            print("|	   --	     ATM IRS      --            |")
            print("=================================================")
            print("|Waktu  : ", str(waktu),"\t\t|")
            print("|Lokasi : Jl. Prof. Dr. Ir. Sumantri Brojonegoro|")
            print("|No.Record : ", random.randint(10000, 1000000), "\t\t\t\t|")
            print("|\t\t\t\t\t\t|")
            print("|Nama Pengirim    : ", user[inisial1]['nama'], "\t\t|")
            print("|Norek. Pengirim  : ", user[inisial2]['norek'], "\t\t|")
            print("|Nama Penerima    : ", user[inisial2]['nama'],"\t\t|")
            print("|Norek. Penerima  : ", user[inisial2]['norek'],"\t\t|") 
            print("|Jumlah		  : Rp.", nominal,"\t\t\t|")
            print("|Sisa Saldo\t  : Rp ",user[inisial1]['saldo'],"\t\t|")
            print("|\t\t\t\t\t\t|")
            print("================================================")
            print("|\t PERBARUI SEGERA DATA ANDA\t\t|")
            print("|\tDGN MENGHUBUNGI CUSTOMER SERVICE\t|")
            print("|\tDI CABANG TERDEKAT BANK IRS\t\t|")
            print("|\tINFO : IRS CALL 18900\t\t\t|")
            print("================================================")
        else:
            print("Maaf Saldo Anda Tidak Cukup")

def kembali(ulang):
    ulang = input("Apakah Anda Ingin Transaksi Lagi?(Y/T)")
    if ulang == "T":
        print("\n\t ======== SILAHKAN AMBIL KARTU ANDA ======== ")
        print("")
        print("\n\t ---Terima Kasih Telah Menggunakan ATM IRS---")
        print('=================================================')
        exit()

while login == False:
    splash()
     
    for i in range (3):
        username = input("Username Anda : ")
        pin = input("Masukkan Pin ATM : ")
        cp = cekpin(pin)
        if cp != False:
            print("")
            print("NOTIFIKASI !!!")
            print("Pin Anda Benar")
            print("Username Anda : ", username.upper())
            id_user = cp['id']
            login = True
            ulang = "Y"
            break
        else:
            print("PIN ANDA SALAH, COBA LAGI!")
            if i ==2:
                print("==================================================")
                print("  ANDA TELAH SALAH MEMASUKKAN PIN SEBANYAK 3X ")
                print(" KARTU ATM ANDA TERBLOKIR \t\t")
                print(" Silahkan Kunjungi Cabang Bank IRS Terdekat ")
                print("==================================================")
                exit()
         
    ulang = "Y"
    while ulang == "Y" and login == True:
        us = user[cek_user(id_user)]
        os.system('cls')
        print("")
        splash()
        print("================================================")
        print("|       Pilih Transaksi Yang Anda Inginkan      |")
        print("================================================")
        print("| 1. Informasi Saldo\t\t\t\t|")
        print("| 2. Setor Tunai\t\t\t\t|")
        print("| 3. Tarik Tunai\t\t\t\t|")
        print("| 4. Transfer\t\t\t\t\t|")
        print("| 5. Keluar\t\t\t\t\t|")
        print("================================================")
        try:
            pilihan = int(input("Masukkan Pilihan Anda : "))
            if pilihan < 0 or pilihan > 5:
                raise ValueError 
        except ValueError():
            print("Menu Yang Anda Pilih Tidak Tersedia")

        if pilihan == 1:
            print("Saldo Anda Sebesar    : Rp ", us['saldo'])
            kembali(ulang)

        elif pilihan == 2:
            print("*** SETOR TUNAI HANYA DAPAT DILAKUKAN DENGAN KELIPATAN RP 50000 ***")
            setor = int(input("Masukkan Jumlah Setor Tunai : Rp "))
            if setor % 50000 == 0:
                us['saldo'] = us['saldo'] + setor
                print("--- SETOR TUNAI BERHASIL ---")
                print("Sisa Saldo Anda adalah: Rp ", us['saldo'])

                print(" ")
                time.sleep(3)
                print("==================================================")
                print("|	      RESI SETOR TRANSAKSI		 |")
                print("|	    --	     ATM IRS      --             |")
                print("==================================================")
                print("| Waktu  : ", str(waktu), "\t\t |")
                print("| Lokasi : Jl. Prof. Dr. Ir. Sumantri Brojonegoro|")
                print("| No.Record : ", random.randint(10000, 1000000), "\t\t\t\t |")
                print("|\t\t\t\t\t\t |")
                print("| Setor Ke Tabungan  : Rp ", setor, "\t\t |")
                print("| Saldo Anda         : Rp ",us['saldo'], "\t\t |")
                print("|================================================|")
                print("|                    ATM IRS                     |")
                print("|-------- Transaksi Menjadi Lebih Mudah ---------|")
                print("==================================================")
            else:
                print("Nominal Tidak Sesuai")
            kembali(ulang)

        elif pilihan == 3:
            print("*** TARIK TUNAI HANYA DAPAT DILAKUKAN DENGAN KELIPATAN RP 50000")
            tarik = int(input("Masukkan Jumlah Penarikan: Rp "))
            if tarik % 50000 == 0:
                if us['saldo'] >= tarik:
                    us['saldo'] = us['saldo'] - tarik
                    print("---- TARIK TUNAI BERHASIL ----")
                    print("Sisa Saldo Anda adalah: Rp ", us['saldo'])
                    print("")
                    print("")
                    time.sleep(3)
                    print("==================================================")
                    print("|	      RESI TARIK TRANSAKSI		 |")
                    print("|	    --	     ATM IRS      --             |")
                    print("==================================================")
                    print("| Waktu  : ", str(waktu), "\t\t |")
                    print("| Lokasi : Jl. Prof. Dr. Ir. Sumantri Brojonegoro|")
                    print("| No.Record : ", random.randint(10000, 1000000), "\t\t\t\t |")
                    print("|\t\t\t\t\t\t |")
                    print("| Tarik Ke Tabungan  : Rp ", tarik, "\t\t |")
                    print("| Saldo Anda         : Rp ",us['saldo'], "\t\t |")
                    print("|================================================|")
                    print("|                    ATM IRS                     |")
                    print("|-------- Transaksi Menjadi Lebih Mudah ---------|")
                    print("==================================================")
                elif us['saldo'] < tarik:
                    print("Maaf Saldo Anda Tidak Cukup")
            else:
                print("Nominal Tidak Sesuai")
            kembali(ulang)

        elif pilihan == 4:
            print("Saldo Anda Sebesar\t\t : Rp ", us['saldo'])
            rektf=input("Masukkan Nomor Rekening Tujuan   : ")
            cekno = cek_norek(rektf)
            if cekno >= 0:
                jumlah=int(input("Masukkan Jumlah Nominal Transfer : Rp "))
                transfer(jumlah,rektf)
            else:
                print("Nomor Rekening Tidak Ditemukan")
            kembali(ulang)
	
	elif pilihan == 5 :
            print("")
            print("DAFTAR PEMBAYARAN E-WALLET")
            print("1. Dana\n2. Shopeepay\n3. Gopay")
            pilih=int(input("Masukkan pilihan Anda : "))
            print("")
            for i in range (1,4):
                if pilih == i:
                    print("Jenis E-wallet : ", ewallet[i])
                    print('1. Top Up\n2. Pembayaran')
                    t1 = int(input("Masukkan Pilihan Anda : "))
                    if t1 == 1:
			no=input("Masukkan Nomor Hp : ")
                        for i in range(1,len(nohp)+1) :
                            if no == nohp[i][0] :
				print("Nama Akun : ", nohp[i][1])
                    elif t1==2:
                        kode=input("Masukkan Kode Pembayaran : ")
                        print("Kode Pembayaran : ", kode.upper())
                    else :
                        print("Pilihan Anda Tidak Sesuai")
                        break
                    harga=int(input("Masukkan Nominal Pembayaran : Rp "))
                    subtotal=harga+admin[i-1]
                    print("Total Pembayaran : Rp ",subtotal)
                    us['saldo'] = us['saldo'] - subtotal
                    print("Sisa Saldo : Rp ",us['saldo'])

            kembali(ulang)

        else : 
            print("\n ======== SILAHKAN AMBIL KARTU ANDA ======== ")
            print("")
            print("\n ---Terima Kasih Telah Menggunakan ATM IRS---")
            print('=================================================')
            exit()
