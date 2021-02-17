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
from preprocessing import get_raw_str
# %%
VALID_CHARS = list(open('./data/charset.txt', 'r').read())
# %%
# TODO: validate tyep-engine. e.g not Unicode
def parse(text: str, exclude=[]):
    # remove irregular chars
    charset = VALID_CHARS.copy()
    if exclude:
        for c in exclude:
            if c in charset:
                charset.remove(c)


def compare_words(src_word: str, tg_word: str, raw_str: bool=False, rate: int=50):
    if raw_str:
        src_word = get_raw_str(src_word)
        tg_word = get_raw_str(tg_word)

    rt = fuzz.ratio(src_word, tg_word)
    return rt>=rate
