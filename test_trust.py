import numpy as np

from qblock_behavior.core.trust import adaptive_trust, coordinate_median, poisoning_risk, trust_weighted_aggregate


def test_poisoning_risk_increases_for_large_deviation():
    reference = np.ones(4)
    benign = np.array([1.0, 1.1, 0.9, 1.0])
    malicious = np.array([-5.0, -5.0, -5.0, -5.0])
    assert poisoning_risk(malicious, reference) > poisoning_risk(benign, reference)


def test_coordinate_median():
    updates = [np.array([1.0, 2.0]), np.array([1.2, 2.2]), np.array([100.0, -50.0])]
    median = coordinate_median(updates)
    assert np.allclose(median, np.array([1.2, 2.0]))


def test_trust_weighted_aggregate_rejects_low_trust():
    updates = [np.array([1.0, 1.0]), np.array([10.0, 10.0])]
    trusts = [0.9, 0.2]
    aggregate = trust_weighted_aggregate(updates, trusts, tau_trust=0.7)
    assert np.allclose(aggregate, updates[0])


def test_adaptive_trust_range():
    value = adaptive_trust(0.95, True, 0.9, 0.85, 0.1)
    assert 0.0 <= value <= 1.0

