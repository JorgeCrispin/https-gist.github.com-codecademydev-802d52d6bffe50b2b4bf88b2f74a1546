medical_data = \
"""Marina Allison   ,27   ,   31.1 , 
#7010.0   ;Markus Valdez   ,   30, 
22.4,   #4050.0 ;Connie Ballard ,43 
,   25.3 , #12060.0 ;Darnell Weber   
,   35   , 20.6   , #7500.0;
Sylvie Charles   ,22, 22.1 
,#3022.0   ;   Vinay Padilla,24,   
26.9 ,#4620.0 ;Meredith Santiago, 51   , 
29.3 ,#16330.0;   Andre Mccarty, 
19,22.7 , #2900.0 ; 
Lorena Hodson ,65, 33.1 , #19370.0; 
Isaac Vu ,34, 24.8,   #7045.0"""

# Add your code here
#print(medical_data)
#step 2 show insurance costs in dollars
updated_medical_data = medical_data.replace('#', '$')


#print(updated_medical_data)
#counts the number of records
num_records = 0
for num in updated_medical_data:
  if num == '$':
    num_records += 1
print("==================")
print("There are "+str(num_records)+" medical records in the data.")
#splitting medical data
medical_data_split = updated_medical_data.split(';')
#print(medical_data_split)
#still not readable new list called medical_records
medical_records = []
for record in medical_data_split:
  medical_records.append(record.split(','))
#print(medical_records)
# still not pretty, do a medical_records_clean
print("=======================")
medical_records_clean = []

for record in medical_records:
  record_clean = []
  for item in record:
    record_clean.append(item.strip())
  medical_records_clean.append(record_clean)

print(medical_records_clean)
print("======================")
#print the names in uppercase
for record in medical_records_clean:
  record[0] = record[0].upper()
  print(record[0])
print("============================")
names = []
ages  = []
bmis  = []
insurance_costs = []
for record in medical_records_clean:
  names.append(record[0])
  ages.append(record[1])
  bmis.append(record[2])
  insurance_costs.append(record[3])

print("Names: " + str(names))
print("Ages: " + str(ages))
print("BMI: " + str(bmis))
print("Insurance Costs: " + str(insurance_costs))

print("===============================")
#since the data is separate we can calculate now
total_bmi = 0

for num in bmis:
  total_bmi += float(num)
average_bmi = total_bmi/len(bmis)

print("Average BMI: "+ str(round(average_bmi,2)))
print("=====================")
#extra credit
#print(insurance_costs[0].strip('$'))
temp_insurance_cost = []
count = len(insurance_costs)
i = 0
while count > 0:
  temp_insurance_cost.append(insurance_costs[i].strip('$'))
  i += 1
  count -= 1
#print(temp_insurance_cost)
total = 0.0
for i in temp_insurance_cost:
  total += float(i)
print("=====================")
print("Average Cost: $" + str(total/len(insurance_costs)))
print("=======================")

count = 0
while count < 10:
  print(
     str(names[count]) + " is " +
     ages[count] + " years old with a BMI of " +
     bmis[count] + " and an insurance cost of " + 
     insurance_costs[count] + " ."
    )  
  count +=1



