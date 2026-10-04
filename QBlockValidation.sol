// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract QBlockValidation {
    struct UpdateCommitment {
        address submitter;
        bytes32 didHash;
        bytes32 vcHash;
        bytes32 payloadHash;
        uint256 nonce;
        uint256 modelVersion;
        uint256 timestamp;
    }

    mapping(bytes32 => bool) public revokedCredentials;
    mapping(address => mapping(uint256 => bool)) public usedNonces;
    mapping(bytes32 => UpdateCommitment) public commitments;

    event CredentialRevoked(bytes32 indexed vcHash);
    event UpdateAccepted(bytes32 indexed commitmentId, address indexed submitter, uint256 modelVersion);

    function revokeCredential(bytes32 vcHash) external {
        revokedCredentials[vcHash] = true;
        emit CredentialRevoked(vcHash);
    }

    function submitUpdate(
        bytes32 didHash,
        bytes32 vcHash,
        bytes32 payloadHash,
        uint256 nonce,
        uint256 modelVersion
    ) external returns (bytes32) {
        require(!revokedCredentials[vcHash], "revoked credential");
        require(!usedNonces[msg.sender][nonce], "replayed nonce");
        usedNonces[msg.sender][nonce] = true;

        bytes32 commitmentId = keccak256(
            abi.encodePacked(msg.sender, didHash, vcHash, payloadHash, nonce, modelVersion, block.timestamp)
        );

        commitments[commitmentId] = UpdateCommitment({
            submitter: msg.sender,
            didHash: didHash,
            vcHash: vcHash,
            payloadHash: payloadHash,
            nonce: nonce,
            modelVersion: modelVersion,
            timestamp: block.timestamp
        });

        emit UpdateAccepted(commitmentId, msg.sender, modelVersion);
        return commitmentId;
    }
}

