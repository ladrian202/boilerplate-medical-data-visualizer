import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('medical_examination.csv')

# 2
df['overweight'] = np.where((df['weight'] / ((df['height'] / 100) **2)) >= 25, 1, 0 )

# 3
df['cholesterol'] = np.where(df['cholesterol'] <= 1, 0, 1)
df['gluc'] = np.where(df['gluc'] <= 1, 0, 1)

# 4
def draw_cat_plot():
    # 5
    df_cat = pd.melt(
        df,
        value_vars=["cholesterol", "gluc", "smoke", "alco", "active", "overweight"]
    )


    # 6
    df_cat = pd.melt(
        df,
        id_vars=['cardio'], 
        value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight']
    )
    

    # 7
    df_cat = (
    df_cat
    .groupby(['cardio', 'variable', 'value'])
    .size()
    .reset_index(name='total')
    )

    g = sns.catplot(
    x="variable",
    y="total",
    hue="value",
    col="cardio",
    kind="bar",
    data=df_cat
)


    # 8
    fig = g.fig


    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = df[(df['ap_lo'] <= df['ap_hi']) & (df['height'] >= df['height'].quantile(0.025)) & (df['height'] <= df['height'].quantile(0.975)) & (df['weight'] >= df['weight'].quantile(0.025)) & (df['weight'] <= df['weight'].quantile(0.975))]

    # 12
    corr = None

    # 13
    mask = None



    # 14
    fig, ax = None

    # 15



    # 16
    fig.savefig('heatmap.png')
    return fig
