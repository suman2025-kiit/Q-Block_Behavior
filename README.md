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
# Q-Block_Behavior: Poisoning Detection and Validation

Reference implementation of the poisoning-detection and adaptive-trust stages in
the **Q-Block_Behavior** workflow. The code follows the order used by Algorithms
4–5 of the manuscript:

1. validate each submitted update;
2. build a coordinate-wise median from authenticated updates;
3. calculate update consistency and poisoning risk;
4. update reliability and adaptive trust;
5. accept or quarantine each update;
6. aggregate accepted updates and create a chained audit commitment;
7. report detection rate (DR), false-positive rate (FPR), and update-level attack
   success rate (ASR).

> **Research-use notice:** the bundled demonstration uses synthetic local model
> updates so that reviewers can reproduce the detector without the TON_IoT data
> or a full federated-learning model. Its numerical output is a software test,
> not a reproduction of the manuscript's experimental table.

## Mathematical implementation

For authenticated updates, the robust reference is the coordinate-wise median:

```text
reference = median(update_i)
```

The implementation then evaluates

```text
C_i = (1 + cosine(update_i, reference)) / 2

D_i = ||update_i - reference||_2 / (||reference||_2 + epsilon)

P_i = min(1, omega_1 D_i + omega_2 (1 - cosine(update_i, reference)) / 2)

T_i = clip(alpha F_i + beta V_i + gamma R_i + delta C_i - lambda P_i, 0, 1)
```

Here, `F_i` is the fidelity evidence, `V_i` is the authentication-validation
flag, `R_i` is historical reliability, `C_i` is consistency, and `P_i` is
poisoning risk. An update is accepted only when `V_i = 1` and `T_i >= tau_T`.
All coefficients and thresholds are configurable; the defaults are demonstration
parameters and should be selected on validation data for a reported experiment.

## Repository structure

```text
config/default.json                  Reproducible demonstration settings
src/qblock_poisoning/core.py         Equations (37)–(38), trust, aggregation
src/qblock_poisoning/attacks.py      Four poisoning-attack generators
src/qblock_poisoning/audit.py        Canonical chained audit commitments
src/qblock_poisoning/simulation.py   Coordinated validation experiment
src/qblock_poisoning/cli.py          Command-line entry point
tests/test_core.py                   Unit and integration tests
outputs/                             Generated CSV and terminal evidence
docs/sample_poison_detection_output.jpg  Screenshot from an actual run
```

## Quick start

Python 3.10 or newer is recommended.

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m pip install -e .
qblock-poisoning --config config/default.json --output-dir outputs
pytest
```

To regenerate the JPEG after a run:

```bash
python scripts/render_terminal_screenshot.py \
  outputs/sample_run.txt docs/sample_poison_detection_output.jpg
```

The CLI writes:

- `device_decisions.csv`: per-device fidelity, validation, consistency, risk,
  reliability, trust, ground truth, and decision;
- `round_metrics.csv`: TP, TN, FP, FN, DR, FPR, ASR, accepted count, and audit
  commitment for every round;
- `attack_summary.csv`: attack-level metrics over all seeds and rounds;
- `sample_run.txt`: human-readable run summary used to produce the screenshot.

## Metric definitions

- **DR** = `TP / (TP + FN)`: fraction of malicious updates quarantined.
- **FPR** = `FP / (FP + TN)`: fraction of benign updates quarantined.
- **Update-level ASR** = `FN / (TP + FN)`: fraction of malicious updates that
  bypassed the detector. It equals `100 - DR` in this detector-only demo.

The manuscript may additionally report a **downstream global-model ASR**, defined
by a task-specific attack objective after aggregation. That quantity requires an
actual trained model and test set and is intentionally not invented here. Connect
the returned aggregate to your federated model and implement the objective in the
evaluation layer if you need that metric.

## Connecting to TON_IoT or a federated training loop

Replace `generate_round()` in `simulation.py` with the outputs of local training.
Pass one flattened update vector per device to `evaluate_updates()`, together
with fidelity scores, smart-contract/DID validation flags, prior reliabilities,
and local sample counts. Do not fit preprocessing or choose thresholds using the
test partition.

`audit.py` uses canonical JSON and SHA3-256 so the demo has no blockchain
dependency. Ethereum uses Keccak-256, which differs from standardized SHA3-256;
replace `sha3_256()` with `Web3.keccak()` or the contract's exact ABI encoding
before comparing commitments with Solidity.

## Reproducibility and responsible reporting

The default configuration uses 20 devices, a 20% malicious-device ratio, 30
rounds, and seeds 11, 23, 37, 51, and 79. The attack generators implement label
flipping, sign flipping, Gaussian noise, and model replacement at the update
level. Synthetic behavior is intentionally simple and must not be presented as
TON_IoT or physical-device evidence.

## The complete coding regarding this is uploaded herewith as a .zip file named: "complete_qblock-poisoning-validation.zip"
## License

MIT. Cite the associated manuscript if you use this implementation in research.
<img width="1326" height="749" alt="Poison" src="https://github.com/user-attachments/assets/d2545d99-e3d0-41e8-8865-32eabf05261d" />


## Ruuning using the dataset

while running the same using the running commands , please store the dataset in appropriate path
as we have set it as - DATA_PATH = "data/real_time_iob_runtime_dataset.csv", but we are providing some part of the dataset as "Q-Block_Behaviour-dataset.csv" for your reference.


