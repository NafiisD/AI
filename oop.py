# Case 1
def check_even_odd(n):
    return f"The number is{' Even' if n%2 ==0 else ' Odd'}"

print(check_even_odd(4))
print(check_even_odd(7))

# Case 2
def pos_neg_zer(m):
    return f"The number is{' Positive' if m > 0 else ' Negative' if m < 0 else ' Zero'}"

print(pos_neg_zer(10))
print(pos_neg_zer(-10))
print(pos_neg_zer(0))

# Case 3
def anagrams(string1, string2):
    return sorted(string1) == sorted(string2)

print(anagrams("eat", "tea"))
print(anagrams("sleep", "list"))

# Case 4
def factorial(f):
    return 1 if f == 0 else f * factorial(f - 1)

print(factorial(6))
print(factorial(0))

# Case 5
def palindrome(s):
    return s == s [:: - 1]

print(palindrome("racecar"))
print(palindrome("tobot"))
print(palindrome("phyton"))

# Case 6
def i_armstrong(num):
    digits = str(num)
    n = len(digits)
    total = sum(int(d) ** n for d in digits)
    return total == num

print(i_armstrong(153))
print(i_armstrong(370))
print(i_armstrong(123))

# Case 7
class BankAccount:
    def __init__(self, name):
        self.name = name
        self.balance = 0  # saldo awal

    def deposit(self, amount):
        if amount >= 0:
            self.balance += amount
            return f"Deposited {amount}. New balance: {self.balance}"
        else:
            return "Invalid deposit amount"

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return f"Withdrew {amount}. New balance: {self.balance}"
        else:
            return "Invalid withdrawal amount or insufficient funds"


# Test
account = BankAccount("Name")
print(account.deposit(1000))   # Expected: Deposited 1000. New balance: 1000
print(account.withdraw(500))   # Expected: Withdrew 500. New balance: 500
print(account.deposit(1500))   # Expected: Deposited 1500. New balance: 2000
print(account.withdraw(600))   # Expected: Withdrew 600. New balance: 1400
print(account.withdraw(2000))   # Expected: Invalid withdrawal amount or insufficient funds

# Case 8
class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def addGrade(self, grade) :
        self.grades.append(grade)
        return f"Grade {grade} added."
    
    def getAverage(self) :
        return f"Average Grade: {sum(self.grades)/len(self.grades):.if}" if self.grades else "No Grades Available"
    
# Test
student = Student("Alice")
print(student.addGrade(100))
print(student.addGrade(100))
print(student.addGrade(90))
print(student.getAverage())

