import streamlit as st

st.set_page_config(layout="wide")

hide_footer_style = """
<style>
header {
    display: none !important;
}
footer {
    display: none !important;
}
section > div.block-container {
    padding-top: 0px !important;
    padding-bottom: 0px !important;
}
h1,
h2,
h3,
h4,
h5,
h6,
p,
span,
div {
  font-family: "Roboto", sans-serif !important;
  font-weight: 500;
}
[data-baseweb="slider"] {
    padding-left: 10px !important;
}
#MainMenu {
    visibility: hidden;
}
footer {
    visibility: hidden;
}
.modebar{
      display: none !important;
}
</style>
"""
st.write(hide_footer_style, unsafe_allow_html=True)

from streamlit_ace import st_ace
import json
from api_utils import calculate

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
