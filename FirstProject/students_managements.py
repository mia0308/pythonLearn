"""
学生管理系统
展示系统功能
用户不退出可一直操作
添加学生姓名和学号  字典{学号：姓名}如果有其他更多信息，[{姓名：123，年龄：12，班级：01},{}]
删除
修改
查询
展示所有学生
"""

students = {}


def showMenu():
    """
    展示系统功能
    :return:
    """
    print('*'*10, '学生系统管理系统', '*'*10)
    print('1.添加学生信息')
    print('2.删除学生信息')
    print('3.修改学生信息')
    print('4.查询学生信息')
    print('5.查看所有学生信息')
    print('6.退出操作系统')
    print('*' * 34)


def addStu():
    """
    添加一个学生，提供学生姓名学号，学号唯一
    :return:
    """
    name = input('请输入学生姓名:')
    stuId = input('请输入学生学号（学号必须唯一）:')
    exist = True
    while exist:
        if stuId in students.keys():
            stuId = input('该学生已存在，请重新输入：')
        else:
            exist = False
    students[stuId] = name
    print('添加成功')


def deleteStu():
    stuId = input("请输入删除学生学号：")
    if stuId in students:
        students.pop(stuId)
        print('删除成功')
    else:
        print('该学号不存在')


def modifyStu():
    stuId = input('请输入修改学生学号：')
    if stuId in students:
        newName = input('请输入新姓名：')
        students[stuId] = newName
        print('修改成功')
    else:
        print('该学号不存在')


def showStu():
    stuId = input('请输入查询学生学号：')
    if stuId in students:
        print(stuId+':'+students[stuId])
    else:
        print('该学号不存在')


def showAllStu():
    print('当前系统中有以下学生：')
    for stuId in students:
        print(stuId+':'+students[stuId])


if __name__ == '__main__':  # 当前文件__name__=__main__;其他文件引用本文件时__name__=本文件名称，studen_management

    while True:
        showMenu()  # 展示
        num = int(input('请选择执行操作：'))
        if num == 1:
            addStu()
        elif num == 2:
            deleteStu()
        elif num == 3:
            modifyStu()
        elif num == 4:
            showStu()
        elif num == 5:
            showAllStu()
        elif num == 6:
            print('退出操作')
            break
        else:
            print('选择功能不存在，请重新选择')
