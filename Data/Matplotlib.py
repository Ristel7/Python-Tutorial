# ---------------------------------------------------------
# Day 44: Matplotlib Basics to Practical
# ---------------------------------------------------------

import matplotlib.pyplot as plt
import numpy as np


# ---------------------------------------------------------
# 1. Basic Line Plot
# ---------------------------------------------------------

x = [1, 2, 3, 4, 5]
y = [10, 20, 30, 25, 35]

plt.plot(x, y)
plt.title("Basic Line Plot")
plt.xlabel("X values")
plt.ylabel("Y values")
plt.show()


# ---------------------------------------------------------
# 2. Line Plot with Markers
# ---------------------------------------------------------

plt.plot(x, y, marker="o")
plt.title("Line Plot with Markers")
plt.show()


# ---------------------------------------------------------
# 3. Multiple Lines in One Plot
# ---------------------------------------------------------

y2 = [5, 15, 25, 30, 40]

plt.plot(x, y, label="Sales A")
plt.plot(x, y2, label="Sales B")
plt.title("Multiple Line Plot")
plt.xlabel("Days")
plt.ylabel("Sales")
plt.legend()
plt.show()


# ---------------------------------------------------------
# 4. Bar Chart
# ---------------------------------------------------------

names = ["Aman", "Riya", "Priyanshu", "Sneha"]
scores = [80, 75, 90, 85]

plt.bar(names, scores)
plt.title("Student Scores")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()


# ---------------------------------------------------------
# 5. Horizontal Bar Chart
# ---------------------------------------------------------

plt.barh(names, scores)
plt.title("Horizontal Bar Chart")
plt.show()


# ---------------------------------------------------------
# 6. Histogram
# ---------------------------------------------------------

data = [10, 20, 20, 30, 30, 30, 40, 50, 50]

plt.hist(data, bins=5)
plt.title("Histogram Example")
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.show()


# ---------------------------------------------------------
# 7. Scatter Plot
# ---------------------------------------------------------

x = [1, 2, 3, 4, 5]
y = [5, 10, 15, 20, 25]

plt.scatter(x, y)
plt.title("Scatter Plot")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()


# ---------------------------------------------------------
# 8. Pie Chart
# ---------------------------------------------------------

labels = ["Python", "Java", "C++", "JavaScript"]
sizes = [40, 25, 20, 15]

plt.pie(sizes, labels=labels, autopct="%1.1f%%")
plt.title("Programming Language Usage")
plt.show()


# ---------------------------------------------------------
# 9. Subplots (Multiple Charts)
# ---------------------------------------------------------

x = np.arange(1, 6)

plt.subplot(1, 2, 1)
plt.plot(x, x * 2)
plt.title("Line Plot")

plt.subplot(1, 2, 2)
plt.bar(x, x * 3)
plt.title("Bar Plot")

plt.tight_layout()
plt.show()


# ---------------------------------------------------------
# 10. Customizing Plot
# ---------------------------------------------------------

plt.plot(x, x**2, linestyle="--", marker="o")
plt.title("Customized Plot")
plt.xlabel("X Axis")
plt.ylabel("X squared")
plt.grid(True)
plt.show()


# ---------------------------------------------------------
# 11. Real-world Example: Sales Trend
# ---------------------------------------------------------

months = ["Jan", "Feb", "Mar", "Apr", "May"]
sales = [12000, 15000, 14000, 17000, 18000]

plt.plot(months, sales, marker="o")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()


# ---------------------------------------------------------
# 12. Real-world Example: Distribution Analysis
# ---------------------------------------------------------

marks = np.random.randint(40, 100, 50)

plt.hist(marks, bins=10)
plt.title("Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Number of Students")
plt.show()



