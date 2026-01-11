import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # 1. Import data dari epa-sea-level.csv
    df = pd.read_csv('epa-sea-level.csv')

    # 2. Buat scatter plot
    plt.figure(figsize=(12, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', label='Original Data', s=10)

    # 3. Buat garis kecocokan terbaik (Line of Best Fit) pertama (1880-2050)
    # Mendapatkan slope dan intercept
    res = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    
    # Buat range tahun dari 1880 sampai 2050
    years_extended = pd.Series([i for i in range(1880, 2051)])
    line_1 = res.slope * years_extended + res.intercept
    
    plt.plot(years_extended, line_1, 'r', label='Best Fit Line 1 (1880-2050)')

    # 4. Buat garis kecocokan terbaik kedua (2000-2050)
    # Filter data mulai dari tahun 2000
    df_recent = df[df['Year'] >= 2000]
    res_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    
    # Buat range tahun dari 2000 sampai 2050
    years_recent = pd.Series([i for i in range(2000, 2051)])
    line_2 = res_recent.slope * years_recent + res_recent.intercept
    
    plt.plot(years_recent, line_2, 'green', label='Best Fit Line 2 (2000-2050)')

    # 5. Tambahkan label dan judul
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()
    
    # Simpan plot dan kembalikan objek canvas untuk testing
    plt.savefig('sea_level_plot.png')
    return plt.gca()
