# -*- coding: UTF-8 -*-
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from soccerplots.radar_chart import Radar

#CABEÇALHO DO FORM
st.markdown("<h1 style='text-align: center;'>Garantia Mínima para FLA & COR</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center;'>Qual a contribuição do seu clube?</h1>", unsafe_allow_html=True)
st.markdown("<h6 style='text-align: center;'>app by @JAmerico1898</h6>", unsafe_allow_html=True)
st.markdown("<h6 style='text-align: center;'>A análise utiliza o conceito de AUDIÊNCIA EFETIVA\n em concordância com a LEI DO MANDANTE</h6>", unsafe_allow_html=True)
st.markdown("<h6 style='text-align: center;'>Os resultados obtidos são BEM DIFERENTES daqueles que utilizam o critério de audiência da LIBRA</h6>", unsafe_allow_html=True)
st.markdown("---")

import streamlit as st

club_options = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)
with st.form("captura"):
    
    fla_gm = 296.2
    cor_gm = 239.6
    
    clube_1 = "Flamengo"
    clube_2 = "Corinthians"
    colocação_1 = st.selectbox("Defina a colocação do Flamengo", options=club_options)
    colocação_2 = st.selectbox("Defina a colocação do Corinthians", options=club_options)
    
    clube_3 = st.selectbox("Escolha seu clube", options=('América', 'Athlético', 'Atlético-MG', 'Bahia', 'Botafogo', 'Coritiba', 'Cruzeiro', 'Cuiabá', 'Fluminense', 'Fortaleza', 'Goiás', 'Grêmio', 'Internacional', 'Palmeiras', 'Red Bull', 'Santos', 'São Paulo', 'Vasco'))
    colocação_3 = st.selectbox("Escolha a colocação de seu clube", options=club_options)

    contrato = st.radio("Defina o valor do Contrato", options=('3 bilhões', '4 bilhões', '5 bilhões'))
    button = st.form_submit_button("Comparar!")

