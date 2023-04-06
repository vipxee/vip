#CH @VIPJL BY @VV00JJ
import os,sys,subprocess
import requests,time,random,os,sys
subprocess.getoutput("pip install requests")
import requests,sys,os,time
#BY HAMO
def jalan(z):
 for e in z + '\n':
  sys.stdout.write(e)
  sys.stdout.flush()
  time.sleep(00000.05)

logo='''\n\n\n
\t\t░░░░░▄▄▀▀▀▀▀▀▀▀▀▄▄░░░░░
\t\t░░░░█░░░░░░░░░░░░░█░░░░
\t\t░░░█░░░░░░░░░░▄▄▄░░█░░░
\t\t░░░█░░▄▄▄░░▄░░███░░█░░░
\t\t░░░▄█░▄░░░▀▀▀░░░▄░█▄░░░
\t\t░░░█░░▀█▀█▀█▀█▀█▀░░█░░░
\t\t░░░▄██▄▄▀▀▀▀▀▀▀▄▄██▄░░░
\t\t░▄█░█▀▀█▀▀▀█▀▀▀█▀▀█░█▄░'''

jalan(logo)

w = input ("\033[1;35m \n\n[~] ENTER NAME :  \t")

jalan ("\n \033[1;33m Hello "+ w + " welcome to my tool \n and love my friend MO ELSHAFEY , IRON , ASHRAF , ADN HACKER , SNIPER , مرعب , AND LOVE ALL 🔥❤️")
time.sleep(2)
os.system('clear')
while True :
	pas=input("\033[1;37m [~]\033[1;35m ENTER THE PASSWORD :\033[1;33m")
	if pas == "1" or pas =="مرعب" or pas=="الغلابه":
		print ('\n\n\033[1;32mHello '+ w +' welcome to my tool')
		break
	else:
			print ('\033[1;31m\n\n  WRONG PASWORD '+ w +' PLEASE TRY AGAIN..!')		





time.sleep(2)
os.system("clear")
print("\033[1;36m########################\033[1;31m[\033[1;37m BY HAMO  \033[1;31m]\033[1;36m########################")
print()
print()


TOKEN=input('\033[1;31m TOKEN : ')
ID=input('\033[1;31m ID : ')
os.system('clear')
MM=int(input('\033[1;31m [^]\033[1;36m AMOUNT OF USERS :\033[1;37m'))
os.system('clear')
print("\033[1;36m########################\033[1;31m[\033[1;37m   HAMO   \033[1;31m]\033[1;36m########################")
print()
print("\t\033[1;35m##################################")
print("\t\033[1;35m#\033[1;33m  \t[1] USER NAME        \033[1;35m    #")
print("\t\033[1;35m#\033[1;33m  \t[2] BOT User             \033[1;35m#")
print("\t\033[1;35m##################################\033[1;37m")
print()
ask =input('\t 1 or 2  ? »')
if ask =='1':
	abc3 ='abcdefghijklmnopqrstuvwxyz0123456789'
	abc2 ='abcdefghijklmnopqrstuvwxyz0123456789'
	abc1='abcdefghijklmnopqrstuvwxyz'
	for b in range (MM):
		hamo11 = str(''.join((random.choice(abc1) for i in range(1))))
		hamo22 = str(''.join((random.choice(abc2) for i in range(1))))
		hamo33 = str(''.join((random.choice(abc3) for i in range(1))))
		kk=(hamo11+'_'+hamo22+'_'+hamo33)
		ree = requests.get(f'https://t.me/{kk}').text
		if 'tgme_username_link' in ree:
			Account = requests.post(f'https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={ID}&text=  جبتلك يوزر جديد 📳\n[🔥]متاح او مبند \n──┈┈┈┄╌╌╌┄┄┈┈┈\n UserName :» @{kk}\n Valide :» Telegram   ✅\n──┈┈┈┄╌╌╌┄┄┈┈┈\n 🎉︙By :  \n 🇱🇾︙Ch : @VIPJL ')
			print(f' \033[1;32m AVAILABLE : {kk} \033[1;31m')
		else:
			print(f' \033[1;31m NOT AVAILABLE : {kk}')

if ask =='2':
	abcd3 ='abcdefghijklmnopqrstuvwxyz_0123456789'
	abcd2 ='abcdefghijklmnopqrstuvwxyz_0123456789'
	abcd1='abcdefghijklmnopqrstuvwxyz'
	for b in range (MM):
		hamo111 = str(''.join((random.choice(abcd1) for i in range(1))))
		hamo222 = str(''.join((random.choice(abcd2) for i in range(1))))
		hamo333 = str(''.join((random.choice(abcd3) for i in range(1))))
		h1h=(hamo111+hamo222+hamo333+'bot')
		ree = requests.get(f'https://t.me/{h1h}').text
		if 'tgme_username_link' in ree:
			Account = requests.post(f'https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={ID}&text= ⌯  ʜɪ ѕɪʀ ɴᴇᴡ BOTUser📳\n[✔️]متاح او مبند \n──┈┈┈┄╌╌╌┄┄┈┈┈\nBOTUser :» @{h1h}\n Valide :» Telegram   ✅\n──┈┈┈┄╌╌╌┄┄┈┈┈\n ︙By : @VV00JJ \n 🇱🇾︙Ch : @VIPJL')
			print(f' \033[1;32m AVAILABLE : {h1h} \033[1;31m')
		else:
			print(f' \033[1;31m NOT AVAILABLE : {h1h}')