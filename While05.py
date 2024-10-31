def main(s):
    """
    A variable of type str is given. Find how many lowercase letters there are and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    return c

s='ASDFewrq12345'
n=len(s)
i=0
c=0
while i!=n:
    if s[i].islower():   
        c+=1
    i+=1
print(c)
