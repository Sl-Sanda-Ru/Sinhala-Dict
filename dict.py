from time import sleep
from os import system,get_terminal_size,name
system('git stash && git pull')
clear = 'clear' if name == 'posix' else 'cls'
try:
	from colorama import init,Fore
	from bs4 import BeautifulSoup as bsp
	from pyfiglet import Figlet
	from requests import get
except ModuleNotFoundError:
	system('pip3 install requests bs4 colorama lolcat pyfiglet')
from random import choice
#Colors
blu=Fore.BLUE
cya=Fore.CYAN
gre=Fore.GREEN
yel=Fore.YELLOW
red=Fore.RED
mag=Fore.MAGENTA
liyel=Fore.LIGHTYELLOW_EX
lired=Fore.LIGHTRED_EX
limag=Fore.LIGHTMAGENTA_EX
liblu=Fore.LIGHTBLUE_EX
licya=Fore.LIGHTCYAN_EX
ligre=Fore.LIGHTGREEN_EX
rst=Fore.RESET
bold='\x1b[1m'
fore=list((blu,cya,gre,yel,red,mag,liyel,lired,limag,liblu,licya,ligre))
tsize = get_terminal_size().columns
init(autoreset=True)
def req_soup(search):
	html = get('https://www.maduraonline.com',params={'find':search}).text
	global soup
	soup = bsp(html,'html.parser')
def is_res():
	if soup.find('p',class_='pt'):
		for i in soup.find_all('td',class_='td'):
			words.append(i.text)
		return False
	else:
		return True
def res_scrape():
	for i in soup.find_all('td',class_='td'):
		if i.text.strip():
			words.append(i.text.strip())
def logo():
	system('clear')
	col = choice(fore)
	print(bold+col+'_'*tsize)
	h = 'Sinhala Dict'
	ex = system(f'pyfiglet -f ogre -j center -w {tsize} {h} | lolcat -F 0.3 -a -d 2')
	msg = '[+] By Sandaru Ashen'
	nu = int(tsize/2)
	nu -= int(len(msg)/2)
	print(bold+col+'_'*nu+liyel+msg+col+'_'*nu+'\n')
	sleep(1.3)
def main():
	global words
	words = []
	try:
		logo()
		search = input(bold+choice(fore)+'[+] Enter The Word: ')
		req_soup(search)
		if is_res():
			res_scrape()
			print(choice(fore)+bold+' [+] Results For Your Search: ')
			for i in enumerate((words),start=1):
				print(bold+choice(fore)+'\t'+str(i[0])+'.'+i[1])
		else:
			print(bold+lired+'[!] No Results')
			sleep(0.9)
			print(bold+ligre+'   [?] Do You Mean')
			for i in enumerate((words),start=1):
				print(bold+choice(fore)+'\t'+str(i[0])+'.'+i[1])
			while True:
				try:
					num = int(input(bold+liyel+'  [+] Enter Number: '))
					if num > len(words) or num <= 0:
						print(bold+lired+'   [!] Entered Number Not In Range')
					else:
						break
				except ValueError:
					print(bold+lired+'   [!] Wrong Input')
			req_soup(words[num-1])
			words.clear()
			res_scrape()
			print(choice(fore)+bold+' [+] Results For Your Search: ')
			for i in enumerate((words),start=1):
				print(bold+choice(fore)+'\t'+str(i[0])+'.'+i[1])
		sleep(1.1)
		if input(bold+choice(fore)+'[+] Press Enter To Exit Or Any Other Key To Goto Main Menu'):
			main()
		else:
			exit()
	except KeyboardInterrupt:
		exit()
if __name__ == '__main__':
	main()
