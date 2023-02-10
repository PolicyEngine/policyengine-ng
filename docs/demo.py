import streamlit as st

st.set_page_config(layout="wide")
from streamlit_ace import st_ace
import json
import requests
from policyengine_ng import Simulation, system
from api_utils import calculate

st.title("PolicyEngine Nigeria")

st.write(
    "PolicyEngine Nigeria is a model of Nigeria's tax and benefit system."
)

default_situation = {
    "household": {
        "people": {
            "parent": {
                "employment_income": {2023: 30_000},
                "tax": {2023: None},
            },
        },
        "households": {
            "household": {
                "members": ["parent"],
            },
        },
    },
    "policy": {},
}
data_input, api_output = st.tabs(["JSON input", "API output"])
with data_input:
    st.caption("Describe people, households and reforms")
    situation = json.loads(
        st_ace(
            language="json",
            theme="github",
            value=json.dumps(default_situation, indent=4),
            height=300,
        )
    )
    result = calculate(situation["household"], situation["policy"])

with api_output:
    st.caption("PolicyEngine's API computes their taxes and benefits")
    st.json(result)
