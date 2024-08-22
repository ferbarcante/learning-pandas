# %%

import pandas as pd

# %%

df = pd.read_csv("../data/products.csv", 
                 sep=";", 
                 names=["Id", "Name", "Description"]
                 )

df

# %% 
df = df.rename(columns={"Id": "ID", "Name": "Nome", "Description": "Descrição"})
df