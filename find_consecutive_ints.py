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
def find_consecutive_runs(in_array):
	if in_array == None: return None
	seq_len = 3
	out_array = []
	for i in range(0, len(in_array)-seq_len+1):
		if is_consecutive( in_array[i:i+seq_len] ):
			out_array.append(i)
	return out_array if len(out_array) > 0 else None

def run_test():
	assert (find_consecutive_runs([1,2,3]) == [0])
	assert (find_consecutive_runs([3,2,1]) == [0])
	assert (find_consecutive_runs(None) == None)
	assert (find_consecutive_runs([0]) == None)
	assert (find_consecutive_runs([1,2,1]) == None)
	assert (find_consecutive_runs([-1,0,1]) == [0])
	assert (find_consecutive_runs([-1,-2,-3]) == [0])
	assert (find_consecutive_runs([2,5,7,2,3,4]) == [3])
	assert (find_consecutive_runs([3,4,6,8,3,1]) == None)
	assert (find_consecutive_runs([1,2,3,4,5,6,7]) == [0,1,2,3,4])
	assert (find_consecutive_runs([1,2,3,5,10,9,8,9,10,11,7,8,7]) == [0,4,6,7])

run_test()
print "Passed all tests"
