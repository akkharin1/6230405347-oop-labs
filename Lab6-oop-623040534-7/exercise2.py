list = [2, 123.4567, 10000, 12345.67]
list.sort()
a = list[1]
b = list[2]
c = list[3]
for file in list:
    if file < 10:
        file_name = "file_00"  + str(file)
floating = "{0:6.2f}".format(a)
scientific_notation = format(b, "10.2e")
significant_figures = format(c,"10.2e")

print('{}:  {}, {}, {}'.format(file_name, floating, scientific_notation, significant_figures ))