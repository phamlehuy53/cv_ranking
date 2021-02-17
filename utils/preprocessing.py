#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : preprocessing.py
# Author            : phamlehuy53 <unknownsol98@gmail>
# Date              : 17.02.2021
# Last Modified Date: 17.02.2021
# Last Modified By  : phamlehuy53 <unknownsol98@gmail>
import re
from trankit import Pipeline
P = Pipeline('vietnamese')
# %%

INTAB = 'ạảãàáâậầấẩẫăắằặẳẵóòọõỏôộổỗồốơờớợởỡéèẻẹẽêếềệểễúùụủũưựữửừứíìịỉĩýỳỷỵỹđ'
OUTTAB = "a"*17 + "o"*17 + "e"*11 + "u"*11 + "i"*5 + "y"*5 + "d"
R = re.compile("|".join(INTAB))
replaces_dict = dict(zip(INTAB, OUTTAB))
# TODO: case-sensitive not implemented
def get_raw_str(utf8_str):
    return R.sub(lambda m: replaces_dict[m.group(0)], utf8_str.lower())


def tokenize_sent(setence: str):

