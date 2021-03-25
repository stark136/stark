import os,time,colorama
from colorama import Fore,Back, Style
colorama.init()
print(Fore.BLUE+'''

███╗   ███╗██╗   ██╗███████╗██╗ ██████╗    ██████╗ ██╗      █████╗ ██╗   ██╗███████╗██████╗ 
████╗ ████║██║   ██║██╔════╝██║██╔════╝    ██╔══██╗██║     ██╔══██╗╚██╗ ██╔╝██╔════╝██╔══██╗
██╔████╔██║██║   ██║███████╗██║██║         ██████╔╝██║     ███████║ ╚████╔╝ █████╗  ██████╔╝
██║╚██╔╝██║██║   ██║╚════██║██║██║         ██╔═══╝ ██║     ██╔══██║  ╚██╔╝  ██╔══╝  ██╔══██╗
██║ ╚═╝ ██║╚██████╔╝███████║██║╚██████╗    ██║     ███████╗██║  ██║   ██║   ███████╗██║  ██║
╚═╝     ╚═╝ ╚═════╝ ╚══════╝╚═╝ ╚═════╝    ╚═╝     ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝''')
                                                                                            
print(Fore.RESET)
print(Fore.YELLOW+          "MADE BY ANSHUMAAN SHARMA @STARK IN INDIA")
print(Fore.RESET)
print(Fore.GREEN)
z=input("ENTER THE PASSWORD TO PROCCED:-")
print(Fore.RESET)
print(Fore.YELLOW)
if 'stark' in z:

  



  filenames=("music.py","music2.py")
  frames=[]
  os.system('clear')

  for name in filenames:
    with open(name,"r",encoding="utf8") as f:
        frames.append(f.readlines())


  a=10
  while a>=10:

   
   
   for frame in frames:
     
    
     print("".join(frame))
     
     time.sleep(0.02)
     
     os.system('clear')

    
