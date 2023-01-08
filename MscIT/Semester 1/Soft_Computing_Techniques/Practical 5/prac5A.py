# 5A. Write a program for hopfield network.

import numpy as np

def compute_next_state(state, weight):
    # @ is a shorthand for 'np.matmul()'
    # the numpy.where() function return thr indices of
    # element in an input array where condition is satisfied
    next_state = np.where(weight @ state >= 0, +1, -1)
    return next_state

def compute_final_state(initial_state, weight, max_iter=1000):
    previous_state = initial_state
    next_state = compute_next_state(previous_state, weight)
    is_stable = np.all(previous_state == next_state)
    n_iter = 0
    while (not is_stable) and (n_iter <= max_iter):
        previous_state = next_state
        next_state = compute_next_state(previous_state, weight)
        print("Previous State: ", previous_state)
        print("Next State: ", next_state)
        is_stable = np.all(previous_state == next_state)
        n_iter += 1
    return previous_state, is_stable, n_iter

initial_state = np.array([+1, -1, -1, -1])
weight = np.array([[0, -1, -1, +1], [-1, 0, +1, -1], [-1, +1, 0, -1], [+1, -1, -1, 0]])
final_state, is_stable, n_iter = compute_final_state(initial_state, weight)
print("final State : ", final_state)
print("is_stable : ", is_stable)