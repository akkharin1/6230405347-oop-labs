tuple_1 = 1
tuple_2 = (2, 2)
tuple_3 = (3, 3, 3)
list_a = [tuple_1, tuple_2, tuple_3]
second_element_a = list_a[1]
second_sequence_a = second_element_a[1]

list_1 = list(range(0, 10))
list_2 = list(range(10, 20))
list_3 = list(range(20, 30))
list_4 = list(range(30, 40))
list_b = [list_1, list_2, list_3, list_4]
first_element_b = list_b[0]
last_two_elements = first_element_b[-2:]

print(second_sequence_a)
print(last_two_elements)
