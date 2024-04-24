import pandas as pd
import matplotlib.pyplot as plt  # library to whatch information in tables
import seaborn as sns

# log in to the file
file = pd.read_csv('multas.csv')
print(file)

# Creat a line graphic
sns.lineplot(x="Fecha", y="Multas", data=file)

# Show graphic with plg library
plt.show()
