import math

def Bin_Search(arr, value):
    '''
    Takes list and a search value as arguments, searches list for value using the Binary search algorithm   
    '''
    if value not in arr:
        print('Number not in list')
    else: 
        for val in range(0, len(arr)):
            arr.sort()
            mid = math.floor(len(arr)/2)
            if arr[mid] == value:
                print("Found")
                break
            elif arr[mid] < value:
                arr = arr[mid:]
                return Bin_Search(arr, value)
            elif arr[mid] > value:
                arr = arr[:mid]
                return Bin_Search(arr, value)
        





        