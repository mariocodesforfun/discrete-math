

x = input('write an expression ')
y = None
x = x.split()
print(x)
if x[1] == '+':
   y = float(x[0]) + float(x[-1])
elif x[0] == '-':
   y = float(x[0]) - float(x[-1])
elif x[0] == '*':
   y = float(x[0]) * float(x[-1])
print(y)