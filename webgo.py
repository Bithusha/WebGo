import os,sys,time
os.system('clear')
os.system('xdg-open https://youtube.com/c/SLPhoneTechnician')
os.system('figlet WebGo')




print('\033[1;31m______________________________________________________')
print("\033[1;31mEnter what are you want to search without spaces")







print("               example:termux+hacking+tools")
print('______________________________________________________')


name = input("Search\n")
os.system('w3m https://www.google.com/search?q=%s'%name)
