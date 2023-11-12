total = 0
hbs = []
lst = []
b = int(input("input angka->"))
for i in range(1, b+1):
    lst.append(i)
print(lst)
for i in lst :
            if i % 3 == 0:
                hbs.append(i)
                
total = sum(hbs)
print("total angka yang habis di bagi 3 = ",total)