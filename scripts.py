"""
ADM Homework 1, Algorithmic Methods of Data Mining, Sapienza 2026/27
Adnan Malkani, matricola 15721951

Each section is a separate HackerRank submission.
Most of them read from standard input, so run one section at a time,
not the whole file.
"""

# ============================================================
# PROBLEM 1: PYTHON
# ============================================================

# === Introduction: Say "Hello, World!" With Python ===

print("Hello, World!")

# === Introduction: Python If-Else ===

if __name__ == '__main__':
    n = int(input().strip())
    
    if n % 2 != 0:
        print('Weird')
    elif n % 2 == 0 and n in range(2, 6): 
        print('Not Weird')
    elif n % 2 == 0 and n in range(6, 21): 
        print('Weird')
    elif n % 2 == 0 and n > 20:
        print('Not Weird')

# === Introduction: Arithmetic Operators ===

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    
print(a + b)
print(a - b)
print(a * b)

# === Introduction: Python: Division ===

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    
print(a//b)
print(float(a / b))

# === Introduction: Loops ===

if __name__ == '__main__':
    n = int(input())
    
for i in range(n):
    print(i*i)

# === Introduction: Write a function ===

def is_leap(year):
    leap = False
    
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 ==0:
                leap = True
            else:
                leap = False
        else:
            leap = True
    else:
        leap = False   
    return leap

year = int(input())
print(is_leap(year))

# === Introduction: Print Function ===

if __name__ == '__main__':
    n = int(input())
    
output = ''.join(str(i) for i in range(1, n + 1))

print(output)

# ---------- Basic Data Types ----------

# === Basic Data Types: List Comprehensions ===

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    print([[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if i + j + k != n])



# === Basic Data Types: Find the Runner-Up Score! ===

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    print(sorted(set(arr))[-2])

# === Basic Data Types: Nested Lists ===

if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])

    # 1. Extract all scores, remove duplicates with set(), and sort them
    scores = sorted(list(set([s[1] for s in students])))
    
    # 2. The second lowest score is at index 1 (index 0 is the lowest)
    second_lowest_score = scores[1]

    # 3. Find all names that have this second lowest score
    second_lowest_names = [s[0] for s in students if s[1] == second_lowest_score]
    
    # 4. Sort names alphabetically
    second_lowest_names.sort()

    # 5. Print each name on a new line
    for name in second_lowest_names:
        print(name)

# === Basic Data Types: Finding the percentage ===

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    average_marks = sum(student_marks[query_name]) / len(student_marks[query_name])
    print(f"{average_marks:.2f}")

# === Basic Data Types: Lists ===

if __name__ == '__main__':
    N = int(input())
    l = []
    for _ in range(N):
        command = input().split()
        
        if command[0] == 'insert':
            l.insert(int(command[1]), int(command[2]))
        elif command[0] == 'print':
            print(l)
        elif command[0] == 'remove':
            l.remove(int(command[1]))
        elif command[0] == 'append':
            l.append(int(command[1]))
        elif command[0] == 'sort':
            l.sort()
        elif command[0] == 'pop':
            l.pop()
        elif command[0] == 'reverse':
            l.reverse()

# === Basic Data Types: Tuples ===
# Not accepted on HackerRank: hash() output differs between Python versions

if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())


# ============================================================
# PROBLEM 2: ALGORITHMS
# ============================================================

# === Problem 2: Birthday Cake Candles ===

def birthdayCakeCandles(candles):
    max_height = max(candles)
    count = candles.count(max_height)
    return count

# === Problem 2: Number Line Jumps (kangaroo) ===

def kangaroo(x1, v1, x2, v2):
    # Write your code here
    if (x1 < x2 and v1 <= v2) or (x2 < x1 and v2 <= v1):
        return "NO"
    
    if v1 != v2:
        n = (x2 - x1) / (v1 - v2)
        if n >= 0 and n == int(n):
            return "YES"
    
    return "NO"

# === Problem 2: Viral Advertising (strange-advertising) ===

def viralAdvertising(n):
    # Write your code here
    shared = 5
    cumulative = 0
    
    for day in range(1, n + 1):
        liked = shared // 2  # floor division
        cumulative += liked
        shared = liked * 3  # next day's recipients
    
    return cumulative

# === Problem 2: Recursive Digit Sum ===

def superDigit(n, k):
    # Calculate sum of digits of n
    digit_sum = sum(int(d) for d in n)
    
    # Multiply by k to get the sum for the concatenated number
    total_sum = digit_sum * k
    
    # Find super digit recursively
    def find_super_digit(num):
        if num < 10:
            return num
        digit_sum = sum(int(d) for d in str(num))
        return find_super_digit(digit_sum)
    
    return find_super_digit(total_sum)

# === Problem 2: Insertion Sort - Part 1 ===

def insertionSort1(n, arr):
    # Write your code here
    e = arr[n - 1]
    
    # Iterate backwards through the sorted portion of the array
    for i in range(n - 2, -1, -1):
        if arr[i] > e:
            # Shift the larger element to the right
            arr[i + 1] = arr[i]
            print(' '.join(map(str, arr)))
        else:
            # Found the correct spot, insert the element
            arr[i + 1] = e
            print(' '.join(map(str, arr)))
            return
            
    # If the element is smaller than all others, it goes at the beginning
    arr[0] = e
    print(' '.join(map(str, arr)))

# === Problem 2: Insertion Sort - Part 2 ===

def insertionSort2(n, arr):
    # Write your code here
    # Start from the second element (index 1)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        
        # Shift elements greater than 'key' to the right
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
            
        # Insert 'key' in its correct sorted position
        arr[j + 1] = key
        
        # Print the array after each iteration
        print(' '.join(map(str, arr)))



