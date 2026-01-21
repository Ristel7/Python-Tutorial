# ---------------------------------------------------------
# Day 45: Advanced Matplotlib
# ---------------------------------------------------------

import matplotlib.pyplot as plt
import numpy as np


# ---------------------------------------------------------
# 1. Figure & Axes (MOST IMPORTANT CONCEPT)
# ---------------------------------------------------------

x = np.linspace(0, 10, 100)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_title("Figure & Axes Example")
ax.set_xlabel("X")
ax.set_ylabel("sin(x)")
plt.show()


# ---------------------------------------------------------
# 2. Multiple Subplots (Correct Way)
# ---------------------------------------------------------

fig, axes = plt.subplots(2, 2, figsize=(10, 6))

axes[0, 0].plot(x, np.sin(x))
axes[0, 0].set_title("sin(x)")

axes[0, 1].plot(x, np.cos(x))
axes[0, 1].set_title("cos(x)")

axes[1, 0].plot(x, np.tan(x))
axes[1, 0].set_title("tan(x)")

axes[1, 1].plot(x, np.exp(x))
axes[1, 1].set_title("exp(x)")

plt.tight_layout()
plt.show()


# ---------------------------------------------------------
# 3. Styles (Make plots look good instantly)
# ---------------------------------------------------------

plt.style.use("ggplot")

plt.plot(x, y)
plt.title("Using ggplot style")
plt.show()


# ---------------------------------------------------------
# 4. Customizing Lines
# ---------------------------------------------------------

plt.plot(x, y, linewidth=3, linestyle="--", marker="o", markevery=10)
plt.title("Customized Line")
plt.show()


# ---------------------------------------------------------
# 5. Legends (Advanced Control)
# ---------------------------------------------------------

plt.plot(x, np.sin(x), label="sin(x)")
plt.plot(x, np.cos(x), label="cos(x)")
plt.legend(loc="upper right", frameon=True, shadow=True)
plt.title("Legend Control")
plt.show()


# ---------------------------------------------------------
# 6. Annotations (Highlight Insights)
# ---------------------------------------------------------

plt.plot(x, y)
plt.annotate(
    "Peak",
    xy=(np.pi / 2, 1),
    xytext=(5, 1.5),
    arrowprops=dict(arrowstyle="->")
)
plt.title("Annotations")
plt.show()


# ---------------------------------------------------------
# 7. Grid Customization
# ---------------------------------------------------------

plt.plot(x, y)
plt.grid(True, linestyle="--", alpha=0.6)
plt.title("Custom Grid")
plt.show()


# ---------------------------------------------------------
# 8. Twin Axes (Two Y-axes)
# ---------------------------------------------------------

y1 = x ** 2
y2 = x ** 3

fig, ax1 = plt.subplots()

ax1.plot(x, y1, label="x^2")
ax1.set_ylabel("x^2")

ax2 = ax1.twinx()
ax2.plot(x, y2, linestyle="--", label="x^3")
ax2.set_ylabel("x^3")

ax1.set_title("Twin Axes Example")
plt.show()


# ---------------------------------------------------------
# 9. Axis Limits & Scaling
# ---------------------------------------------------------

plt.plot(x, np.exp(x))
plt.yscale("log")
plt.title("Log Scale")
plt.show()


# ---------------------------------------------------------
# 10. Saving High-Quality Figures
# ---------------------------------------------------------

plt.plot(x, y)
plt.title("Saved Plot")
plt.savefig("high_quality_plot.png", dpi=300, bbox_inches="tight")
plt.close()


# ---------------------------------------------------------
# 11. Performance Tip: Large Data
# ---------------------------------------------------------

large_x = np.arange(1_000_000)
large_y = large_x * 2

plt.plot(large_x[::100], large_y[::100])
plt.title("Downsampled Large Data")
plt.show()


# ---------------------------------------------------------
# 12. Real-world Example: Sales Dashboard Plot
# ---------------------------------------------------------

months = ["Jan", "Feb", "Mar", "Apr", "May"]
sales = [12000, 15000, 14000, 18000, 20000]
expenses = [8000, 9000, 8500, 10000, 11000]

fig, ax = plt.subplots()

ax.plot(months, sales, marker="o", label="Sales")
ax.plot(months, expenses, marker="o", label="Expenses")

ax.set_title("Sales vs Expenses")
ax.set_xlabel("Month")
ax.set_ylabel("Amount")
ax.legend()

plt.show()


# ---------------------------------------------------------
# End of Day 45: Advanced Matplotlib
# ---------------------------------------------------------
