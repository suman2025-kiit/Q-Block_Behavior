import numpy as np

def compute_trust_scores(fidelity_scores, validation_scores, reliability_scores=None,
                         alpha=0.4, beta=0.4, gamma=0.2):
    if reliability_scores is None:
        reliability_scores = np.ones(len(fidelity_scores))

    trust_scores = (
        alpha * np.array(fidelity_scores)
        + beta * np.array(validation_scores)
        + gamma * np.array(reliability_scores)
    )
    return trust_scores
