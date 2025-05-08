import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

wage = wage.read_csv("datos.csv.proyecto3")

st.title("")

tab1, tab2 = st.tabs(["Tab1", "Tab2"])



with tab1:
    st.header("Analisis Univariado")
    #analisis univariado
    fig, ax = plt.subplots(1,4, figsize = (10,4))
#años
    ax[0].hist(wage['Años'])
#sexo
    conteo = wage['Sexo'].value_counts()
    ax[1].bar(conteo.index, conteo.values)

#salario
    ax[2].hist(wage['educación'])

    ax[3].hist(wage['Salario'])

    fig.tight_layout()
    

with tab2:
    st.header("Analisis bivariado")
    
    fig, ax = plt.subplots(1,3, figsize = (11,5))

#años vs salario

    sns.scatterplot(data = wage, x ='Años', y = 'Salario', ax = ax[0])      #scatterplot da el tipo de grafica
#sexo vs salario

    sns.violinplot(data=wage, x = 'Sexo', y = 'Salario', ax = ax[1])           #boxplot el tipo de grafica             #violinplot para grafica de forma violín

#educación vs salario

    sns.scatterplot(data = wage, x ='educación', y = 'Salario', ax = ax[2])

    fig.tight_layout()                                                    #ajustar recuadros


    



