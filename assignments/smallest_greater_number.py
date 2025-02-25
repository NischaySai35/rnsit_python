# my original NON-AI code--------------------------------------------------------------------------------------------------------------------------------------------------

input_no = input("Enter the number: ")
num = [i for i in input_no]

def is_true_des(num):
    num = [i for i in num]
    #print(num)
    if num == sorted(num, reverse=True):
        #print("true from des")
        return True
    #print("false from des")
    return False

def least(num, arr):
    arr = [int(i) for i in arr]
    #print(arr)
    arry = sorted(arr)
    for i in range(len(arr)):
        if arry[i] > num:
            return arr.index(arry[i])
    
    
for i in range(len(num)):
    if is_true_des(''.join(num[i:])):
        
        if i == 0:
            break

        elif i > 0:
            prev_no = int(num[i-1])
            req_list = num[i:]
            
            index = least(prev_no, req_list)
            #print("came back with index", index+i)
            tmp = num[index+i]
            num[index+i] = num[i-1]
            num[i-1] = tmp

            num[i:] = sorted(num[i:])
            break

#print(num)
number = ''
for i in num:
    number += i 

if number == input_no:
    print("Not Possible")
else:
    print(number, "is the next number that is just greater than", input_no, "when the digits are rearranged.")



# ChatGPT code that has just optimised MY original code------------------------------------------------------------------------------------------------------------------

# input_no = input("Enter the number: ")
# num = list(input_no)

# def is_descending(num):
#     return num == sorted(num, reverse=True)

# def find_least_greater(num, arr):
#     arr = sorted(arr)
#     for x in arr:
#         if x > num:
#             return x

# for i in range(len(num) - 1, 0, -1):
#     if num[i - 1] < num[i]:
#         req_list = num[i:]
#         least_greater = find_least_greater(num[i - 1], req_list)
        
#         index = num.index(least_greater, i)  
#         num[index], num[i - 1] = num[i - 1], num[index]
        
#         num[i:] = sorted(num[i:])
#         print("".join(num), "is the next number that is just greater than", input_no)
#         break
# else:
#     print("Not Possible")
