from policyengine_ng.model_api import *


class Gender(Enum):
    MALE = "Male"
    FEMALE = "Female"


label = "Gender"


class gender(Variable):
    label = "gender"
    entity = Person
    definition_period = YEAR
    value_type = Enum
    possible_values = Gender
    default_value = Gender.MALE
