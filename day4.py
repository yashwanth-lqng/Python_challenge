n=int(input("Enter number of entries: "))
nums_and_strings = [0] * n
number_of_strings=0
number_of_nums=0
for i in range(n):
    str = input("Enter a data: ")
    if str.isdigit():
        nums_and_strings[i] = int(str)
    else:
        nums_and_strings[i] = str
nums_list = []
strings_list = []
for item in nums_and_strings:
    if type(item) == int:
        nums_list.append(item)
        number_of_nums+=1
    else:
        if len(item)>0:
            strings_list.append(item)
            number_of_strings+=1

print("Numbers: ", nums_list)
print("Strings: ", strings_list)

print("B) Length of my name 'Yashwanth' is 9(odd): (So last elements of both the lists will be removed)")
if(len(nums_list)>0):
    last_element=nums_list[len(nums_list)-1]
    nums_list.remove(last_element)
if(len(strings_list)>0):
    last_element=strings_list[len(strings_list)-1]
    strings_list.remove(last_element)

print("Numbers: ", nums_list)
print("Strings: ", strings_list)
print("Number of nums: ", number_of_nums)
print("Number of strings: ", number_of_strings)