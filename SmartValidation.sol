// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract SmartValidation {
    mapping(bytes32 => bool) public validatedRecords;

    function validateRecord(bytes32 recordHash) public {
        validatedRecords[recordHash] = true;
    }

    function isValidated(bytes32 recordHash) public view returns (bool) {
        return validatedRecords[recordHash];
    }
}
