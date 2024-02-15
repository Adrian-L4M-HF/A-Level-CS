"""Sorting Algorithms"""

def bubble_sort(numbers):
    """Pairs of items are sorted, larger item bubble up"""
    n = len(numbers)
    for i in range(n-1):
        for j in range(n-i-1):
            if numbers[j] > numbers[j+1]:
                numbers[j],numbers[j+1] = numbers[j+1],numbers[j]
    return numbers

def merge_sort(merge_list):
    """items are split into singlr items, then merge into sorted pairs"""
    if len(merge_list) > 1:
        middle_value = len(merge_list) // 2 # Integer division
        # Split up into single items
        left_half = merge_list[:middle_value] 
        right_half = merge_list[middle_value:]
        merge_sort(left_half)
        merge_sort(right_half)
        # Merge into sorted pairs
        i = 0 #left counter
        j = 0 #right counter
        k = 0 #merge_list item counter
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                merge_list[k] = left_half[i]
                i += 1
            else:
                merge_list[k] = right_half[j]
                j += 1
            k += 1
        """check for any unmerged elements on left half"""
        while i < len(left_half): 
              merge_list[k] = left_half[i]
              i += 1
              k += 1
        """check for any unmerged elements on right half"""
        while j < len(right_half): 
              merge_list[k] = right_half[j]
              j += 1
              k += 1
    return merge_list

def tests():           
    numbers1 = [12,6,9,5,8,0,-6]
    numbers2 = [5,3,2,7,24,1,3,-7]
    char = ["John", "Brown", "Cat", "Def", "Cal", "Broad", "Kio", "Jo"]
    
    print(f"{bubble_sort(numbers1) = }")
    print(f"{merge_sort(numbers1) = }")
    print(f"{bubble_sort(numbers2) = }")
    print(f"{merge_sort(numbers2) = }")
    
    print(char)
    print(merge_sort(char))
     
tests()

