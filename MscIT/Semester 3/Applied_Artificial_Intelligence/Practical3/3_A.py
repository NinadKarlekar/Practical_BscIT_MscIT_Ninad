def bayes_theorem(p_h, p_e_given_h, p_e_given_not_h):
    p_not_h = 1 - p_h
    p_e = (p_e_given_h * p_h) + (p_e_given_not_h * p_not_h)
    p_h_given_e = (p_e_given_h * p_h) / p_e
    return p_h_given_e

p_h = float(input("Enter the probability of NK having a cold: "))
p_e_given_h = float(
    input("Enter the probability of observing sneezing when NK has a cold: ")
)
p_e_given_not_h = float(
    input(
        "Enter the probability of observing sneezing when NK does not have a cold: "
    )
)

result = bayes_theorem(p_h, p_e_given_h, p_e_given_not_h)

print(
    "NK's probability of having a cold given that he sneezes (P(H|E)) is:",
    round(result, 2),
)
