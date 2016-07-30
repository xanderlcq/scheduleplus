class Student():
    def __init__(self, name):
        self.name = name
        self.schedule = ['', '', '', '', '', '', '']

    def add_course(self, period, course_name):
        assert 7 > period >= 0
        if course_name == '':
            self.schedule[period] = 'free'
        else:
            self.schedule[period] = course_name

    def get_course(self, period):
        return self.schedule[period-1]

    def get_schedule(self):
        return self.schedule

    def get_schedule_json(self):
        pass

    def get_frees(self):
        frees = [self.name]
        for index in range(len(self.schedule)):
            if self.schedule[index]=='free':
                frees.append(str(index))
        return frees

    def __str__(self):
        schedule_string = self.schedule.__str__()
        return 'name: ' + self.name + ', schedule: '+ schedule_string

