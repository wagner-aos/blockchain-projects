const { Web3 } = require('web3');
const assert = require('assert');
const ganache = require('ganache');
const web3 = new Web3(ganache.provider());
const { interface, bytecode } = require('../compile');

//Old sintaxe using callbacks
// beforeEach(() => {
//     //Get a list of accounts
//     web3.eth.getAccounts().then( fetchedAccounts => {
//         console.log(fetchedAccounts);
//     });
//     //Use one of the accounts to deploy the contract
// });

let accounts;

beforeEach( async () => {
    //Get a list of accounts
    accounts  = await web3.eth.getAccounts();
    
    //Use one of the accounts to deploy the contract
    inbox = await new web3.eth.Contract(JSON.parse(interface))
        .deploy({ data: bytecode, arguments: ['Hi there!']})
        .send({ from: accounts[0], gas: '1000000'});
});

describe('Inbox', () => {
    it('deploy a contract', () => {
        assert.ok(inbox.options.address);
    });

    it('has a default message', async () => {
        const message = await inbox.methods.message().call();
        assert.equal(message, 'Hi there!');
    });

    it('can change the message', async () => {
        await inbox.methods.setMessage('bye').send({ from: accounts[0] });
        const message = await inbox.methods.message().call();
        assert.equal(message, 'bye');
    })
});


