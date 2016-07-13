import re
def matchs(str,allow):
    for part in allow:
        if(re.match(part,str)!=None): return True
    return False