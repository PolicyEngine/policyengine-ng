from policyengine_ng.model_api import *


class employment_income(Variable):
    label = "employment income"
    documentation = "Total employment income, including bonuses and tips."
    entity = Person
    definition_period = YEAR
    value_type = float
    unit = "currency-NGN"
