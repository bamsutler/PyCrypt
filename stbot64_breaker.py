
###
# StBot Base 64 Coder
#
#       Filename: stbot64_breaker
#       Author:   StBot
#       Date:     June 27, 2013
#       Version:  1.0
#
###
# Revisions
#
#     1. total over haul. better optimization and integration
#     
#      
#       
#       
###
#       TODO S and FIXME S
#      
#       
#       
#
##################################################################################
import stbot64_coder
import stbot64_core
import en_word

def finder(filename):
    """ This function takes a single xor encoded hex file and esxtrapalates the key 
    Then takes this key decodes the file and deturmines which line in the file is English text
    by compairing the decoded strings to an american english word dictionary"""
    thisfile = open(filename)
    filelinelist = []
    for eachline in thisfile:           #loop to read the file and put it in the list
        filelinelist.append(eachline.strip())
    canlist,val,line = key_freak(filelinelist)            # call to find the key frequency
    thisfile.close()
    indexer = -1
    loop_controler = 0
    vallist = []
    found = 0 
    while len(canlist)>loop_controler:
        if found == 1:
            break
        print "Line number: " + str(line[indexer])
        print "Target hex: " + str(canlist[indexer])
        print "current Value: " +str(val[indexer])
        keys = getkeylist(val[indexer])
        print "Keys to be tested:  " + str(keys)
        print "*********************************************"
        for x in keys:
            vallist.append(stbot64_coder.decode(stbot64_coder.hexorsum(canlist[indexer],stbot64_coder.keylen(canlist[indexer],x)),1))
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

def repxor_finder(filename):
    document = open (filename)
    linelist = []
    for eachline in document:
        linelist.append(eachline.strip())
    document.close()
    possible_sizelist = []
    lowhamm = 100
    for key_size in range(2,40,2):
        target = stbot64_core.chunks(stbot64_core.base_to_hex(linelist[0]),key_size)
        currenthamm = hamm_calc(target[0],target[1])/key_size
        #print currenthamm
        #print key_size
        if currenthamm <= lowhamm:
            lowhamm = currenthamm
            possible_sizelist.append(key_size) 
    #print possible_sizelist
    split_line_list = []
    for x in range(1,len(possible_sizelist)):
        for line in linelist:
            line = stbot64_core.base_to_hex(line)
            split_line_list.append(stbot64_core.chunks(line,possible_sizelist[-x]))
        print split_line_list    
        break
        #TODO So we have a list of lines that are broken into sizes =to the suspected keysize
        #now we have to find the key. this is sudgested to take byte 1 from every line and make a list
        #ie. [1234][1234][1234][1234][1234][1234] becomes [111111][222222][333333][444444] and then 
        #use the single xor cypher code.
        #TODO What i may end up doing here is building a document with the keys printed the testing eachone
        #useing the en_dict
        
def key_freak(linelist):
    print linelist
    canadateList = []
    linenumber = 0
    total = 0
    greatestvalL = []
    greatestnumber = 0
    greatestnumberL = []
    glinenumberL = []
    for eachline in linelist:
        #print eachline
        linenumber+=1
        charcountmap = {}
        charstring = stbot64_coder.decode(eachline,1)
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
        
    return canadateList,greatestvalL,glinenumberL
    
def getkeylist(val):
    """generates a list of possible keys based on the ' etaoinshr' string  of most frequent values in english sentences"""
    COMMON_CHAR_STRING = " etaoinshr"
    keylist = []
    for x in COMMON_CHAR_STRING:
        decx = ord(x)
        hexx = stbot64_core.dec_to_hex(decx,False)  #Flase passed for single char convertion
        char = stbot64_core.dec_to_hex(ord(val),False) #Flase passed for single char convertion
        keylist.append(stbot64_coder.hexorsum(hexx,char))   
    return keylist
    
def hamm_calc(string1,string2):
    """ Takes 2 hex inputs and calculated the hamming distance between them"""
    answer = stbot64_coder.hexorsum(string1,string2)
    answer = stbot64_core.hex_to_bin(answer)
    hamm = 0
    for x in answer:
        hamm += int(x)
    return hamm

def correct_size(text_string):
    """Takes the Strings and trys to find the correct size of the key based on the
    normalized hamming distances"""
    lowest_list = []
    current_lowest = 100
    size_list = []
    for x in range(2,40,2):
        #print x
        keylist = stbot64_core.chunks(text_string,x)
        #print keylist
        newval = hamm_calc(keylist[0],keylist[1])/x #devided my the current number to normalize.
        if newval<current_lowest:
            lowest_list.append(newval)
            size_list.append(x)
            current_lowest = newval
    return lowest_list, size_list