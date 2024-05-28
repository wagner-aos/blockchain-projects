const { Alchemy, Network, Wallet, ContractFactory } = require("alchemy-sdk");
const { interface, bytecode } = require('./compile');

const { env } = require('./test.env');
require('dotenv').config(env);

const settings = {
    apiKey: ALCHEMY_API_KEY,
    network: Network.ETH_SEPOLIA,
};
const alchemy = new Alchemy(settings);

const deploy = async function () {
    try {
        const wallet = new Wallet(PRIVATE_KEY, alchemy);

        const ContractInstance = new ContractFactory(interface, bytecode, wallet);

        // Set gas limit and gas price, using the default Ropsten provider
        //const price = ethers.formatUnits(await provider., 'gwei')
        //const options = {gasLimit: 1000000};

        const contractInstance = await ContractInstance.deploy("Hi there!");

        await contractInstance.deployed();

        console.log("Deployed contract address - ", contractInstance.address);

    } catch (err) {
        console.log("Error in deploying contract.");
        console.log(err);
    }
};
 
deploy();








// const config = {
//     apiKey: ALCHEMY_API_KEY,
//     network: Network.ETH_SEPOLIA,
// };



// const deploy = async () => {
//   const accounts = await web3.eth.getAccounts();

//   console.log("Attempting to deploy from account", accounts[0]);

//   const result = await new web3.eth.Contract(JSON.parse(interface))
//     .deploy({ data: bytecode, arguments: ["Hi there!"] })
//     .send({ gas: "1000000", from: accounts[0] });

//   console.log("Contract deployed to", result.options.address);
//   provider.engine.stop();
// };
// deploy();

