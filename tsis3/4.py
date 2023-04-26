 
def prime(x):
    prime_list = []
    for i in x:
        if i == 0 or i == 1:
            continue
        else:
            for j in x(2, x.length-1):
                if i % j == 0:
                    break
            else:
                prime_list.append(i)
    return prime_list
 
# Driver program
list1=list(map(int, input().split()))
prime(list1)