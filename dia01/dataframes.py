# %%
import pandas as pd 

# %% 

data = {
    "nome": ["teo", "maria", "lara", "nah"],
    "sobrenome": ["calvo", "pereira", "carvalho", "mendes"],
    "idade": [31, 32, 32, 59]
}

# %%

data["idade"][0]

# %% 

df = pd.DataFrame(data)
df

# %% 
df["idade"].iloc[0]

# %%
# acessando uma linha
df.iloc[0]


# %%
df.index

# %% 
df.columns

# %% 
# pegando especificamente o espaço q o df está ocupando na ram
df.info(memory_usage='deep')

# %%
df.dtypes

# %%
# criando atributo novo do dataframe
df['peso'] = [80, 58, 62, 50]
# estatisticas descritivas em um dataframe
sumario = df.describe()

sumario['peso']['mean']

# %% 
# escolher qtd de primeiras linhas para mostrar
df.head(2)
# escolher ultimas linhas pra mostrar
df.tail(2)