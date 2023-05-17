N'''
NAMA    : HILMY ZHAFRAN DAY TAQY
NIM     : 1202213167
KELAS   : SI-45-06
MATKUL  : ALGORITMA DAN PEMROGRAMAN
DOSEN   : Dr. Teguh Nurhadi Suharsono, S.T., M.T.
TUGAS   : TUGAS BESAR DENGAN JUDUL "PROGRAM ADMINISTRASI LIMUS PRATAMA HOSPITAL"
'''
from prettytable import PrettyTable
import time
from time import sleep
from rich.console import Console
import datetime
from rich.progress import Progress
from os import system
import sys

list_pasien = []                #LIST DATA PASIEN
list_id = []                    #LIST DATA ID PASIEN

noroom = 0                      #JUMLAH PASIEN YANG TIDAK DIRAWAT
noicu = 0                       #JUMLAH PASIEN YANG BERADA DI RUANGAN ICU
nohcu = 0                       #JUMLAH PASIEN YANG BERADA DI RUANGAN HCU
nonicu = 0                      #JUMLAH PASIEN YANG BERADA DI RUANGAN NICU
nopicu = 0                      #JUMLAH PASIEN YANG BERADA DI RUANGAN PICU
noiccu = 0                      #JUMLAH PASIEN YANG BERADA DI RUANGAN ICCU

class color:                    #CLASS WARNA OUTPUT
    purple = '\033[95m'
    cyan = '\033[96m'
    darkcyan = '\033[36m'
    blue = '\033[94m'
    green = '\033[92m'
    yellow = '\033[93m'
    red = '\033[91m'
    bold = '\033[1m'
    underline = '\033[4m'
    end = '\033[0m'

def getNo_id(room):             #FUNGSI UNTUK MENDAPATKAN ID PASIEN
    global noroom, noicu, nohcu, nonicu, nopicu, noiccu
    if room == 1:
        noicu += 1
        return "001-" + "0" * (3-len(str(noicu))) + str(noicu)
    elif room == 2:
        nohcu += 1
        return "002-" + "0" * (3-len(str(nohcu))) + str(nohcu)
    elif room == 3:
        nonicu += 1
        return "003-" + "0" * (3-len(str(nonicu))) + str(nonicu)
    elif room == 4:
        nopicu += 1
        return "004-" + "0" * (3-len(str(nopicu))) + str(nopicu)
    elif room == 5:
        noiccu += 1
        return "005-" + "0" * (3-len(str(noiccu))) + str(noiccu)
    elif room == 0:
        noroom += 1
        return "000-" + "0" * (3-len(str(noroom))) + str(noroom)

def loading():                  #FUNGSI LOADING SEBELUM MAIN MENU
    with Progress() as progress:

        task1 = progress.add_task("[bold red]PLEASE WAIT...", total=100)

        while not progress.finished:
            progress.update(task1, advance=0.5)
            time.sleep(0.01)

    print(color.green + "DONE...!" + color.end)
    sleep(1)

def progress():                 #FUNGSI PROGRESS SCREEN SAAT PEMBAYARAN
    console = Console()
    tasks = [f"Tahap {n}" for n in range(1, 6)]

    with console.status("[bold green]Sedang Diproses...") as status:
        while tasks:
            task = tasks.pop(0)
            sleep(1.1)
            console.log(f"{task} berhasil")

