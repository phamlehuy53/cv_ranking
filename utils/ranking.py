#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : ranking.py
# Author            : phamlehuy53 <unknownsol98@gmail>
# Date              : 15.02.2021
# Last Modified Date: 17.02.2021
# Last Modified By  : phamlehuy53 <unknownsol98@gmail>
# %%
import os
from typing import List, Tuple
import numpy as np
import unicodedata
from fuzzywuzzy import fuzz
import re

from utils.preprocessing import simplize, remove_html_tag, trim
from utils.extraction import match_keyword, tokenize_sent, approximate_best_match
# from trankit import Pipeline
# from pyvi import ViTokenizer

KWS_WORKING_AWARD = {
    'match': ['best', 'excellence', 'xuất sắc', 'giỏi'],
    'rank': {
        2: ['team', 'nhóm', 'giải thưởng', 'award']                           ,
        3: ['phòng', 'ban']                           ,
        4: ['khu vực', 'area', 'hội']                        ,
        5: ['company', 'công ty', 'group', 'tập đoàn']
    }
}
KWS_LEARNING_AWARD = {
    'match': ['giải thưởng', 'giải', 'award', 'scholarship', 'giỏi'],
    'rank':{
        2: ['xã', 'phường', 'thị trấn'],
        3: ['huyện', 'thị xã', 'quận', 'tỉnh'],
        4: ['thành phố'],
        5: ['quốc gia', 'quốc tế']
    }
}
# %%
# TODO: validate tyep-engine. e.g not Unicode

JOB_KWS = set(map(lambda x: x[:-1], open('./data/Job-keywords.txt', 'r', encoding='utf-8').readlines()))

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

    tokens = set(tokenize_sent(in_text))
    # print(tokens)
    matched_tokens = tokens.intersection(JOB_KWS)
    # print(matched_tokens)
    print(matched_tokens)

    if len(matched_tokens) >= len(tokens) / 10:
        star = 5
    return star

# %%
def rank_working_award(in_text: str) -> int:
    '''
    'None': 1*
    'Giai thuong cap nhom': 2*
    'Giai thuong cap phong, ban': 3*
    'Giai thuong cap khu vuc': 4*
    'Giai thuong cap cong ty': 5*
    '''
    in_text = in_text.lower()
    star = 1
    if len(in_text) < 10 and 'none' in in_text:
        star = 1
        return star
    
    match_thresh = 0.8
    corpus = split_props(in_text=in_text)
    
    matched = False
    tg_matches = KWS_WORKING_AWARD['match']
    ranks = KWS_WORKING_AWARD['rank']
    for prop in corpus:
        tokens = tokenize_sent(prop)
        match_ratio, _, _ = approximate_best_match(tokens, tg_matches)
        if match_ratio > match_thresh:
            matched = True
        if matched:
            for k, v in ranks.items():
                r, _, _ = approximate_best_match(v, tokens)
                if r > match_thresh:
                    star = max(star, k)

    return star

def rank_learning_award(in_text: str) -> int:
    '''
    'None': 0*
    'Giai thuong cap xa': 2*
    'Giai thuong cap huyen, tinh': 3*
    'Giai thuong cap Thanh pho': 4*
    'Giai thuong cap quoc gia': 5*
    '''
    in_text = in_text.lower()
    star = 0
    if len(in_text) < 10 and 'none' in in_text:
        star = 0
        return star

    match_thresh = 0.8
    corpus = split_props(in_text=in_text)
    
    matched = False
    tg_matches = KWS_LEARNING_AWARD['match']
    ranks = KWS_LEARNING_AWARD['rank']
    for prop in corpus:
        breakpoint()

        tokens = tokenize_sent(prop)
        match_ratio, _, _ = approximate_best_match(tokens, tg_matches)
        if match_ratio > match_thresh:
            matched = True
        if matched:
            for k, v in ranks.items():
                r, _, _ = approximate_best_match(v, tokens)
                if r > match_thresh:
                    star = max(star, k)

    return star
