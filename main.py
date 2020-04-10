'''

                            Online Python Interpreter.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

        
def solution(N):
    list1 = []
    list2 = []
    num = str(N)
    for i in num:
        list1.append(i)
    j = 0    
    while j <= len(list1):    
        list1.insert(j, '5')
        list3 = "".join(list1)
        list2.append(int(list3))
        del list1[j]
        j = j + 1
    print(max(list2))    

solution(268)        
