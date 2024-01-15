import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def ke_angka(data):
    data = str(data)
    data = data.replace(",", "")
    data = data.replace(".", "")
    return int(data)


data = pd.read_csv(
    "https://raw.githubusercontent.com/ezerinz/datasets/main/Kemantapan%20Jalan%20Provinsi%20Tahun%202022_0.csv",
    sep=";",
)
data_frame = data.head(10)
data_frame = data_frame.sort_values(by="Total_Panjang")

data_frame["Total_Panjang"] = data_frame["Total_Panjang"].apply(ke_angka)
data_frame["Mantap_%"] = data_frame["Mantap_%"].apply(ke_angka)

x = np.array(data_frame["Total_Panjang"])
y = np.array(data_frame["Mantap_%"])

m, b = np.polyfit(x, y, 1)

plt.plot(x, y, "o")
plt.plot(x, m * x + b)

plt.show()
