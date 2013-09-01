###############################################################################
import b64_mod
from binascii import unhexlify

###############################################################################
def decode(bstring,flag = 0):
    """Decode, when flag is set to 0 or not set takes a Base64 strig and converts it to english plain test. when flag is set to 1 the input string is already in hex format."""
    declist = []
    outstring = ''
    if flag ==0:
        declist = b64_mod.hextodec(b64_mod.basetohex(bstring))
    elif flag == 1:
        declist = b64_mod.hextodec(bstring)
    for x in declist:
        outstring += ""+chr(x)
    return outstring

##############################################################################    
def encode(ascstring, key=None):
    """Given an ascii english string of text with any quotes properly escaped this will encode it into a Base64 string."""
    if key!=None:
        if len(key)<len(ascstring):
            key = keylen(b64_mod.ascitohex(ascstring),key)    
    outlist = []
    for x in ascstring:
        outlist.append(ord(x))
    return b64_mod.hextobase(''.join(b64_mod.dec_to_hex(outlist)))
##############################################################################
def hexorsum(hexstring1, hexstring2):
    """Calculates the Xor sum of 2 equal length hex strings"""
    binlist1 = []
    binlist2 = []
    binstring1 = b64_mod.hextobin(hexstring1)
    binstring2 = b64_mod.hextobin(hexstring2)
    for x in binstring1:
        binlist1.append(x)
    for x in binstring2:
        binlist2.append(x)
    sumlist = []
    sumstring = ''
    #print len(binlist1)
    #print len(binlist2)
    for x in range (len(binlist1)):
        if binlist1[x] == binlist2[x]:
            sumlist.append('0')
        elif binlist1[x] != binlist2[x]: 
            sumlist.append('1')
    sumstring = ''.join(sumlist)
    return b64_mod.bintohex(sumstring)
##############################################################################   
def keylen(hexstring, key, flag =0):
    if flag == 0:
        key = b64_mod.ascitohex(key)
    while len(hexstring) != len(key):
        if len(key)>len(hexstring):
            key = key[:len(key)-1]
        if len(key)<len(hexstring):
            key+=key
    return key
##############################################################################

def repkeyxor_encoder(text, key):
    text = b64_mod.ascitohex(text)
    if len(key)<len(text):
        key = keylen(text,key)
    return hexorsum(text,key)
    
    
