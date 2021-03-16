from utils.person_info import Person
from utils.score_cv import *
from utils.ranking import *

NUMBER_OF_CRITERIA = 12

FEATURE_SCORING = {
    'info':{    
        'feature': ['CanEmail', 'CanTelNum', 'CanFullName'],
        'fn': None
    },
    'introduction':{
        'feature': ['CanDob', 'SexCode', 'CanAddress', 'CanNationality', 'Interest', 'Strength', 'FutureGoals' ],
        'fn': None
    }, 
    'experience':{
        'features': ['ExperienceYears'], 
        'fn': None
    },
    'softskill':{

    }

    
}

def pointing_cv(candidate: Person):
    point = 0
    point = point + pointing_skill(candidate.Skill)
    point = point + pointing_email_address(candidate.CanEmail, candidate.CanFullName)
    point = point + pointing_experience_year(candidate.Years)
    point = point + pointing_cv_image(candidate.CanImgCandi)
    point = point + pointing_address(candidate.AddressNow)
    point = point + pointing_soft_skill(candidate.SoftSkill)
    point = point + pointing_interest(candidate.Interest)
    personal_summary = PersonalSummary(candidate.CanFullName,
                                       candidate.CanDob,
                                       candidate.CanAddress1,
                                       candidate.CanEmail,
                                       candidate.CanTelNum,
                                       candidate.CanEthnic,
                                       candidate.CanReligion,
                                       candidate.CanNominee,
                                       candidate.CanNationality,
                                       candidate.CanIdentityName,
                                       candidate.CanNearestWork,
                                       candidate.Career)
    point = point + pointing_personal_summary(personal_summary)
    point = point + pointing_spell(candidate)
    point = point + pointing_diploma(candidate.Diploma)
    point = point + rank_diploma(candidate.Diploma)
    point = point + pointing_tel_num(candidate.CanTelNum)
    # point = point + rank_introduction()
    return point/NUMBER_OF_CRITERIA

def 
