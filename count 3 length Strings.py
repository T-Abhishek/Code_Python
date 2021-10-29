
# Function to count possible number of strings

# such that each string consists of atleast

# 2 different characters of length 3

def countStrings(a, b, c) :

	# Array to store the 3 frequencies

	arr = [0]*3;

	arr[0] = a;

	arr[1] = b;

	arr[2] = c;

	# Total number of strings that can be

	# formed irrespective of the given

	# condition i.e, neglecting the condition

	# that each string consists of atleast 2

	# different characters of length 3

	count = (arr[0] + arr[1] + arr[2]) // 3;

	# Sort the array

	arr.sort();

	# If the sum of smallest and 2nd largest

	# element is less than the count, then

	# assign the sum to count

	if (arr[0] + arr[1] < count) :

		count = arr[0] + arr[1];

	# Return the count

	return count;

# Driver Code

if __name__ == "__main__" :

	a = 5; b = 4; c = 3;

	print(countStrings(a, b, c));

	# This code is contributed by AnkThon# Python3 implementation for the above approach

# Function to count possible number of strings

# such that each string consists of atleast

# 2 different characters of length 3

def countStrings(a, b, c) :

	# Array to store the 3 frequencies

	arr = [0]*3;

	arr[0] = a;

	arr[1] = b;

	arr[2] = c;

	# Total number of strings that can be

	# formed irrespective of the given

	# condition i.e, neglecting the condition

	# that each string consists of atleast 2

	# different characters of length 3

	count = (arr[0] + arr[1] + arr[2]) // 3;

	# Sort the array

	arr.sort();

	# If the sum of smallest and 2nd largest

	# element is less than the count, then

	# assign the sum to count

	if (arr[0] + arr[1] < count) :

		count = arr[0] + arr[1];

	# Return the count

	return count;

# Driver Code

if __name__ == "__main__" :

	a = 5; b = 4; c = 3;

	print(countStrings(a, b, c));

	# This code is contributed by AnkThon
