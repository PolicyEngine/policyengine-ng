from policyengine_ng.model_api import *


class is_adult(Variable):
    label = "is an adult"
    documentation = "Whether this individual is over 18."
    entity = Person
    definition_period = YEAR
    value_type = bool

    def formula(person, period, parameters):
        age = person("age", period)
        return age >= 18