def Insert():                   #FUNGSI INPUT DATA PASIEN KEDALAM LIST PASIEN
    while True:
        try:
            nama = input("Masukkan Nama Pasien\t\t: ")
            gender = input("Masukkan Jenis Kelamin Pasien\t: ")
            umur = int(input("Masukkan Umur Pasien\t\t: "))
            alamat = input("Masukkan Alamat Pasien\t\t: ")
            no_phone = input("Masukkan Nomor Handphone\t: ")
            penyakit = input("Penyakit yang Dialami\t\t: ")
            
            check = input("Apakah Pasien Ingin Dirawat(y/n)? ")
            if check == "y":
                while True:
                    print(color.green + color.bold + "\n>>SELECT ROOM TO PATIENT<<" + color.end)
                    print(color.bold + color.blue + "[1]" + color.end, "Intensive Care Unit (ICU)")
                    print(color.bold + color.blue + "[2]" + color.end, "High Care Unit (HCU)")
                    print(color.bold + color.blue + "[3]" + color.end, "Intensive Coronary Care Unit (ICCU)")
                    print(color.bold + color.blue + "[4]" + color.end, "Neonatal Intensive Care Unit (NICU)")
                    print(color.bold + color.blue + "[5]" + color.end, "Pediatric Intensive Care Unit (PICU)")
                    channel = int(input("-> "))
                    
                    if channel == 1:
                        room = "Intensive Care Unit (ICU)"
                        print("\nIntensive Care Unit (ICU)")
                        print("Pasien Harus Cepat mendapatkan perawatan")
                        print("Ruangan dilengkapi peralatan canggih")
                        print("Price per day- Rp.350000\n")
                        break
                    elif channel == 2:
                        room = "High Care Unit (HCU)"
                        print("\nHigh Care Unit (HCU)")
                        print("Untuk pasien rawat inap")
                        print("Ruangan dilengkapi peralatan canggih")
                        print("Price per day - Rp.400000\n")
                        break
                    elif channel == 3:
                        room = "Intensive Coronary Care Unit (ICCU)"
                        print("\nIntensive Coronary Care Unit (ICCU)")
                        print("Ruangan untuk penderita penyakit jantung")
                        print("Ruangan kedap suara dan hening")
                        print("Price per day - Rp.450000\n")
                        break
                    elif channel == 4:
                        room = "Neonatal Intensive Care Unit (NICU)"
                        print("\nNeonatal Intensive Care Unit (NICU)")
                        print("Ruangan untuk yang melahirkan")
                        print("Ruangan dilengkapi dengan ruang tunggu orang tua")
                        print("Price- 500000\n")
                        break
                    elif channel == 5:
                        room = "Pediatric Intensive Care Unit (PICU)"
                        print("\nPediatric Intensive Care Unit (PICU)")
                        print("Ruangan untuk bayi dan 18 tahun")
                        print("Ruangan dilengkapi dengan ruang tunggu orang tua")
                        print("Harga kamar perhari- Rp.500000\n")
                        break
                    else:
                        print("\nTOLONG MASUKKAN INPUT YANG SESUAI DENGAN KETENTUAN\n")
                
                while True:
                    tgl_masuk = input("Waktu masuk(dd/mm/yyyy)\t: ")
                    if not tgl_masuk:
                        print("TIDAK BOLEH KOSONG!!!")
                    else:
                        pass
                    tgl_keluar = input("Waktu keluar(dd/mm/yyyy): ")
                    if not tgl_keluar:
                        print("TIDAK BOLEH KOSONG!!!")
                    else:
                        break

                status = "Dirawat\nBelum Dibayar\n"
                no_id = getNo_id(channel)
                pasien = [no_id, nama, gender, umur, alamat, no_phone, penyakit, status, room, tgl_masuk, tgl_keluar]
                list_pasien.append(pasien)
                list_id.append(no_id)
                print(f"\nAnda sudah terdaftar sebagai pasien rumah sakit dengan ID {no_id}")
                break

            elif check == "n":
                status = "Tidak Dirawat\nBelum Dibayar\n" 
                no_id = getNo_id(0)
                pasien = [no_id, nama, gender, umur, alamat, no_phone, penyakit, status, None, None, None]
                list_pasien.append(pasien)
                list_id.append(no_id)
                print(f"\nAnda sudah terdaftar sebagai pasien rumah sakit dengan ID {no_id}")
                break

            else:
                ValueError

        except ValueError:
            print("TOLONG MASUKKAN INPUT YANG SESUAI DENGAN KETENTUAN")
    
    back = input("PRESS ENTER KEY TO RETURN TO THE MAIN MENU")
    if not back:
        menu()

