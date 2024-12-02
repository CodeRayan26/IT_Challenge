input = "input02.txt"


# def isSafe(arr):
#     asc = arr[0] < arr[1]
#     if arr[0] == arr[1]:
#         return False
#     if(asc):
#         for i in range(0,len(arr)-1):
#             if not(arr[i] < arr[i+1] and 1 <= (arr[i+1] - arr[i]) <= 3):
#                 return False
#     else:
#         for i in range(0,len(arr)-1):
#             if not(arr[i] > arr[i+1] and 1 <= (arr[i] - arr[i+1]) <= 3):
#                 return False
            
#     return True

def isSafe(arr):
    
    asc = arr[0] < arr[1]
    if arr[0] == arr[1]:
        return False
    if(asc):
        for i in range(0,len(arr)-1):
            if not(arr[i] < arr[i+1] and 1 <= (arr[i+1] - arr[i]) <= 3):
                return False
                
    else:
        for i in range(0,len(arr)-1):
            if not(arr[i] > arr[i+1] and 1 <= (arr[i] - arr[i+1]) <= 3):
                return False
    return True

def verify(arr):
    for k in range (0,len(arr)):
        tmp = []
        for i in range(0,len(arr)):
            tmp.append(arr[i])
        tmp.pop(k)
        if isSafe(tmp):
            return True
    return False


def countSafe(file):
    count = 0
    with open(file,"r") as input:
        for line in input:
            numbers = line.split()
            reports = []
            for i in range(0,len(numbers)):
                reports.append(int(numbers[i]))
            if isSafe(reports) or verify(reports):
                count = count + 1
            
    return count


# print(f"number of safe reports is : {countSafe(input)}")

print(f"number of safe with tolerance is: {countSafe(input)}")


    




