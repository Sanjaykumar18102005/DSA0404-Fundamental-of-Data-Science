import pandas as pd
import numpy as np

df = pd.read_csv(r"C:\python\FDS\house_data.csv")

print("Dataset:")
print(df)

house_data = df.to_numpy()

filtered_houses = house_data[house_data[:, 1] > 4] 

average_price = np.mean(filtered_houses[:, 3])       
print("\nAverage Sale Price of Houses with more than 4 Bedrooms: ₹", average_price)