def Info():                     #FUNGSI TAMPILAN INFO KAMAR DI RUMAH SAKIT LIMUS PRATAMA
    print("\t\t\t\t" + color.bold + color.green + ">>LIMUS PRATAMA HOSPITAL<<" + color.end)
    print("\t\t\t\t" + color.bold + color.green + ">>\tROOMS INFO\t<<" + color.end)
    print(f"""
    {color.bold + color.yellow + "Intensive Care Unit (ICU)" + color.end}
---------------------------------------------------------------------------------------------
ICU adalah ruangan khusus yang disediakan rumah sakit untuk merawat pasien dengan keadaan 
yang membutuhkan pengawasan ketat.

    {color.bold + color.yellow + "High Care Unit (HCU)" + color.end}
---------------------------------------------------------------------------------------------
HCU adalah pelayanan yang dikendalikan ke ruangan rawat inap ruangan ini di peruntukkan kepada
pasien dengan kondisi yang sudah membaik namun masih memerlukan pengawasan ketat oleh tenaga 
medis.

    {color.bold + color.yellow + "Intensive Coronary Care Unit (ICCU)" + color.end}
---------------------------------------------------------------------------------------------
Ruangan yang melayani perawatan pasien kritis dewasa yang mengalami gangguan pada jantung.
    
    {color.bold + color.yellow + "Neonatal Intensive Care Unit (NICU)" + color.end}
---------------------------------------------------------------------------------------------
Ruangan ini digunakan untuk bayi baru lahir yang memerlukan perawatan khusus misalnya berat 
badan rendah, fungsi pernafasan kurang sempurna, prematur, mengalami kesulitan dalam 
persalinan, menunjukkan tanda tanda mengkuatirkan dalam beberapa hari pertama kehidupan

    {color.bold + color.yellow + "Pediatric Intensive Care Unit (PICU)" + color.end}
---------------------------------------------------------------------------------------------
Perawatan khusus ruang intensive pediatrik dengan batasan usia umur 28 hari dan anak-anak 
sampai umur 18 tahun yang memerlukan perawatan intensif dengan harapan hidup dan pengobatan 
serta perawatan khusus, guna mencegah dan mengobati terjadinya kegagalan organ-organ vital,
dan bisa sewaktu-waktu meninggal\n""")
    
    if not input("PRESS ENTER KEY TO RETURN TO THE MAIN MENU"):
        menu()

