def main(s):
    """
    A string of numbers is given. Find how many even digits there are and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    
s='12345678'
n=len(s)
i=0
c=0
while i!=n:
    if int (s[i])%2==0:
        c+=1
    i+=1
print (c)
  
      
 
    
    
    
    