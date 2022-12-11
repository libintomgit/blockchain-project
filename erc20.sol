// SPDX-License-Identifier: GPL-3.0

pragma solidity >=0.7.0 <0.9.0;

interface ERC20 {
 
 function totalSupply() external view returns (uint256);
 function balanceOf(address account) external view returns (uint256);
 function transfer(address recipient, uint256 amount) external returns (bool);
 function allowance(address owner, address spender) external view returns (uint256);
 function approve(address spender, uint256 amount) external returns (bool);
 function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
 
 event Transfer(address indexed from, address indexed to, uint256 value);
 event Approval(address indexed owner, address indexed spender, uint256 value);
}


contract MySpecialTokenSHIB3 is ERC20{


    mapping (address => uint256) balances;

    //allowances
    mapping(address => mapping(address => uint256)) private _allowances;


    function balanceOf(address account) public override view returns (uint256) {
        uint256 myBalance;
        myBalance = balances[account];
        return myBalance;
    }

    string private _name;
    string private _symbol;
    uint8 private _decimals;


    address public owner;

    // step 1 make a variable to store total supply
    uint256 private _totalSupply;

    // this runs when the contract is deployed
    constructor() {
    // **msg.sender** is the account that digitally signed the tx
    owner = msg.sender;
    _totalSupply = 1000000;
   _decimals = 18;
    balances[owner] = _totalSupply * 10**uint(_decimals);

    _name = "SHB_04420";
    _symbol = "SHB";
    }

    function name() public view returns ( string memory ) {
        return _name;
    }

    function symbol() public view returns (string memory) {
        return _symbol;
    }

    function decimals() public view returns (uint8) {
        return _decimals;
    }
    
    function allowance(address owner, address spender) public override view returns (uint256){
        return _allowances[owner][spender];
    }

    function totalSupply() public view override returns (uint256) {
        return _totalSupply;
    }

    function getOwner() public view returns (address) {
        return owner;
    }


    function transferFrom(address sender, address recipient, uint256 amount) public override returns (bool){
        balances[recipient] = balances[recipient] - amount;
        emit Transfer(sender, recipient, amount);

        _allowances[sender][recipient] = amount;
        emit Approval(sender, recipient, amount);
        return true;
    }


    function transfer(address recipient, uint256 amount) public override returns(bool) {
        address sender;
        sender = msg.sender;
        balances[sender] = balances[sender] - amount;
        balances[recipient] = balances[recipient] + amount;
        emit Transfer(sender, recipient, amount);
        return true;
    }

// function approve(address spender, uint256 amount) external returns (bool);

function approve(address spender, uint256 amount) public override returns (bool) {
    address sender;
    sender = msg.sender;
    _allowances[sender][spender] = amount;
    emit Approval(sender, spender, amount);
}

}
