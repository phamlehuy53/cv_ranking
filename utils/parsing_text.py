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

def remove_html_tag(text: str, repl: ''):
    assert text is str
    res = re.sub(r"<[^>]{1, 5}>", repl, text)
    return res

def trim(text: str):
    res = re.sub(r"\s+", r" ", text)
    res = re.sub(r"\n+", r" ", res)
    return res
