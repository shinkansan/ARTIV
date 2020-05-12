def read_data(file_name):

	data_list = []

	with open(file_name, "rt") as f:
		file_contents = f.read()

	data = file_contents.splitlines()
	n = len(data)
	for i in range(1,n):
		temp_list = data[i].split(",")
		temp_list1 = temp_list[6:9]
		data_list.append(temp_list1)
	return data_list

data = read_data('cordinate.txt')
print(data)
