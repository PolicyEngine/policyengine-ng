from policyengine_ng.model_api import *


class minimum_tax(Variable):
    label = "minimum tax"
    entity = Person
    definition_period = YEAR
    value_type = float
    unit = "currency-NGN"

    def formula(person, period, parameters):
        gross_income = person("gross_income", period)
        p = parameters(period).tax
        return p.minimum * gross_income
