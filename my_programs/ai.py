import csv

from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix


# ---------- Načtení CSV a úprava dat ----------
X = []  # = vstupy
Y = []  # = výstupy

with open("stroke_dataset/healthcare-dataset-stroke-data.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        age = float(row["age"])

        # Na vstupu mohou být jen číselné vstupy:
        if row["gender"] == "Male":
            gender = 0
        else:
            gender = 1
            
        heart_disease = float(row["heart_disease"])
        
        stroke = float(row["stroke"])

        X.append([age, gender, heart_disease])
        Y.append(stroke)


print(stroke)


# ---------- Ruční rozdělení na trénování a testování ----------
X = X[:500]
Y = Y[:500]

trening_X, test_X, trening_Y, test_Y = train_test_split(X, Y, test_size=0.2, random_state=40)



# ---------- Neuronová síť ----------
neural_network = MLPClassifier(
    hidden_layer_sizes=(64, 64, 8),
    activation="relu",
    max_iter=2000,
    random_state=4
)

neural_network.fit(trening_X, trening_Y)



# ---------- Vyhodnocení ----------
results = neural_network.predict(test_X)

correct = 0
for i in range(len(results)):
    if test_Y[i] == results[i]:
        correct += 1
print(correct / len(results))

#print(test_Y)
#print(results)
print(confusion_matrix(test_Y, results))
