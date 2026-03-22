from config import DATA_PATH, OUTPUT_PATH, FIDELITY_THRESHOLD, ALPHA, BETA, GAMMA
from src.data_aggregation import load_and_preprocess_data
from src.quantum_model import run_quantum_pipeline
from src.blockchain_validation import blockchain_validate
from src.trust_evaluation import compute_trust_scores
from src.metrics import evaluate_results

def main():
    X, y = load_and_preprocess_data(DATA_PATH)
    predictions, fidelity_scores, metadata = run_quantum_pipeline(X, y, FIDELITY_THRESHOLD)
    validation_scores, block_hashes = blockchain_validate(X, predictions, fidelity_scores, metadata)
    trust_scores = compute_trust_scores(
        fidelity_scores, validation_scores, alpha=ALPHA, beta=BETA, gamma=GAMMA
    )
    evaluate_results(y, predictions, trust_scores, block_hashes, OUTPUT_PATH)
    print("Pipeline completed successfully.")
    print(f"Results saved to: {OUTPUT_PATH}")

if __name__ == "__main__":
    main()
