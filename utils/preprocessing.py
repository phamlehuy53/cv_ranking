#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
from fuzzywuzzy import fuzz
from trankit import Pipeline
P = Pipeline('vietnamese')
# %%

INTAB = 'ạảãàáâậầấẩẫăắằặẳẵóòọõỏôộổỗồốơờớợởỡéèẻẹẽêếềệểễúùụủũưựữửừứíìịỉĩýỳỷỵỹđ'
OUTTAB = "a"*17 + "o"*17 + "e"*11 + "u"*11 + "i"*5 + "y"*5 + "d"
R = re.compile("|".join(INTAB))
replaces_dict = dict(zip(INTAB, OUTTAB))
# TODO: case-sensitive not implemented
def remove_sign(utf8_str):
    return R.sub(lambda m: replaces_dict[m.group(0)], utf8_str.lower())

def get_raw_str(str_in: str):
    str_out = re.sub(r"")

def tokenize_sent(sentence: str):
    tokenized_text = P.tokenize(sentence, is_sent=True)
    return [token['text'] for token in tokenized_text['tokens']]

def match_keyword(words:list, sentence: str, thresh=0.5):
    words_sen = tokenize_sent(sentence)
    res = []
    for word in words_sen:
        bw = (0, '')
        for tg_word in words:
            sc = fuzz.ratio(word, tg_word)/100
            if sc > bw[0]:
                bw = (sc, tg_word)
        if bw[0] < thresh:
            continue
        res.append((bw[0], word, bw[1]))
    
    return res
