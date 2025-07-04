# webapp/services/pricing_service.py

import streamlit as st
from typing import List

class PricingService:
    def __init__(self, class_names: List[str], role: str):
        self.role = role
        self.class_names = [c for c in class_names if c != "person"]

    def get_price_dict(self):
        price_dict = {}
        for cls in self.class_names:
            key = f"price_{cls}"
            default = st.session_state.get(key, 0.0)
            if self.role == "Admin":
                price = st.sidebar.number_input(
                    label=cls, min_value=0.0, value=default,
                    step=0.1, format="%.2f", key=key
                )
            else:
                price = st.sidebar.number_input(
                    label=cls, min_value=0.0,
                    value=default, step=0.1,
                    format="%.2f", key=key,
                    disabled=True
                )
            price_dict[cls] = price
        return price_dict
