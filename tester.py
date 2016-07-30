from dainfo_data import *
from schedule_parser import *


dainfo_parsed = DainfoParser(html_doc)
students_schedules = dainfo_parsed.get_students_schedule()
#print len(students_schedules)

p1free=[]
p2free=[]
p3free=[]
p4free=[]
p5free=[]
p6free=[]
p7free=[]
frees = [[],[],[],[],[],[],[]]
for period in range(0,7):
    for student in students_schedules:
        #print student.get_frees()
        if str(period) in student.get_frees():
            frees[period].append(student.get_frees()[0])
for period in range(0,7):
    print '\n================\nThere are ' +str(len(frees[period])) + ' has ' + str(period+1) + ' free'
    print 'They are:\n'
    for name in frees[period]:
        print name