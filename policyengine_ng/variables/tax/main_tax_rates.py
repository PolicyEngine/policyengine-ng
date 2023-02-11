from policyengine_ng.model_api import *


class main_tax_rates(Variable):
    label = "main tax rates"
    entity = Person
    definition_period = YEAR
    value_type = float
    unit = "currency-NGN"

    def formula(person, period, parameters):
        taxable_income = person("taxable_income", period)
        p = parameters(period).tax
        return p.main_rates.calc(taxable_income)
