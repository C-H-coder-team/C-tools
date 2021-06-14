#function_include tool
#MIT Licenses
#By Lijun_Network_Studio
#Made by fanjun

import os

def func(setting=str(),name=str(),ret=str(),num=str()):
    file=os.open('include\ func.h',os.O_RDWR|os.O_CREAT)
    
    pra='#pragma once \n'
    ifndef='#ifndef FUNC_H \n'
    define='#define FUNC_H \n'
    endif='#endif  // !FUNC_H \n'
    include='#include"stdc.h"\n'
    
    rt=0
    rt+=os.write(file,bytes(pra,'UTF-8'))
    rt+=os.write(file,bytes(ifndef,'UTF-8'))
    rt+=os.write(file,bytes(define,'UTF-8'))
    rt+=os.write(file,bytes(include,'UTF-8'))

    func=str()
    if ret==True:
        func+=setting+' '+name+'()'+'\n'+'{'+'\n'+'\n'+'    '+'return '+num+';'+'\n'+'}'+'\n'
    else:
        func+=setting+' '+name+'()'+'\n'+'{'+'\n'+'}'+'\n'

    rt+=os.write(file,bytes(func,'UTF-8'))
    rt+=os.write(file,bytes(endif,'UTF-8'))
    os.close(file)
#format:func('void','fuck',True,"0")