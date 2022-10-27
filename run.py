import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3,rich,base64
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import print as rprint
from rich.text import Text as tekz
#-------------------------------------#
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,h,u,b])
#-----------------------------------#
def clear():
    os.system('clear')
#----------------------------------#
def boki(s):
    for c in s + '':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.random() * 0.005)
#----------------------------------#
def wijaya(s):
    for c in s + '':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.random() * 0.2)
#----------------------------------#
def logo():
    boki(f"""{x}
{u}   ______                __   _                                  
{u}  / ____/________ ______/ /__(_)___  ____ _  
 {p}/ /   / ___/ __ `/ ___/ //_/ / __ \/ __ `/ {x}=== Kiki Wijaya
{u}/ /___/ /  / /_/ / /__/ ,< / / / / / /_/ /  {x}=== {M}INDONESIA
{p}\____/_/   \__,_/\___/_/|_/_/_/_/_/\__, /   {x}=== {p}2022
          {u}/  _/___  _____/ /__ ____ ___/ __________ _____ ___ 
          {p}/ // __ \/ ___/ __/ __ `/ __ `/ ___/ __ `/ __ `__ \ 
    {u}    _/ // / / (__  ) /_/ /_/ / /_/ / /  / /_/ / / / / / /
       {p}/___/_/ /_/____/\__/\__,_/\__, /_/   \__,_/_/ /_/ /_/ 
                                /____/ 
{x}           +======================================+
           |{H}-{x} Creator   :  Kiki Wijaya            |
           |{H}-{x} Whatsapp  :  083192495253           |
           |{H}-{x} Contack   :  kikimskj935@gmail.com  |
           |{H}-{x} MyInsta   :  bokiofficial88         |
           +======================================+\n""")
#--------------------------------------------------#
def notprem():
    clear()
    cetak(nel('[red]You Not Premium!!!!'))
    time.sleep(2)
    kiki()
#-------------------------------------------------#
def kiki():
    clear()
    logo()
    cetak(nel('[[green]01[white]] Lihat List Harga Tools\n[[green]02[white]] Informasi Tools'))
    
    anu = input(f'{u}[{h}+{u}]{x} Pilih : ')
    
    if anu in ['1','01']:
        pilat()
    elif anu in ['2','02']:
        cetak(nel('\tNOTE'))
        wijaya(f'{u}[{h}+{u}]{x}Tools Ini Dibuat Untuk Crack Instagram Atau Hack Account Secara Random\n\t{m}This is a Legal Program!!!{x}\n{u}[{h}+{u}]{x}Jadi Anda Mau Berbuat Jahat Atau Kebaikan Itu Resiko Anda')
        print('\n')
        cetak(nel('[green]Press Enter To Continue.......'))
        input(' ')
        time.sleep(2)
        kiki()
#-----------------------------#
def pilat():
    clear()
    boki("""
My Instagram  :  
\t _           _    _        __  __ _      _       _  ___   ___  
\t| |__   ___ | | _(_) ___  / _|/ _(_) ___(_) __ _| |( _ ) ( _ ) 
\t| '_ \ / _ \| |/ / |/ _ \| |_| |_| |/ __| |/ _` | |/ _ \ / _ \ 
\t| |_) | (_) |   <| | (_) |  _|  _| | (__| | (_| | | (_) | (_) |
\t|_.__/ \___/|_|\_\_|\___/|_| |_| |_|\___|_|\__,_|_|\___/ \___/ 
                                                               \n""")
    au=' (\x1b[1;92m01\33[m) \033[33mRp.50K\33[m  Tools Permanen\n (\x1b[1;92m02\33[m) \033[33mRp.25K\33[m  Tools Perbulan\n (\x1b[1;92m03\33[m) \033[33mRp.100K\33[m Tools Open Source'
    men=nel(au,style="")
    cetak(nel(men, title='List Harga Tools'))
    wow = input(f'Pilih Harga Tools : ')
    if wow in ['1','01']:
        boki(f'Anda Akan Di Arah Kan Ke {h}WhatsApp{x}')
        time.sleep(2)
        os.system('xdg-open https://wa.me/6283192495253?text=Assalamualaikum+Bang+Kiki+Saya+Ingin+Membeli+Tools+Crack+Instagram+Permanen+Bang')
        exit()
    elif wow in ['2','02']:
        boki(f'Anda Akan Di Arah Kan Ke {h}WhatsApp{x}')
        time.sleep(2)
        os.system('xdg-open https://wa.me/6283192495253?text=Assalamualaikum+Bang+Kiki+Saya+Ingin+Membeli+Tools+Crack+Instagram+Perminggu+Bang')
        exit()
    elif wow in ['3','03']:
        boki(f'Anda Akan Di Arah Kan Ke {h}WhatsApp{x}')
        time.sleep(2)
        os.system('xdg-open https://wa.me/6283192495253?text=Assalamualaikum+Bang+Kiki+Saya+Ingin+Membeli+Tools+Crack+Instagram+Open+Source+Bang')
        exit()
    elif wow in ['']:
        boki(f'Jangan Kosong Bang{m}!!!')
        kiki()
#----------------------------------------------------------------------#
if __name__=='__main__':
    notprem()
