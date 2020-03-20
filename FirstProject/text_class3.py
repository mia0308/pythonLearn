class StudentInfo(object):
    classroom = 101
    address = 'Beijing'

    def __init__(self):
        print('新建学生信息')

    def print_classroom(self):
        print(self.classroom)


stu1 = StudentInfo()
print(stu1.classroom)
