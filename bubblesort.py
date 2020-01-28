def bubble_sort(list): 
    for i, num in enumerate(list): 
        try: 
            if list[i+1] < num: 
                list[i] = list[i+1] 
                list[i+1] = num 
                bubble_sort(list) 
        except IndexError: 
            pass
    return list
  
list = [64, 34, 25, 12, 22, 11, 90] 
bubble_sort(list) 
  
print("Sorted array:"); 
for i in range(0, len(list)):
    print(list[i], end=' ') 