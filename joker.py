import os
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

os.system("title joker@guest")

os.system("cls")

print(f"""
{Fore.RED}                          _____                          
{Fore.MAGENTA}                   _.+sd$$$$$$$$$bs+._                   
{Fore.RED}               .+d$$$$$$$$$$$$$$$$$$$$$b+.               
{Fore.MAGENTA}            .sd$$$$$$$P^*^T$$$P^*"*^T$$$$$bs.            
{Fore.RED}          .s$$$$$$$$P*     `*' _._  `T$$$$$$$s.          
{Fore.MAGENTA}        .s$$$$$$$$$P          ` :$;   T$$$$$$$$s.        
{Fore.RED}       s$$$$$$$$$$;  db..+s.   `**'    T$$$$$$$$$s       
{Fore.MAGENTA}     .$$$$$$$$$$$$'  `T$P*'             T$$$$$$$$$$.     
{Fore.RED}    .$$$$$$$$$$$$P                       T$$$$$$$$$$.    
{Fore.MAGENTA}   .$$$$$$$$$$$$$b                       `$$$$$$$$$$$.   
{Fore.RED}  :$$$$$$$$$$$$$$$.                       T$$$$$$$$$$$;  
{Fore.MAGENTA}  $$$$$$$$$P^*' :$$b.                     d$$$$$$$$$$$$  
{Fore.RED} :$$$$$$$P'      T$$$$bs._               :P'`*^T$$$$$$$; 
{Fore.MAGENTA} $$$$$$$P         `*T$$$$$b              '      `T$$$$$$ 
{Fore.RED}:$$$$$$$b            `*T$$$s                      :$$$$$;
{Fore.MAGENTA}:$$$$$$$$b.                                        $$$$$;  .GG/schuhack
{Fore.RED}$$$$$$$$$$$b.                                     :$$$$$$
{Fore.MAGENTA}$$$$$$$$$$$$$bs.                                 .$$$$$$$
{Fore.RED}$$$$$$$$$$$$$$$$$bs.                           .d$$$$$$$$
{Fore.MAGENTA}:$$$$$$$$$$$$$P*"*T$$bs,._                  .sd$$$$$$$$$;
{Fore.RED}:$$$$$$$$$$$$P     TP^**T$bss++.._____..++sd$$$$$$$$$$$$;
{Fore.MAGENTA} $$$$$$$$$$$$b           `T$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ 
{Fore.RED} :$$$$$$$$$$$$b.           `*T$$P^*"*"*^^*T$$$$$$$$$$$$; 
{Fore.MAGENTA}  $$$b       `T$b+                        :$$$$$$$BUG$$  
{Fore.RED}  :$P'         `"'               ,._.     ;$$$$$$$$$$$;  
{Fore.MAGENTA}   \                            `*TP*     d$$P*******$   
{Fore.RED}    \                                    :$$P'      /    
{Fore.MAGENTA}     \                                  :dP'       /     
{Fore.RED}      `.                               d$P       .'      
{Fore.MAGENTA}        `.                             `'      .'        
{Fore.RED}          `-.                               .-'          
{Fore.MAGENTA}             `-.                         .-'             
{Fore.RED}                `*+-._             _.-+*'                
{Fore.MAGENTA}                      `"*-------*"'
{Fore.RED}                  type $ start port scan to START""")


print(f"""
{Fore.MAGENTA}╔═[{Fore.RED}Guest@Joker{Fore.MAGENTA}]
╚════>""", end='')
command111 = launch = input()

if command111 == '$ start port scan':
    os.system("color a")
    #$ start port scan
    os.system("netstat -a")
    print(f"""
    {Fore.MAGENTA}╔═[{Fore.RED}DONE{Fore.MAGENTA}]
    ╚════>""", end='')
    launch = input()
else:
    print(f"""
    {Fore.MAGENTA}╔═[{Fore.RED}WRONG COMMAND{Fore.MAGENTA}]
    ╚════>""", end='')
    launch = input()
