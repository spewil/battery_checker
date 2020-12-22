import numpy as np
import matplotlib.pyplot as plt
import pathlib
import matplotlib
matplotlib.use("MacOSX")

temps = ["45C", "35C", "25C"]
capacity_folder = pathlib.Path("Capacity data")
capacity_data = np.genfromtxt(capacity_folder / "Data_Capacity_35C01.txt",
                              delimiter="\t",
                              skip_header=1).reshape(-1, 6)

# spectra_data = np.loadtxt("EIS_data_35.txt")

# EIS_data_35 is the EIS data of the cell cycled at 35°C.
# X_train is the input of the model after normalization

# Capacity_data is the corresponding capacity of the training cell at 35°C, defined as Y_train, the output of the model.

cols = ["time [s]", "cycle number", "ox []", "current [mA]", "capacity [mAh]"]

print(capacity_data.shape)
END = 50
plt.plot(capacity_data[:END, 0], capacity_data[:END, -1])
plt.xlabel(cols[0])
plt.ylabel(cols[-1])

plt.show()
