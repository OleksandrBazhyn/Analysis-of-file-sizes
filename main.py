import numpy as np
import matplotlib.pyplot as plt

try:
    with open("gathered_file_sizes.txt") as f:
        sizes = np.array([int(line.strip()) for line in f if line.strip().isdigit()])
except FileNotFoundError:
    print("Файл не знайдено. Переконайтесь, що `gathered_file_sizes.txt` існує.")
    exit()

if sizes.size == 0:
    print("Файл `gathered_file_sizes.txt` порожній або містить некоректні дані.")
    exit()

bins = [0, 512, 1024, 5_120, 10_240, 100_240, 1_024_000, 10_240_000, 100_240_000, 
        1_024_000_000, float("inf")]
labels = ["0 B - 0.5 KB", "0.5 KB - 1 KB", "1 KB - 5 KB", "5 KB - 10 KB", 
          "10 KB - 100 KB", "100 KB - 1 MB", "1 MB - 10 MB", "10 MB - 100 MB", 
          "100 MB - 1 GB", "1 GB+"]

hist, _ = np.histogram(sizes, bins=bins)

total_files = sizes.size
percentages = (hist / total_files) * 100

plt.figure(figsize=(12, 6))
bars = plt.bar(labels, hist, color="skyblue", edgecolor="black", alpha=0.7)

for bar, perc, count in zip(bars, percentages, hist):
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height(), 
             f"{perc:.1f}% ({count})", 
             ha='center', va='bottom', fontsize=10, fontweight='bold')

plt.xlabel("Розмір файлів")
plt.ylabel("Кількість файлів")
plt.title("Частотний розподіл розміру файлів")
plt.xticks(rotation=30)
plt.grid(axis="y", linestyle="--", linewidth=0.5)

plt.show()

print()
for label, perc, count in zip(labels, percentages, hist):
    print(f"{label}: {perc:.2f}% файлів ({count} шт.)")
print()
