import numpy as np

def _mock_fidelity(sample):
    score = 0.65 + 0.3 * float(np.mean(sample))
    return min(score, 0.99)

def run_quantum_pipeline(X, y, fidelity_threshold=0.70):
    predictions = []
    fidelity_scores = []
    metadata = []

    for i, sample in enumerate(X):
        fidelity = _mock_fidelity(sample)
        fidelity_scores.append(fidelity)

        if fidelity < fidelity_threshold:
            pred = 0
        else:
            pred = int(np.mean(sample) > 0.5)

        predictions.append(pred)
        metadata.append({
            "sample_id": i,
            "model_version": "v1.0",
            "confidence": round(float(0.5 + 0.5 * fidelity), 4),
            "device_context": "consumer-electronics"
        })

    return np.array(predictions), np.array(fidelity_scores), metadata
