#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
from fuzzywuzzy import fuzz
from trankit import Pipeline

P = Pipeline('vietnamese')


# %%


def tokenize_sent(sentence: str):
    tokenized_text = P.tokenize(sentence, is_sent=True)
    return [token['text'] for token in tokenized_text['tokens']]


def match_keyword(words: list, sentence: str, thresh=0.5):
    """
    Args:
        words: list of words to compare
        sentence: input sentence to extract
        thresh: the similarity of 2 words to keep word
    Return:
        res: list of (score, src_word, tg_word)
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
