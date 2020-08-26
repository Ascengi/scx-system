import time
#bebas recode
import os,sys

#silahkan ubah nilai variabel sesuai nama dan umur anda tetapi jangan ubah nama variabelnya
#di perbolehkan mengubah dan menambah script ini
nama = "Ascen'gi"
umur = 12
s = "scx: "

def restart():
    ngulang = sys.executable
    os.execl(ngulang, ngulang, *sys.argv)

i=input("perintah: ")
if("hallo" in i):
    print(s,"hai")

elif("halo" in i):
    print(s,"hai")

elif("hai" in i):
    print(s,"hallo")

elif("siapa namamu" in i):
    print(s,"scx system"):

elif("siapa aku" in i):
    print(s,"kamu adalah",nama,"umur kamu",umur)

elif("siapa namaku" in i):
    print(s,"nama anda adalah",nama)

elif("siapa nama aku" in i):
    print(s,"nama anda adalah",nama)

elif("siapa nama saya" in i):
    print(s,"nama anda adalah",nama)

elif("siapa nama anda" in i):
    print(s,"nama saya adalah scx system")

elif("siapa pembuatmu" in i):
    print(s,"pembuat saya adalah Ascen'gi ")

elif("exit" in i):
    os.system('exit')

elif("keluar" in i):
    os.system('exit')

elif("ulangi" in i):
    os.system('clear')

elif("film anak sange" in i):
    print("film anak sange di indonesia yang paling terkenal adalah Dari jendela SMP")

else:
    print("error: maaf saya tidak paham")

time.sleep(2)
restart()