if button:
    base = pd.read_excel("simulador_mg2.xlsx")
    base = pd.DataFrame(base)
    base[[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]] = (round(base[[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]], 0)).astype(int)
    libra_audiência = {'Clubes': {0: 'Flamengo', 1: 'Corinthians', 2: 'São Paulo', 3: 'Palmeiras', 4: 'Fluminense', 5: 'Internacional', 6: 'Vasco', 7: 'Grêmio', 8: 'Atlético-MG', 9: 'Athlético', 10: 'Cruzeiro', 11: 'Santos', 12: 'Botafogo', 13: 'Bahia', 14: 'América', 15: 'Fortaleza', 16: 'Goiás', 17: 'Coritiba', 18: 'Red Bull', 19: 'Cuiabá'}, 'Audiência': {0: 0.107, 1: 0.09, 2: 0.071, 3: 0.069, 4: 0.058, 5: 0.052, 6: 0.05, 7: 0.05, 8: 0.047, 9: 0.046, 10: 0.045, 11: 0.045, 12: 0.04, 13: 0.039, 14: 0.037, 15: 0.033, 16: 0.031, 17: 0.03, 18: 0.03, 19: 0.03}}
    libra_audiência = pd.DataFrame(libra_audiência)
    libra_performance = {'Posição': {0: 1, 1: 2, 2: 3, 3: 4, 4: 5, 5: 6, 6: 7, 7: 8, 8: 9, 9: 10, 10: 11, 11: 12, 12: 13, 13: 14, 14: 15, 15: 16, 16: 17, 17: 18, 18: 19, 19: 20}, 'Performance': {0: 0.09499999999999999, 1: 0.091, 2: 0.08599999999999998, 3: 0.08099999999999997, 4: 0.07599999999999998, 5: 0.071, 6: 0.06699999999999998, 7: 0.061999999999999986, 8: 0.056999999999999995, 9: 0.052, 10: 0.04799999999999999, 11: 0.04299999999999999, 12: 0.03799999999999999, 13: 0.03299999999999999, 14: 0.027999999999999997, 15: 0.022, 16: 0.0125, 17: 0.0125, 18: 0.0125, 19: 0.0125}}
    libra_performance = pd.DataFrame(libra_performance)
    lff_audiência = {'Clubes': {0: 'Flamengo', 1: 'Corinthians', 2: 'São Paulo', 3: 'Palmeiras', 4: 'Fluminense', 5: 'Internacional', 6: 'Vasco', 7: 'Grêmio', 8: 'Atlético-MG', 9: 'Athlético', 10: 'Cruzeiro', 11: 'Santos', 12: 'Botafogo', 13: 'Bahia', 14: 'América', 15: 'Fortaleza', 16: 'Goiás', 17: 'Coritiba', 18: 'Red Bull', 19: 'Cuiabá'}, 'Audiência': {0: 0.097, 1: 0.0921, 2: 0.0871, 3: 0.0822, 4: 0.0772, 5: 0.0723, 6: 0.0673, 7: 0.0624, 8: 0.0574, 9: 0.0525, 10: 0.0475, 11: 0.0426, 12: 0.0376, 13: 0.0327, 14: 0.0277, 15: 0.0228, 16: 0.0178, 17: 0.0129, 18: 0.0079, 19: 0.003}}
    lff_audiência = pd.DataFrame(lff_audiência)
    lff_performance = {'Posição': {0: 1, 1: 2, 2: 3, 3: 4, 4: 5, 5: 6, 6: 7, 7: 8, 8: 9, 9: 10, 10: 11, 11: 12, 12: 13, 13: 14, 14: 15, 15: 16, 16: 17, 17: 18, 18: 19, 19: 20}, 'Performance': {0: 0.089, 1: 0.085, 2: 0.081, 3: 0.077, 4: 0.073, 5: 0.068, 6: 0.064, 7: 0.06, 8: 0.056, 9: 0.052, 10: 0.048, 11: 0.044, 12: 0.04, 13: 0.036, 14: 0.032, 15: 0.027, 16: 0.023, 17: 0.019, 18: 0.015, 19: 0.011}}
    lff_performance = pd.DataFrame(lff_performance)

    #Cálculo dos Buckets para os 3 valores de contratos
    if contrato == "3 bilhões":
        igualdade_libra = (0.4*3000*0.05)
        performance_libra_1 = libra_performance.iloc[colocação_1-1, 1]
        performance_libra_1 = (0.3*3000*performance_libra_1)
        #audiência_libra_1 = libra_audiência.loc[libra_audiência['Clubes'] == clube_1, 'Audiência'].values
        #audiência_libra_1 = (0.3*3000*(audiência_libra_1[0]))
        audiência_libra_1 = 0.3*3000*0.1071
        performance_libra_2 = libra_performance.iloc[colocação_2-1, 1]
        performance_libra_2 = (0.3*3000*performance_libra_2)
        #audiência_libra_2 = libra_audiência.loc[libra_audiência['Clubes'] == clube_2, 'Audiência'].values
        #audiência_libra_2 = (0.3*3000*(audiência_libra_2[0]))
        audiência_libra_2 = 0.3*3000*0.09005
        performance_libra_3 = libra_performance.iloc[colocação_3-1, 1]
        performance_libra_3 = (0.3*3000*performance_libra_3)
        audiência_libra_3 = libra_audiência.loc[libra_audiência['Clubes'] == clube_3, 'Audiência'].values
        audiência_libra_3 = (0.3*3000*(audiência_libra_3[0]))
        igualdade_lff = (0.45*3000*0.05)
        performance_lff_1 = lff_performance.iloc[colocação_1-1, 1]
        performance_lff_1 = (0.3*3000*performance_lff_1)
        #audiência_lff_1 = lff_audiência.loc[lff_audiência['Clubes'] == clube_1, 'Audiência'].values
        #audiência_lff_1 = (0.25*3000*(audiência_lff_1[0]))
        audiência_lff_1 = 0.25*3000*0.097
        performance_lff_2 = lff_performance.iloc[colocação_2-1, 1]
        performance_lff_2 = (0.3*3000*performance_lff_2)
        #audiência_lff_2 = lff_audiência.loc[lff_audiência['Clubes'] == clube_2, 'Audiência'].values
        #audiência_lff_2 = (0.25*3000*(audiência_lff_2[0]))
        audiência_lff_2 = 0.25*3000*0.0921
        performance_lff_3 = lff_performance.iloc[colocação_3-1, 1]
        performance_lff_3 = (0.3*3000*performance_lff_3)
        audiência_lff_3 = lff_audiência.loc[lff_audiência['Clubes'] == clube_3, 'Audiência'].values
        audiência_lff_3 = (0.25*3000*(audiência_lff_3[0]))

    elif contrato == '4 bilhões':
        igualdade_libra = 0.45*4000*0.05
        performance_libra_1 = libra_performance.iloc[colocação_1-1, 1]
        performance_libra_1 = (0.3*4000*performance_libra_1)
        #audiência_libra_1 = libra_audiência.loc[libra_audiência['Clubes'] == clube_1, 'Audiência'].values
        #audiência_libra_1 = (0.25*4000*(audiência_libra_1[0]))
        audiência_libra_1 = 0.25*4000*0.1071
        performance_libra_2 = libra_performance.iloc[colocação_2-1, 1]
        performance_libra_2 = (0.3*4000*performance_libra_2)
        #audiência_libra_2 = libra_audiência.loc[libra_audiência['Clubes'] == clube_2, 'Audiência'].values
        #audiência_libra_2 = (0.25*4000*(audiência_libra_2[0]))
        audiência_libra_2 = 0.25*4000*0.09005
        performance_libra_3 = libra_performance.iloc[colocação_3-1, 1]
        performance_libra_3 = (0.3*4000*performance_libra_3)
        audiência_libra_3 = libra_audiência.loc[libra_audiência['Clubes'] == clube_3, 'Audiência'].values
        audiência_libra_3 = (0.25*4000*(audiência_libra_3[0]))
        igualdade_lff = 0.45*4000*0.05
        performance_lff_1 = lff_performance.iloc[colocação_1-1, 1]
        performance_lff_1 = (0.3*4000*performance_lff_1)
        #audiência_lff_1 = lff_audiência.loc[lff_audiência['Clubes'] == clube_1, 'Audiência'].values
        #audiência_lff_1 = (0.25*4000*(audiência_lff_1[0]))
        audiência_lff_1 = 0.25*4000*0.097
        performance_lff_2 = lff_performance.iloc[colocação_2-1, 1]
        performance_lff_2 = (0.3*4000*performance_lff_2)
        #audiência_lff_2 = lff_audiência.loc[lff_audiência['Clubes'] == clube_2, 'Audiência'].values
        #audiência_lff_2 = (0.25*4000*(audiência_lff_2[0]))
        audiência_lff_2 = 0.25*4000*0.0921
        performance_lff_3 = lff_performance.iloc[colocação_3-1, 1]
        performance_lff_3 = (0.3*4000*performance_lff_3)
        audiência_lff_3 = lff_audiência.loc[lff_audiência['Clubes'] == clube_3, 'Audiência'].values
        audiência_lff_3 = (0.25*4000*(audiência_lff_3[0]))

    else:    
        igualdade_libra = 0.45*5000*0.05
        performance_libra_1 = libra_performance.iloc[colocação_1-1, 1]
        performance_libra_1 = 0.3*5000*performance_libra_1
        #audiência_libra_1 = libra_audiência.loc[libra_audiência['Clubes'] == clube_1, 'Audiência'].values
        #audiência_libra_1 = 0.25*5000*(audiência_libra_1[0])
        audiência_libra_1 = 0.25*5000*0.1071
        performance_libra_2 = libra_performance.iloc[colocação_2-1, 1]
        performance_libra_2 = 0.3*5000*performance_libra_2
        #audiência_libra_2 = libra_audiência.loc[libra_audiência['Clubes'] == clube_2, 'Audiência'].values
        #audiência_libra_2 = 0.25*5000*(audiência_libra_2[0])
        audiência_libra_2 = 0.25*5000*0.09005
        performance_libra_3 = libra_performance.iloc[colocação_3-1, 1]
        performance_libra_3 = 0.3*5000*performance_libra_3
        audiência_libra_3 = libra_audiência.loc[libra_audiência['Clubes'] == clube_3, 'Audiência'].values
        audiência_libra_3 = 0.25*5000*(audiência_libra_3[0])
        igualdade_lff = 0.45*5000*0.05
        performance_lff_1 = lff_performance.iloc[colocação_1-1, 1]
        performance_lff_1 = 0.3*5000*performance_lff_1
        #audiência_lff_1 = lff_audiência.loc[lff_audiência['Clubes'] == clube_1, 'Audiência'].values
        #audiência_lff_1 = 0.25*5000*(audiência_lff_1[0])
        audiência_lff_1 = 0.25*5000*0.097
        performance_lff_2 = lff_performance.iloc[colocação_2-1, 1]
        performance_lff_2 = 0.3*5000*performance_lff_2
        #audiência_lff_2 = lff_audiência.loc[lff_audiência['Clubes'] == clube_2, 'Audiência'].values
        #audiência_lff_2 = (0.25*5000*(audiência_lff_2[0]))
        audiência_lff_2 = 0.25*5000*0.0921
        performance_lff_3 = lff_performance.iloc[colocação_3-1, 1]
        performance_lff_3 = 0.3*5000*performance_lff_3
        audiência_lff_3 = lff_audiência.loc[lff_audiência['Clubes'] == clube_3, 'Audiência'].values
        audiência_lff_3 = (0.25*5000*(audiência_lff_3[0]))

    # Montagem de DataFrame intermediário com os 3 pacotes das 2 propostas para os 6 clubes
    composição = {'clubes': [clube_1, clube_2, clube_3], 'igualdade_libra':[igualdade_libra, igualdade_libra, igualdade_libra], 'igualdade_lff':[igualdade_lff, igualdade_lff, igualdade_lff], 'performance_libra':[performance_libra_1, performance_libra_2, performance_libra_3], 'performance_lff':[performance_lff_1, performance_lff_2, performance_lff_3], 'audiência_libra': [audiência_libra_1, audiência_libra_2, audiência_libra_3], 'audiência_lff':[audiência_lff_1, audiência_lff_2, audiência_lff_3]}
    composição = pd.DataFrame(composição)

    #####################################################################################################
    #####################################################################################################
    # Captura do Faturamento na LIBRA para clube_1
    condition_libra_1 = (base['Proposta']=='LIBRA') & (base['Contrato']==contrato) & (base['Clubes']==clube_1)
    filtered_base_libra_1 = base[condition_libra_1]
    filtered_base_libra_1 = pd.DataFrame(filtered_base_libra_1)
    faturamento_libra_1 = filtered_base_libra_1[colocação_1].values
    faturamento_libra_1 = faturamento_libra_1[0]
    faturamento_libra_1 = (round(faturamento_libra_1, 0)).astype(int)

    # Captura do Faturamento na LIBRA para clube_2
    condition_libra_2 = (base['Proposta']=='LIBRA') & (base['Contrato']==contrato) & (base['Clubes']==clube_2)
    filtered_base_libra_2 = base[condition_libra_2]
    filtered_base_libra_2 = pd.DataFrame(filtered_base_libra_2)
    faturamento_libra_2 = filtered_base_libra_2[colocação_2].values
    faturamento_libra_2 = faturamento_libra_2[0]
    faturamento_libra_2 = (round(faturamento_libra_2, 0)).astype(int)

    # Captura do Faturamento na LIBRA para clube_2
    condition_libra_3 = (base['Proposta']=='LIBRA') & (base['Contrato']==contrato) & (base['Clubes']==clube_3)
    filtered_base_libra_3 = base[condition_libra_3]
    filtered_base_libra_3 = pd.DataFrame(filtered_base_libra_3)
    faturamento_libra_3 = filtered_base_libra_3[colocação_3].values
    faturamento_libra_3 = faturamento_libra_3[0]
    faturamento_libra_3 = (round(faturamento_libra_3, 0)).astype(int)

    # Captura do Faturamento na LFF para clube_1
    condition_lff_1 = (base['Proposta']=='LFF') & (base['Contrato']==contrato) & (base['Clubes']==clube_1)
    filtered_base_lff_1 = base[condition_lff_1]
    filtered_base_lff_1 = pd.DataFrame(filtered_base_lff_1)
    faturamento_lff_1 = filtered_base_lff_1[colocação_1].values
    faturamento_lff_1 = faturamento_lff_1[0]
    faturamento_lff_1 = (round(faturamento_lff_1, 0)).astype(int)

    # Captura do Faturamento na LFF para clube_2
    condition_lff_2 = (base['Proposta']=='LFF') & (base['Contrato']==contrato) & (base['Clubes']==clube_2)
    filtered_base_lff_2 = base[condition_lff_2]
    filtered_base_lff_2 = pd.DataFrame(filtered_base_lff_2)
    faturamento_lff_2 = filtered_base_lff_2[colocação_2].values
    faturamento_lff_2 = faturamento_lff_2[0]
    faturamento_lff_2 = (round(faturamento_lff_2, 0)).astype(int)

    # Captura do Faturamento na LFF para clube_3
    condition_lff_3 = (base['Proposta']=='LFF') & (base['Contrato']==contrato) & (base['Clubes']==clube_3)
    filtered_base_lff_3 = base[condition_lff_3]
    filtered_base_lff_3 = pd.DataFrame(filtered_base_lff_3)
    faturamento_lff_3 = filtered_base_lff_3[colocação_3].values
    faturamento_lff_3 = faturamento_lff_3[0]
    faturamento_lff_3 = (round(faturamento_lff_3, 0)).astype(int)

    #####################################################################################
    #####################################################################################
    #Cálculo da Recomposição da GM
    if fla_gm > faturamento_libra_1:
        dif_fla = fla_gm - faturamento_libra_1
        n_faturamento_libra_1 = fla_gm  
    else:
        dif_fla = 0
        n_faturamento_libra_1 = faturamento_libra_1

    if cor_gm > faturamento_libra_2:
        dif_cor = cor_gm - faturamento_libra_2
        n_faturamento_libra_2 = cor_gm
    else:
        dif_cor = 0
        n_faturamento_libra_2 = faturamento_libra_2


    #Cálculo da Contribuição Geral de cada clube
    if (dif_fla + dif_cor) > 0:
        pal_gm = 0.10194*(dif_fla + dif_cor)
        sao_gm = 0.08425*(dif_fla + dif_cor)
        int_gm = 0.07507*(dif_fla + dif_cor)
        flu_gm = 0.07443*(dif_fla + dif_cor)
        atl_gm = 0.07020*(dif_fla + dif_cor)
        gre_gm = 0.06655*(dif_fla + dif_cor)
        bot_gm = 0.05633*(dif_fla + dif_cor)
        vas_gm = 0.05601*(dif_fla + dif_cor)
        ath_gm = 0.05477*(dif_fla + dif_cor)
        for_gm = 0.05383*(dif_fla + dif_cor)
        cru_gm = 0.04953*(dif_fla + dif_cor)
        san_gm = 0.04701*(dif_fla + dif_cor)
        ame_gm = 0.04636*(dif_fla + dif_cor)
        goi_gm = 0.03974*(dif_fla + dif_cor)
        cor_gm = 0.03380*(dif_fla + dif_cor)
        red_gm = 0.03328*(dif_fla + dif_cor)
        cui_gm = 0.02861*(dif_fla + dif_cor)
        bah_gm = 0.02828*(dif_fla + dif_cor)
    
    else:
        pal_gm = 0
        sao_gm = 0
        int_gm = 0
        flu_gm = 0
        atl_gm = 0
        gre_gm = 0
        bot_gm = 0
        vas_gm = 0
        ath_gm = 0
        for_gm = 0
        cru_gm = 0
        san_gm = 0
        ame_gm = 0
        goi_gm = 0
        cor_gm = 0
        red_gm = 0
        cui_gm = 0
        bah_gm = 0

