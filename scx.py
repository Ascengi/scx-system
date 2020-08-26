#bebas recode
import os,sys

def restart():
    os.system('clear')
    ngulang = sys.executable
    os.execl(ngulang, ngulang, *sys.argv)

#membuat variabel
nama = "Ascen'gi"
umur = 12

#membuat logo
def logo():
    print("|+++++++++++++++++++|")
    print("|                   |")
    print("|                   |")
    print("|   ===      +++    |")
    print("|                   |")
    print("|        ||         |")
    print("|      ------       |")
    print("\     /______\     / ")
    print(" \________________/")

logo()
print("hai saya adalah scx")
inp=input("Anda: ")
#langsung main if else
if("hallo" in inp):
    print("hai")

elif("halo" in inp):
    print("hai")

elif("nama kamu siapa" in inp):
    print("nama saya scx system")

elif("siapa namaku" in inp):
    print("nama kamu adalah",nama,"kamu berumur",umur)

elif("siapa nama saya" in inp):
    print("nama kamu adalah",nama,"umur kamu",umur)

elif("kamu siapa" in inp):
    print("saya adalah scx system")

elif("anjing" in inp):
    print("war boss?")

elif("exit" in inp):
    sys.exit()

elif("keluar" in inp):
    sys.exit()

else:
    print("maaf saya tidak mengerti")

restart()