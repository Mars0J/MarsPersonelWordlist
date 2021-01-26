#!/usr/bin/env python
# -*- coding: utf-8 -*- 
from past.builtins import xrange
#Mars #hack

import sys
import itertools
import os
import time

print ("""\033[1;36m
███╗   ███╗ █████╗ ██████╗ ███████╗    
████╗ ████║██╔══██╗██╔══██╗██╔════╝    
██╔████╔██║███████║██████╔╝███████╗    
██║╚██╔╝██║██╔══██║██╔══██╗╚════██║    
██║ ╚═╝ ██║██║  ██║██║  ██║███████║    
╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝    
                                       
\033[1;35m
██████╗ ███████╗██████╗ ███████╗ ██████╗ ███╗   ██╗███████╗██╗         ██╗    ██╗ ██████╗ ██████╗ ██████╗ ██╗     ██╗███████╗████████╗
██╔══██╗██╔════╝██╔══██╗██╔════╝██╔═══██╗████╗  ██║██╔════╝██║         ██║    ██║██╔═══██╗██╔══██╗██╔══██╗██║     ██║██╔════╝╚══██╔══╝
██████╔╝█████╗  ██████╔╝███████╗██║   ██║██╔██╗ ██║█████╗  ██║         ██║ █╗ ██║██║   ██║██████╔╝██║  ██║██║     ██║███████╗   ██║   
██╔═══╝ ██╔══╝  ██╔══██╗╚════██║██║   ██║██║╚██╗██║██╔══╝  ██║         ██║███╗██║██║   ██║██╔══██╗██║  ██║██║     ██║╚════██║   ██║   
██║     ███████╗██║  ██║███████║╚██████╔╝██║ ╚████║███████╗███████╗    ╚███╔███╔╝╚██████╔╝██║  ██║██████╔╝███████╗██║███████║   ██║   
╚═╝     ╚══════╝╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝╚══════╝     ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚══════╝╚═╝╚══════╝   ╚═╝   
                                                                                                                                      
""")

def slowprint(s):
    for c in s + '\n' :
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(10. / 100)
slowprint("\033[1;33m > Made By Mars <")
time.sleep(1)

isim = input("\033[32m\n Wordlist Oluşturmak istediğiniz kişinin İsmi :  ")
soyad = input("\033[32m Wordlist Oluşturmak istediğiniz kişinin Soyadı : ")
yaş = input("\033[32m Wordlist Oluşturmak istediğniz kişinin Yaşı : ")
hayvan = input("\033[32m Wordlist Oluşturmak istediğiniz kişinin sevdiği hayvan : ")
min_length = int(input("\033[31m Minimum Karakter Uzunluğu : "))
max_length = int(input("\033[31m Maxümum Karakter Uzunluğu : "))
wordlist = input("\033[1;33m Wordlist Dosyasının ismini  Girin : ")
psd = open(wordlist, "w")
timeS=time.asctime()
start=time.time()
for i in xrange(min_length,max_length+1):
  r=100*i/max_length
  l="İlerleme : "+str(r)+' %'

  sys.stdout.write("\r%s"%l+"\033[34m Tamamlandı." )
  sys.stdout.flush()
  psd.flush()
  for xs in itertools.product(isim, soyad, yaş, hayvan, repeat=i):
    psd.write(''.join(xs)+'\n')
end=time.time()
totaltime=end-start
print ("\033[31m\n[-]------------------------[Sonuç]--------------------------[-]")
print ("\033[33mİşlem Başlatıldı :",timeS)
print ("\033[32mİşlem Bitti :",time.asctime())
print ("\033[35mToplam Zaman :",totaltime,"İkinci")
print ("\033[35mŞu isim Olarak Kaydedildi : "+wordlist)
print ("\033[35mLokasyon : "+os.getcwd()+"/"+wordlist)
print ("\033[31m[-]----------------------------------------------------------[-]")
psd.flush()    
psd.close()
