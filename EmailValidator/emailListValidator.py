# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 17:35:01 2021

@author: BloodShot
"""

import re
import json
import requests
import socket
from getmac import get_mac_address as gma
import requests




######################### Check Email is Active or not ################################################
def isActiveEmail(email_address):
    response = requests.get("https://isitarealemail.com/api/email/validate",params = {'email': email_address})

    status = response.json()['status']
    if status == "valid":
        print("email is valid")
        return True
    elif status == "invalid":
        print("email is invalid")
        return False
    else:
        print("email was unknown")
        return False
    
#####################################################################################################
    
    
    

############## Email Validator Method ######################
def validateEmail(email, choice):
    #regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    regexForYahoo = '^[a-z0-9]+[\._]?[a-z0-9]+[@]+[y]+[a]+[h]+[o]+[o]+[.]+[c]+[o]+[m]+$'
    regexForAOL = '^[a-z0-9]+[\._]?[a-z0-9]+[@]+[a]+[o]+[l]+[.]+[c]+[o]+[m]+$'  
    regexForDenounce = '^[a-z0-9]+[\._]?[a-z0-9]+[@]+[d]+[e]+[n]+[o]+[u]+[n]+[c]+[e]+[.]+[c]+[o]+[m]+$'
    regexForPaypal = '^[a-z0-9]+[\._]?[a-z0-9]+[@]+[p]+[a]+[y]+[p]+[a]+[l]+[l]+[.]+[c]+[o]+[m]+$'
    regexForNetflix = '^[a-z0-9]+[\._]?[a-z0-9]+[@]+[n]+[e]+[t]+[f]+[l]+[i]+[x]+[.]+[c]+[o]+[m]+$'
    # pass the regular expression
    # and the string in search() method
    
    #Setting the regex for particullar email validation
    if(choice == 1):
        regex = regexForAOL
    if(choice == 2):
        regex = regexForYahoo
    if(choice == 3):
        regex = regexForDenounce
    if(choice == 4):
        regex = regexForPaypal
    if(choice == 5):
        regex = regexForNetflix
        
        
    if(re.search(regex, email)):
        #print("Valid Email")
        return True
 
    else:
        #print("Invalid Email")
        return False
#############################################################





################ Authenticate User ##########################
def authenticateDevice(pwd):
    

    # Getting the IP address of machine
    #s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    #hostname = socket.gethostname()   
    #IPAddr = socket.gethostbyname(hostname)
    MACAddr = gma()
    print(MACAddr)
    apiUrl = "http://192.168.43.186:105/login?ip="+MACAddr
    #request = requests.get('http://localhost/RestfulAPI/api/product/read.php?id=192.18.06.1')
    #request = requests.get('https://api-grooming.online/api/product/read.php?id=91.2')
    request = requests.get(apiUrl)
    credential = request.text

    # Getting the IPs and password from database/API
    #request = requests.get('https://api.agify.io/?name=bella')
    credentialList = json.loads(credential)
    print("Welcome\n")
    print(len(credentialList))
    
    '''#y = {'ip': '192.20', 'pwd':'123'}
    #if(credentialList['message'] != ' '):
     #   print("You are not registered. Please contact Admin for register yourself!!!!")
      #  return False
    print(credentialList[0]['pwd'])'''
    
    
    if(len(credentialList)>0):
        
        if(credentialList['pwd']==pwd and credentialList['ipaddr']==MACAddr):
            return True
        else:
            print("Please enter correct password!!!!")
            return False
    else:
        print("You are not registered. Please contact Admin for register yourself!!!!")
        return False
        
############################################################





if __name__ == '__main__':
    
    print('''
     __________     ___          ___                      _______________
    /_________/     \  \        /  /                     /_/  /______\  \
   /  /____   _____  \  \      /  /            ______     /  /        \  \
  /  /____/   _____   \  \    /  /  /\     /     |       /  /         /  /
 /  /______            \  \  /  /  /__\   /      |    __/  /_________/  /
/__/______/             \__\/__/  /    \ /___ ___|___/_/__/_________/__/
                                              
            Bounce Email Valid Checker V1 
''')
    
    pwd = input("Enter your password\n")
    #try:
    
    if(1):
        if(authenticateDevice(pwd)):
            print("You are logged in now!!\n")
            print("\n")
            print("Which validation do you want? Please enter your the selection as below\n\n ")
            print("1. For AOL mail validation\n")
            print("2. For Yahoo mail validation\n")
            print("3. For Debounce mail validation\n")
            print("4. For Paypal mail validation\n")
            choice = int(input())
            emailListFile = input("Enter the full path of emailList file !!!!!\n")
            try:
                f = open(emailListFile, 'r')
                emailsList = f.read()
            #print(emailsList)
            
                emails = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", emailsList)
                print (emails)
                f.close()
            #Creating a file which is having the valid email ids in same directory where the script is kept
                f1 = open('validEmailListFile.txt', 'w')
                f2 = open('invalidEmailListFile.txt', 'w')
                for i in emails:
                    statusOfEmailValidation = validateEmail(i, choice)
                    if(statusOfEmailValidation):
                        if(isActiveEmail(i)):
                            f1.write(i+"\n")
                            print("Done\n")
                        else:
                            f2.write(i+"\n")
                    else:
                        f2.write(i+"\n")
                f1.close()
                f2.close()
            except FileNotFoundError:

                print ("File is not present, please enter the correct path")
    #except:
    else:
        print("Sorry you are not authorised to access this application. Please try again with correct credentials or contact with System Administrator!\n")
    
    #emailListFile = input("Enter the full path of emailList file !!!!!") 
#emailListFile  = 'C:/Users/BloodShot/Desktop/ProblemSolving/emailList1.txt'       
    





