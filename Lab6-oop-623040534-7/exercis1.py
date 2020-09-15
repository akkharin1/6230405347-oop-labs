filename = [2, 10, 11, 3]
pad_zero =list()
for file in filename:
    pad_zero.append("file_{:04d}".format(file))


print('{:<30s} {} '.format('input filename are',filename))
print('{:<30s} {} '.format('zero padded filenames', pad_zero))
filenames_sort = pad_zero
filenames_sort.sort()
print('{:<30s} {} '.format('sorted filenames are', filenames_sort))




