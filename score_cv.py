import re
from fuzzywuzzy import fuzz

email_address_rank = [0, 5]
experience_year_range = [[0, 1], [1, 2], [2, 3], [3, 5], [5, 100]]
skill_range = [[0, 1], [1, 2], [3, 4], [4, 5], [5, 100]]
soft_skill_range = [[0, 1], [1, 2], [3, 4], [4, 5], [5, 100]]
is_update_point = [0, 5]
address_now_point = [0, 5]
cv_image_point = [3, 5]
interest_point = [0, 3, 5]
personal_summary_coefficient = {
    'CanFullName': 1,
    'CanDob': 1,
    'CanAddress1': 1,
    'CanEmail': 1,
    'CanTelNum': 1,
    'CanEthnic': 1,
    'CanReligion': 1,
    'CanNominee': 1,
    'CanNationality': 1,
    'CanIdentityName': 1,
    'CanNearestWork': 1,
    'Career': 1,
}
personal_attribute = ['CanFullName',
                      'CanDob',
                      'CanAddress1',
                      'CanEmail',
                      'CanTelNum',
                      'CanEthnic',
                      'CanReligion',
                      'CanNominee',
                      'CanNationality',
                      'CanIdentityName',
                      'CanNearestWork',
                      'Career',
                      'SumOfCoefficient']


class PersonalSummary:
    CanFullName = ''
    CanDob = ''
    CanAddress1 = ''
    CanEmail = ''
    CanTelNum = ''
    CanEthnic = ''
    CanReligion = ''
    CanNominee = ''
    CanNationality = ''
    CanIdentityName = ''
    CanNearestWork = ''
    Career = ''


def no_accent_vietnamese(s):
    s = re.sub('[áàảãạăắằẳẵặâấầẩẫậ]', 'a', s)
    s = re.sub('[ÁÀẢÃẠĂẮẰẲẴẶÂẤẦẨẪẬ]', 'A', s)
    s = re.sub('[éèẻẽẹêếềểễệ]', 'e', s)
    s = re.sub('[ÉÈẺẼẸÊẾỀỂỄỆ]', 'E', s)
    s = re.sub('[óòỏõọôốồổỗộơớờởỡợ]', 'o', s)
    s = re.sub('[ÓÒỎÕỌÔỐỒỔỖỘƠỚỜỞỠỢ]', 'O', s)
    s = re.sub('[íìỉĩị]', 'i', s)
    s = re.sub('[ÍÌỈĨỊ]', 'I', s)
    s = re.sub('[úùủũụưứừửữự]', 'u', s)
    s = re.sub('[ÚÙỦŨỤƯỨỪỬỮỰ]', 'U', s)
    s = re.sub('[ýỳỷỹỵ]', 'y', s)
    s = re.sub('[ÝỲỶỸỴ]', 'Y', s)
    s = re.sub('đ', 'd', s)
    s = re.sub('Đ', 'D', s)
    return s


def pointing_experience_year(years):
    experience_year = int(years)
    for i in range(len(experience_year_range)):
        if experience_year in range(experience_year_range[i][0], experience_year_range[i][1]):
            return i + 1
    return 0


def pointing_skill(skill):
    number_of_skills = len(skill)
    for i in range(len(skill_range)):
        if number_of_skills in range(skill_range[i][0], skill_range[i][1]):
            return i + 1
    return 0


def pointing_soft_skill(soft_skill):
    number_of_soft_skills = len(soft_skill)
    for i in range(len(soft_skill_range)):
        if number_of_soft_skills in range(soft_skill_range[i][0], soft_skill_range[i][1]):
            return i + 1
    return 0


def pointing_update_cv(is_update):
    if is_update:
        return is_update_point[1]
    return is_update_point[0]


def pointing_address(address_now):
    if address_now is not None:
        return address_now_point[1]
    return address_now_point[0]


def pointing_tel_num(tel_num):
    tel_num_reg = r"^[0]{1}[0-9]{9}$"
    if len(re.findall(tel_num_reg, tel_num)) == 1:
        return True
    return False


def pointing_cv_image(cv_image):
    if cv_image is not None:
        return cv_image_point[1]
    return cv_image_point[0]


def pointing_email_address(email_address, fullname):
    email_address_point = 0
    fullname = fullname.lower()
    fullname = no_accent_vietnamese(fullname)
    fullname_no_space = fullname.replace(" ", '')
    name_split = fullname.split(" ")
    email_name = email_address.split('@')[0]
    if fuzz.ratio(fullname_no_space, email_name) > 0.5:
        return email_address_rank[0]
    acronym_name_1 = ''
    acronym_name_2 = ''
    for i in range(len(name_split) - 1):
        acronym_name_1 = acronym_name_1 + name_split[i][0]
    acronym_name_2 = acronym_name_2 + name_split[len(name_split) - 2][0] + name_split[len(name_split) - 1][0]
    name_split.append(acronym_name_1)
    name_split.append(acronym_name_2)
    print(acronym_name_2)
    for checker in name_split:
        if email_name.find(checker) != -1:
            email_address_point = email_address_point + 1
    if email_address_point > 1:
        return email_address_rank[1]
    return email_address_rank[0]


def pointing_personal_summary(person_sum: PersonalSummary):
    summary_point = 0
    sum_of_coefficient = 0
    for attr in personal_attribute:
        value = person_sum.__getattribute__(attr)
        sum_of_coefficient = sum_of_coefficient + personal_summary_coefficient[attr]
        if value is not None:
            summary_point = summary_point + personal_summary_coefficient[attr]
    return round(summary_point / sum_of_coefficient * 5, 0)


def pointing_interest(interest):
    if interest is not None:
        return interest_point[2]
    return interest_point[0]


