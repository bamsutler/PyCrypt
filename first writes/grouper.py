from itertools import izip_longest

def grouper(iterable, n, fillvalue=None):
    """Collect data into fixed-length chunks or blocks"""
    # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx
    args = [iter(iterable)] * n
    return izip_longest(fillvalue=fillvalue, *args)
    #the return here is a tuple? what a pain in that arse

def chunks(s,n,z=None):
    output = []
    for start in range(0, len(s), n):
         output.append(s[start:start+n])
    return output
    