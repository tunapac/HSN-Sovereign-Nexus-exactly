// SPDX-License-Identifier: Huma-Sovereign
pragma solidity ^0.8.20;

contract HAtom {
    mapping(address => uint256) public balances;
    mapping(address => uint256) public collateral;
    uint256 public constant PEG_RATIO = 100;

    event Mint(address indexed user, uint256 amount);
    event Burn(address indexed user, uint256 amount);

    function mintHAtom(uint256 _amount) public {
        emit Mint(msg.sender, _amount);
    }

    function redeemHAtom(uint256 _amount) public {
        emit Burn(msg.sender, _amount);
    }
}
