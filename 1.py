Python 3.11.3 (tags/v3.11.3:f3909b8, Apr  4 2023, 23:49:59) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> if __name__ == '__main__':
...     n = int(input())
...     student_marks = {}
...     for _ in range(n):
...         name, *line = input().split()
...         scores = list(map(float, line))
...         student_marks[name] = scores
...     query_name = input()
... output = list(student_marks[query_name])    
... per = sum(output)/len(output);
