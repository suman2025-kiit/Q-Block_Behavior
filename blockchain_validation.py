import hashlib
import json
import numpy as np

def _keccak_like(payload: str) -> str:
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()

def blockchain_validate(X, predictions, fidelity_scores, metadata):
    validation_scores = []
    block_hashes = []
    prev_hash = "GENESIS"

    for i in range(len(predictions)):
        artifact = {
            "x": np.round(X[i], 4).tolist(),
            "y_hat": int(predictions[i]),
            "fidelity": round(float(fidelity_scores[i]), 4),
            "meta": metadata[i],
        }
        serialized = json.dumps(artifact, sort_keys=True) + prev_hash
        block_hash = _keccak_like(serialized)
        valid = int(fidelity_scores[i] >= 0.70)

        validation_scores.append(valid)
        block_hashes.append(block_hash)
        prev_hash = block_hash

    return np.array(validation_scores), block_hashes
