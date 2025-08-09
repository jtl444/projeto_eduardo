#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import datetime

st.set_page_config(page_title="Recovery Wheel", layout="centered")

st.title("RECOVERY WHEEL")

# Formulário de entrada
with st.form("recovery_form"):
    col1, col2, col3 = st.columns(3)
    with col1:
        site = st.text_input("Site:")
    with col2:
        assessor = st.text_input("Assessor:")
    with col3:
        date = st.date_input("Date:", value=datetime.date.today())

    st.markdown("---")
    # Indicadores
    st.markdown("#### 1. Absence of threats")
    over_utilization = st.number_input("Over-utilization:", min_value=0, max_value=5, value=0, key="over_utilization")
    invasive_species = st.number_input("Invasive species:", min_value=0, max_value=5, value=0, key="invasive_species")
    contamination = st.number_input("Contamination:", min_value=0, max_value=5, value=0, key="contamination")

    st.markdown("#### 2. Physical conditions")
    substrate_physical = st.number_input("Substrate physical:", min_value=0, max_value=5, value=0, key="substrate_physical")
    substrate_chemical = st.number_input("Substrate chemical:", min_value=0, max_value=5, value=0, key="substrate_chemical")
    water_chemo_physical = st.number_input("Water chemo-physical:", min_value=0, max_value=5, value=0, key="water_chemo_physical")

    st.markdown("#### 3. Species composition")
    desirable_plants = st.number_input("Desirable plants:", min_value=0, max_value=5, value=0, key="desirable_plants")
    desirable_animals = st.number_input("Desirable animals:", min_value=0, max_value=5, value=0, key="desirable_animals")
    no_undesirable_species = st.number_input("No undesirable species:", min_value=0, max_value=5, value=0, key="no_undesirable_species")

    st.markdown("#### 4. Structural diversity")
    all_strata_present = st.number_input("All strata present:", min_value=0, max_value=5, value=0, key="all_strata_present")
    all_trophic_level = st.number_input("All trophic level:", min_value=0, max_value=5, value=0, key="all_trophic_level")
    spatial_mosaic = st.number_input("Spatial mosaic:", min_value=0, max_value=5, value=0, key="spatial_mosaic")

    st.markdown("#### 5. Ecosystem function")
    productivity_cycling = st.number_input("Productivity, cycling:", min_value=0, max_value=5, value=0, key="productivity_cycling")
    habitat_interactions = st.number_input("Habitat interactions:", min_value=0, max_value=5, value=0, key="habitat_interactions")
    resilience_recruitment = st.number_input("Resilience, recruitment:", min_value=0, max_value=5, value=0, key="resilience_recruitment")

    st.markdown("#### 6. External exchanges")
    landscape_flows = st.number_input("Landscape flows:", min_value=0, max_value=5, value=0, key="landscape_flows")
    gene_flows = st.number_input("Gene flows:", min_value=0, max_value=5, value=0, key="gene_flows")
    habitat_links = st.number_input("Habitat links:", min_value=0, max_value=5, value=0, key="habitat_links")

    submitted = st.form_submit_button("Update wheel")

# Dados para o radar chart
labels = [
    "Over-utilization", "Invasive species", "Contamination",
    "Substrate physical", "Substrate chemical", "Water chemo-physical",
    "Desirable plants", "Desirable animals", "No undesirable species",
    "All strata present", "All trophic level", "Spatial mosaic",
    "Productivity, cycling", "Habitat interactions", "Resilience, recruitment",
    "Landscape flows", "Gene flows", "Habitat links"
]
values = [
    over_utilization, invasive_species, contamination,
    substrate_physical, substrate_chemical, water_chemo_physical,
    desirable_plants, desirable_animals, no_undesirable_species,
    all_strata_present, all_trophic_level, spatial_mosaic,
    productivity_cycling, habitat_interactions, resilience_recruitment,
    landscape_flows, gene_flows, habitat_links
]

# Radar chart
if submitted:
    N = len(labels)
    angles = np.linspace(0, 2 * np.pi, N, endpoint=False).tolist()
    values += values[:1]  # Fechar o gráfico
    angles += angles[:1]

    fig, ax = plt.subplots(figsize=(7, 7), subplot_kw=dict(polar=True))
    ax.plot(angles, values, color='b', linewidth=2)
    ax.fill(angles, values, color='b', alpha=0.25)

    # Ajustar labels
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels, fontsize=10)
    ax.set_yticks([1, 2, 3, 4, 5])
    ax.set_yticklabels(['1', '2', '3', '4', '5'])
    ax.set_ylim(0, 5)

    plt.tight_layout()
    st.pyplot(fig)

    st.write(f"**ASSESSOR:** {assessor}   **SITE:** {site}   **DATE:** {date}")


# In[ ]:




