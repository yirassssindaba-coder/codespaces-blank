import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1. Import the data from medical_examination.csv and assign it to the df variable.
df = pd.read_csv('medical_examination.csv')

# 2. Add an overweight column to the data.
# Calculate BMI: weight in kg / (height in meters)^2
df['height_m'] = df['height'] / 100
df['bmi'] = df['weight'] / (df['height_m'] ** 2)
# Use the value 0 for NOT overweight and the value 1 for overweight.
df['overweight'] = (df['bmi'] > 25).astype(int)

# Drop the temporary height_m and bmi columns
df = df.drop(columns=['height_m', 'bmi'])

# 3. Normalize data by making 0 always good and 1 always bad.
# If the value of cholesterol or gluc is 1, set the value to 0. If the value is more than 1, set the value to 1.
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)

# 4. Draw the Categorical Plot in the draw_cat_plot function.
def draw_cat_plot():
    # 5. Create a DataFrame for the cat plot using pd.melt
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])

    # 6. Group and reformat the data in df_cat to split it by cardio.
    # We need to count occurrences and rename the column for the plot to work
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')
    
    # 7. Convert the data into long format and create a chart that shows the value counts
    # Use the seaborn library import: sns.catplot().
    fig = sns.catplot(
        x='variable',
        y='total',
        hue='value',
        col='cardio',
        data=df_cat,
        kind='bar'
    )
    # 8. Get the figure for the output and store it in the fig variable.
    fig = fig.fig

    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig

# 9. Draw the Heat Map in the draw_heat_map function.
def draw_heat_map():
    # 10. Clean the data in the df_heat variable by filtering out incorrect data
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))
    ]

    # 11. Calculate the correlation matrix and store it in the corr variable.
    corr = df_heat.corr()

    # 12. Generate a mask for the upper triangle and store it in the mask variable.
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # 13. Set up the matplotlib figure.
    fig, ax = plt.subplots(figsize=(12, 12))

    # 14. Plot the correlation matrix using the method provided by the seaborn library import: sns.heatmap().
    sns.heatmap(
        corr,
        mask=mask,
        annot=True,
        fmt='.1f',
        linewidths=.5,
        center=0,
        cbar_kws={'shrink': 0.5},
        ax=ax
    )

    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
