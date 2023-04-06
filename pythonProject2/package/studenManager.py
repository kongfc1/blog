# 11.1 魔法方法
# 不手动调用，会自动执行的方法 __str__  __init__
student_list = []
class student():
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def __str__(self):
        return 'name: %s score:%d' % (self.name, self.score)
class SystemManger():
    def __init__(self, version, name, author):
        self.version = version
        self.name = name
        self.author = author

    def showMwnu(self):
        print("欢迎光临%s %s" % (self.name, self.version))
        print("1,add student")
        print("2,show student")
        print("3,exit student")

    def addStudent(self, stu):
        student_list.append(stu)

    def showAllStudents(self):
        for stu in student_list:
            print(stu)
            print(stu.__str__())

    def systemExit(self):
        print('谢谢使用')
        exit()
if __name__ == '__main__':
    manager = SystemManger('v3.0', '学生管理系统', 'kongfc')
    while True:
        manager.showMwnu()
        choice = input("请选择1-3  ")
        if choice == '1':
            name = input('请输入姓名')
            score = int(input("请输入分数"))
            stu = student(name, score)
            manager.addStudent(stu)
        elif choice == '2':
            manager.showAllStudents()
        elif choice == '3':
            manager.systemExit()
        else:
            print("输入有误")
