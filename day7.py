n=int(input("Number of energy readings:"))
energy_readings=[0]*n
for i in range(n) :
    energy_readings[i]=int(input())

energy_usage={
    "invalid":[],
    "efficient":[],
    "moderate":[],
    "high":[]
}
for e in energy_readings :
    if e<0:
        energy_usage["invalid"].append(e)
    elif e<=50:
        energy_usage["efficient"].append(e)
    elif e<=150:
        energy_usage["moderate"].append(e)
    else:
        energy_usage["high"].append(e)

valid_readings=[x for x in energy_readings if x>=0]
total_consumption=sum(valid_readings)
number_of_buildings=len(valid_readings)
if len(energy_usage["high"])>3:
    efficiency_result="Overconsumption"
elif total_consumption>600:
    efficiency_result="Energy Waste"
elif abs(len(energy_usage["efficient"])-len(energy_usage["moderate"]))<=1:
    efficiency_result="Balanced Usage"
else:
    efficiency_result="Moderate Usage"

print(energy_usage)
print("Total Consumption: ",total_consumption)
print("Number of buildings: ",number_of_buildings)
print("Efficiency Result: ",efficiency_result)