import csv
import matplotlib.pyplot as plt


path = r"2. prace_se_soubory\data\teploty.csv"

years = []
temperatures = []

with open(path, "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for line in reader:
        if(line["TIME"] == "AVG"):
            print(line["YEAR"], " | ", line["TEMPERATURE"], "°C")

            years.append(int(line["YEAR"]))
            temperatures.append(float(line["TEMPERATURE"]))

plt.plot(years, temperatures, color="hotpink")
plt.title("average global temperatures")
plt.xlabel("years")
plt.ylabel("temperature (°C)")
plt.show()