def Apotek ():                  #FUNGSI APOTEK LIMUS PRATAMA
    harga = (40,75,85,45,30,170,80,150,90,170,110,110,110,110,110,110,110,120,120,140,
            140,140,140,140,140,140,150,170,150,140,130,120,90,90,110,110,130,143,130,130,
            130,140,60,60,60,60)
    print("------------------------------------------------------------------------------")
    print(color.bold + color.green + "\t\t\t\tGENERAL PHARMACY" + color.end)
    print("------------------------------------------------------------------------------")
    print(color.bold + color.yellow + "\t\t\t\tLIST OF MEDICINE" + color.end)
    print("------------------------------------------------------------------------------")
    print("\n Obat Batuk/pilek/demam                26) minyak kayu putih 50ml...... 14000")
    print("-----------------------------------    27) minyak kayu putih 100ml..... 15000")
    print(" 1) Paracetamol............... 4000    28) minak kayu putih 120ml...... 17000")
    print(" 2) Panadol................... 7500")
    print(" 3) Entrostop................. 8500      Alkohol")
    print(" 4) Neozep.................... 4500     --------------------------------------")
    print(" 5) Sanmol.................... 3000     29) Alkohol 100%............ 15000")
    print(" 6) Laserin.................. 17000     30) Alkohol 70%............. 14000")
    print(" 7) Napacin................... 8000     31) Alkohol 50%............. 13000")
    print(" 8) Woods.................... 15000     32) Alkohol 30%............. 12000")
    print(" 9) OBH Anak.................. 9000")
    print(" 10) OBH Batuk............... 17000      P3k")
    print("                                        --------------------------------------")
    print(" Obat salep                                33) Handsplast........... 9000")
    print("----------------------------------------   34) Betadin.............. 9000")
    print(" 11) Gentamicin................... 11000   35) Perban.............. 11000")
    print(" 12) Hydrocortison................ 11000   36) Revanol............. 11000")
    print(" 13) Bacitracin................... 11000")
    print(" 14) Neosporin.................... 11000    Obat Infus")
    print(" 15) Clotrimazole................. 11000   -----------------------------------")
    print("                                           37) Cairan saline....... 13000")
    print(" Minyak                                    38) Ringer laktat....... 14300")
    print("---------------------------------------    39) Dextrose............ 13000")
    print(" 16) Fresh Care.................. 11000    40) Gelatin............. 13000")
    print(" 17) Safe care................... 11000    41) Cairan NaCl......... 13000")
    print(" 18) Minyak kapak 10ml........... 12000    42) Dekstran............ 14000")
    print(" 19) Minyak kapak 20ml........... 12000")
    print(" 20) Minyak kapak 30ml........... 14000     Vitamin pill")
    print(" 21) Minyak tawon cc............. 14000    -----------------------------------")
    print(" 22) Minyak tawon dd............. 14000    43) Laxing.......... 6000")
    print(" 23) Minyak tawon EE............. 14000    44) Vitamin C....... 6000")
    print(" 24) Minyak telon 3 anak 60ml.... 14000    45) Inzana.......... 6000")
    print(" 25) Minyak telon 3 anak 100ml... 14000    46) Hemaviton....... 6000")
    print("------------------------------------------------------------------------------")
    print("Press Enter Key to Return to The Main Menu")
    list_obat = list(map(int, input("List obat yang mau dibeli (ex: 1 2 3 4 5): ").strip().split()))
    if not list_obat:
        menu()
    else:
        pass
    price = 0
    for _ in list_obat:
        price += harga[_-1]
    total_obat = price * 100
    while True:
        try:
            print(f"Total harga obat yang perlu dibayar adalah Rp. {total_obat}\n")
            print(f"""{color.bold + color.green + "Methods Payment" + color.end}
-----------------------
{color.bold + color.blue + "[1]" + color.end} Debit
{color.bold + color.blue + "[2]" + color.end} Cash
""")
            methods = int(input("Masukkan metode pembayaran: "))
            if methods == 1:
                print("Anda memilih metode pembayaran dengan Debit")
                progress()
                print(f"Pembayaran berhasil dilakukan sebesar Rp. {total_obat}")
                back = input("PRESS ENTER KEY TO RETURN TO THE MAIN MENU")
                if not back:
                    menu()
                break
            elif methods == 2:
                print("Anda memilih metode pembayaran dengan Cash")
                while True:
                    try:
                        uang = int(input(f"Masukkan uang tunai untuk membayar tagihan sebesar Rp. {total_obat}: "))
                        if uang - total_obat == 0:
                            print("Transaksi berhasil dilakukan, Terimakasih atas pembeliannya semoga anda lekas sembuh")
                            back = input("PRESS ENTER KEY TO RETURN TO THE MAIN MENU")
                            if not back:
                                menu()
                            break
                        elif uang - total_obat < 0:
                            print(f"Uang yang anda berikan kurang, tolong masukkan uang sebesar Rp. {abs(uang - total_obat)} untuk menyelesaikan transaksi")
                            lengkapi = int(input("Masukkan uang tunai untuk melengkapi tagihan yang masih kurang: "))
                            if lengkapi - (abs(uang - total_obat))  == 0:
                                print("Transaksi selesai, terimakasih atas pembeliannya semoga anda lekas sembuh")
                                back = input("PRESS ENTER KEY TO RETURN TO THE MAIN MENU")
                                if not back:
                                    menu()
                            elif lengkapi - (abs(uang - total_obat)) > 0:
                                print(f"Uang yang berikan kelebihan, kembalian yang anda terima sebesar Rp. {lengkapi - (abs(uang - total_obat))}")
                                back = input("PRESS ENTER KEY TO RETURN TO THE MAIN MENU")
                                if not back:
                                    menu()
                            elif lengkapi - (abs(uang - total_obat)) < 0:
                                print("Nampaknya anda tidak memiliki uang yang cukup, transaksi gagal")
                                back = input("PRESS ENTER KEY TO RETURN TO THE MAIN MENU")
                                if not back:
                                    menu()
                            break
                        elif uang - total_obat > 0:
                            print(f"Uang yang berikan kelebihan, kembalian yang anda terima sebesar Rp. {uang - total_obat}")
                            back = input("PRESS ENTER KEY TO RETURN TO THE MAIN MENU")
                            if not back:
                                menu()
                            break
                        else:
                            ValueError
                    except ValueError:
                        print("TOLONG MASUKKAN INPUT YANG SESUAI DENGAN KETENTUAN (HANYA ANGKA TANPA 'Rp' atau 'Rupiah')")
                break
            else:
                ValueError
        except ValueError:
            print("TOLONG INPUT MENU SESUAI KETENTUAN")

