student_details={'names':['Rishan','Advait','Ted','Sebastian','MK','Yajat','Hunter','Sankeerthan','Amudhan','Lucas'],
'maths':[97,99,98,74,54,93,91,89,86,91],
'science':[92,98,93,68,60,88,84,90,85,96],
'english':[98,98,98,82,57,95,89,90,83,87]}
for i in range(10):
    avgscore=(int(student_details['maths'][i])+int(student_details['english'][i])+int(student_details['science'][i]))/3
    print(student_details['names'][i]+' : '+str(round(avgscore)))
def topper(a):
    highest=0
    hi=0
    for i in range(len(a)):  
        if a[i]>highest:
            highest=a[i]
            hi=i
    return hi       
print(f'The topper for maths is {student_details['names'][topper(student_details['maths'])]}')
print(f'The topper for english is {student_details['names'][topper(student_details['english'])]}')
print(f'The topper for science is {student_details['names'][topper(student_details['science'])]}')