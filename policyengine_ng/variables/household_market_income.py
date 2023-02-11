from policyengine_ng.model_api import *


class household_market_income(Variable):
    label = "market income"
    documentation = "Total non-government income."
    entity = Household
    definition_period = YEAR
    value_type = float
    unit = "currency-NGN"
    adds = ["market_income"]
