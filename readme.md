## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)

## General info
This project is a simple script to automate the uploading of many handshakes, hashes or files to OnlineHashCrack.com with ease.
Just change the path of the folder you want to upload files from and add an email address for notifications.

This tool is meant to be used by authorised personel to "crack" or just handle and send the hashes, etc to the internet.
Im not responsable of any misuse of this script.
Use at your own discretion.
	
## Technologies
Project is created with:
* Python3.10
* "requests" python library
* "os" python library
	
## Setup
To run this project :

* Remember to change <path/to/folder/...> and <your@email.com> in hash_uploader.py with your own.

```
$ pip install requests
$ pip install os
$ python3 hash_uploader.py
```
