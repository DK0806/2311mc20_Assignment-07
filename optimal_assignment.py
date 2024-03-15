def optimal_assignment(available, choices):
    # Tally demand for each flavor
    flavor_demand = {flavor: 0 for flavor in available}
    for choice_set in choices.values():
        for flavor in choice_set:
            if flavor in flavor_demand:
                flavor_demand[flavor] += 1

    # Sort customers by the number of choices (ascending) and demand for their choices (descending)
    sorted_customers = sorted(choices.keys(), key=lambda x: (len(choices[x]), -max(flavor_demand[flavor] for flavor in choices[x] if flavor in flavor_demand)))

    assignment = {}
    for customer in sorted_customers:
        assigned = False
        for flavor in sorted(choices[customer], key=lambda x: (-flavor_demand[x], -available[x])):
            if available[flavor] > 0:
                assignment[customer] = flavor
                available[flavor] -= 1
                assigned = True
                break
        if not assigned:
            assignment[customer] = None
    return assignment

# Sample input as per the question
available = {"chocolate": 2, "vanilla": 1, "rose": 3, "strawberry": 1}
choices = {
    "alice": {"chocolate", "vanilla"},
    "bob": {"chocolate", "strawberry"},
    "charlie": {"vanilla"},
    "duke": {"vanilla", "rose", "chocolate"},
}

# Let's see the output
optimal_assignment_output = optimal_assignment(available, choices)
optimal_assignment_output
