from policyengine_ng.model_api import *


class is_tax_exempt(Variable):
    label = "is tax exempt"
    entity = Person
    definition_period = YEAR
    value_type = bool

    def formula(person, period, parameters):
        employment_income = person("employment_income", period)
        p = parameters(period).tax
        employment_income_at_or_below_threshold = (
            employment_income <= p.exempt_threshold
        )
        gross_income = person("gross_income", period)
        has_non_employment_income = gross_income > employment_income
        return (
            employment_income_at_or_below_threshold
            & ~has_non_employment_income
        )
