import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters

register_matplotlib_converters()

# 1. Use Pandas to import the data from "fcc-forum-pageviews.csv". Set the index to the date column.
df = pd.read_csv(
    "fcc-forum-pageviews.csv",
    parse_dates=["date"],
    index_col="date"
)

# 2. Clean the data by filtering out days when the page views were in the top 2.5% of the dataset or bottom 2.5% of the dataset.
# Calculate 2.5th percentile and 97.5th percentile thresholds
bottom_threshold = df['value'].quantile(0.025)
top_threshold = df['value'].quantile(0.975)

# Filter the DataFrame
df = df[
    (df['value'] >= bottom_threshold) &
    (df['value'] <= top_threshold)
]

# 3. Create a draw_line_plot function
def draw_line_plot():
    # Use Matplotlib to draw a line chart
    fig, ax = plt.subplots(figsize=(15, 6))
    ax.plot(df.index, df['value'], color='red', linewidth=1)

    # Set title and labels
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')

    # Save and return the image
    fig.savefig('line_plot.png')
    return fig

# 4. Create a draw_bar_plot function
def draw_bar_plot():
    # Make a copy of the data frame
    df_bar = df.copy()

    # Prepare data for the bar plot (average daily page views for each month grouped by year)
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.month_name()

    # Group data by year and month to get the average
    df_grouped = df_bar.groupby(['year', 'month'])['value'].mean().reset_index()

    # Ensure correct month order
    month_order = [
        'January', 'February', 'March', 'April', 'May', 'June',
        'July', 'August', 'September', 'October', 'November', 'December'
    ]
    df_grouped['month'] = pd.Categorical(df_grouped['month'], categories=month_order, ordered=True)
    df_grouped = df_grouped.sort_values('month')

    # Draw the bar chart using seaborn
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.barplot(
        x='year',
        y='value',
        hue='month',
        data=df_grouped,
        ax=ax
    )

    # Set labels and legend title
    ax.set_xlabel('Years')
    ax.set_ylabel('Average Page Views')
    ax.legend(title='Months')

    # Save and return the image
    fig.savefig('bar_plot.png')
    return fig

# 5. Create a draw_box_plot function
def draw_box_plot():
    # Prepare data for box plots (year and month columns)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date] # Abbreviated month names (Jan, Feb, ...)

    # Set up the matplotlib figure with two subplots
    fig, axes = plt.subplots(1, 2, figsize=(18, 6))

    # Year-wise Box Plot (Trend)
    sns.boxplot(x="year", y="value", data=df_box, ax=axes[0])
    axes[0].set_title("Year-wise Box Plot (Trend)")
    axes[0].set_xlabel("Year")
    axes[0].set_ylabel("Page Views")

    # Month-wise Box Plot (Seasonality)
    # Ensure correct month order (abbreviated)
    month_order_abbr = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    sns.boxplot(x="month", y="value", data=df_box, order=month_order_abbr, ax=axes[1])
    axes[1].set_title("Month-wise Box Plot (Seasonality)")
    axes[1].set_xlabel("Month")
    axes[1].set_ylabel("Page Views")

    # Save and return the image
    fig.savefig('box_plot.png')
    return fig
