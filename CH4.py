#1.1分別寫出四個function可以印出字元'K', 'D', 'A', 'Y', 請使用迴圈寫

def k():
  for a in range(1, 8):
    if a <= 4:
       spaces = " " * (4 - a)
    elif a > 4:
       spaces = " " * (a - 4)
    print("*" + spaces + "*")
  else:
    print("\n")

def d():
    for b in range(1, 8):
        if b <= 4:
            spaces = " " * (b - 1)
        elif b > 4:
            spaces = " " * (7 - b)
        print("*" + spaces + "*")
    else:
        print("\n")

def a():
    for c in range(1, 7):
        spaces1 = " " * (6 - c)
        spaces2 = " " * ((c - 2) * 2 + 1)
        if c == 1:
            print(spaces1 + "*")
        elif c == 4:
            stars = "*" * ((c - 2)*2 + 1)
            print(spaces1 + "*" + stars + "*")
        else:
            print(spaces1 + "*" + spaces2 + "*")
    else:
        print("\n")

def y():
    for d in range(1, 8):
        if d <= 3:
            spaces1 = " " * (d - 1)
            spaces2 = " " * (8 - 2*d)
            print(spaces1 + "*" + spaces2 + "*")
        elif d > 3:
            spaces = " " * 3
            print(spaces + "*")
    else:
        print("\n")

k()
k()
d()
a()
y()

#1.2 多加一個function可以印出一棵聖誕樹

def tree(n):
  height = 11
  stars = 1
  for i in range(height):
    print((' ' * (height - i)) + ('*' * stars))
    stars += 2
    print((' ' * height) + '|')

tree(11)

#1.3 印個花樣多一點的聖誕樹

height = 12
quotation = 0
line = 18

for i in range(height):
   if i == 0 :
      print((' ' * (height -  i)) + ('[') + (']'))
   elif i >= 1 and i <= 8 :
      print((' ' * (height - i)) + ('[')+ ('~' * (quotation + (i * 2))) +(']'))
   elif i == 9 :
      print((' ' * (height - i)) + ('[')+ ('_' * line ) +(']'))
   elif i == 10 :
      print((' ' * (height - i)) + ('[]').center(20))
   else:
      print((' ' * (height - i)) + ('[]').center(22))

#2. 使用迴圈找出 300 以下的質數

def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

n = 300

for i in range(2, n + 1):
    i_is_prime = is_prime(i)
    if i_is_prime:
        print(i)

#3. 費氏數列, f(0)=0, f(1)=1, f(n)=f(n-1)+f(n-2),列出f(20)的完整費氏數列

def fi(n):
    if n == 0 or n == 1:
        return n
    else:
        return fi(n-1) + fi(n-2)
for i in range(0,21):
    print("f(%d)=%d" %(i,fi(i)))

#4. 四位數中，使用迴圈找出 0 ~ 7 所能組成的奇數個數

oddList = list()

for tho in range(0,8):
  for hun in range(0,8):
     for ten in range(0,8):
        for one in range(0,8):
           number = (1000 * tho) + (100 * hun) + (10 * ten) + one
           if number % 2 == 0:
              continue
           else:
              odd_number = str(tho) + str(ten) + str(one)
              oddList.append(odd_number)

print(oddList)