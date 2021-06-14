#headfiles_include tool
#MIT Licenses
#By Lijun_Network_Studio
#Made by fanjun

import os

def makedir():
    os.mkdir('include')
#format:makedir()

def headfile():
    file=os.open("include\stdc.h",os.O_RDWR|os.O_CREAT)

    head=['algorithm','bitset','conio.h','cctype','cerrno','clocale','cmath','complex','cstdio','cstdlib','cstring','ctime','deque','exception','fstream','functional','limits','list','map','iomanip','ios','iosfwd','iostream','queueSTL','setSTL','sstream','stackSTL','stdexcept','streambuf','string','utilitySTL','vectorSTL','cwchar','cwctype','complex.h','fenv.h','inttypes.h','stdbool.h','stdint.h','Windows.h','time.h']
    pra='#pragma once \n'
    ifndef='#ifndef STDC_H \n'
    define='#define STDC_H \n'
    endif='#endif  //!STDC_H \n'
    include='#include<'
    using='using namespace std; \n'
    rt=0

    rt+=os.write(file,bytes(pra,'UTF-8'))
    rt+=os.write(file,bytes(ifndef,'UTF-8'))
    rt+=os.write(file,bytes(define,'UTF-8'))

    for l in head:
        rt+=os.write(file,bytes(include+l+'>'+'\n','UTF-8'))

    rt+=os.write(file,bytes(using,'UTF-8'))
    rt+=os.write(file,bytes(endif,'UTF-8'))

    print('写入完毕。\n写入位数：%d',rt)
    os.close(file)
#format:headfile()