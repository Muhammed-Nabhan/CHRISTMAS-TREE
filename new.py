import colorama
from colorama import Fore,Back,Style
colorama.init(autoreset=True)

height=16
wood=height//3
floor=1
k=1

print(Fore.RED+'###===***THE CHRISTMAS TREE***===###') 

for i in range(height):
    print((' ' * (height - i)) + ( Fore.GREEN+'*' * ((2 * i) + 1)))
  
for i in range(wood):
     print(('  '*((height-1)//2))+(Fore.MAGENTA+'#' * wood) )
for i in range(floor):
    for j in range(k):
       print(Fore.GREEN+'v '*18)
       print(Fore.YELLOW+'@@'*18)
       print(Fore.GREEN+'o0'*18)
    
    
###===***THE CHRISTMAS TREE***===###
                *
               ***
              *****
             *******
            *********
           ***********
          *************
         ***************
        *****************
       *******************
      *********************
     ***********************
    *************************
   ***************************
  *****************************
 *******************************
              #####
              #####
              #####
              #####
              #####
v v v v v v v v v v v v v v v v v v 
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
o0o0o0o0o0o0o0o0o0o0o0o0o0o0o0o0o0o0
