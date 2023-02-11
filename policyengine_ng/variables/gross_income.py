from policyengine_ng.model_api import *


class gross_income(Variable):
    label = "gross income"
    entity = Person
    definition_period = YEAR
    value_type = float
    unit = "currency-NGN"
    adds = ["employment_income"]
