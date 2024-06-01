

project_folder=examples/lottery #inbox
contract_name=Lottery #Inbox

create-project:
	mkdir -p ${project_folder}
	cd ${project_folder} && npm init

install-dependencies:
	make install-basic-dependencies
	make install-solidity-compiler
	make install-test-dependencies
# cd ${project_folder} && \
# npm install 
# dotenv ether alchemy-sdk

install-basic-dependencies:
	cd ${project_folder} && \
	npm install alchemy-sdk dotenv

install-solidity-compiler:
	cd ${project_folder} && \
	npm install solc@0.4.26

create-initial-folders-and-files:
	cd ${project_folder} && \
	mkdir -p contracts && \
	mkdir -p test
	
create-contract-file:
	cd ${project_folder} && \
	touch contracts/${contract_name}.sol

create-compile-file:
	cd ${project_folder} && \
	rm -rf compile.js && \
	touch compile.js && \
	echo "const path = require('path');" >> compile.js && \
	echo "const fs = require('fs');" >> compile.js && \
	echo "const solc = require('solc');" >> compile.js && \
	echo "" >> compile.js && \
	echo "const contractPath = path.resolve(__dirname, 'contracts', '${contract_name}.sol');" >> compile.js && \
	echo "const source = fs.readFileSync(contractPath, 'utf8');" >> compile.js && \
	echo "" >> compile.js && \
	echo "// console.log(solc.compile(source,1).contracts[':${contract_name}']);" >> compile.js && \
	echo "module.exports = solc.compile(source,1).contracts[':${contract_name}'];" >> compile.js
	

compile-contract:
	node --trace-warnings ${project_folder}/compile.js

install-test-dependencies:
	cd ${project_folder} && \
	npm install mocha ganache web3

# create-test-file:
# 	cd ${project_folder}/tests && \
# 	rm -rf ${project_folder}.test.js && \
# 	touch ${project_folder}.test.js && \
# 	echo "const Web3 = require('web3');" >> ${project_folder}.test.js && \
# 	echo "const assert = require('assert');" >> ${project_folder}.test.js && \
# 	echo "const ganache = require('ganache');" >> inb${project_folder}ox.test.js && \
# 	echo "" >> compile.js && \
# 	echo "const web3 = new Web3(ganache.provider());" >> ${project_folder}.test.js

test-contract:
	cd ${project_folder} && \
	npm run test 

# =======================================
# Interacting with wallet

instal-wallet:
	cd ${project_folder} && \
	npm install @truffle/hdwallet-provider

deploy-contract:
	cd ${project_folder} && \
	node deploy.js 
