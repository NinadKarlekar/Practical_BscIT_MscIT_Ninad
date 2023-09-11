def drug_user(
    prob_th=0.5, sensitivity=0.97, specificity=0.95, prevelance=0.005, verbose=True
):
    # FORMULA
    p_user = prevelance
    p_non_user = 1 - prevelance
    p_pos_user = sensitivity
    p_neg_user = specificity
    p_pos_non_user = 1 - specificity
    num = p_pos_user * p_user
    den = p_pos_user * p_user + p_pos_non_user * p_non_user
    prob = num / den
    print("Probability of the NK being a drug user is", round(prob, 3))
    if verbose:
        if prob > prob_th:
            print("The NK could be an user")
        else:
            print("The NK may not be an user")
    return prob

drug_user()
