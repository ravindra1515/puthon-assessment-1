'''8.Output dictionary which contains only the odd numbers that are present in the input list as keys and their cubes as values using List Comprehension'''
input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_cube_dict = {num: num**3 for num in input_list if num % 2 != 0}
print(odd_cube_dict)
print("PROGRAM 8 COMPLETED")