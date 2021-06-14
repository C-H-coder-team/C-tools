#variable_include tool
#MIT Licenses
#By Lijun_Network_Studio
#Made by fanjun

import os

def var(setting=str(),name=str(),array=bool(),num=str()):
    file=os.open('include\ vars.h',os.O_RDWR|os.O_CREAT)
    
    pra='#pragma once \n'
    ifndef='#ifndef HVARS_H \n'
    define='#define HVARS_H \n'
    endif='#endif  // !HVARS_H \n'
    include='#include"stdc.h"\n'
    
    rt=0
    rt+=os.write(file,bytes(pra,'UTF-8'))
    rt+=os.write(file,bytes(ifndef,'UTF-8'))
    rt+=os.write(file,bytes(define,'UTF-8'))
    rt+=os.write(file,bytes(include,'UTF-8'))

    vars=str()
    if array==True:
        vars+=setting+' '+name+'['+num+']'+';'+'\n'
    else:
        vars+=setting+' '+name+';'+'\n'

    rt+=os.write(file,bytes(vars,'UTF-8'))
    rt+=os.write(file,bytes(endif,'UTF-8'))
    os.close(file)

#format:var('int','n',True,'101')