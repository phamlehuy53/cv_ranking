'''
    Read unpurified json file to csv
'''
# %%
import os
import glob
import json
import pandas as pd 
import sys
from typing import Union
# %%
SPEC_CHAR = r"<~>"
REPLACE_TEXT = [
    ("'CanId'", '"CanId"'),
    ("'CanFullName'", '"CanFullName"'),
    ("'CanDob'", '"CanDob"'),
    ("'SexCode'", '"SexCode"'),
    ("'CanAddress'", '"CanAddress"'),
    ("'CanEmail'", '"CanEmail"'),
    ("'CanTelNum'", '"CanTelNum"'),
    ("'CanImgCand'", '"CanImgCand"'),
    ("'CanNationality'", '"CanNationality"'),
    ("'CanFileCv'", '"CanFileCv"'),
    ("'Interest'", '"Interest"'),
    ("'Strength'", '"Strength"'),
    ("'FutureGoals'", '"FutureGoals"'),
    ("'LearningDiploma'", '"LearningDiploma"'),
    ("'Specialize'", '"Specialize"'),
    ("'ExperienceYears'", '"ExperienceYears"'),
    ("'DesiredJob'", '"DesiredJob"'),
    ("'Skill'", '"Skill"'),
    ("'SoftSkill'", '"SoftSkill"'),
    ("'LanguageCertificate'", '"LanguageCertificate"'),
    ("'Diploma'", '"Diploma"'),
    ("'IsUpdate'", '"IsUpdate"'),
    ("'LearningAwards'", '"LearningAwards"'),
    ("'WorkingAwards'", '"WorkingAwards"'),
    ("'Project'", '"Project"'),
    ("'ProjectPosition'", '"ProjectPosition"'),
    ("'CompanyWorked'", '"CompanyWorked"'),
    ("'CompanyPosition'", '"CompanyPosition"'),
    ("'ReferencePerson'", '"ReferencePerson"'),
    ("'ReferencePersonPosition'", '"ReferencePersonPosition"'),
    ("'Point'", '"Point"'),
    ("'JobTitle'", '"JobTitle"'),
    ("'UpdateDate'", '"UpdateDate"')
]

# %%
def json2dict( json_path: str) -> Union[None, dict]:
    """
    Read json file to dict

    [TODO:description]

    Parameters
    ----------
    json_path : str
        Path to json file

    Returns
    -------
    Union[None, dict]:
        dict if successful
        None if failed
    """
    with open(json_path, 'r') as fr:
        # text = fr.read()
        # text = text.replace('\\', SPEC_CHAR)
        # text = text.replace("\'", '\"')
        # try:
        #     js_obj = json.loads( text )
        #     for k, v in js_obj.items():
        #         if SPEC_CHAR in v:
        #             js_obj[k] = v.replace(SPEC_CHAR, '\\')
        # except Exception as e:
        #     print(f"{e} - {json_path}")
        #     # raise e
        #     return None

        text = fr.read()
        
        # TODO: 
        text = text.replace(r'"', r"'")
        text = text.replace(r"{'", r'{"')
        text = text.replace(r"'}", r'"}')
        text = text.replace(r"':", r'":')
        text = text.replace(r":'", r':"')
        text = text.replace(r"',", r'",')
        text = text.replace(r",'", r',"')
        text = text.replace('\\', '\\\\')
        # breakpoint()
        try:
            js_obj = json.loads(text)
            return js_obj
        except Exception as e:
            print(e, json_path)
    # return js_obj
# %%
def load_json( json_dir: str ):
    for root_dir, sub_dir, files in os.walk(json_dir):
        if files:
            for f in files:
                yield json2dict(os.path.join( root_dir, f ))

def main(args):
    assert len(args) == 3
    input_dir = args[1]
    output_file = args[2]
    
    assert os.path.isdir(input_dir)
    out_dir = os.path.dirname(output_file)
    if not os.path.isdir(out_dir):
        print('Making directory {out_dir}')
        os.makedirs(out_dir)

    data = []
    err_cnt = 0
    for json_obj in load_json( input_dir ):
        if json_obj:
            data.append(json_obj)
        else:
            err_cnt += 1
    
    print(f"Completed! {err_cnt} failed")

    # breakpoint()
    df = pd.DataFrame(data)
    df.to_csv(output_file)

if __name__ == "__main__":
    main(sys.argv)
# %%
# %%
