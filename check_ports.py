import socket
from contextlib import closing
import os
os.system("cls")

RED = "\033[0;31m"
LIGHT_CYAN = "\033[1;36m"

print(LIGHT_CYAN + "Advanced Port Scanner By " + RED + "StrikeXD\n")
ports = [80, 20, 21, 23, 25, 443, 88, 161, 162, 194, 8080, 3389, 53, 22, 50, 56, 57, 107, 115, 118, 465, 445]


LIGHT_GREEN = "\033[1;32m"
YELLOW = "\033[1;33m"

def main():

    print(LIGHT_GREEN + "[1] " + YELLOW + "Check All Ports (Slow)\n" + LIGHT_GREEN + "[2] " + YELLOW + "Check Specific Port (Faster)\n")

    selection = input(LIGHT_GREEN + "[+] " + YELLOW + "Sellect: ")

    if selection == "1":
        print("\n")
        ip = input(LIGHT_GREEN + "[+] " + YELLOW + "Enter The IP: ")
        print("\n" + LIGHT_GREEN + "Pinging " + YELLOW + ip + "\n")

        print(LIGHT_CYAN + "\nScan Resualt: \n")

        try:
            for i in ports:

                with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as sock:
                    
                    if sock.connect_ex((ip, i)) == 0:
                        service = socket.getservbyport(i)
                        print(LIGHT_CYAN + "Port " + YELLOW + str(service) + LIGHT_CYAN + " is " + LIGHT_GREEN + "open")
                    else:
                        service = socket.getservbyport(i)
                        print(LIGHT_CYAN + "Port " + YELLOW + str(service) + LIGHT_CYAN + " is " + RED + "closed")
        except:
            print(RED + "[!] Invalid Port Or IP")

    if selection == "2":

        print("\n")

        ip_sep = input(LIGHT_GREEN + "[+] " + YELLOW + "Enter The IP: ")
        scanned_port = input(LIGHT_GREEN + "[+] " + YELLOW + "Enter The Port You Want to scan: ")
        print("\nPinging " + ip_sep + " at the port " + scanned_port)
        print(LIGHT_CYAN + "\nScan Resualt: \n")

        try:
            

            for i in ports:

                with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as sock:
                    
                    if sock.connect_ex((ip_sep, scanned_port)) == 0:
                        service = socket.getservbyport(scanned_port)
                        print(LIGHT_CYAN + "Port " + YELLOW + str(service) + LIGHT_CYAN + " is " + LIGHT_GREEN + "open")
                    else:
                        service = socket.getservbyport(i)
                        print(LIGHT_CYAN + "Port " + YELLOW + str(service) + LIGHT_CYAN + " is " + LIGHT_GREEN + "closed")
        except:
            print(RED + "[!] Invalid Port Or IP")

        exit()
main()