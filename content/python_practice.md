Title: 从零写一个学生成绩管理系统（Python练习）
Date: 2026-02-19
Category: Python学习
Tags: Python, 入门, 项目

今天开始练习Python基础，第一个小项目是“学生成绩管理系统”。主要练习了函数、列表、字典、异常处理。

## 功能
- 添加学生（姓名+成绩）
- 删除学生
- 修改成绩
- 查询学生
- 显示所有学生
- 计算平均分

## 核心代码片段
```python
def add_student():
    name = input("姓名：")
    score = float(input("成绩："))
    students.append({"name": name, "score": score})
```

完整代码放在 GitHub 上：[gds061020/python-practice](https://github.com/gds061020/python-practice)
## 遇到的问题

1.输入非数字时程序崩溃 → 用`try-except`解决

2.删除学生时找不到对应姓名 → 遍历列表查找


这样既记录了学习，又展示了代码，还用了 Git 链接，一举三得。