def find_two_smallest(numbers):
    
    if len(numbers) < 2:
        raise ValueError("List must contain at least two elements")
 
    # Скопируем список, чтобы не портить исходный
    nums = numbers.copy()
    nums.sort()
    return nums[0], nums[1]