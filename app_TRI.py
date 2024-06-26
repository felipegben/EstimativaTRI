# -*- coding: utf-8 -*-
"""
Created on Sun May 19 18:08:15 2024

@author: usuario

Programa pra mostrar a media TRI para um numero de acertos em um app streamlit
"""
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
import numpy as np
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter, AutoMinorLocator)
import streamlit as st

#importar arquivo com TRI min media max para cada área (média dos últimos anos)
#filepath
areas = ['LC','CH','CN','MT']

   
df = pd.concat([pd.read_csv(i+'.csv', delimiter = ',', index_col=None, header=0, encoding='latin-1') for i in areas],axis = 1)
    


#montar pagina streamlit e pedir input de acertos
st.title('Estimativa TRI')

acertoLC = st.slider("Acertos em Linguagens",0,45)
acertoCH = st.slider("Acertos em Humanas",0,45)
acertoCN = st.slider("Acertos em Natureza",0,45)
acertoMT = st.slider("Acertos em Matemática",0,45)

#montar dataframe com TRI pra cada número de acertos
TRI_LC = [df.iloc[acertoLC,i] for i in range(0,3)]
TRI_CH = [df.iloc[acertoCH,i] for i in range(3,6)]
TRI_CN = [df.iloc[acertoCN,i] for i in range(6,9)]
TRI_MT = [df.iloc[acertoMT,i] for i in range(9,12)]


dfTRI = pd.DataFrame({'Linguagens': TRI_LC, 'Humanas': TRI_CH,'Natureza': TRI_CN,'Matemática': TRI_MT}, index = ['TRI Mín','TRI Média','TRI Máx'])

#apresentar TRI
st.dataframe(dfTRI.T.style \
  .format(precision=2, decimal=".") \
  .format_index(str.upper, axis=1) , use_container_width = True)
    

#Pegar input nota da redação
redacao = st.slider("Redação",0,1000,step = 20)

#calcular media simples e mostrar
notas = np.array([dfTRI.iloc[1,i] for i in range(0,4)])
notas = np.append(notas,redacao)
media = notas.mean()

st.subheader(f'Média: {media:.2f}')
st.caption("*Estimativa baseada nas edições do ENEM de 2020 a 2023")

st.write("---")
st.caption("Versão 1.0 - 2024 @felipeben")
