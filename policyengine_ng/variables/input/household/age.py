from policyengine_ng.model_api import *


class age(Variable):
    label = "age"
    documentation = "Age of the person in years."
    entity = Person
    definition_period = YEAR
    value_type = float
    unit = "year"
