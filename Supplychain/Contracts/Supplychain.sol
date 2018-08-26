pragma solidity ^0.4.24;

contract RegistrarContract{
    address ownerAddr;
    
    struct RC{
        address accAddr;			// Account address of user
		address sumAddr;			// Summary address of user
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
    
    function NewRecord(uint64 id_number, address accAddr) onlyOwner public{
        rc.accAddr = accAddr;
		rc.sumAddr = new SummaryContract(accAddr);
        
        Users[id_number] = rc;
    }
    
    function GetInfo(uint64 id_number) public view returns(address, address){
        return (Users[id_number].accAddr, Users[id_number].sumAddr);
    }
}

contract SummaryContract{
	address ownerAddr;
	int total_pcr = 0;
	
	struct PCR{
		address pcrAddr;
		string pcrAbtract;
		string pcrParticipant;
		bool pcrStatus;
	}
	PCR pcr;
	
	modifier onlyOwner{
		require(msg.sender == ownerAddr);
		_;
	}
	
	constructor(address owner) public{
		ownerAddr = owner;
	}
}

contract SupplyContract {
	
}