#############################################################################
    #Cáculo da Contribuição de cada clube para FLA
    if (dif_fla) > 0:
        pal_gm_fla = 0.10194*(dif_fla)
        sao_gm_fla = 0.08425*(dif_fla)
        int_gm_fla = 0.07507*(dif_fla)
        flu_gm_fla = 0.07443*(dif_fla)
        atl_gm_fla = 0.07020*(dif_fla)
        gre_gm_fla = 0.06655*(dif_fla)
        bot_gm_fla = 0.05633*(dif_fla)
        vas_gm_fla = 0.05601*(dif_fla)
        ath_gm_fla = 0.05477*(dif_fla)
        for_gm_fla = 0.05383*(dif_fla)
        cru_gm_fla = 0.04953*(dif_fla)
        san_gm_fla = 0.04701*(dif_fla)
        ame_gm_fla = 0.04636*(dif_fla)
        goi_gm_fla = 0.03974*(dif_fla)
        cor_gm_fla = 0.03380*(dif_fla)
        red_gm_fla = 0.03328*(dif_fla)
        cui_gm_fla = 0.02861*(dif_fla)
        bah_gm_fla = 0.02828*(dif_fla)
    
    else:
        pal_gm_fla = 0
        sao_gm_fla = 0
        int_gm_fla = 0
        flu_gm_fla = 0
        atl_gm_fla = 0
        gre_gm_fla = 0
        bot_gm_fla = 0
        vas_gm_fla = 0
        ath_gm_fla = 0
        for_gm_fla = 0
        cru_gm_fla = 0
        san_gm_fla = 0
        ame_gm_fla = 0
        goi_gm_fla = 0
        cor_gm_fla = 0
        red_gm_fla = 0
        cui_gm_fla = 0
        bah_gm_fla = 0

