#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
from fuzzywuzzy import fuzz
# from trankit import Pipeline
from typing import List, Tuple
# P = Pipeline('vietnamese')

from pyvi import ViTokenizer

# %%
def tokenize_sent(sentence: str) -> List[str]:
    # tokenized_text = P.tokenize(sentence, is_sent=True)
    # return [token['text'] for token in tokenized_text['tokens']]
    tokens = ViTokenizer.tokenize(sentence).split()
    tokens = list(map( lambda x: x.replace(r"_", " "), tokens ))
    return tokens


def match_keyword(words: list, sentence: str, thresh=0.5):
    """
    Args:
        words: list of words to compare
        sentence: input sentence to extract
        thresh: the similarity of 2 words to keep word
    Return:
        res: list of (score, extracted_word, tg_word)
    """
    words_sen = tokenize_sent(sentence)
    res = []
    for word in words_sen:
        bw = (0, '')
        for tg_word in words:
            sc = fuzz.ratio(word, tg_word) / 100
            if sc > bw[0]:
                bw = (sc, tg_word)
        if bw[0] < thresh:
            continue
        res.append((bw[0], word, bw[1]))
    return res

def approximate_best_match(src_words: List[str], tg_words: List[str]) -> Tuple[float, str, str]:
    best_coef = 0
    best_src = ''
    best_tg = ''
    for s in src_words:
        for t in tg_words:
            coef = fuzz.ratio(s, t)/100
            if coef > best_coef:
                best_coef = coef
                best_src = s
                best_tg = t
    return (best_coef, best_src, best_tg)
