# wasm_contracts_search
Search wasm contracts for a supplied search term (based on substrate pallet contracts)

Extracts the wasm code from the storage function, decodes it to text, and searches for a given term.

I didn't include a requirements file, but you will need the following modules in addition to pandas:
* https://docs.wasmer.io/integrations/examples/instance
* https://github.com/polkascan/py-substrate-interface
