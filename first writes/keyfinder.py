

import b64cy
import b64_mod
import en_word
import grouper


def keyfreq(filename , flag = 0):
    if flag == 0:
        canadateList = []
        thefile = open(filename)
        linenumber = 0
        total = 0
        greatestvalL = []
        greatestnumber = 0
        greatestnumberL = []
        glinenumberL = []
        for eachline in thefile:
            #print eachline
            linenumber+=1
            charcountmap = {}
            charstring = b64cy.decode(eachline.strip(),1)
            #print charstring
            for x in charstring:
                #print x
                if charcountmap.has_key(x):
                    count = charcountmap[x]
                    count +=1
                    charcountmap[x] = count
                else:
                    charcountmap[x] = 1
                #print charcountmap
            topval = ''
            number = 0
            for x,i in charcountmap.iteritems():
                if i>number:
                    number = i
                    topval = x
            if number>=greatestnumber:
                greatestnumberL.append(number)
                greatestnumber = number 
                greatestvalL.append(topval)
                glinenumberL.append(linenumber)
                canadateList.append(eachline.strip())
            total += number
        
    elif flag == 1:         #when flag is 1 we are not reading a file
        charcountmap = {}
        testname = b64cy.decode(filename,1)
        print testname
        for x in testname:
            print x
        return 00
    return canadateList,greatestvalL,glinenumberL
    # in this return canadateList is a list containing all the values out of the file that qualified as haveing a greatest occuring charicter.
    # the order they are listed in should corispond to the other lists.
    # the greatestvalL is what the symbol is and the glinenumberL is the number of the line that this occors on



def getkeylist(val):
    """generates a list of possible keys based on the ' etaoinshr' string  of most frequent values in english sentences"""
    COMMON_CHAR_STRING = " etaoinshr"
    keylist = []
    for x in COMMON_CHAR_STRING:
        decx = ord(x)
        hexx = b64_mod.dec_to_hex(decx,False)  #Flase passed for single char convertion
        char = b64_mod.dec_to_hex(ord(val),False) #Flase passed for single char convertion
        keylist.append(b64cy.hexorsum(hexx,char))   
    return keylist
    
def find(filename):
    canlist,val,line = keyfreq(filename)
    indexer = -1
    loop_controler = 0
    vallist = []
    found = 0 
    while len(canlist)>loop_controler:
        if found == 1:
            break
        print "Line number: " + str(line[indexer])
        print "Target hex: " + str(canlist[indexer])
        keys = getkeylist(val[indexer])
        print "Keys to be tested:  " + str(keys)
        print "*********************************************"
        for x in keys:
            vallist.append(b64cy.decode(b64cy.hexorsum(canlist[indexer],b64cy.keylen(canlist[indexer],x,1)),1))
        for x in vallist:
            tocheck = x.split(' ')
            truecount = 0 
            for y in tocheck:
                if en_word.is_english_word(y) == "true":
                    truecount +=1
            if truecount > 3:
                found  = 1 
                print str(keys[loop_controler])+ "  " + str(x)
                break    
        indexer-=1
        loop_controler +=1    
# This is the code i used to dycript the hex message in the email. 'X' was 
###1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736
   # the hex code from the e-mail decoded this reads "Cooking MC's like a pound 
#of bacon"
   # b64cy.decode(b64cy.hexorsum(var,b64cy.keylenmatcher(var,'X')),1)
    
def repxor_key_finder(filename):
    document = open (filename)  
    thisline = document.readline()
    thisline = b64_mod.basetohex(thisline.strip())
    
    lowest_list, size_list = correct_size(thisline)
    for x in size_list:
        print 'Size List' + str(x)
        codedBlocks = grouper.chunks(thisline,x) #FIXME here x can be passd as a odd number. this breaks hex_to_dec in keyfreq
        for x in codedBlocks:
            keyfreq(x,1)
    document.close()
    
def hamm_calc(string1,string2):
    answer = b64cy.hexorsum(string1,string2)
    answer = b64_mod.hextobin(answer)
    hamm = 0
    for x in answer:
        hamm += int(x)
    return hamm

def correct_size(text_string):
    lowest_list = []
    current_lowest = 100
    size_list = []
    for x in range(2,40,1):
        #print x
        keylist = grouper.chunks(text_string,x)
        #print keylist
        newval = hamm_calc(keylist[0],keylist[1])/x
        if newval<current_lowest:
            lowest_list.append(newval)
            size_list.append(x)
            current_lowest = newval
    return lowest_list, size_list
