#!/usr/bin/env python
########################
# author:terry         #
# 27/11/15             #
########################

import time
import os
import getopt
import sys

filename       = ''
name           = '' #author name
hasdes         = False #whether has description 
cusdate        = '' #custom date

def usage():
    print "FILESIGNER    Auth:Terry"
    print "              Version:1.1.0"
    print "              Date:2015-12-27"
    print
    print "Usage: ./filesigner.py -f test.txt -a terry -d"
    print 
    print "-h,--help           -show the usage."
    print "-f,--file           -the file need to sign."
    print "-a,--author         -the file author name."
    print "-d                  -need to write a description."
    print "-c,--cusdate        -enter the custom date for file."
    print
    print 
    sys.exit(1)


def main():
    global filename
    global name
    global hasdes
    global cusdate

    if not len(sys.argv[1:]):
        usage()

    try:
        opts,args = getopt.getopt(sys.argv[1:],'hf:a:dc:',
                                  ['help','file=','author=','cusdate='])
    except getopt.GetoptError,e:
        print str(e)
        usage()

    for o,a in opts:
        if o in ('-h','--help'):
            usage()
        elif o in ('-f','--file'):
            filename = a
        elif o in ('-a','--author'):
            name = 'Author:'+a
        elif o in ('-d'):
            hasdes = True
        elif o in ('-c','--cusdate'):
            cusdate = a
        else:
            assert False,'Unhandled Option.'

    #filename = raw_input("please input your filename:")
    #name = "autor:"+raw_input("please input your name:")
    #description = raw_input("please input your description:")
    #date = time.strftime("%d/%m/%Y")
    #print name,filename,date

    if hasdes:
        description = raw_input("Please input your description:")
    
    if cusdate is '':
        date = 'Date:'+time.strftime("%d/%m/%Y")
    else:
        date = 'Date:'+cusdate

    markfile = file(filename,"a+")
    length = max(len(name),len(filename),len(date))*3/2
    
    marklist = ["#"*length,forstr(length,name),forstr(length,date),"#"*length]
    for i in marklist:
        markfile.write(i+"\n")
        
    markfile.close()
        
#formatstring,make the string has same length as ### line
def forstr(length,string):
    #lenth of space
    spacelen = length - len(string) -3
    return "# "+string+" "*spacelen + "#"

if (__name__ == "__main__"):
    main()
