def convert_list_to_abs(list_string):
    abs_list_of_nums = [abs(float(el)) for el in list_string]
    return abs_list_of_nums


list_of_string = input().split()
abs_list = convert_list_to_abs(list_of_string)
print(abs_list)