#############################################################################
    #Cáculo da Contribuição de cada clube para COR
    if (dif_cor) > 0:
        pal_gm_cor = 0.10194*(dif_cor)
        sao_gm_cor = 0.08425*(dif_cor)
        int_gm_cor = 0.07507*(dif_cor)
        flu_gm_cor = 0.07443*(dif_cor)
        atl_gm_cor = 0.07020*(dif_cor)
        gre_gm_cor = 0.06655*(dif_cor)
        bot_gm_cor = 0.05633*(dif_cor)
        vas_gm_cor = 0.05601*(dif_cor)
        ath_gm_cor = 0.05477*(dif_cor)
        for_gm_cor = 0.05383*(dif_cor)
        cru_gm_cor = 0.04953*(dif_cor)
        san_gm_cor = 0.04701*(dif_cor)
        ame_gm_cor = 0.04636*(dif_cor)
        goi_gm_cor = 0.03974*(dif_cor)
        cor_gm_cor = 0.03380*(dif_cor)
        red_gm_cor = 0.03328*(dif_cor)
        cui_gm_cor = 0.02861*(dif_cor)
        bah_gm_cor = 0.02828*(dif_cor)
    
    else:
        pal_gm_cor = 0
        sao_gm_cor = 0
        int_gm_cor = 0
        flu_gm_cor = 0
        atl_gm_cor = 0
        gre_gm_cor = 0
        bot_gm_cor = 0
        vas_gm_cor = 0
        ath_gm_cor = 0
        for_gm_cor = 0
        cru_gm_cor = 0
        san_gm_cor = 0
        ame_gm_cor = 0
        goi_gm_cor = 0
        cor_gm_cor = 0
        red_gm_cor = 0
        cui_gm_cor = 0
        bah_gm_cor = 0

