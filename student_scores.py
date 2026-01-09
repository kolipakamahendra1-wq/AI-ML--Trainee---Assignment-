import matplotlib.pyplot as plt

students = [
    {"name": "Asha", "score": 78},
    {"name": "Ravi", "score": 85},
    {"name": "Neha", "score": 92},
    {"name": "Arjun", "score": 70}
]

names = [s["name"] for s in students]
scores = [s["score"] for s in students]

average = sum(scores) / len(scores)
print("Average Score:", average)

plt.bar(names, scores)
plt.xlabel("Students")
plt.ylabel("Scores")
plt.title("Student Test Scores")
plt.show()