def Payment(no_id):             #FUNGSI PEMBAYARAN KAMAR PASIEN SESUAI DENGAN ID KAMAR MASING-MASING
    if no_id not in list_id:
        print("NOMOR ID TIDAK DITEMUKAN, SILAHKAN MELAKUKAN PENDAFTARAN MELALUI MENU INSERT DATA PATIENT")
        back = input("PRESS ENTER KEY TO RETURN TO THE MAIN MENU")
        if not back:
            menu()
    else:
        ruangan = list_pasien[list_id.index(no_id)][8]
        if ruangan == None:
            harga = 100000  #biaya konsultasi
        else:
            tgl_masuk = list(map(int,(list_pasien[list_id.index(no_id)][9].strip().split("/"))))
            tgl_keluar = list(map(int,(list_pasien[list_id.index(no_id)][10].strip().split("/"))))
            check_in = datetime.datetime(tgl_masuk[2],tgl_masuk[1],tgl_masuk[0])
            check_out = datetime.datetime(tgl_keluar[2],tgl_keluar[1],tgl_keluar[0])

            waktu = int(str(check_out - check_in).split()[0])

            if ruangan == "Intensive Care Unit (ICU)":
                harga = waktu * 350000
            elif ruangan == "High Care Unit (HCU)":
                harga = waktu * 400000
            elif ruangan == "Intensive Coronary Care Unit (ICCU)":
                harga = waktu * 450000
            elif ruangan == "Neonatal Intensive Care Unit (NICU)":
                harga = waktu * 500000
            elif ruangan == "Pediatric Intensive Care Unit (PICU)":
                harga = waktu * 550000

        while True:
            try:
                print(f"Total biaya rumah sakit yang perlu anda bayar adalah Rp. {harga}\n")
                print(f"""{color.bold + color.green + "Methods Payment" + color.end}
-----------------------
{color.bold + color.blue + "[1]" + color.end} Debit
{color.bold + color.blue + "[2]" + color.end} Cash
{color.bold + color.blue + "[3]" + color.end} BPJS
""")
                methods = int(input("Masukkan metode pembayaran: "))
                if methods == 1:
                    print("Anda memilih metode pembayaran dengan debit")
                    progress ()
                    print(f"Transaksi sebesar Rp. {harga} berhasil dilakukan, terimakasih dan semoga anda lekas sembuh dan sehat selalu")
                    if (list_pasien[list_id.index(no_id)][1])[:3] == "000":
                        list_pasien[list_id.index(no_id)][7] = "Tidak Dirawat\nSudah Dibayar"
                    else:
                        list_pasien[list_id.index(no_id)][7] = "Dirawat\nSudah Dibayar"      
                    back = input("PRESS ENTER KEY TO RETURN TO THE MAIN MENU")
                    if not back:
                        menu() 
                    break   

                elif methods == 2:
                    print("Anda memilih metode pembayaran dengan Cash")
                    while True:
                        try:
                            uang = int(input(f"Masukkan uang tunai untuk membayar tagihan sebesar Rp. {harga}: "))
                            if uang - harga == 0:
                                print("Transaksi berhasil dilakukan, terimakasih dan semoga anda lekas sembuh dan sehat selalu")
                                if (list_pasien[list_id.index(no_id)][1])[:3] == "000":
                                    list_pasien[list_id.index(no_id)][7] = "Tidak Dirawat\nSudah Dibayar"
                                else:
                                    list_pasien[list_id.index(no_id)][7] = "Dirawat\nSudah Dibayar"
                                back = input("PRESS ENTER KEY TO RETURN TO THE MAIN MENU")
                                if not back:
                                    menu()
                                break
                            elif uang - harga < 0:
                                print(f"Uang yang anda berikan kurang, tolong masukkan uang sebesar Rp. {abs(uang - harga)} untuk menyelesaikan transaksi")
                                lengkapi = int(input("Masukkan uang tunai untuk melengkapi tagihan yang masih kurang: "))
                                if lengkapi - (abs(uang - harga))  == 0:
                                    print("Transaksi selesai, terimakasih dan semoga anda lekas sembuh dan sehat selalu")
                                    if (list_pasien[list_id.index(no_id)][1])[:3] == "000":
                                        list_pasien[list_id.index(no_id)][7] = "Tidak Dirawat\nSudah Dibayar"
                                    else:
                                        list_pasien[list_id.index(no_id)][7] = "Dirawat\nSudah Dibayar"
                                    back = input("PRESS ENTER KEY TO RETURN TO THE MAIN MENU")
                                    if not back:
                                        menu()
                                elif lengkapi - (abs(uang - harga)) > 0:
                                    print(f"Uang yang berikan kelebihan, kembalian yang anda terima sebesar Rp. {lengkapi - (abs(uang - harga))}")
                                    print("Transaksi selesai, terimakasih dan semoga anda lekas sembuh dan sehat selalu")
                                    if (list_pasien[list_id.index(no_id)][1])[:3] == "000":
                                        list_pasien[list_id.index(no_id)][7] = "Tidak Dirawat\nSudah Dibayar"
                                    else:
                                        list_pasien[list_id.index(no_id)][7] = "Dirawat\nSudah Dibayar"
                                    back = input("PRESS ENTER KEY TO RETURN TO THE MAIN MENU")
                                    if not back:
                                        menu()
                                elif lengkapi - (abs(uang - harga)) < 0:
                                    print("Nampaknya anda tidak memiliki uang yang cukup, transaksi gagal")
                                    back = input("PRESS ENTER KEY TO RETURN TO THE MAIN MENU")
                                    if not back:
                                        menu()
                                break
                            elif uang - harga > 0:
                                print(f"Uang yang berikan kelebihan, kembalian yang anda terima sebesar Rp. {uang - harga}")
                                print("Transaksi selesai, terimakasih dan semoga anda lekas sembuh dan sehat selalu")
                                if (list_pasien[list_id.index(no_id)][1])[:3] == "000":
                                    list_pasien[list_id.index(no_id)][7] = "Tidak Dirawat\nSudah Dibayar"
                                else:
                                    list_pasien[list_id.index(no_id)][7] = "Dirawat\nSudah Dibayar"
                                back = input("PRESS ENTER KEY TO RETURN TO THE MAIN MENU")
                                if not back:
                                    menu()
                                break
                            else:
                                ValueError
                        except ValueError:
                            print("TOLONG MASUKKAN INPUT YANG SESUAI DENGAN KETENTUAN (HANYA ANGKA TANPA 'Rp' atau 'Rupiah')")
                    break
                elif methods == 3:
                    bpjs = int(input("Masukkan No-BPJS: "))
                    if len(str(bpjs)) == 13:
                        progress()
                        print(f"Transaksi sebesar Rp. {harga} telah berhasil dilakukan melalui claim BPJS dengan No. {bpjs}")
                        print("Transaksi selesai, terimakasih dan semoga anda lekas sembuh dan sehat selalu")
                        if (list_pasien[list_id.index(no_id)][1])[:3] == "000":
                            list_pasien[list_id.index(no_id)][7] = "Tidak Dirawat\nSudah Dibayar"
                        else:
                            list_pasien[list_id.index(no_id)][7] = "Dirawat\nSudah Dibayar"
                        back = input("PRESS ENTER KEY TO RETURN TO THE MAIN MENU")
                        if not back:
                            menu()
                    else:
                        print("NO BPJS TIDAK DITEMUKAN")
                        back = input("PRESS ENTER KEY TO RETURN TO THE MAIN MENU")
                        if not back:
                            menu()  
                    break
                else:
                    ValueError
            except ValueError:
                print("TOLONG INPUT MENU SESUAI KETENTUAN")

