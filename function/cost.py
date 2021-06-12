def cost_fun(state):
    temp1 = state[0:5]
    temp2 = state[7:12]
    cost = -1*sum([x1 - x2 for (x1, x2) in zip(temp1, temp2)])
    return cost
