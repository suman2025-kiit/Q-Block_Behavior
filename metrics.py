import pandas as pd
from sklearn.metrics import accuracy_score, roc_auc_score

def evaluate_results(y_true, y_pred, trust_scores, block_hashes, output_path):
    accuracy = accuracy_score(y_true, y_pred)
    try:
        roc_auc = roc_auc_score(y_true, y_pred)
    except ValueError:
        roc_auc = 0.5

    df = pd.DataFrame({
        "metric": ["accuracy", "roc_auc", "avg_trust_score", "num_blocks"],
        "value": [accuracy, roc_auc, float(trust_scores.mean()), len(block_hashes)]
    })
    df.to_csv(output_path, index=False)
    return df
