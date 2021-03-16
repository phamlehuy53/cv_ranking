#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : ranking.py
# Author            : phamlehuy53 <unknownsol98@gmail>
# Date              : 15.02.2021
# Last Modified Date: 17.02.2021
# Last Modified By  : phamlehuy53 <unknownsol98@gmail>
# %%
import os
from typing import List
import numpy as np
import unicodedata
from fuzzywuzzy import fuzz
import re

from utils.preprocessing import simplize, remove_html_tag, trim
from utils.extraction import match_keyword
# from trankit import Pipeline
from pyvi import ViTokenizer

KWS_WORKING_AWARD = ['best', 'excellence', 'xuất sắc', 'giỏi']
# %%
# TODO: validate tyep-engine. e.g not Unicode

JOB_KWS = set(map(lambda x: x[:-1], open('./data/Job-keywords.txt', 'r').readlines()))

def split_props(in_text: str) -> List[str]:
    res = in_text.split(r';')
    res = list(map( lambda x: x.strip(), res))
    return res

def rank_diploma(in_text: str):
    star = 1
    if not in_text:
        return star
    # Khong co truong tot nghiep -> 1*
    edu = ['đại học',
           'cao đẳng',
           'học viện',
           'chứng chỉ',
           'university',
           'college',
           'academy']
    # Khong co loai bang -> 1*
    gra_lv = {
        'trung bình': 2,
        'tb khá': 3,
        'khá': 4,
        'giỏi': 5
    }
    pr_text = trim(in_text)
    pr_text = remove_html_tag(pr_text)
    # Check university
    mtc_edu = match_keyword(edu, in_text, )
    if mtc_edu:
        # print( 'Universiy matched!', mtc_edu)
        pass
    else:
        return star
    # Check diploma
    mtc_lv = match_keyword(list(gra_lv.keys()), pr_text)
    if mtc_lv:
        mtc_lv.sort(reverse=True, key=lambda x: x[0])
        star = gra_lv[mtc_lv[0][1]]
    return star


def rank_introduction(in_text: str):
    star = 1
    if not in_text:
        return star

    # Tom luoc qua ve ban than -> 3*
    if len(in_text) < 10:
        star = 3

    tokens = ViTokenizer.tokenize(in_text).split()
    tokens = set([re.sub(r"_", ' ', tk) for tk in tokens])
    # print(tokens)
    matched_tokens = tokens.intersection(JOB_KWS)
    # print(matched_tokens)
    if len(matched_tokens) >= len(tokens) / 10:
        star = 5
    return star

def rank_working_award(in_text):
    '''
    'None': 1*
    'Team award': 2*
    'Department award': 3*
    'Area award': 4*
    'Company award': 5*
    '''
    if len(in_text) < 10 and 'None' in in_text:
        return 1
    corpus = split_props(in_text=in_text)

