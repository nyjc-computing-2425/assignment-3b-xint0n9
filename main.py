stdform = input('Enter a number in scientific notation: ')
stdform = stdform.strip()
m, e = stdform.split('x10^')
print('This number in E notation is', m+'E'+e+'.')