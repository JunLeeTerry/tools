#!/usr/bin/env python

import urllib2
import time
import getopt
import sys

stoptime =          0.0
times    =          0


def usage():
    print "WEBSITE REQUEST     Author:Terry"
    print "                    Version:1.1.0"
    print "                    Date:2015-12-27"
    print "Usage: ./website_request -i 1 -t 500"
    print
    print "-h,--help           -show the help content."
    print "-i,--interval       -the value of interval."
    print "-t,--times          -how many times to request url."
    print
    print 
    sys.exit(1)

def main():
    global stoptime
    global times

    if not len(sys.argv[1:]):
        usage()
    
    try:
        opts,args = getopt.getopt(sys.argv[1:],'hi:t:',
                                  ['help','interval=','times='])
    except getopt.GetoptError,e:
        print str(e)
        usage()

    for o,a in opts:
        if o in ('-h','--help'):
            usage()
        elif o in ('-i','--interval'):
            stoptime = float(a)
        elif o in ('-t','--times'):
            times = int(a)
  
    url = raw_input('Please enter url:')

    opener = urllib2.build_opener()
    opener.addheaders = [('User-agent','Mozilla/5.0')]
    
    print "total requst times: "+str(times)
    for i in range(times):
        try:
            start = time.time()
            opener.open(url).read().decode('utf-8')
            end = time.time()
            print "index: " + str(i+1) + " interval: " + str(end-start) + "s"
            
        except urllib2.HTTPError,e:
            print e
            time.sleep(2)
            
        except urllib2.URLError,e:
            print e
            time.sleep(2)
            
            time.sleep(stoptime)
        

if __name__=='__main__':
    main()
