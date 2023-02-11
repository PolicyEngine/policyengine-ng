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
        return parameters(period).gov.tax_rate.calc(market_income)
