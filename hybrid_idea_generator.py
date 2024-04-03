import random

# Ideas from two domains
Fruits = [('Apple', 5), ('Banana', 3), ('Cherry', 7)]  # (Idea, Potential Energy)
TechGadgets = [('Phone', 6), ('Laptop', 8), ('Watch', 4)]

# Function to calculate interaction force between two ideas
def calculate_interaction_force(idea1, idea2):
    # For simplicity, just use the average of their potential energies
    return (idea1[1] + idea2[1]) / 2

# Function to check if the combination is viable (for simplicity, just a random check here)
def is_viable_combination():
    return random.choice([True, False])

# Combine ideas if they have a positive interaction force and are deemed viable
HybridIdeas = []
for fruit in Fruits:
    for gadget in TechGadgets:
        interaction_force = calculate_interaction_force(fruit, gadget)
        if interaction_force > 5 and is_viable_combination():  # Threshold of 5 for simplicity
            newIdeaName = fruit[0] + " " + gadget[0]
            newIdeaPotential = interaction_force  # Using interaction force as the new idea's potential
            HybridIdeas.append((newIdeaName, newIdeaPotential))

# Print the resulting hybrid ideas
for idea in HybridIdeas:
    print(f"Hybrid Idea: {idea[0]}, Potential: {idea[1]}")
