def readRecords(filename):
    with open(filename, "r") as f:
        rows = f.readlines()[1:]
        lists = []
    for line in rows:
        line = line.rstrip("\n")
        fields = line.split(",")
        for i in range(len(fields)):
            if len(lists) <= i:
                lists.append([])
            lists[i].append(fields[i])
    return lists

            
def calcBMI(weight, height):
    weight = int(weight)
    height = int(height)
    return weight / height **2 * 703

    
result = readRecords('medrec.csv')

for i in result:
    weight = result[4]
    height = result[3]
    
l = len(height)
bmi_list = []
for i in range(l):
    bmis = calcBMI(weight[i], height[i])
    bmi_list.append(bmis)
    
marker = []
for bmi in bmi_list:
    if bmi > 30: marker.append("++")
    elif bmi > 25: marker.append("+")
    elif bmi < 18.5: marker.append("-")
    else: marker.append("")

output = (format('PersonID',"^8s"), format('BMI',"^5s"), format('Marker', "^6s"))
with open("bmi.txt", "w") as f:
    for i in output:
        f.write(i)
    f.write("\n")
    for j in range(len(result[0])):
        f.write("{0} \t {1} \t {2}".format(result[0][j], format(bmi_list[j], ".2f"), marker[j]) + "\n")
  
        
        



