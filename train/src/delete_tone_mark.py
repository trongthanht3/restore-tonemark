#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
# from viet_preprocessing.vietprepro import BoDau

def delete_tonemark(string):
    """声調記号を削除する"""
    return u''.join([BoDau(c) for c in string])

def BoDau(a): #hoạt động chính xác
    #convert kí tự tiếng Việt sang kí tự latin.
    Char = u"àảãáạăằẳẵắặâầẩẫấậòỏõóọôồổỗốộơờởỡớợèẻẽéẹêềểễếệùủũúụưừửữứựìỉĩíịỳỷỹýỵđ"
    kqua = u"aAoOeEuUiIyYdD"
    a+=u""
    lower = False
    b = a.lower()
    #print a, b==a
    if (a==b): lower = True
    else : lower = False
    i = Char.find(b)
    if i==-1 :return a
    if i<=16 :return kqua[0+1-lower]
    if i<=33 :return kqua[2+1-lower]
    if i<=44 :return kqua[4+1-lower]
    if i<=55 :return kqua[6+1-lower]
    if i<=60 :return kqua[8+1-lower]
    if i<=65 :return kqua[10+1-lower]
    if i<=66 :return kqua[12+1-lower]

def no_tone_open(filename):
    result = []
    for line in open(filename, 'r'):
        sentence = line.rstrip().decode('utf-8')
        no_tone_mark_sentence = delete_tonemark_from_sentence(sentence)
        result.append(no_tone_mark_sentence.lower().encode('utf-8'))
    return result

def delete_tonemark_from_sentence(sentence):
    return u''.join([BoDau(a) for a in sentence])

