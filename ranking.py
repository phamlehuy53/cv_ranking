#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : ranking.py
# Author            : phamlehuy53 <unknownsol98@gmail>
# Date              : 15.02.2021
# Last Modified Date: 17.02.2021
# Last Modified By  : phamlehuy53 <unknownsol98@gmail>
# %%
import os
import numpy as np
import unicodedata
from fuzzywuzzy import fuzz
import re

from utils.preprocessing import simplize, remove_html_tag, trim
from utils.extraction import match_keyword
# %%
# TODO: validate tyep-engine. e.g not Unicode

def rank_diploma(in_text: str):
    star = 1
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
    mtc_lv = match_keyword(gra_lv.keys(), pr_text)
    if mtc_lv:
        mtc_lv.sort(reverse=True, key=lambda x: x[0])
        star = gra_lv[mtc_lv[0][1]]
    return star