##########################################################################

    #Contribuição dos 18 Clubes para o Mínimo Garantido de Flamengo e Corinthians
    cont_18 = dif_fla + dif_cor

    #Contribuição do seu clube para o Mínimo Garantido de Flamengo e Corinthians

    if clube_3 == "América":
        clube_gm = ame_gm
        clube_gm_fla = ame_gm_fla
        clube_gm_cor = ame_gm_cor
    elif clube_3 == 'Athlético':
        clube_gm = ath_gm
        clube_gm_fla = ath_gm_fla
        clube_gm_cor = ath_gm_cor
    elif clube_3 == 'Atlético-MG':
        clube_gm = atl_gm
        clube_gm_fla = atl_gm_fla
        clube_gm_cor = atl_gm_cor
    elif clube_3 == 'Bahia':
        clube_gm = bah_gm
        clube_gm_fla = bah_gm_fla
        clube_gm_cor = bah_gm_cor
    elif clube_3 == 'Botafogo':
        clube_gm = bot_gm
        clube_gm_fla = bot_gm_fla
        clube_gm_cor = bot_gm_cor
    elif clube_3 == 'Coritiba':
        clube_gm = cor_gm
        clube_gm_fla = cor_gm_fla
        clube_gm_cor = cor_gm_cor
    elif clube_3 == 'Cruzeiro':
        clube_gm = cru_gm
        clube_gm_fla = cru_gm_fla
        clube_gm_cor = cru_gm_cor
    elif clube_3 == 'Cuiabá':
        clube_gm = cui_gm
        clube_gm_fla = cui_gm_fla
        clube_gm_cor = cui_gm_cor
    elif clube_3 == 'Fluminense':
        clube_gm = flu_gm
        clube_gm_fla = flu_gm_fla
        clube_gm_cor = flu_gm_cor
    elif clube_3 == 'Fortaleza':
        clube_gm = for_gm
        clube_gm_fla = for_gm_fla
        clube_gm_cor = for_gm_cor
    elif clube_3 == 'Goiás':
        clube_gm = goi_gm
        clube_gm_fla = goi_gm_fla
        clube_gm_cor = goi_gm_cor
    elif clube_3 == 'Grêmio':
        clube_gm = gre_gm
        clube_gm_fla = gre_gm_fla
        clube_gm_cor = gre_gm_cor
    elif clube_3 == 'Internacional':
        clube_gm = int_gm   
        clube_gm_fla = int_gm_fla
        clube_gm_cor = int_gm_cor
    elif clube_3 == 'Palmeiras':
        clube_gm = pal_gm
        clube_gm_fla = pal_gm_fla
        clube_gm_cor = pal_gm_cor
    elif clube_3 == 'Red Bull':
        clube_gm = red_gm
        clube_gm_fla = red_gm_fla
        clube_gm_cor = red_gm_cor
    elif clube_3 == 'Santos':
        clube_gm = san_gm
        clube_gm_fla = san_gm_fla
        clube_gm_cor = san_gm_cor
    elif clube_3 == 'São Paulo':
        clube_gm = sao_gm
        clube_gm_fla = sao_gm_fla
        clube_gm_cor = sao_gm_cor
    else:
        clube_gm = vas_gm
        clube_gm_fla = vas_gm_fla
        clube_gm_cor = vas_gm_cor

    if (dif_fla or dif_cor) > 0:
        faturamento_libra_3 = faturamento_libra_3 - clube_gm
        faturamento_libra_3 = (round(faturamento_libra_3, 0)).astype(int)
    
