#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : parsing_text.py
# Author            : phamlehuy53 <unknownsol98@gmail>
# Date              : 15.02.2021
# Last Modified Date: 15.02.2021
# Last Modified By  : phamlehuy53 <unknownsol98@gmail>

# %%
import os
import numpy as np
import unicodedata
import re

# %%
INTAB = 'ạảãàáâậầấẩẫăắằặẳẵóòọõỏôộổỗồốơờớợởỡéèẻẹẽêếềệểễúùụủũưựữửừứíìịỉĩýỳỷỵỹđ'
OUTTAB = "a" * 17 + "o" * 17 + "e" * 11 + "u" * 11 + "i" * 5 + "y" * 5 + "d"
R = re.compile("|".join(INTAB))
replaces_dict = dict(zip(INTAB, OUTTAB))


# TODO: case-sensitive not implemented
def remove_diacritic(utf8_str):
    return R.sub(lambda m: replaces_dict[m.group(0)], utf8_str)


def remove_html_tag(text: str, repl=''):
    assert type(text) is str
    res = re.sub(r"<[^>]{1, 5}>", repl, text)
    return res


def trim(text: str):
    res = re.sub(r"\s+", r" ", text)
    res = re.sub(r"\n+", r" ", res)
    return res


def simplize(text: str):
    text = trim(text)
    text = remove_diacritic(text)
    text = remove_html_tag(text)
    return text
