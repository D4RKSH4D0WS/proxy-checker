#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
#Author D4RK5H4D0W5

G0 = "\033[0;32m"
G1 = "\033[1;32m"
C0 = "\033[0;36m"
C1 = "\033[1;36m"
W0 = "\033[0;37m"
W1 = "\033[1;37m"
R0 = "\033[0;31m"
R1 = "\033[1;31m"
Y1 = "\033[1;33m"
Y0 = "\033[0;33m"

from multiprocessing.pool import ThreadPool
import requests as r
import json
import sys
import os

def scan(target):
	web=r.post('https://onlinechecker.proxyscrape.com/index.php',headers={'user-agent': 'Mozilla/5.0 (Linux; Android 5.1.1; SM-J111F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.90 Mobile Safari/537.36'},data={'ip_addr':target.split(':')[0],'port':target.split(':')[1]}).text
	js=json.loads(web)
	if js['working'] == True:
		print '%s[ %sLIVE %s] %s%s'%(W1,G1,W1,W0,target)
		open('proxy_live.txt','a+').write(target+'\n')
	else:
		print '%s[ %sDIEE %s] %s%s'%(W1,R1,W1,W0,target)
	print '%s[ %sINFO %s] %sCounty:%s , Type:%s'%(W1,Y1,W1,W0,js['country'],js['type'])
	print

try:
	os.system('cls' if os.name == 'nt' else 'clear')
	print '''%s   ___                   __
  / o |_   _  _ ___ __ ,'_/ /7  __  __ /7   __ _
 / _,'//7,'o| \V,'\V // /_ / \,'o/,','//_7,'o///7
/_/  //  |_,','n\  )/ |__//n_/|_( \_\//\\ |_(//
                  //     %sCoded by D4RKSH4D0WS
'''%(C1,W0)
	ThreadPool(5).map(scan,open(sys.argv[1]).read().splitlines())
	print '%s[ %sDONE %s] %sSaved in proxy_live.txt'%(W1,G1,W1,W0)
except r.exceptions.ConnectionError:
        exit('%s[%s!%s] %sCheck internet'%(W1,R1,W1,W0))
except IndexError:
        exit('%s[%s!%s] %sUse : python2 %s proxy.txt'%(W1,R1,W1,W0,sys.argv[0]))
except IOError:
        exit('%s[%s!%s] %sFile does not exist'%(W1,R1,W1,W0))
except KeyboardInterrupt:
        exit('\n%s[%s!%s] %sExit'%(W1,R1,W1,W0))