###############################################################################################################
###############################################################################################################

    fontsize = 20
    markdown_amount = f"<div style='text-align:center; font-size:{fontsize}px'>R$ {cont_18:.1f} milhões</div>"
    markdown_amount_2 = f"<div style='text-align:center; font-size:{fontsize}px'>R$ {dif_fla:.1f} milhões</div>"
    markdown_amount_3 = f"<div style='text-align:center; font-size:{fontsize}px'>R$ {dif_cor:.1f} milhões</div>"

    st.markdown("<h4 style='text-align: center;'>Doação dos 18 Clubes para o Mínimo Garantido de FLA & COR</b></h4>", unsafe_allow_html=True)
    st.markdown(markdown_amount, unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("<h4 style='text-align: center;'>Doação dos 18 para o Flamengo</b></h4>", unsafe_allow_html=True)
        st.markdown(markdown_amount_2, unsafe_allow_html=True)
    with col2:
        st.markdown("<h4 style='text-align: center;'>Doação dos 18 para o Corinthians</b></h4>", unsafe_allow_html=True)
        st.markdown(markdown_amount_3, unsafe_allow_html=True)
        
    st.markdown("---")    

###############################################################################################################
###############################################################################################################

    markdown_amount_4 = f"<div style='text-align:center; font-size:{fontsize}px'>R$ {clube_gm:.1f} milhões</div>"
    markdown_amount_5 = f"<div style='text-align:center; font-size:{fontsize}px'>R$ {clube_gm_fla:.1f} milhões</div>"
    markdown_amount_6 = f"<div style='text-align:center; font-size:{fontsize}px'>R$ {clube_gm_cor:.1f} milhões</div>"

    st.markdown("<h4 style='text-align: center;'>Doação do SEU CLUBE para o Mínimo Garantido de FLA & COR</b></h4>", unsafe_allow_html=True)
    st.markdown(markdown_amount_4, unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("<h4 style='text-align: center;'>Doação do SEU CLUBE para o Flamengo</b></h4>", unsafe_allow_html=True)
        st.markdown(markdown_amount_5, unsafe_allow_html=True)
    with col2:
        st.markdown("<h4 style='text-align: center;'>Doação do SEU CLUBE para o Corinthians</b></h4>", unsafe_allow_html=True)
        st.markdown(markdown_amount_6, unsafe_allow_html=True)
    st.markdown("---")    

###############################################################################################################
###############################################################################################################

    markdown_amount_7 = f"<div style='text-align:center; font-size:{fontsize}px'>R$ {-(n_faturamento_libra_1 - faturamento_libra_3):.1f} milhões</div>"
    markdown_amount_8 = f"<div style='text-align:center; font-size:{fontsize}px'>R$ {-(faturamento_libra_1 - faturamento_libra_3 - clube_gm):.1f} milhões</div>"
    markdown_amount_9 = f"<div style='text-align:center; font-size:{fontsize}px'>R$ {-(n_faturamento_libra_2 - faturamento_libra_3):.1f} milhões</div>"
    markdown_amount_10 = f"<div style='text-align:center; font-size:{fontsize}px'>R$ {-(faturamento_libra_2 - faturamento_libra_3 - clube_gm):.1f} milhões</div>"

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("<h4 style='text-align: center;'>Diferença do SEU CLUBE para o Flamengo com Mínimo Garantido</b></h4>", unsafe_allow_html=True)
        st.markdown(markdown_amount_7, unsafe_allow_html=True)
    with col2:
        st.markdown("<h4 style='text-align: center;'>Diferença do SEU CLUBE para o Flamengo sem Mínimo Garantido</b></h4>", unsafe_allow_html=True)
        st.markdown(markdown_amount_8, unsafe_allow_html=True)

    st.markdown("---")    

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("<h4 style='text-align: center;'>Diferença do SEU CLUBE para o Corinthians com Mínimo Garantido</b></h4>", unsafe_allow_html=True)
        st.markdown(markdown_amount_9, unsafe_allow_html=True)
    with col2:
        st.markdown("<h4 style='text-align: center;'>Diferença do SEU CLUBE para o Corinthians sem Mínimo Garantido</b></h4>", unsafe_allow_html=True)
        st.markdown(markdown_amount_10, unsafe_allow_html=True)

    st.markdown("---")    


###############################################################################################################
###############################################################################################################
    
    # Gráfico 1: Comparação do Faturamento dos clubes nas 2 Propostas
    plt.rcParams["figure.figsize"] = [4.5, 4.0]
    plt.rcParams["figure.autolayout"] = True

    faturamento_1 = (n_faturamento_libra_1, faturamento_lff_1)
    faturamento_2 = (n_faturamento_libra_2, faturamento_lff_2)
    faturamento_3 = (faturamento_libra_3, faturamento_lff_3)

    ind = np.arange(len(faturamento_1)) # the x locations for the groups
    width = 0.2 # the width of the bars

    fig, ax = plt.subplots()
    rects1 = ax.bar(ind - width/2, faturamento_1, width, label=f"{clube_1}, {colocação_1}", zorder=1, color='#B6282F', alpha=1)
    rects2 = ax.bar(ind + width/2, faturamento_2, width, label=f"{clube_2}, {colocação_2}", zorder=1, color='black', alpha=1)
    rects3 = ax.bar(ind + 1.5*width, faturamento_3, width, label=f"{clube_3}, {colocação_3}", zorder=1, color='#344D94', alpha=1)


    plt.ylim([0, 500])
    plt.xlabel('Propostas')
    ax.set_ylabel('Faturamento (R$ milhões)')
    ax.set_title('Comparativo LIBRA x LFF - Efeito do Mínimo Garantido FLA & COR\n')
    ax.set_xticks(ind)
    ax.set_xticklabels(('LIBRA', 'LFF'))
    ax.legend()

    def autolabel(rects, xpos='center'):
        ha = {'center': 'center', 'right': 'center', 'left': 'center'}
        offset = {'center': 0, 'right': 0, 'left': 0}
        for rect in rects:
            height = rect.get_height()
            ax.annotate('{}'.format(height),
                xy=(rect.get_x() + rect.get_width() / 2, height),
                xytext=(offset[xpos]*3, 3), # use 3 points offset
                textcoords="offset points", # in both directions
                ha=ha[xpos], va='bottom')

    autolabel(rects1, "left")
    autolabel(rects2, "center")
    autolabel(rects3, "right")

    st.pyplot(fig)
    fig.savefig("Comparação_Propostas.png", dpi=600, bbox_inches="tight")
    ###########################################################################################
    ###########################################################################################
    