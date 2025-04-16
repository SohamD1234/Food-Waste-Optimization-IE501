import pulp

# Create a LP minimization problem
prob = pulp.LpProblem("Minimize_Wastage", pulp.LpMinimize)

# Decision Variables
x1 = pulp.LpVariable("Quantity_of_Rice", lowBound=0, cat='Continuous')
x2 = pulp.LpVariable("Quantity_of_Vegetables", lowBound=0, cat='Continuous')

# Objective Function: Minimize Cost and Wastage
prob += 5*x1 + 3*x2 + 10*(pulp.lpSum([pulp.lpSum([0, x1-1]), pulp.lpSum([0, x2-2])]))

# Demand Constraints
prob += x1 >= 1
prob += x2 >= 2

# Total Prepared Quantity Constraint (Assuming Total Available Quantity is 10 for the example)
prob += x1 + x2 <= 8  # Reducing the total available quantity

# Budget Constraint (Assuming Budget is 20 for the example)
prob += 5*x1 + 3*x2 <= 18  # Reducing the budget slightly

# Solve the LP problem
prob.solve()

# Print the optimal quantities and total cost
print("Optimal Quantity of Rice:", pulp.value(x1))
print("Optimal Quantity of Vegetables:", pulp.value(x2))
print("Total Cost:", pulp.value(prob.objective))
