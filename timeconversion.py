import math
import os
import re
import sys

def timeConversion(s):


    hh=re.split('(\d+)',s)

    j=hh[6]


    if j=="PM" and int(hh[1])==12:
        return ("{}:{}:{}".format(hh[1],hh[3],hh[5]))

    elif j=="PM" and  int(hh[1]) <=12:
        hi=int(hh[1])+12
        l=hh[3]
        h=hh[5]
        return ("{}:{}:{}".format(hi,l,h))
    elif j=="AM" and int(hh[1]) ==12:
        return("00:{}:{}".format(hh[3],hh[5]))


    elif j=="AM" and int(hh[1]) <=12:
        
        return ("{}:{}:{}".format(hh[1],hh[3],hh[5]))
