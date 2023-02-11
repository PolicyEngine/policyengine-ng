from policyengine_ng.model_api import *


class marginal_tax_rate(Variable):
    label = "marginal tax rate"
    entity = Person
    definition_period = YEAR
    value_type = float
    unit = "/1"
