#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
コーパスからユニークな音節の辞書を作成する。
なお音節はすべて小文字とする。
"""

__author__ = "takahashi <takahashi@jnlp.org>"
__version__ = "1"
__date__ = "dd m yyyy"

import sys
from collections import defaultdict
# from viet_preprocessing.vietprepro import delete_tonemark

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

def make_syllable(filename):
    # ユニークな音節を保持するための辞書
    syllable_dic = defaultdict(int)

    # コーパスから読み込み
    for line in open(filename, 'r'):
        sentence = line.rstrip().encode('utf-8').decode('utf-8')
        syllables = sentence.split(u' ')

        for syllable in syllables:
            # 声調記号を削除する
            no_tonemark_syllable = delete_tonemark(syllable)

            # 声調記号を削除して、アルファベットのみであれば追加
            if no_tonemark_syllable.isalpha():
                syllable_dic[no_tonemark_syllable.lower()] += 1

            # アルファベットから始まり、記号で終わる文字列に対して処理を行う
            elif no_tonemark_syllable[0].isalpha() and not no_tonemark_syllable[-1].isalpha():
                # . , ! ?が文字列の末端にある場合に削除し、小文字にする。
                syllable = no_tonemark_syllable.rstrip('.').rstrip(',').rstrip('!').rstrip('?').lower()
                # 上記処理のあと、アルファベットのみで構成されていれば、追加する。
                if syllable.isalpha():
                    syllable_dic[syllable] += 1

    return [k for k, v in sorted(syllable_dic.items())]

if __name__ == "__main__":
    main()
