import numpy as np

# 1-----1D Array (Student IDs)
student_ids = np.array([101,102,103,104,105])
print("Student IDs:", student_ids)

# 2-----2D Array (Marks of students in 3 subjects)
# rows = students
# columns = subjects (Math, Science, English)

marks = np.array([
    [78,85,90],
    [88,79,92],
    [67,70,75],
    [90,91,89],
    [76,84,80]
])

print("\nStudent Marks Matrix:")
print(marks)

# 3---- Multidimensional Array (3D example)
data_3d = np.array([
    [[1,2],[3,4]],
    [[5,6],[7,8]]
])

print("\n3D Array:")
print(data_3d)

# 4---- Array Attributes
print("\nArray Attributes:")
print("Shape:", marks.shape)
print("Dimensions:", marks.ndim)
print("Total Elements:", marks.size)
print("Data Type:", marks.dtype)

# 5----- Aggregation Functions
print("\nAggregation Functions:")
print("Total Marks:", np.sum(marks))
print("Average Marks:", np.mean(marks))
print("Maximum Marks:", np.max(marks))
print("Minimum Marks:", np.min(marks))


# 7----- Slicing
print("\nSlicing Examples:")
print("First Two Students:\n", marks[0:2])
print("Only Math and Science columns:\n", marks[:,0:2])

# 8---- Filtering (Boolean Indexing)
print("\nFiltering Examples:")
high_scores = marks[marks > 85]
print("Marks greater than 85:", high_scores)

