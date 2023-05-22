import os
import matplotlib.pyplot as plt

# Function to save the data to a file
def save_data(data):
    with open('investment_data.txt', 'a') as file:
        file.write(data + '\n')

# Function to load the data from a file
def load_data():
    data = []
    if os.path.isfile('investment_data.txt'):
        with open('investment_data.txt', 'r') as file:
            data = file.readlines()
    return data

# Variables
land_price = float(input("Land price: "))
selling_price = float(input("Selling price: "))
my_investment = float(input("My investment: "))

# Calculate the percentage
my_share = (my_investment / land_price) * 100
my_profit = (selling_price - (land_price + selling_price * 2 / 100)) * (my_share / 100)
my_total = ((selling_price - selling_price * (2 / 100)) * my_share) / 100

# Save the data
data = f"My Share: {my_share}%, Net Profit: {my_profit} kyat, Current amount: {my_total} kyat"
save_data(data)

# Print the result
print("My Share:", my_share,"%")
print("Net Profit:", my_profit,"kyat")
print("Current amount:", my_total,"kyat")

# Load past data
past_data = load_data()

# Extract values for plotting
labels = []
profits = []
totals = []

for data in past_data:
    parts = data.strip().split(',')
    labels.append(parts[0].split(':')[1].strip())
    profits.append(float(parts[1].split(':')[1].strip().split(' ')[0]))
    totals.append(float(parts[2].split(':')[1].strip().split(' ')[0]))

# Create bar graph
x = range(len(labels))
width = 0.35

fig, ax = plt.subplots()
rects1 = ax.bar(x, profits, width, label='Net Profit')
rects2 = ax.bar([i + width for i in x], totals, width, label='Current Amount')

ax.set_ylabel('Amount (kyat)')
ax.set_title('Investment Summary')
ax.set_xticks([i + width / 2 for i in x])
ax.set_xticklabels(labels)
ax.legend()

# Add labels to the bars
def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate(f'{int(height)}', xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3), textcoords="offset points",
                    ha='center', va='bottom')
        
autolabel(rects1)
autolabel(rects2)

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
