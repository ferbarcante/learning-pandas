# %% 

import pandas as pd

df_customers = pd.read_csv("../data/customers.csv", sep=";")
df_customers

# %% 
df_customers.shape

# %%
df_customers.info(memory_usage="deep")

# %% 
df_customers["Points"].astype(int)

# %% 

condicao = df_customers["Points"] == df_customers["Points"].max()
df_maior = df_customers[condicao]
df_maior["Name"].iloc[0]

# %% 

condicao = (df_customers["Points"] >= 1000) & (df_customers["Points"] <= 2000)
df_1000_2000 = df_customers[condicao].copy()

df_1000_2000["Points"] = df_1000_2000["Points"] + 1000
df_1000_2000
#%% 

df_1000_2000.info(memory_usage="deep")
# %% 

a = [1,2,3,4]
b = a
print(a)
print(b)

b.append(5)
print(a)
print(b)

# %% 
# como pegar mais de uma colunas
df_customers[["UUID", "Name"]]

# %%
# ordenando em ordem alfabetica
colunas = df_customers.columns.tolist()
colunas.sort()
colunas 

# reatribundo pro df original
df_customers = df_customers[colunas]

# %%
# como renomear 
df_customers = df_customers.rename(columns= {"Name": "Nome", "Points": "Pontos"})

# %% 
df_customers