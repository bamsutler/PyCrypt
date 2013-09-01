
###
# StBot Base 64 Coder
#
#       Filename: stbot64_coder
#       Author:   StBot
#       Date:     June 27, 2013
#       Version:  1.0
#
###
# Revisions
#       6/27/13
#        1. better  documentation
#        2. updated to work with the new stbot64_core
#        3. fixed the encoder to work with a key entry
#        4. Full rewrite ready for full testing.
#      
#       
#       
###
#       TODO S and FIXME S
#      
#       TODO Build repeating key xor decode that reaaaas from a key file and 
#       comapairs results with an english text dic (en_words)
#       
#
##################################################################################
import stbot64_core


def decode(bstring,flag = 0):
    """Decode, when flag is set to 0 takes a Base64 string and converts it to english plain test. when flag is set to 1 the input string is already in hex format."""
    declist = []
    outstring = ''
    if flag ==0:
        declist = stbot64_core.hex_to_dec(stbot64_core.base_to_hex(bstring))
    elif flag == 1:
        declist = stbot64_core.hex_to_dec(bstring)
    for x in declist:
        outstring += ""+chr(x)
    return outstring

def encode(ascstring,key = None):
    """Given an ascii english string of text with any quotes properly escaped this will encode it into a Base64 string."""
    outlist = []
    if type(key) is str:
        if len(key)<len(ascstring):
            ascstring = stbot64_core.ascii_to_hex(ascstring)
            key = keylen(stbot64_core.ascii_to_hex(ascstring),stbot64_core.ascii_to_hex(key))   
            value = stbot64_core.hex_to_base(hexorsum(ascstring,key))
    else:
        for x in ascstring:
            outlist.append(ord(x))
            value = stbot64_core.hex_to_base(''.join(stbot64_core.dec_to_hex(outlist)))
    return value

def hexorsum(hexstring1, hexstring2):
    """Calculates the Xor sum of 2 equal length hex strings"""
    binlist1 = []
    binlist2 = []
    binstring1 = stbot64_core.hex_to_bin(hexstring1)
    binstring2 = stbot64_core.hex_to_bin(hexstring2)
    for x in binstring1:
        binlist1.append(x)
    for x in binstring2:
        binlist2.append(x)
    sumlist = []
    sumstring = ''
    for x in range (len(binlist1)):
        if binlist1[x] == binlist2[x]:
            sumlist.append('0')
        elif binlist1[x] != binlist2[x]: 
            sumlist.append('1')
    sumstring = ''.join(sumlist)
    print "sum string" + str(stbot64_core.bin_to_hex(sumstring))
    return stbot64_core.bin_to_hex(sumstring)
  
def keylen(hexstring, key):
    """ Function to Take a hex key of x length and make its lenght == the length of the hex string passed. only the new hex key string is returned
    convertions to hex should be done in calling functions."""
    #key = stbot64_core.ascii_to_hex(key)   repkeyxor_encoder calls this conversion already
    while len(hexstring) != len(key):
        if len(key)>len(hexstring):
            key = key[:len(key)-1]
        if len(key)<len(hexstring):
            key+=key
    return key


def repkeyxor_encoder(text, key):
    """ xors a ascii string against a repaeted key. """
    text = stbot64_core.ascii_to_hex(text) # turns ascii to a hex string here
    key = stbot64_core.ascii_to_hex(key) # turns the key to hex
    if len(key) != len(text): # if the key is not the same length as the hexstring sends it to the keylen method to add or subtract chars.
        key = keylen(text,key)
    return hexorsum(text,key)
    
    
