import csv
import matplotlib.pyplot as plt


path = r"2. prace_se_soubory\data\vira_v_cesku.csv"

islam_count = 0
islam_count_brno = 0
islam_count_praha = 0
islam_count_ostrava = 0

islam_count_categories = ["Praha", "Brno", "Ostrava"]

with open(path, "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for line in reader:
        if(line["vira_txt"] == "islám"):
            islam_count += int(line["hodnota"])
            if(line["uzemi_txt"] == "Brno"):
                islam_count_brno += int(line["hodnota"])
            elif(line["uzemi_txt"] == "Praha"):
                islam_count_praha += int(line["hodnota"])
            elif(line["uzemi_txt"] == "Ostrava"):
                islam_count_ostrava += int(line["hodnota"])
            


plt.bar(islam_count_categories, [islam_count_praha, islam_count_brno, islam_count_ostrava], color="red")
plt.title("Islam across the republic")
plt.xlabel("category")
plt.ylabel("count")
plt.show()

