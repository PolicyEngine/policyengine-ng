from policyengine_ng.model_api import *


class consolidated_relief_allowance(Variable):
    label = "consolidated relief allowance"
    entity = Person
    definition_period = YEAR
    value_type = float
    unit = "currency-NGN"

    def formula(person, period, parameters):
        gross_income = person("gross_income", period)
        p = parameters(period).tax.consolidated_relief_allowance
        return p.flat + (gross_income * p.percent)
