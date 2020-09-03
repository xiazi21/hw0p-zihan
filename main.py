c = float(input("Enter temperature: "))
d=input('Enter unit in F/f or C/c: ')
if d=="C" or d=="c":
 f=(c*1.8)+32
 print('%.1f° in Celsius is equivalent to %.1f° Fahrenheit.'%(c,f))
elif d=="F" or d=="f":
 a=(c-32)/1.8
 print('%.1f° in Fahrenheit is equivalent to %.14f° Celsius.'%(c,a))
else:
  print('bad')
