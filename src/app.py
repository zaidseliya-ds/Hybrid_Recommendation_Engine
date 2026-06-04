# ==============================================================================
# Project: Streamlit Portal for Scale Recommendation Infrastructure
# Author: Zaid Seliya | UIN: 231A050
# AI&DS Engineering | Rizvi College of Engineering
# ==============================================================================

import streamlit as st
import plotly.express as px
from src.model import RecommendationMatrixRouter

st.set_page_config(page_title="Personalization Delivery Console", layout="wide")
st.title("🎯 Hybrid Recommendation Engine Infrastructure Interface")

router_model = RecommendationMatrixRouter()

st.sidebar.header("User Context Management")
selected_user = st.sidebar.number_input("Target User Profile Account ID Lookup", min_value=1, max_value=9999, value=55)

st.info(f"⚡ Production Metrics Status: System running at scale deployment ({router_model.deployment_scale}) delivering an optimal {router_model.ctr_boost_metric}.")

# Pull algorithmic data arrays
recommendations_dataframe = router_model.retrieve_hybrid_recommendation_matrix(user_account_id=selected_user)

st.subheader("Dynamic Latent Space Item Recommendations Logs")
st.dataframe(recommendations_dataframe, use_container_width=True)

# Graph visual representation
st.subheader("Algorithmic Recommendation Attribution Strength")
fig = px.pie(recommendations_dataframe, values='Match_Score_Confidence', names='Algorithmic_Attribution_Vector',
             title="Latent Personalization Model Weight Segment Distributions",
             color_discrete_sequence=px.colors.sequential.RdBu)
fig.update_layout(template="plotly_dark")
st.plotly_chart(fig, use_container_width=True)

