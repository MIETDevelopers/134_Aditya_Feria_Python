'''Purpose:Program to print all positive numbers in a range
'''
st = int(input("Enter the starting range :"))
en = int(input("Enter the ending range :"))
for i in range(st, en + 1):
    if i >= 0:
        print(i, end = " ")