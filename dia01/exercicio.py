# %%
import pandas as pd

# %%

dados = [10, 20, 42, 9, 12, 35, 24, 10, 8]

# %%

dados_series = pd.Series(dados)

# %%
 
dados_series.mean()

# %%

dados_series.std()

# %% 

dados_series.max()

# %% 

dados = {
    "nome":["Teo", "Nah", "Napoleão"],
    "idade":[31, 32, 14]
}

# %% 

df = pd.DataFrame(dados)

# %5 

df["idade"].mean()

# %% 

df["nome"].tail(1)