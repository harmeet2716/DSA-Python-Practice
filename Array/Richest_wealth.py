
# Question 2: Richest Customer Wealth

# Step 1: Take number of customers
m = int(input("Enter number of customers: "))

# Step 2: Create an empty 2D list
accounts = []

# Step 3: Take account balances for each customer
for i in range(m):
    customer = list(map(int, input(
        f"Enter account balances for customer {i + 1}: "
    ).split()))

    accounts.append(customer)

# Step 4: Calculate maximum wealth
max_wealth = 0

for customer in accounts:

    total_wealth = 0

    for money in customer:
        total_wealth += money

    if total_wealth > max_wealth:
        max_wealth = total_wealth

# Step 5: Print result
print("Richest Customer Wealth:", max_wealth)
