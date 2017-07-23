# !/usr/bin/python  
# -*- coding: utf-8 -*- 
import sys
import os
import json  
import urllib  
import urllib2  
import re
import socket,threading
import time,Queue
IPGeo=''
DNS=''
flag = True
flag1 = True


def ipgeo(IP):
    global IPGeo
    global flag
    if IP!='':
        IP = urllib.quote_plus(IP)
        url = 'http://freegeoip.net/json/'+IP 
        urlobj = urllib2.urlopen(url)  
        data = urlobj.read()  
        datadict = json.loads(data, encoding='utf-8')
        IPGeo=datadict ['country_name'].encode("utf-8") +'-'+datadict ['region_name'].encode("utf-8") +'-'+datadict['city'].encode("utf-8")
    else:
        IPGeo=''
    print 'ip_geo'
    flag = False

def whois(domain):
    global flag1
    ddd = re.compile('.+\\.cn')
    domainn = re.compile('Domain Name:.+')
    DomainID2 = re.compile('ROID:.+')
    DomainID = re.compile('Registry Domain ID:.+')
    Registrar = re.compile('Registrar:.+')
    Email = re.compile('Registrar Abuse Contact Email:.+')
    Email2 = re.compile('Registrant Contact Email:.+')
    Phone = re.compile('Abuse Contact Phone:.+')
    RegistrarID = re.compile('Registrar IANA ID:.+')
    RegistrarID2 = re.compile('Registrant ID:.+')
    NameServer = re.compile('Name Server:.+')
    Status = re.compile('Status:.+')
    UpdatedD = re.compile('Updated Date:.+')
    CreationD = re.compile('Creation Date:.+')
    CreationD2 = re.compile('Registration Time:.+')
    ExpirationD = re.compile('Expiration Date:.+')
    ExpirationD2 = re.compile('Registry Expiry Date:.+')
    ExpirationD3 = re.compile('Expiration Time:.+')

    sss="whois "+domain
    val = os.popen(sss).read()
    D = domainn.search(val)
    Did = DomainID.search(val)
    Did2 = DomainID2.search(val)
    EML = Email.search(val)
    EML2 = Email2.search(val)
    PHO = Phone.search(val)
    R = Registrar.search(val)
    ID = RegistrarID.search(val)
    ID2 = RegistrarID2.search(val)
    NA = NameServer.findall(val)
    STA = Status.search(val)
    UPd = UpdatedD.search(val)
    CEd = CreationD.search(val)
    CEd2 = CreationD2.search(val)
    EXd = ExpirationD.search(val)
    EXd2 = ExpirationD2.search(val)
    EXd3 = ExpirationD3.search(val)
    print D.group(0)
    try:
        print Did.group(0)
    except:
        print Did2.grouop(0)
    try:
        print EML.group(0)
    except:
        print EML2.group(0)
    try:
        print PHO.group(0)
    except:
        print('Phone:')
    print R.group(0)
    try:
        print ID.group(0)
    except:
        print ID2.group(0)
    if re.match(ddd,domain):
        for i in range(0,len(NA)):
            print NA[i]
    else:
        for i in range(0,len(NA)/2):
            print NA[i]
    print STA.group(0)
    try:
        print UPd.group(0)
    except:
        print ('Updated Date:none')
    try:
        print CEd.group(0)
    except:
        print CEd2.group(0)
    try:
        print EXd.group(0)
    except:
        try:
            print EXd2.group(0)
        except:
            print EXd3.group(0)
    print 'DNS'
    flag1 = False



if __name__=='__main__':
    tt=time.time()
    global IPGeo
    global DNS
    global flag
    domain = 'baidu.com'
    IP,IPGeo = '',''
    DNS=''
    try:
        IP = socket.gethostbyname(domain)
    except:
        IP=''
    t1 = threading.Thread(target=ipgeo, args=(IP,))
    t2 = threading.Thread(target=whois, args=(domain,))
    t1.start()
    t2.start()
    
    
    t1.join() 
    t2.join() 
    while (flag or flag1):
        time.sleep(0.5)
    print DNS
    print IPGeo
    print time.time()-tt
    