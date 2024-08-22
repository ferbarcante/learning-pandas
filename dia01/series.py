# %%
import pandas as pd
# %%

idades = [30, 42, 90, 34]
idades

# %%
media = sum(idades) / len(idades)

total = 0
for i in idades:
    total+= (media - i)**2

variancia = total/(len(idades) - 1)
variancia
# %%
series_idades = pd.Series(idades)
series_idades.mean
# os metodos no pandas são os verbos/ação 
# %% 
series_idades.mean()
# %% 
series_idades.var()

# %% 
series_idades.median()
# %% 
series_idades.describe()
# %%
series_idades.shape # o shape é um atributo de tupla que diz quantas linhas a series tem

# %%

# acessando elemento da series
series_idades[0]

# %%
# alterando o indicie
series_idades.index = ['t', 'e', 'o', 'c']

# %%
series_idades
series_idades[1]

# %% 

# expressando especificamente que quer a posição
series_idades.iloc[0]
# %%

# pedindo do zero a posição 2
series_idades.iloc[0:3]

# $$

# nomeando series
series_idades.name = 'idades'
series_idades