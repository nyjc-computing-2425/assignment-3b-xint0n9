stdform = input('Enter a number in scientific notation: ')
stdform = stdform.strip()
print('This number in E notation is', stdform.replace('x10^','E')+'.')