def record_patient (no_id):     #FUNGSI TAMPILAN DATA PASIEN SESUAI ID YANG DIINPUT
    if no_id in list_id:
        PTables = PrettyTable()
        PTables.field_names = ["No-ID", "Nama", "Gender", "Umur", "Alamat", "No-Phone", "Penyakit", 
                                "Status", "Ruangan", "Tgl Masuk", "Tgl Keluar"]
        PTables.add_row(list_pasien[list_id.index(no_id)])
        print(PTables)
        back = input("PRESS ENTER KEY TO RETURN TO THE MAIN MENU")
        if not back:
            menu()
    else:
        print("ID TIDAK DITEMUKAN")
        back = input("PRESS ENTER KEY TO RETURN TO THE MAIN MENU")
        if not back:
            menu()

def record_allpatient ():       #FUNGSI TAMPILAN SEMUA DATA PASIEN RUMAH SAKIT LIMUS PRATAMA
    if not list_id:
        print("BELUM ADA DATA PASIEN YANG DIMASUKKAN")
        back = input("PRESS ENTER KEY TO RETURN TO THE MAIN MENU")
        if not back:
            menu()
    else:
        PTables = PrettyTable()
        PTables.field_names = ["No-ID", "Nama", "Gender", "Umur", "Alamat", "No-Phone", "Penyakit",
                                 "Status", "Ruangan", "Tgl Masuk", "Tgl Keluar"]
        
        for i in range(len(list_id)):
            PTables.add_row(list_pasien[i])
        
        print(PTables)
        back = input("PRESS ENTER KEY TO RETURN TO THE MAIN MENU")
        if not back:
            menu()

