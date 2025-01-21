import numpy as np

first  = np.array([[1,2,3,4,5,6]])

second = np.random.randint(10,19,[1,6],dtype=np.uint16)

third = np.random.randint(21,30,[1,6],dtype=np.uint16)



result = np.vstack([first, second, third]).T
npoints = 6

choice = np.random.choice(len(result), npoints, replace=True) # Create a list of random positions for the result_set

result_set = result[choice, :] # New point set with random index (Chosen from original)

mean_array = np.mean(result_set, axis=0) # Mean along all x, all y and all z (columns) of the random set
# print(f"Mean array: {mean_array.shape} \n{mean_array}")

expanded_array = np.expand_dims(mean_array, 0) # Establish a (1,3) dimmension instead of (3,)
print(f"Expanded array: {expanded_array.shape} \n{expanded_array}")

sub_result_set = result_set - expanded_array # Substract the mean to the random set
# print(f"Substracting mean: \n{sub_result_set}")

sum_squared = np.sqrt(np.sum(sub_result_set**2, axis=1)) # Adding each row (x+y+z)
print(f"Sum: \n {sum_squared}")

max = np.max(sum_squared, 0)
print(f"Max: {max}")

print(f"Result [Org], Shape: {result_set.shape}")
print(f"{result_set}")
#
# print(f"Choice, Shape: {choice.shape}")
# print(f"{choice}")
#
# print(f"Result_set, Shape: {result_set.shape}")
# print(f"{result_set}")

# point_set = pts[choice, :]

# point_set = point_set - np.expand_dims(np.mean(point_set, axis=0), 0)  # center
# dist = np.max(np.sqrt(np.sum(point_set ** 2, axis=1)), 0)
# point_set = point_set / dist  # scale



