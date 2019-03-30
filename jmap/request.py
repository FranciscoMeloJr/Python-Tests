#Import for the libs:
import urllib2
import sys

def do_request(arg):
   #print sys.argv[1]
   #Do the request:
   some_url = 'http://localhost:8080/servlet/HelloServlet?buffer='+arg
   #Get content
   try:
       content = urllib2.urlopen(some_url).read()
       #Print content
       return 1
   except:
       return -1

def do_test(arg):
   i = 0
   while i < int(arg):
       try:
           do_request(str(i))
       except:
           print "it is down"
           break
       i+=1

do_test(sys.argv[1])
