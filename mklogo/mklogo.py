#!/usr/bin/env python
#########################
# author:terry          #
# 11/12/15              #
#########################

import sys
import getopt

content             = ''             #the content of input 
w2file              = False
filepath            = ''             #the file path
backletter          = ''             
foreletter          = ''

def usage():
    print "MKLOGO    Auth:Terry"
    print "          Version:1.0.0"
    print "          Date:2015-12-11"
    print 
    print "Usage: ./mklogo -i 'terry' -b '#' -f '$' -w -p ./test.txt"
    print 
    print "-h,--help        - show the usage."
    print "-i,--input       - input some string to show."
    print "-w,--write       - write the output to some file."
    print "-p,--path        - the path of file need to be written in."
    print "-f,--fore        - use which letter to make the signal."
    print "-b,--back        - use which letter to make the background."
    print 
    print "Special Signal:"
    print "\l               - the signal of love."
    print 
    print "[*] Symbols in bash need to add Quotes!"
    print "Examples:"
    print "./mklogo -i 'Terry'"
    print "./mklogo -i 'Hello\lWorld' -f '@' -b '^'"
    print "./mklogo -i 'Hello' -f '!' -b '$' -w -p ./output.txt"
    print 
    print 
    sys.exit(1)

def main():
    global content
    global w2file
    global filepath
    global foreletter
    global backletter

    if not len(sys.argv[1:]):
        usage()

    try:
        opts,args = getopt.getopt(sys.argv[1:],'hi:wp:f:b:',
                                  ['help','input=','write','path=','fore=','back='])
    except getopt.GetoptError,e:
        print str(e)
        usage()
    
    for o,a in opts:
        if o in ('-h','--help'):
            usage()
        elif o in ('-i','--input'):
            content = a
        elif o in ('-w','--write'):
            w2file = True
        elif o in ('-p','--path'):
            path = a 
        elif o in ('-f','--fore'):
            foreletter = a
        elif o in ('-b','--back'):
            backletter = a
        else:
            assert False,'Unhandled Option.'        
        
    def printlogo(content,foreletter,backletter):
        matrix = []
        issignal = False
        index = 0
        signalnum = 0
        for letter in content:
            if issignal:
                issignal = False
                continue

            if letter != '\\':               
                simplematrix = letter2matrix(letter)
            else:
                signalnum += 1
                simplematrix = signal2matrix(content[index+signalnum])
                issignal = True
            
            for xyindex in range(len(simplematrix)):
                x,y = simplematrix[xyindex]
                x = index*8 + x
                simplematrix[xyindex] = (x,y)
            matrix += simplematrix
            index += 1
            


        line = ''
        area = []
        for i in range(8):
            for j in range(8*len(content)):
                line += (foreletter if (j,i) in matrix else backletter)
            area.append(line)
            line = ''
        for linecontent in area:
            print linecontent
            
    def signal2matrix(signal):
        matrix = None
        if signal is 'l': matrix = [(1,1),(2,1),(5,1),(6,1),(0,2),(3,2),(4,2),(7,2),(0,3),(7,3),(1,4),(6,4),(2,5),(5,5),(3,6),(4,6)]
        else :            matrix = []
        return matrix
   
    def letter2matrix(letter):
        matrix = None
        if letter is 'a':  matrix = [(2,5),(3,2),(3,4),(3,6),(4,2),(4,4),(4,6),(5,3),(5,4),(5,5)]
        elif letter is 'b':matrix = [(2,1),(2,2),(2,3),(2,4),(2,5),(2,6),(3,3),(3,6),(4,3),(4,6),(5,4),(5,5)]
        elif letter is 'c':matrix = [(3,3),(4,3),(2,4),(2,5),(3,6),(4,6)]               
        elif letter is 'd':matrix = [(2,4),(2,5),(3,3),(3,6),(4,3),(4,6),(5,1),(5,2),(5,3),(5,4),(5,5),(5,6)]               
        elif letter is 'e':matrix = [(2,3),(2,4),(2,5),(3,2),(3,4),(3,6),(4,2),(4,4),(4,6),(5,3),(5,4)]               
        elif letter is 'f':matrix = [(2,3),(3,2),(3,1),(3,3),(3,4),(3,5),(3,6),(4,1),(4,3)]               
        elif letter is 'g':matrix = [(2,2),(2,5),(3,1),(3,3),(3,6),(4,1),(4,2),(4,3),(4,4),(4,5),(4,6)]               
        elif letter is 'h':matrix = [(3,1),(3,2),(3,3),(3,4),(3,5),(3,6),(4,4),(5,4),(5,5),(5,6)]               
        elif letter is 'i':matrix = [(3,3),(4,3),(4,4),(4,5),(4,6),(5,6),(4,1)]               
        elif letter is 'j':matrix = [(4,1),(3,3),(4,3),(4,4),(4,5),(4,6),(4,7),(3,7),(2,6)]               
        elif letter is 'k':matrix = [(3,1),(3,2),(3,3),(3,4),(3,5),(3,6),(4,4),(4,5),(5,3),(5,6)]                            
        elif letter is 'l':matrix = [(3,1),(4,1),(4,2),(4,3),(4,4),(4,5),(4,6),(5,6)]               
        elif letter is 'm':matrix = [(2,4),(2,5),(2,6),(3,3),(4,4),(4,5),(4,6),(5,3),(6,4),(6,5),(6,6)]               
        elif letter is 'n':matrix = [(2,4),(2,5),(2,6),(3,3),(4,3),(5,4),(5,5),(5,6)]               
        elif letter is 'o':matrix = [(2,4),(2,5),(3,3),(3,6),(4,3),(4,6),(5,4),(5,5)]               
        elif letter is 'p':matrix = [(2,1),(2,2),(2,3),(2,4),(2,5),(2,6),(3,1),(3,3),(4,1),(4,3),(5,2)]               
        elif letter is 'q':matrix = [(2,2),(3,1),(3,3),(4,1),(4,3),(5,1),(5,2),(5,3),(5,4),(5,5),(5,6)]               
        elif letter is 'r':matrix = [(3,3),(3,4),(3,5),(3,6),(4,4),(5,3)]               
        elif letter is 's':matrix = [(2,3),(3,2),(3,4),(3,6),(4,2),(4,4),(4,6),(5,5)]              
        elif letter is 't':matrix = [(3,1),(3,2),(3,3),(3,4),(3,5),(3,6),(2,3),(4,3),(4,6)]               
        elif letter is 'u':matrix = [(2,3),(2,4),(2,5),(3,6),(4,6),(5,3),(5,4),(5,5)]               
        elif letter is 'v':matrix = [(2,3),(2,4),(2,5),(2,6),(3,5),(4,4),(5,3)]
        elif letter is 'w':matrix = [(2,4),(2,5),(3,6),(4,4),(4,5),(5,6),(6,4),(6,5)]               
        elif letter is 'x':matrix = [(2,3),(3,4),(4,5),(5,6),(5,3),(4,4),(3,5),(2,6)]               
        elif letter is 'y':matrix = [(2,1),(2,2),(3,3),(4,1),(4,2),(4,3),(4,4),(4,5),(4,6),(3,6),(2,5)]               
        elif letter is 'z':matrix = [(2,3),(3,3),(4,3),(5,3),(4,4),(3,5),(2,6),(3,6),(4,6),(5,6)]               
        elif letter is 'A':matrix = [(1,2),(1,3),(1,5),(1,6),(2,1),(2,3),(3,0),(3,3),(1,4),(4,0),(4,3),(5,1),(5,3),(6,2),(6,3),(6,4),(6,5),(6,6)]  
        elif letter is 'B':matrix = [(1,0),(1,1),(1,2),(1,3),(1,4),(1,5),(1,6),(2,0),(2,3),(2,6),(3,0),(3,3),(3,6),(4,0),(4,3),(4,6),(5,1),(5,2),(5,4),(5,5)]           
        elif letter is 'C':matrix = [(1,1),(1,2),(1,3),(1,4),(1,5),(2,0),(2,6),(3,0),(3,6),(4,0),(4,6),(5,1),(5,5)]               
        elif letter is 'D':matrix = [(1,0),(1,1),(1,2),(1,3),(1,4),(1,5),(1,6),(2,0),(2,6),(3,0),(3,6),(4,1),(4,5),(5,2),(5,3),(5,4)]               
        elif letter is 'E':matrix = [(1,0),(1,1),(1,2),(1,3),(1,4),(1,5),(1,6),(2,0),(3,0),(4,0),(4,0),(5,0),(2,3),(3,3),(4,3),(5,3),(2,6),(3,6),(4,6),(5,6)]   
        elif letter is 'F':matrix = [(1,0),(1,1),(1,2),(1,3),(1,4),(1,5),(1,6),(2,0),(3,0),(4,0),(4,0),(5,0),(2,3),(3,3),(4,3),(5,3)]               
        elif letter is 'G':matrix = [(1,1),(1,2),(1,3),(1,4),(1,5),(2,0),(2,6),(3,0),(3,6),(4,0),(4,6),(4,3),(5,1),(5,3),(5,4),(5,5)]               
        elif letter is 'H':matrix = [(1,0),(1,1),(1,2),(1,3),(1,4),(1,5),(1,6),(5,0),(5,1),(5,2),(5,3),(5,4),(5,5),(5,6),(2,3),(3,3),(4,3)]               
        elif letter is 'I':matrix = [(1,0),(2,0),(3,0),(4,0),(5,0),(1,6),(2,6),(3,6),(4,6),(5,6),(3,1),(3,2),(3,3),(3,4),(3,5)]               
        elif letter is 'J':matrix = [(4,0),(5,0),(5,1),(5,2),(5,3),(5,4),(5,5),(4,6),(3,6),(2,6),(1,4),(1,5)]               
        elif letter is 'K':matrix = [(1,0),(1,1),(1,2),(1,3),(1,4),(1,5),(1,6),(2,3),(3,2),(3,4),(4,1),(4,5),(5,0),(5,6)]               
        elif letter is 'L':matrix = [(1,0),(1,1),(1,2),(1,3),(1,4),(1,5),(1,6),(2,6),(3,6),(4,6),(5,6)]               
        elif letter is 'M':matrix = [(1,0),(1,1),(1,2),(1,3),(1,4),(1,5),(1,6),(5,0),(5,1),(5,2),(5,3),(5,4),(5,5),(5,6),(2,1),(3,2),(4,1)]               
        elif letter is 'N':matrix = [(1,0),(1,1),(1,2),(1,3),(1,4),(1,5),(1,6),(5,0),(5,1),(5,2),(5,3),(5,4),(5,5),(5,6),(2,1),(3,2),(3,3),(3,4),(4,5)]               
        elif letter is 'O':matrix = [(1,1),(1,2),(1,3),(1,4),(1,5),(5,1),(5,2),(5,3),(5,4),(5,5),(2,0),(3,0),(4,0),(2,6),(3,6),(4,6)]               
        elif letter is 'P':matrix = [(1,1),(1,0),(1,2),(1,3),(1,4),(1,5),(5,1),(5,2),(2,0),(3,0),(4,0),(2,3),(3,3),(4,3),(1,6)]               
        elif letter is 'Q':matrix = [(1,1),(1,2),(1,3),(1,4),(1,5),(5,1),(5,2),(5,3),(5,4),(5,5),(2,0),(3,0),(4,0),(2,6),(3,6),(4,6),(3,4),(4,5)]               
        elif letter is 'R':matrix = [(1,1),(1,0),(1,2),(1,3),(1,4),(1,5),(5,1),(5,2),(2,0),(3,0),(4,0),(2,3),(3,3),(4,3),(3,4),(4,5),(5,6),(1,6)]               
        elif letter is 'S':matrix = [(1,1),(1,2),(1,5),(2,0),(2,3),(2,6),(3,0),(3,3),(3,6),(4,0),(4,3),(4,6),(5,1),(5,4),(5,5)]               
        elif letter is 'T':matrix = [(1,0),(2,0),(3,0),(4,0),(5,0),(3,1),(3,2),(3,3),(3,4),(3,5),(3,6)]               
        elif letter is 'U':matrix = [(1,1),(1,2),(1,3),(1,4),(1,5),(5,1),(5,2),(5,3),(5,4),(5,5),(2,6),(3,6),(4,6),(1,0),(5,0)]               
        elif letter is 'V':matrix = [(1,1),(1,2),(1,3),(1,4),(5,1),(5,2),(5,3),(5,4),(3,6),(4,5),(2,5),(1,0),(5,0)]               
        elif letter is 'W':matrix = [(1,0),(1,1),(1,2),(1,3),(1,4),(1,5),(1,6),(5,0),(5,1),(5,2),(5,3),(5,4),(5,5),(5,6),(2,5),(3,4),(4,5)]               
        elif letter is 'X':matrix = [(1,0),(1,6),(2,1),(2,5),(3,2),(3,3),(3,4),(4,1),(4,5),(5,0),(5,6)]               
        elif letter is 'Y':matrix = [(1,0),(2,1),(4,1),(5,0),(3,2),(3,3),(3,4),(3,5),(3,6)]           
        elif letter is 'Z':matrix = [(1,0),(2,0),(3,0),(4,0),(5,0),(4,1),(3,2),(3,3),(3,4),(2,5),(1,6),(2,6),(3,6),(4,6),(5,6)]
        elif letter is ' ':matrix = []
        elif letter is '!':matrix = [(3,1),(3,2),(3,3),(3,4),(3,6)]
        elif letter is '.':matrix = [(3,6)]
        elif letter is '?':matrix = [(2,1),(2,2),(3,0),(4,0),(5,1),(5,2),(4,3),(4,4),(4,6)]
        elif letter is '-':matrix = [(2,3),(3,3),(4,3),(1,3),(5,3)]
        elif letter is '+':matrix = [(2,3),(3,3),(4,3),(3,2),(3,4),(3,1),(3,5),(1,3),(5,3)]
        elif letter is '0':matrix = [(3,2),(3,0),(4,0),(2,1),(2,2),(2,3),(2,4),(2,5),(5,1),(5,2),(5,3),(5,4),(5,5),(3,6),(4,6)]
        elif letter is '1':matrix = [(3,1),(3,6),(4,0),(4,1),(4,2),(4,3),(4,4),(4,5),(4,6),(5,6)]
        elif letter is '2':matrix = [(2,1),(2,5),(2,6),(3,0),(3,4),(3,6),(4,0),(4,3),(4,6),(5,1),(5,2),(5,6)]
        elif letter is '3':matrix = [(2,1),(2,5),(3,0),(3,3),(3,6),(4,0),(4,3),(4,6),(5,1),(5,2),(5,4),(5,5)]
        elif letter is '4':matrix = [(2,0),(2,1),(2,2),(2,3),(3,3),(4,1),(4,2),(4,3),(4,4),(4,5),(4,6),(5,3)]
        elif letter is '5':matrix = [(2,0),(2,1),(2,2),(2,3),(2,6),(3,0),(3,3),(3,6),(4,0),(4,3),(4,6),(5,0),(5,4),(5,5)]
        elif letter is '6':matrix = [(2,1),(2,2),(2,3),(2,4),(2,5),(3,0),(3,3),(3,6),(4,0),(4,3),(4,6),(5,1),(5,4),(5,5)]
        elif letter is '7':matrix = [(2,0),(3,0),(4,0),(5,0),(5,1),(5,2),(5,3),(5,4),(5,5),(5,6)]
        elif letter is '8':matrix = [(3,0),(4,0),(2,1),(2,2),(2,4),(2,5),(3,3),(3,6),(4,3),(4,6),(5,1),(5,2),(5,4),(5,5)]
        elif letter is '9':matrix = [(2,1),(2,2),(2,5),(3,0),(3,3),(3,6),(4,0),(4,3),(4,6),(5,1),(5,2),(5,3),(5,4),(5,5)] 
        else:matrix = []
        return matrix


    def outputlogo(content,foreletter='#',backletter=' '):
        printlogo(content,foreletter,backletter)
           
            
        
    if (foreletter != '') and (backletter != ''):
        outputlogo(content,foreletter=foreletter,backletter=backletter)
    elif foreletter != '' :
        outputlogo(content,foreletter)
    elif backletter != '':
        outputlogo(content,backletter)
    else:
        outputlogo(content)
    


if __name__ == "__main__":
    main()

