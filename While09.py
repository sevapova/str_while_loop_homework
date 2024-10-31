def main(s):
    """
    A string of numbers is given. Find the sum of all the digits and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
s='12345678'
n=len(s)
c=0
i=0
while n!=i:
    if int (s[i]):
        c+=1
    i+=1
    
    