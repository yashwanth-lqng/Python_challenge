n=int(input("Enter the number of packages: "))
weights=[0]*n
for i in range(0,n) :
    weights[i]=int(input())
invalid_entries=[]
very_light=[]
normal_load=[]
heavy_load=[]
overload=[]

for w in weights :
    if w<=0:
        invalid_entries.append(w)
    elif w<=5:
        very_light.append(w)
    elif w<=25:
        normal_load.append(w)
    elif w<=60:
        heavy_load.append(w)
    else:
        overload.append(w)

print("Length of my name is 9(YASHWANTH) and 9%3=0.")
L=len("YASHWANTH")
PLI = L%3
print("So Rule A is implemented. Moving all Overload items to Invalid Entries.")

no_of_overload_items=len(overload)
for i in range(no_of_overload_items) :
    invalid_entries.append(overload[i])

print("Total Valid weights:",len(very_light)+len(normal_load)+len(heavy_load))
print("The affected items due to PLI is:",no_of_overload_items)
print("L(length of my name) and PLI(personalisation rule) are:",L,",",PLI)
print("Invalid weights:",invalid_entries)
print("Very light weight items:",very_light)
print("Normal load items:",normal_load)
print("Heavy load items:",heavy_load)
