pragma solidity ^0.4.18;

contract RegistrarContract{
    address ownerAddr;
    
    struct RC{
        uint64 id_number;			// ID number of user
        address accAddr;			// Account address of user
    }
    RC rc;
    
    mapping(uint64 => RC) private Users;
    
    modifier onlyOwner{
        require(msg.sender == ownerAddr);
        _;
    }
    
    constructor() public{
        ownerAddr = msg.sender;
    }
    
    function newRecord(uint64 id_number, address accAddr) onlyOwner public{
        rc.id_number = id_number;
        rc.accAddr = accAddr;
        
        Users[id_number] = rc;
    }
    
    function getInfo(uint64 id_number) public view returns(address){
        return (Users[id_number].accAddr);
    }
}

contract Supplychain {
	
}