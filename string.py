def reverse(temple1):
    cock = temple1[::-1]
    return cock
temple1 = temple(input())
if len(temple1) <= 1000:
    
    print(reverse(temple1))

else:
    print("invalid")
