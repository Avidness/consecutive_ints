# Alan David Ness
# https://github.com/Avidness

# Returns an array of number differences between each pair in the sub_array
def get_diff(sub_array):
	diff = []
	for i in range(0, len(sub_array)-1):
		diff.append(sub_array[i] - sub_array[i+1])
	return diff

# Check whether the difference between the array elements are all 1 or -1
def is_consecutive(sub_array):
	diff = get_diff(sub_array)
	return all(x == 1 for x in diff) or all(x == -1 for x in diff)

# Check each sub_array of size seq_len
def find_consecutive_runs(in_array, seq_len):
	out_array = []	
	for i in range(0, len(in_array)-seq_len):
		if is_consecutive( in_array[i:i+seq_len] ):
			out_array.append(i)
	return out_array if len(out_array) > 0 else None

in_array = [1, 2, 3, 5, 10, 9, 8, 9, 10, 11, 7, 8, 7]
seq_len = 3
print find_consecutive_runs(in_array, seq_len)
