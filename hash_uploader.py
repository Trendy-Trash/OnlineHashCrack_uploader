import requests
import os

#set the hanshakes directory and a email for notification below.

email = "<your@email.com>"
dir_path = r'<path/to/folder/with/hashes/handshakes>' #it is important that the path doesn't end with "/"


# this script will loop through the folder containing hashes or handshake files (.pcap .cap), 
# and upload them automatically to OnlineHashCrack.com API using curl :
# curl -X POST -F "email=valid@email.com" -F "file=@/file/path/" https://api.onlinehashcrack.com

#this will loop iterating all files in the directory.
for path in os.listdir(dir_path):

    # check if current path is a file
    if os.path.isfile(os.path.join(dir_path, path)):
        file_path = os.path.join(dir_path, path)
        # print("sending: " + file_path)     # this print is just for debugging the loop
        files = {
            'email': (None, email),
            'file': (file_path, open(file_path, 'rb')),
        }

        # using requests post to interact with api endpoint
        try:
            response = requests.post('https://api.onlinehashcrack.com/', files=files)
            print(response.text)
            print("############################################################################\n")
            if '[-] This file extension is not supported. Please try again or contact us.' in response.text:
                print("Extension is not supported !")
                print("Please try again with another file !")
            elif '[-] File is not valid.' in response.text:
                print("Invalid file !")
                print("Please try again with another file !")
            elif '[+] This file has already been sent!' in response.text:
                print("File already exists !")
                print("This file is in cracking process !")
                print("Check your e-mail...")
            elif '[+] Something went wrong: this file is not password-protected OR the encryption method is not supported.' in response.text:
                print("File is not encrypted !")
                print("Please send an encrypted file !")
            elif 'Yours file' and 'enters in the cracking process' in response.text:
                print("File Uploaded Successfully...")
                print("Started 20M+ wordlist and hybrid bruteforce.")
                print("Check your email to see cracking status.")
                print("It takes maximum 48 hours to crack a file !")
                print("Sit back and relax...")
                print("We will send you an email when it's done !")
            else:
                pass

        except requests.exceptions.ConnectionError as err:
            print("Something Went Wrong!")
            raise SystemExit(err)

        print("###########################################################################\n")
# HAPPY CRACKING!


