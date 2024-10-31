
import string
def main(s):
    """A variable of type str is given. Find and return how many consonant letters there are.
    Args:
        s: str
        consonant: other than vowels(a, e, i, o, u)
    Returns:
        int: return answer
    """

s='Itmarkaz'
un='aieou'
n=len(s)
i=0
c=0
while i!=n:
    if s[i].lower() not in un:
       c+=1
    i+=1
print(c)

    
