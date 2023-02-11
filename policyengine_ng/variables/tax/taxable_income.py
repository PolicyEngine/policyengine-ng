from policyengine_ng.model_api import *


class taxable_income(Variable):
    label = "taxable income"
    entity = Person
    definition_period = YEAR
    value_type = float
    unit = "currency-NGN"

    def formula(person, period, parameters):
        exempt = person("is_tax_exempt", period)
        gross_income = person("gross_income", period)
        consolidated_relief_allowance = person(
            "consolidated_relief_allowance", period
        )
        return where(exempt, 0, gross_income - consolidated_relief_allowance)