def datafile():                  #FUNGSI INPUT DATA INTU CSV FILE
    if not list_id:
        print("TIDAK ADA DATA PASIEN YANG BISA DIINPUT KE DALAM FILE .txt")
        back = input("PRESS ENTER KEY TO RETURN TO THE MAIN MENU")
        if not back:
            menu()
    else:
        pass
    namafile = input("Inputkan nama file (format : NAMAFILE.txt) : ")
    PTables = PrettyTable()
    PTables.field_names = ["No-ID", "Nama", "Gender", "Umur", "Alamat", "No-Phone", "Penyakit",
                                 "Status", "Ruangan", "Tgl Masuk", "Tgl Keluar"]
    
    for i in range(len(list_id)):
        PTables.add_row(list_pasien[i])

    with open(namafile, "w") as file:
        file.write(f"Data Pasien Pada {datetime.datetime.now()}\n")
        file.write(str(PTables))
    
    print("Data Berhasil Diinput")
    back = input("PRESS ENTER KEY TO RETURN TO THE MAIN MENU")
    if not back:
        menu()

def menu ():                    #TAMPILAN MENU UTAMA PROGRAM ADMINISTRASI RUMAH SAKIT
    system ("cls")
    while True:
        try:
            print("")
            print(color.bold + color.green + ">>LIMUS PRATAMA HOSPITAL MENU<<" + color.end)
            print(f"""
{color.bold + color.blue + "[1]" + color.end} Insert Data Patient
{color.bold + color.blue + "[2]" + color.end} Rooms Info
{color.bold + color.blue + "[3]" + color.end} Apotek
{color.bold + color.blue + "[4]" + color.end} Payment
{color.bold + color.blue + "[5]" + color.end} Record of Patient
{color.bold + color.blue + "[6]" + color.end} Record of All Patient
{color.bold + color.blue + "[7]" + color.end} Input Data into TXT File
{color.bold + color.blue + "[0]" + color.end} Exit Program

Select Menu (ex: 1)""")
            menu = int(input("==> "))
            if menu == 1:
                system("cls")
                print("")
                Insert()
            elif menu == 2:
                system("cls")
                print("")
                Info()
            elif menu == 3:
                system("cls")
                print("")
                Apotek()
            elif menu == 4:
                system("cls")
                print("")
                no_id = input("Masukkan No-ID Pasien: ")
                Payment(no_id)
            elif menu == 5:
                system("cls")
                print("")
                no_id = input("Masukkan No-ID Pasien: ")
                record_patient(no_id)
            elif menu == 6:
                system("cls")
                record_allpatient()
                print("")
            elif menu == 7:
                system("cls")
                datafile()
                print("")
            elif menu == 0:
                system("cls")
                print(color.cyan + color.bold + "TERIMA KASIH SUDAH MENGGUNAKAN PROGRAM KAMI\nSEMOGA ANDA SEHAT SELALU" + color.end)
                sys.exit()
            else:
                ValueError
        except ValueError:
            print("TOLONG MASUKKAN INPUT SESUAI DENGAN KETENTUAN")

system("cls")
loading()
menu()