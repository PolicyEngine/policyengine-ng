from policyengine_ng.model_api import *


class tax(Variable):
    label = "tax"
    documentation = "Example tax."
    entity = Person
    definition_period = YEAR
    value_type = float
    unit = "currency-NGN"

    def formula(person, period, parameters):
        market_income = person("market_income", period)
        tax_rate = parameters(period).tax_rate
        return market_income * tax_rate
