from policyengine_ng import (
    Simulation,
    CountryTaxBenefitSystem,
    system as tax_benefit_system,
)
from policyengine_core.parameters import get_parameter
from policyengine_core.periods import instant
from policyengine_core.enums import Enum
import dpath
import json
import logging


def calculate(household: dict, reform: dict) -> dict:
    if len(reform.keys()) > 0:
        system = tax_benefit_system.clone()
        for parameter_name in reform:
            for time_period, value in reform[parameter_name].items():
                start_instant, end_instant = time_period.split(".")
                parameter = get_parameter(system.parameters, parameter_name)
                node_type = type(parameter.values_list[-1].value)
                try:
                    value = float(value)
                except:
                    pass
                parameter.update(
                    start=instant(start_instant),
                    stop=instant(end_instant),
                    value=node_type(value),
                )
    else:
        system = tax_benefit_system

    simulation = Simulation(
        tax_benefit_system=system,
        situation=household,
    )

    household = json.loads(json.dumps(household))

    requested_computations = get_requested_computations(household)

    for (
        entity_plural,
        entity_id,
        variable_name,
        period,
    ) in requested_computations:
        try:
            variable = system.get_variable(variable_name)
            result = simulation.calculate(variable_name, period)
            population = simulation.get_population(entity_plural)
            if "axes" in household:
                count_entities = len(household[entity_plural])
                entity_index = 0
                for _entity_id in household[entity_plural].keys():
                    if _entity_id == entity_id:
                        break
                    entity_index += 1
                result = (
                    result.astype(float)
                    .reshape((-1, count_entities))
                    .T[entity_index]
                    .tolist()
                )
                # If the result contains infinities, throw an error
                if any([math.isinf(value) for value in result]):
                    raise ValueError("Infinite value")
                else:
                    household[entity_plural][entity_id][variable_name][
                        period
                    ] = result
            else:
                entity_index = population.get_index(entity_id)
                if variable.value_type == Enum:
                    entity_result = result.decode()[entity_index].name
                elif variable.value_type == float:
                    entity_result = float(str(result[entity_index]))
                    # Convert infinities to JSON infinities
                    if entity_result == float("inf"):
                        entity_result = "Infinity"
                    elif entity_result == float("-inf"):
                        entity_result = "-Infinity"
                elif variable.value_type == str:
                    entity_result = str(result[entity_index])
                else:
                    entity_result = result.tolist()[entity_index]

                household[entity_plural][entity_id][variable_name][
                    period
                ] = entity_result
        except Exception as e:
            if "axes" in household:
                pass
            else:
                logging.warn(f"Error computing {variable_name}: {e}")
                household[entity_plural][entity_id][variable_name][
                    period
                ] = None

    return household


def get_requested_computations(household: dict):
    requested_computations = dpath.util.search(
        household,
        "*/*/*/*",
        afilter=lambda t: t is None,
        yielded=True,
    )
    requested_computation_data = []

    for computation in requested_computations:
        path = computation[0]
        entity_plural, entity_id, variable_name, period = path.split("/")
        requested_computation_data.append(
            (entity_plural, entity_id, variable_name, period)
        )

    return requested_computation_data
