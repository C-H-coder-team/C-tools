from includes import headfiles
from includes import classes
from includes import func
from includes import struct
from includes import variable

print("""                                                                                             ___________               ___________
        /--/            | |             | |                       | |                       |  _______  |             |  _______  |            |  |
       /  /             | |             | |                       | |                       | |       | |             | |       | |            |  |
      /  /              | |             | |                   ___________                   | |       | |             | |       | |            |  |
     /  /               | |             | |                   ___________                   | |       | |             | |       | |            |  |
    /  /            ___________     ___________                   | |                       | |       | |             | |       | |            |  |
    \  \            ___________     ___________                   | |                       | |       | |             | |       | |            |  |
     \  \               | |             | |                       | |                       | |       | |             | |       | |            |  |
      \  \              | |             | |                       | |                       | |       | |             | |       | |            |  |
       \  \             | |             | |                       | |____                   | |_______| |             | |_______| |            |  |__________
        \--\            | |             | |                       |______|                  |___________|             |___________|            |_____________|
\n
\n
""")

value=input('''
1.万能头文件构造
2.变量头文件构造
3.函数头文件构造
4.结构体头文件构造
5.类定义头文件构造
6.构造大套装
输入选择序号：
''')
if value=='1':
    headfiles.makedir()
    headfiles.headfile()
elif value=='2':
    setting=str(input('输入变量类型：'))
    name=str(input('输入变量名：'))
    array=str(input('变量是否数组（True/False）：'))
    if array=="True":
        num=str(input('输入数组分配个数：'))
    variable.var(setting,name,array,num)
elif value=='3':
    setting=str(input("函数返回类型："))
    name=str(input('函数名：'))
    ret=str(input('函数是否有返回值（True/False）：'))
    if ret=="True":
        num=str(input("返回值："))
    func.func(setting,name,ret,num)
elif value=='4':
    name=str(input("输入结构体名："))
    struct.struct(name)
elif value=='5':
    name=str(input("输入类名："))
    gouzao=str(input("是否添加构造？（True/False）"))
    xigou=str(input("是否添加析构？（True/False）"))
    public=str(input("是否添加共有访问？（True/False）"))
    protected=str(input("是否添加保护访问？（True/False）"))
    private=str(input("是否添加私有访问？（True/False）"))
    classes.classes(name,gouzao,xigou,public,protected,private)
elif value=='6':
    print("万能头文件构造\n")
    headfiles.makedir()
    headfiles.headfile()
    
    print("变量头文件构造\n")
    setting=str(input('输入变量类型：'))
    name=str(input('输入变量名：'))
    array=str(input('变量是否数组（True/False）：'))
    if array=="True":
        num=str(input('输入数组分配个数：'))
    variable.var(setting,name,array,num)

    print('函数头文件构造\n')
    setting=str(input("函数返回类型："))
    name=str(input('函数名：'))
    ret=str(input('函数是否有返回值（True/False）：'))
    if ret=="True":
        num=str(input("返回值："))
    func.func(setting,name,ret,num)

    print("结构体头文件构造\n")
    name=str(input("输入结构体名："))
    struct.struct(name)

    print("类定义头文件构造\n")
    name=str(input("输入类名："))
    gouzao=str(input("是否添加构造？（True/False）"))
    xigou=str(input("是否添加析构？（True/False）"))
    public=str(input("是否添加共有访问？（True/False）"))
    protected=str(input("是否添加保护访问？（True/False）"))
    private=str(input("是否添加私有访问？（True/False）"))
    classes.classes(name,gouzao,xigou,public,protected,private)