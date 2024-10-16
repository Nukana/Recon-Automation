import itertools
import os
import queue
import random
import socket
import sys
import threading
import time
from asyncio import threads
from queue import Queue
from pip._vendor.distlib.compat import raw_input
import phonenumbers
import pyfiglet
import pyqrcode
import requests
from barcode import EAN13
from barcode.writer import ImageWriter
from phonenumbers import carrier
from phonenumbers import geocoder
from pyfiglet import Figlet
from tabulate import tabulate
from tqdm import *

result = pyfiglet.figlet_format("Recon Tool", font="5lineoblique")
print(result)
options = (
        "1- MY IP ADDRESS \n"
        "2- PASSWORD GENERATOR \n"
        "3- WORDLIST GENERATOR \n"
        "4- BARCODE GENERATOR \n"
        "5- QRCODE GENERATOR \n"
        "6- PHONE NUMBER INFO \n"
        "7- SUBDOMAIN SCANNER \n"
        "8- PORT SCANNER \n"
        "9- DDOS ATTACK \n"
        "10- ADMIN PANEL FINDER \n"
    )
print(options)
select = int(input('Enter Your Choice >>>>>>---------------> '))


match select:
    case 1:
        def loading():
            for _ in tqdm(range(100), desc="LOADING...", ascii=False, ncols=75):
                time.sleep(0.01)
            print("LOADING DONE!")

        def font(text):
            cool_text = Figlet(font="slant")
            return str(cool_text.renderText(text))



        def window_size(columns=80, height=20):
            os.system("cls" if os.name == 'nt' else "clear")
            os.system(f'mode con: cols={columns} lines={height}')

        if __name__ == "__main__":
            window_size(80, 20)
            print(Figlet(font="slant").renderText("FIND MY IP"))
            loading()
            hostname = socket.gethostname()
            IPAddr = socket.gethostbyname(hostname)
            print(f"Your Device is: {hostname}")
            print(f"Your IP Address is: {IPAddr}")
            input("PRESS ENTER TO EXIT")

    case 2:
        def loading():
            for _ in tqdm(range(100), desc="LOADING...", ascii = False, ncols = 75):
                time.sleep(0.01)
            print("LETS MOVE!")


        def font(text):
            cool_text = Figlet(font="slant")
            return str(cool_text.renderText(text))

        def window_size(columns=750, height=75):
            os.system('clear')
            os.system('stty cols %s rows %s'%(columns, height))

        if __name__ == "__main__":
            window_size(80, 20)
            print(font("PASSWORD GENERATOR"))
            loading()
            length = int(input('Enter Your Length >>>>>>-------------> '))

            def get_random_string(length):
                lower = "abcdefghijklmnopqrstuvwxyz"
                upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                numbers = "1234567890"
                symbols = "@#&*(){}[]/?"
                all = lower + symbols + numbers + upper
                password = "".join(random.sample(all, length))
                print("GENERATED PASSWORD OF LENGTH:", length,"is ",password, r""">>>>>----------->""")

            get_random_string(length)
            raw_input("PRESS ENTER TO EXIT")
    case 3:
        def loading():
            for _ in tqdm(range(100), desc="LOADING...", ascii = False, ncols = 75):
                time.sleep(0.01)
            print("LETS MOVE!")

        def font(text):
            cool_text = Figlet(font="slant")
            return str(cool_text.renderText(text))

        def window_size(columns=750, height=75):
            os.system('clear')
            os.system('stty cols %s rows %s'%(columns, height))

        if __name__ == "__main__":
            window_size(80, 20)
            print(font("WORDLIST GENERATOR"))
            loading()
            print("GENERATED PASSWORD IS SAVED IN THE PRESENT FOLDER/DIRECTORY")
            chrs = raw_input("ENTER THE LETTERS FOR COMBINATION >>>>>>------> ")
            l = int(raw_input("MINIMUM LENGTH OF PASSWORD >>>>>>-------> "))
            k=l
            j = int(raw_input("MAXIMUM LENGTH OF PASSWORD >>>>>>-------> "))
            n = j + 1
            mtl = len(chrs)
            p=[]
            zt = raw_input("[+] Enter the name of the file"r""">>>>>------->""")
            for ltp in range(k,n):
                ans = mtl ** ltp
                p.append(ans)
                tline = sum(p)
                raw_input('ARE YOU READY?[PRESS ENTER]')
                time1 = time.asctime()
                start = time.time()
                psd = open(zt, 'a')

                for i in range(k,n):
                    r=i*100/n
                    l = str(r) + 'percent'
                    sys.stdout.write("\r%s"% l)
                    psd.flush()

                    for xs in itertools.product(chrs, repeat=i):
                        psd.write(''.join(xs)+'\n')
                        psd.flush()

            psd.close()
            sys.stdout.write("DONE SUCCESS")
            end = time.time()
            '\t [+]  Process Completed      :', time.asctime()
            totaltime = end - start
            rate = tline / totaltime

            raw_input(" PRESS ENTER EXIT")

    case 4:
        def loading():
            for _ in tqdm(range(100), desc="LOADING...", ascii=False, ncols=75):
                time.sleep(0.01)
            print("LETS MOVE!")

        def font(text):
            cool_text = Figlet(font="slant")
            return str(cool_text.renderText(text))
        def window_size(columns=750, height=75):
            os.system('clear')
            os.system('stty cols %s rows %s'%(columns, height))

        def generator(number):
            my_code = EAN13(number, writer=ImageWriter)
            my_code.save("bar_code")

        if __name__ == "__main__":
            window_size(80, 20)
            print(font("BARCODE GENERATOR"))
            loading()
            print("GENERATED BARCODE WILL BE SAVED AS PNG IN THE PRESENT FOLDER/DIRECTORY")
            innumber = input("ENTER 12 digit number to generate barcode:"r"""">>>>>>---------->""")
            print(innumber)
            generator(innumber)
            raw_input("PRESS ENTER EXIT")

    case 5:
        def loading():
            for _ in tqdm(range(100), desc="LOADING...", ascii = False, ncols = 75):
                time.sleep(0.01)
            print("LETS MOVE!")

        def font(text):
            cool_text = Figlet(font="slant")
            return str(cool_text.renderText(text))

        def window_size(columns=750, height=75):
            os.system('clear')
            os.system('stty cols %s rows %s'%(columns, height))

        if __name__ == "__main__":
            window_size(80, 20)
            print(font("QRCODE GENERATOR"))
            loading()
            print("GENERATED QRCODE WILL BE SAVED AS MYQR.PNG IN THE PRESENT FOLDER/DIRECTORY")

            s= input("ENTER THE LINK TO CREATE A QRCODE "r""">>>>>>--------->""")
            url = pyqrcode.create(s)
            url.svg("myqr.svg", scale=8)
            url.png("myqr1.png", scale=6)
            raw_input("PRESS ENTER EXIT")

    case 6:
        def loading():
            for _ in tqdm(range(100), desc="LOADING...", ascii = False, ncols = 75):
                time.sleep(0.01)
            print("LETS MOVE!")


        def font(text):
            cool_text = Figlet(font="slant")
            return str(cool_text.renderText(text))


        def window_size(columns=750, height=75):
            os.system('clear')
            os.system('stty cols %s rows %s' % (columns, height))

        if __name__ == "__main__":
            window_size(80, 20)
            print(font("PHONE NUMBER SCANNER"))
            loading()

        def num_scanner(phn_num):
            number = phonenumbers.parse(phn_num)
            print(number)
            description = geocoder.description_for_number(number, 'en')
            supplier = carrier.name_for_number(number, 'en')
            info = [["country", "SUPPLIER"], description, supplier]
            data = str(tabulate(info,headers='firstrow',tablefmt='github'))
            return data

        if __name__ == "__main__":
            number = input("ENTER THE PHONE NUMBER:"r""">>>>>>------->""")
            print(num_scanner(number))
            raw_input("PRESS ENTER EXIT")

    case 7:
        def loading():
            for _ in tqdm(range(100), desc="LOADING...", ascii = False, ncols = 75):
                time.sleep(0.01)
            print("LETS MOVE!")

        def font(text):
            cool_text = Figlet(font="slant")
            return str(cool_text.renderText(text))


        def window_size(columns=750, height=75):
            os.system('clear')
            os.system('stty cols %s rows %s' % (columns, height))

        if __name__ == "__main__":
            window_size(80, 20)
            print(font("SUBDOMAIN SCANNER"))
            loading()
            print("IT TAKES TIME ACCORDING TO THE DOMAIN")
            print("USING DEFAULT ADDED WORDLIST WITH 649649 WORDS")
            domain = input("ENTER THE DOMAIN TO SCAN"r""">>>>>>>>----->""")
            file = open("subdomain.txt")
            content = file.read()
            subdomains = content.splitlines()
            for subdomain in subdomains:
                url = f"https://{subdomain}.{domain}"
                try:
                    requests.get(url)
                    print(f"[+] Discovered subdomain:", url)
                except requests.ConnectionError:
                    print("[x]Subdomain not found", url)

            raw_input("PRESS ENTER EXIT")



    case 8:
        def loading():
            for _ in tqdm(range(100), desc="LOADING...", ascii=False, ncols=75):
                time.sleep(0.01)
            print("LETS MOVE!")


        def font(text):
            cool_text = Figlet(font="slant")
            return str(cool_text.renderText(text))


        def window_size(columns=750, height=75):
            os.system('clear')
            os.system('stty cols %s rows %s' % (columns, height))

        def portscan(port):
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.connect((target , port))
                return True
            except:
                return False

        def get_ports(mode):
            if mode == "1":
                for port in range(1, 1024):
                    queue.put(port)

            elif mode == "2":
                for port in range(1, 49152):
                    queue.put(port)

            elif mode == "3":
                ports = [20,21,22,23,25,53,80,110,443]
                for port in range(1, 49152):
                    queue.put(port)
            elif mode == "4":
                ports = input("ENTER THE PORT NUMBER SEPERATE BY BLANK:")
                ports = ports.split()
                ports = list(map(int, ports))
                for port in ports:
                    queue.put(port)


        def worker():
            while not queue.empty():
                port = queue.get()
                if portscan(port):
                    print(f"Port {port} is open!")
                    open_ports.append(port)


        def run_scanner(threads=100, mode=1):
            if mode == 1:
                for port in range(1, 1024):
                    queue.put(port)
            elif mode == 2:
                for port in range(1, 49152):
                    queue.put(port)

            thread_list = []
            for t in range(threads):
                thread = threading.Thread(target=worker)
                thread_list.append(thread)
                thread.start()

            for thread in thread_list:
                thread.join()

            print("Open ports are:", open_ports)

        if __name__ == "__main__":
            window_size(80,20)
            print(font("PORT SCANNER"))
            loading()
            print("IT TAKES TIME ACCORDING TO THE OPEN PORT AND PROVIDED IP")
            target = input("ENTER THE IP TO SCAN FROM:"r""">>>>>---------->""")
            mode = int(input("ENTER THE MODE OF SCANNER:"))
            queue = queue.Queue()
            open_ports = []
            run_scanner(100, mode)


