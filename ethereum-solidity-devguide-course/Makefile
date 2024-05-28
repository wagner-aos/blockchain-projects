


create-inbox-project:
	mkdir -p inbox
	cd inbox && npm init

install-dependencies:
	cd inbox && \
	npm install 
# dotenv ether alchemy-sdk

install-inbox-solidity-compiler:
	cd inbox && \
	npm install solc@0.4.26

create-inbox-initial-folders-and-files:
	cd inbox && \
	mkdir -p contracts && \
	mkdir -p test
	
create-inbox-contract-file:
# touch contracts/Inbox.sol

create-inbox-compile-file:
	cd inbox && \
	rm -rf compile.js && \
	touch compile.js && \
	echo "const path = require('path');" >> compile.js && \
	echo "const fs = require('fs');" >> compile.js && \
	echo "const solc = require('solc');" >> compile.js && \
	echo "" >> compile.js && \
	echo "const inboxPath = path.resolve(__dirname, 'contracts', 'Inbox.sol');" >> compile.js && \
	echo "const source = fs.readFileSync(inboxPath, 'utf8');" >> compile.js && \
	echo "" >> compile.js && \
	echo "// console.log(solc.compile(source,1).contracts[':Inbox']);" >> compile.js && \
	echo "module.exports = solc.compile(source,1).contracts[':Inbox'];" >> compile.js
	

compile-inbox:
	node --trace-warnings inbox/compile.js

install-inbox-test-dependencies:
	cd inbox && \
	npm install mocha ganache web3

# create-inbox-test-file:
# 	cd inbox/tests && \
# 	rm -rf inbox.test.js && \
# 	touch inbox.test.js && \
# 	echo "const Web3 = require('web3');" >> inbox.test.js && \
# 	echo "const assert = require('assert');" >> inbox.test.js && \
# 	echo "const ganache = require('ganache');" >> inbox.test.js && \
# 	echo "" >> compile.js && \
# 	echo "const web3 = new Web3(ganache.provider());" >> inbox.test.js

test-inbox:
	cd inbox && \
	npm run test 

# =======================================
# Interacting with wallet

install-inbox-wallet:
	cd inbox && \
	npm install @truffle/hdwallet-provider

deploy-inbox:
	cd inbox && \
	node deploy.js 
