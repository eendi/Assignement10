
from finder import find_two_smallest
import data_lists
 
lists = [
    ("list1", data_lists.list1),
    ("list2", data_lists.list2),
    ("list3", data_lists.list3),
    ("list4", data_lists.list4),
]
 
with open("result.txt", "w", encoding="utf-8") as f:
    for name, numbers in lists:
        smallest1, smallest2 = find_two_smallest(numbers)
        line = f"{name}: {smallest1}, {smallest2}\n"
        f.write(line)
 
print("Results have been written to result.txt")