#function_include tool
#MIT Licenses
#By Lijun_Network_Studio
#Made by fanjun

import os

def classes(name=str(),gouzao=str(),xigou=str(),public=str(),protected=str(),private=str()):
    file=os.open('include\ class.h',os.O_RDWR|os.O_CREAT)
    
    pra='#pragma once \n'
    ifndef='#ifndef CLASS_H \n'
    define='#define CLASS_H \n'
    endif='#endif  // !CLASS_H \n'
    include='#include"stdc.h"\n'
    
    rt=0
    rt+=os.write(file,bytes(pra,'UTF-8'))
    rt+=os.write(file,bytes(ifndef,'UTF-8'))
    rt+=os.write(file,bytes(define,'UTF-8'))
    rt+=os.write(file,bytes(include,'UTF-8'))

    classes=str()
    classes='class '+name+'\n'+'{'+'\n'
    
    if gouzao=="True":
        classes+='    '+'public:'+'\n'+'    '+'    '+name+'();'+'\n'
    
    if xigou=="True":
        classes+='    '+'public:'+'\n'+'    '+'    ~'+name+'();'+'\n'
    
    if public=="True":
        classes+='    '+"public:\n        \n"
    
    if private=="True":
        classes+='    '+"private:\n        \n"
    
    if protected=="True":
        classes+='    '+"protected:\n        \n"
    
    classes+="};\n"

    rt+=os.write(file,bytes(classes,'UTF-8'))
    rt+=os.write(file,bytes(endif,'UTF-8'))
    os.close(file)

#format:classes('name',"True","True","True","True","True")