def main(s):
    """
    A string of numbers is given. Find how many odd digits there are and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    
s='123456789'
n=len(s)
c=0
i=0
while n!=i:
    if int (s[i])%2==1:
        c+=1
    i+=1
print(c)
    
    
