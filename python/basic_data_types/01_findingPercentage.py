if __name__ == '__main__':
	n = int(input())
	student_marks = {}
	for i in range(n):
		name, *line = input().split()
		scores = list(map(float, line))
		student_marks[name] = scores
	query_name = input()
	marks = student_marks[query_name]
	total = sum(marks)
	avg = total / len(marks)
	r_avg = round(avg, 2)
	formatted_avg = "{:.2f}".format(r_avg)
	print(formatted_avg)