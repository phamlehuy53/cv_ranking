# %%
import re
import os
# %%

nation_prefix = [ "0", "84"]

# full len with prefix: 9
mobi_prefix = ["32", "33", "34", "35", "36", "37", "38", "39", "7", "79", "77", "76", "78", "83", "84", "85", "81", "82", "56", "58", "59"]
p = f"^({'|'.join(mobi_prefix)})"
mobi = {'r': re.compile(r"{}".format(p)),
        'len': 9}

# full len with prefix: 10
landlin_prefix = [ "296", "254", "209", "204", "291", "222", "275", "256", "274", "271", "252", "290", "292", "206", "236", "262", "261", "215", "251", "277", "269", "226", "24", "239", "220", "225", "293", "28", "221", "258", "297", "260", "213", "263", "205", "214", "272", "228", "238", "259", "229", "257", "232", "235", "255", "203", "233", "299", "212", "276", "227", "208", "237", "234", "273", "294", "207", "270", "216" ]
p = f"^({'|'.join(landlin_prefix)})"
r_land = re.compile(r"{}".format(p))

landline = {'r': re.compile(r"{}".format(p)),
            'len': 10}

PHONE_CNF = {
    'mobi': mobi,
    'landline': landline
}
# %%

def valid_phonenum( phone_num: str ):
    """

    Args:
        phone_num: Phone number

    Returns:
        bool: valided, str: parsed phone number

    """
    pro_num = re.sub(r"\+|\-|\(|\)|\s", "", phone_num)

    # Check non-digit
    if pro_num != re.sub(r"\D+", "", pro_num):
       return False, pro_num

    # Check nation prefix
    v = False
    for nat_pre in nation_prefix:
        if pro_num[: len(nat_pre )] == nat_pre :
            # print('Nation prefix True', nat_pre)
            pro_num = re.sub(nat_pre, "", pro_num, count=1)
            v = True
    if not v:
        return v, pro_num

    # Check vendor|province's prefix & len
    v = False
    for cnf in PHONE_CNF.keys():
        if PHONE_CNF[cnf]['r'].findall(pro_num):
            # print('Phone prefix True')
            v = True
            if PHONE_CNF[cnf]['len'] != len(pro_num):
                v = False
                break
    # if not v:
    return v, pro_num

def rank_info(phone_num: str):
    
    pass

