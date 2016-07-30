from student import *


class DainfoParser:
    def __init__(self,html):
        self.html_doc = html

    def get_students_schedule(self):
        schedules = []
        first_index = 0
        student_list = []
        while True:
            # Parse into lines including a student's name and schedule
            first_index = self.html_doc.find('<P class="headline">', first_index)
            if first_index == -1:
                break
            second_index = self.html_doc.find('</table>', first_index + 1)
            schedules.append(self.html_doc[first_index:second_index])
            first_index = second_index + 1

        # print schedules[1]
        for schedule_string in schedules:
            # Parse student's name
            name = schedule_string[
                   schedule_string.find('<P class="headline">') + len(
                       '<P class="headline">'):schedule_string.find('</p>')]
            curr_student = Student(name)
            first_index = 0

            # Parse courses in a student
            for x in range(0, 7):
                first_index = schedule_string.find('<td>',
                                                   first_index + 1) + len(
                    '<td>')
                second_index = schedule_string.find('</td>', first_index)
                course = schedule_string[first_index:second_index]
                first_index = second_index + 1
                course = course[course.find('"displayOnPrint">') + len(
                    '"displayOnPrint">'):course.find('</a>')]
                if course == '            ' or course == '                      ':
                    course = ''
                curr_student.add_course(x, course)
            student_list.append(curr_student)
            #print curr_student
        return student_list
