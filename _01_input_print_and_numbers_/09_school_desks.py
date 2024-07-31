
# Reads the number of students in three classrooms and prints the minimum number of desks needed, where each desk seats two students.

a, b, c = int(input()),int(input()),int(input())
print((a+1)//2 + (b+1)//2 + (c+1)//2)
