# Q-Block_Behavior with Trust
Quantum-Blockchain Meets Internet-of- Behavior for Smarter and Secure Consumer Electronics


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


## Quantum Block Behavior based Adaptive Trust Model

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

# Q-Block_Behavior

GitHub-ready reference implementation for **Q-Block_Behavior: Quantum-Assisted
Poisoning Detection and Blockchain-Enabled Adaptive Trust for Secure
Internet-of-Behaviors Systems**.

The repository coordinates the five manuscript algorithms:

1. IoB preprocessing and artifact construction;
2. four-component quantum encoding, GHZ-reference fidelity, and prediction;
3. DID/VC, signature, revocation, nonce, timestamp, and hash validation;
4. two-pass poisoning detection and trust-weighted aggregation;
5. seeded validation against label flipping, sign flipping, Gaussian noise, and
   model replacement.

## Scientific-use statement

The executable demo generates synthetic model updates to test the workflow. It
does **not** manufacture the manuscript's TON_IoT classification results. The
published Table 5 values are stored separately in
`reference/manuscript_table5.csv` for traceability and are never substituted for
computed output. Reproducing the paper requires the public
`Train_Test_Network.csv` file and the same software/hardware environment stated
in the manuscript.

## Implemented equations and controls

For authenticated device updates, Algorithm 4 first constructs the
coordinate-wise median reference and then calculates:

```text
C_i = (1 + cosine(update_i, reference)) / 2
D_i = ||update_i-reference||_2 / (||reference||_2 + epsilon)
P_i = min(1, omega_1*D_i + omega_2*(1-cosine)/2)
R_i(t) = eta*R_i(t-1) + (1-eta)*V_i(t)
T_i = clip(alpha*F_i + beta*V_i + gamma*R_i + delta*C_i-lambda*P_i, 0, 1)
w_i = T_i*n_i / sum_j(T_j*n_j)
```

An update is accepted only if `V_i=1` and `T_i>=0.70`. If no update is
accepted, the gateway retains the previous global model.

## Repository map

```text
config/manuscript.json                 Paper-aligned parameters
src/qblock_poisoning/preprocessing.py  TON_IoT loading and fold-safe transforms
src/qblock_poisoning/quantum.py        ZZ-inspired state and GHZ fidelity
src/qblock_poisoning/identity.py       Algorithm 3 off-chain validator
src/qblock_poisoning/core.py           Algorithm 4 trust aggregation
src/qblock_poisoning/attacks.py        Four attack implementations
src/qblock_poisoning/simulation.py     Algorithm 5 coordinator
src/qblock_poisoning/audit.py          Canonical commitments and L2 batches
contracts/QBlockValidation.sol         Solidity 0.8.24 validation contract
hardhat/                               Deployment and contract tests
tests/                                 Unit and end-to-end tests
reference/manuscript_table5.csv        Reported values, clearly separated
outputs/                               Reproducible computed demonstration
```

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m pip install -e .
qblock-poisoning simulate --config config/manuscript.json --output-dir outputs
pytest -q
```

The simulation writes `device_decisions.csv`, `round_metrics.csv`,
`attack_summary.csv`, `l2_commitments.jsonl`, and `sample_run.txt`.

## TON_IoT preprocessing

Download `Train_Test_Network.csv` from the official TON_IoT source; do not
commit the dataset to GitHub. Prepare the reproducible subset:

```bash
qblock-poisoning prepare-data --csv data/Train_Test_Network.csv \
  --output-dir outputs/prepared --seed 42 --sample-size 20000
```

The command removes timestamps, source/destination IP addresses, ports, and
`type`; preserves the binary label and attack distribution; and saves selected
row indices. Fit imputation, one-hot encoding, scaling, PCA, and feature ranking
inside each training fold only.

## Quantum module

The four selected components enter a twice-repeated, linearly entangled
ZZ-inspired simulator. A separately prepared four-qubit GHZ state is used only
as the fidelity reference; it is not every sample's encoded state. The NumPy
implementation makes CI lightweight. `requirements-quantum.txt` lists the
paper's Qiskit/Aer replication versions.

## Smart contract

The Solidity contract records issuers, credentials, used nonces, artifact
commitments, and global-model commitments. Run it using:

```bash
cd hardhat
npm install
npx hardhat test
```

Use chain ID 31337. Never place raw behavioral records or model vectors on
chain; submit only commitments and validation metadata.

## Metrics

- DR = quarantined malicious updates / all malicious updates.
- FPR = quarantined benign updates / all benign updates.
- update bypass rate = accepted malicious updates / all malicious updates.
- downstream ASR = successful predefined global-model attack objectives /
  attack trials. It requires a trained task model and differs from update-level
  false negatives.

The synthetic demo reports bypass rate under its correct name. It does not
relabel it as downstream ASR.

## Reproducibility defaults

The configuration uses 20 devices, 30 rounds, two local epochs, batch size 32,
learning rate 0.01, 20% malicious devices, Dirichlet alpha 0.5, trust threshold
0.70, reliability eta 0.80, equal poisoning weights, 4,096 shots, and seeds 11,
23, 37, 51, and 79.
<img width="1049" height="632" alt="Poison_JISA" src="https://github.com/user-attachments/assets/5f3360fa-d48a-46ca-bbb6-43f88ac3518f" />

## Citation and license

See `CITATION.cff`. Code is released under the MIT License. Dataset and
third-party licenses remain with their respective owners.




## Ruuning using the dataset

while running the same using the running commands , please store the dataset in appropriate path
as we have set it as - DATA_PATH = "data/real_time_iob_runtime_dataset.csv", but we are providing some part of the dataset as "Q-Block_Behaviour-dataset.csv" for your reference.


