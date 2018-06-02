import urllib
from json import load
from urllib2 import urlopen

ip = load(urlopen('https://api.ipify.org/?format=json'))['ip']
tor = urllib.urlopen('https://check.torproject.org/cgi-bin/TorBulkExitList.py?ip=1.1.1.1')

for ip_tor in tor.readlines():
       ip_tor = ip_tor.replace("\n","")
       if ip == ip_tor:
           success = 1
       	   break
       else:
           success = 0

if success == 1:

        print "[+] Your public Ip " + ip + " is a TOR ip" 

else:

        print "[-] Your public Ip: " + ip + " is not a TOR ip"
