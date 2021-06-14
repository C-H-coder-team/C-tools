#struct_include tool
#MIT Licenses
#By Lijun_Network_Studio
#Made by fanjun

import os

def struct(name):
    file=os.open('include\ struct.h',os.O_RDWR|os.O_CREAT)
    
    pra='#pragma once \n'
    ifndef='#ifndef STRUCT_H \n'
    define='#define STRUCT_H \n'
    endif='#endif  // !STRUCT_H \n'
    include='#include"stdc.h"\n'
    
    rt=0

    rt+=os.write(file,bytes(pra,'UTF-8'))
    rt+=os.write(file,bytes(ifndef,'UTF-8'))
    rt+=os.write(file,bytes(define,'UTF-8'))
    rt+=os.write(file,bytes(include,'UTF-8'))

    stru=str()
    
    stru+="struct"+' '+name+'\n'+'{'+'\n'+'\n'+'}'+';'+'\n'
    
    rt+=os.write(file,bytes(stru,'UTF-8'))
    rt+=os.write(file,bytes(endif,'UTF-8'))

    os.close(file)
#format:struct("a")