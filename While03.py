
import string
def main(s):
    """
    A variable of type str is given. Find how many punctuations it contains and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    p= string.punctuation
    n=len(s)
    i=0
    c=0
    while i!=n:
        
        if s [i] in p:
            c+=1
        i+=1
    return c

print (main(s="23245@#$%^!"))
    
         