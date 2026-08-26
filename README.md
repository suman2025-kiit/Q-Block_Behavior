# Q-Block_Behavior with Trust
Quantum-Blockchain Meets Internet-of- Behavior for Smarter and Secure Consumer Electronics
<img width="136" height="206" alt="image" src="https://github.com/user-attachments/assets/723adcd3-2443-451d-af64-a2807402d7c4" />

##Pre-requisits 
# Q-Block_Behavior

Q-Block_Behavior is a quantum-blockchain-enabled Internet of Behavior (IoB) framework for secure and intelligent consumer electronics. The framework integrates multi-domain behavioral data, quantum machine learning, GHZ-state validation, and blockchain-based smart contract verification for anomaly/fraud detection, trust evaluation, and privacy-preserving analytics.

## Features
- Multi-domain IoB data aggregation
- Four-qubit GHZ-state generation and validation
- ZZ feature map-based quantum encoding
- QML-based anomaly/fraud prediction
- Smart contract-driven blockchain verification
- Trust evaluation using fidelity, validation, and behavioral reliability
- ROC-AUC, accuracy, and latency evaluation

## Repository Modules
- `data_aggregation.py` : Preprocessing and aggregation of IoB data
- `quantum_model.py` : GHZ generation, ZZ encoding, quantum inference
- `blockchain_validation.py` : Hashing, DID binding, smart contract validation
- `trust_evaluation.py` : Trust-score computation
- `metrics.py` : Accuracy, ROC-AUC, latency, and reporting

## Installation
```bash
git clone https://github.com/<your-username>/Q-Block_Behavior.git
cd Q-Block_Behavior
pip install -r requirements.txt

 ## For ruiing and getting the output
Run
python main.py
Input
IoB dataset with behavioral features and labels
Reference GHZ state
Fidelity threshold
Blockchain metadata and DID records
Output
Predicted labels
Fidelity scores
Trust scores
Blockchain hash records
Accuracy, ROC-AUC, and latency results.


#**Q-Block_Behavior Adaptive Trust Model**

Reference implementation of the Adaptive Trust Model used between local
quantum-classical training and blockchain-validated global aggregation.

For device `i` at round `t`, the implementation computes:

```text
R_i(t) = eta R_i(t-1) + (1-eta) V_i(t)
C_i(t) = 0.5 * [1 + cosine(delta_i, delta_ref)]
T_i(t) = clip(alpha F_i + beta V_i + gamma R_i
              + delta C_i - lambda P_i, 0, 1)
```

An update is accepted only when its smart-contract validation flag is `1`
and `T_i(t) >= tau_T`. Accepted models are aggregated using
`T_i(t) * n_i` as their weights.

## Repository contents

- `qblock_trust/model.py`: trust evaluation and aggregation.
- `demo.py`: reproducible round with valid, invalid, and poisoned devices.
- `tests/test_model.py`: unit tests for the main security properties.
- `contracts/QBlockValidation.sol`: compact Solidity validation gateway that
  emits the validation flag consumed by the Python trust model.

## Run

```bash
python -m pip install -r requirements.txt
python demo.py
python -m unittest discover -s tests -v
```

The demo is deterministic and does not train a QML circuit. Replace its local
model arrays and fidelity values with outputs from the Qiskit/QML pipeline, and
replace the simulated validation flags with contract event or call results.

## Smart-contract correlation

1. Submit the DID/credential/signature/artifact-hash evidence to the validation
   contract.
2. Read `validationFlag` from `RecordValidated` (or the stored record).
3. Build `DeviceSubmission` with this flag, fidelity, sample count, and local
   parameters.
4. Call `AdaptiveTrustModel.aggregate_round(...)`.
5. Commit the returned global-model hash and trust scores on-chain.

This code is a research prototype; production deployments must use audited
credential, DID-signature, nonce, and Ethereum Keccak-256 verification.


## Ruuning using the dataset

while running the same using the running commands , please store the dataset in appropriate path
as we have set it as - DATA_PATH = "data/real_time_iob_runtime_dataset.csv", but we are providing some part of the dataset as "Q-Block_Behaviour-dataset.csv" for your reference.
