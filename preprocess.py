# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 21:42:46 2022

@author: ccjm1
"""

import pandas as pd
data = pd.read_csv(r'C:\Users\ccjm1\Downloads\Beneficiarios_M_s_Familias_en_Acci_n.csv')
data['CantidadDeBeneficiarios'].isnull().head()
#data.sort_values('')
data.CantidadDeBeneficiarios = data.CantidadDeBeneficiarios.str.replace(',','')
data.CantidadDeBeneficiarios = data.CantidadDeBeneficiarios.astype('float')

data.sort_values(by='CantidadDeBeneficiarios',ascending=False)
data_fin = data[data['CantidadDeBeneficiarios'].isnull()==False]



data_final = data_fin.groupby(['Bancarizado', 'CodigoDepartamentoAtencion', 'CodigoMunicipioAtencion',
       'Discapacidad', 'EstadoBeneficiario', 'Etnia',
       'FechaInscripcionBeneficiario', 'Genero', 'NivelEscolaridad',
       'NombreDepartamentoAtencion', 'NombreMunicipioAtencion', 'Pais',
       'TipoAsignacionBeneficio', 'TipoBeneficio', 'TipoDocumento',
       'TipoPoblacion', 'RangoBeneficioConsolidadoAsignado',
       'RangoUltimoBeneficioAsignado', 'FechaUltimoBeneficioAsignado',
       'RangoEdad', 'Titular']).sum('CantidadDeBeneficiarios').reset_index()

data_final.head()
data_final = data_final.sample(100000, weights='CantidadDeBeneficiarios', random_state=1)
data_final.to_csv(r'C:\Users\ccjm1\Downloads\Beneficiarios_M_s_Familias_en_Acci_n_process.csv',sep=',',index=False)
