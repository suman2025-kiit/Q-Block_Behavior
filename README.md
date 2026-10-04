# Q-Block_Behavior

Simulation-driven modelling of blockchain-integrated quantum trust for poisoning-resilient federated learning in Internet-of-Behaviour-of-Things (IoBT) networks.

## Overview

`Q-Block_Behavior` is a reproducible Python package for simulating secure model-update exchange in IoBT networks. The framework combines:

- TON_IoT network-flow preprocessing.
- Stratified sampling and non-IID client partitioning.
- Quantum-inspired anomaly scoring using a four-qubit ZZ feature-map interface.
- Smart-contract-style validation of DID, verifiable credential, nonce, revocation, signature, and commitment fields.
- Poisoning attack injection for label flipping, sign flipping, Gaussian noise, and model replacement.
- Robust update screening using a coordinate-wise median reference.
- Adaptive trust computation and trust-weighted federated aggregation.
- Layer-2/App-chain batching cost simulation for audit commitments.

The package is intended for research reproduction, ablation studies, and manuscript artifact release. It does not claim deployment on physical quantum hardware or production blockchain infrastructure.

## Repository Structure

```text
qblock_behavior/
  core/
    attacks.py              Attack injection for FL updates
    blockchain.py           DID, VC, signature, nonce, revocation, and commitment checks
    data.py                 TON_IoT loading, cleaning, scaling, PCA, and partitions
    federated.py            Local clients, update simulation, aggregation, and rounds
    metrics.py              Classification and attack metrics
    quantum.py              ZZ feature-map interface and VQC-style anomaly model
    trust.py                Poisoning risk, consistency score, and adaptive trust
  experiments/
    run_experiment.py       Main reproducible simulation entry point
  utils/
    hashing.py              Keccak/SHA3 commitment utilities
config/
  default.yaml              Main experiment configuration
data/
  README.md                 Dataset placement instructions
docs/
  CITATION.bib              Dataset and project citation examples
smart_contracts/
  QBlockValidation.sol      Minimal Solidity validation contract skeleton
tests/
  test_trust.py             Unit tests for trust scoring
```

## Dataset

Download the TON_IoT dataset from:

https://research.unsw.edu.au/projects/toniot-datasets

Place the network file in:

```text
data/Train_Test_Network.csv
```

The manuscript setting used:

- 461,043 records.
- 45 columns.
- 300,000 benign records.
- 161,043 malicious records.
- Attack classes including DDoS, injection, password, ransomware, backdoor, scanning, XSS, and MITM.

The default configuration samples 20,000 stratified records using seed `42`, preserving the benign/malicious split.

## Installation

Create a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

For optional Qiskit execution:

```bash
pip install qiskit==1.2.4 qiskit-aer==0.15.1 qiskit-machine-learning==0.8.2
```

The default implementation includes a deterministic NumPy fallback so the repository can run on machines without Qiskit.

## Quick Start

Run the default experiment:

```bash
python -m qblock_behavior.experiments.run_experiment --config config/default.yaml
```

Run a small smoke test without the full dataset:

```bash
python -m qblock_behavior.experiments.run_experiment --synthetic --rounds 3
```

Run unit tests:

```bash
pytest -q
```

## Main Workflow

1. Load TON_IoT network-flow records.
2. Remove direct identifiers such as timestamp, IP address, ports, and attack type.
3. Convert labels to binary benign/malicious values.
4. Apply train-fold median/mode imputation, one-hot encoding, min-max scaling, and PCA.
5. Select four components for the quantum feature-map interface.
6. Partition records across IoBT clients using non-IID Dirichlet allocation.
7. Generate local updates and inject adversarial updates.
8. Validate DID, VC, nonce, revocation, signature, and commitment conditions.
9. Compute update consistency and poisoning risk against a coordinate-wise median reference.
10. Aggregate accepted updates using adaptive trust weights.
11. Record audit commitments using Layer-2/App-chain batching simulation.
12. Report detection, false-positive rate, attack success rate, accuracy, and latency estimates.

## Reproducibility Settings

The manuscript-compatible configuration uses:

- Python 3.10 or later.
- NumPy 1.26.x.
- Qiskit 1.2.4, Aer 0.15.1, and Qiskit Machine Learning 0.8.2 for quantum simulation.
- Stratified 10-fold evaluation.
- Seed set `{11, 23, 37, 51, 79}` for repeated experiments.
- Federated clients `K = 20`.
- Non-IID Dirichlet parameter `alpha = 0.5`.
- Federated rounds `T = 30`.
- Local epochs `2`.
- Batch size `32`.
- Adam optimizer learning rate `0.01`.
- Malicious participant ratio `20%`.

## Configuration

Edit `config/default.yaml` to change dataset location, client count, attack type, trust threshold, and batching parameters.

Important fields:

```yaml
dataset:
  path: data/Train_Test_Network.csv
  sample_size: 20000
  seed: 42

federated:
  clients: 20
  rounds: 30
  malicious_fraction: 0.20

trust:
  tau_trust: 0.70
  eta: 0.80
  omega_consistency: 0.50
  omega_poisoning: 0.50
```

## Security Model

The simulation considers:

- Malicious IoBT devices submitting poisoned model updates.
- Replay of previously valid transactions.
- Credential forgery and revoked credential reuse.
- Impersonation of registered devices.
- Off-chain artifact tampering.
- Collusive adversarial clients.

The present package does not model full denial-of-service attacks against an entire blockchain network, physical device compromise, or physical quantum-hardware noise unless custom extensions are added.

## Citation

Use the BibTeX entries in `docs/CITATION.bib` for the TON_IoT dataset and this software artifact.

## Notes for GitHub Upload

Before uploading:

1. Keep the TON_IoT CSV outside the repository if redistribution is restricted.
2. Commit only the `data/README.md` placeholder.
3. Add experimental outputs to a separate `results/` folder or release artifact.
4. Update the author list, affiliation, and manuscript citation in `docs/CITATION.bib`.
5. Mention in the repository description that the project is a simulation artifact for IoBT security research.

