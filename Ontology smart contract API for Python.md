# Ontology smart contract API for Python



| No   | Package                            | Name                   | Parameter                                | Comments                                 |
| ---- | ---------------------------------- | ---------------------- | ---------------------------------------- | ---------------------------------------- |
| 1    | boa.interop.System.Action          | RegisterAction         | event_name, *args                        | register a notirfy event                 |
| 2    | boa.interop.System.App             | RegisterAppCall        | smart_contract_hash, *args               | call other smart contract                |
| 3    | boa.interop.System.Block           | GetTransactionCount    | block                                    | get transaction count of block           |
| 4    | boa.interop.System.Block           | GetTransactions        | block                                    | get transactions of block                |
| 5    | boa.interop.System.Block           | GetTransaction         | block , index                            | get the transaction by index             |
| 6    | boa.interop.System.BlockChain      | GetHeight              |                                          | get height of block chain                |
| 7    | boa.interop.System.BlockChain      | GetHeader              | height or hash                           | get header by height or hash             |
| 8    | boa.interop.System.BlockChain      | GetBlock               | height or hash                           | get block by height or hash              |
| 9    | boa.interop.System.BlockChain      | GetTransaction         | hash                                     | get transaction by hash                  |
| 10   | boa.interop.System.BlockChain      | GetContract            | script_hash                              | get contract by script hash              |
| 11   | boa.interop.System.Contract        | GetScript              | contract                                 | get contract script hash                 |
| 12   | boa.interop.System.Contract        | GetStorageContext      | contract                                 | get contract storage context             |
| 13   | boa.interop.System.Contract        | Create                 | script, paramter_list, return_type,properties,name, version,authoer,email,description | create a contract                        |
| 14   | boa.interop.System.Contract        | Migrate                | script, paramter_list, return_type,properties,name, version,authoer,email,description | migrate  contract                        |
| 15   | boa.interop.System.Contract        | Destroy                |                                          | destroy current contract(self)           |
| 16   | boa.interop.System.ExecutionEngine | GetScriptContainer     |                                          | get the current script container of a smart contract execution |
| 17   | boa.interop.System.ExecutionEngine | GetExecutingScriptHash |                                          | get the hash of the script ( smart contract ) which is currently being executed |
| 18   | boa.interop.System.ExecutionEngine | GetCallingScriptHash   |                                          | get the hash of the script ( smart contract ) which began execution of the current script. |
| 19   | boa.interop.System.ExecutionEngine | GetEntryScriptHash     |                                          | get the hash of the script ( smart contract ) which began execution of the smart contract. |
| 20   | boa.interop.System.Header          | GetIndex               | header                                   | get the height/index of header           |
| 21   | boa.interop.System.Header          | GetHash                | header                                   | get the hash of header                   |
| 22   | boa.interop.System.Header          | GetVersion             | header                                   | get the version of header                |
| 23   | boa.interop.System.Header          | GetPreHash             | header                                   | get the hash of the previous header in the blockchain |
| 24   | boa.interop.System.Header          | GetMerkleRoot          | header                                   | get the merkle root of the transactions contained in the block |
| 25   | boa.interop.System.Header          | GetTimestamp           | header                                   | get the timestamp of when the header was created |
| 26   | boa.interop.System.Header          | GetConsensusData       | header                                   | get the address of the consensus         |
| 27   | boa.interop.System.Header          | GetNextConsensus       | header                                   | get the address where the next consensus will occur |
| 28   | boa.interop.System.Runtime         | GetTrigger             |                                          | get trigger                              |
| 29   | boa.interop.System.Runtime         | CheckWitness           | hash or pubkey                           | check the witness of address             |
| 30   | boa.interop.System.Runtime         | Log                    | message                                  | print log on node                        |
| 31   | boa.interop.System.Runtime         | Notify                 | arg                                      | add notify to event                      |
| 32   | boa.interop.System.Runtime         | GetTime                |                                          | get timestamp of most recent block       |
| 33   | boa.interop.System.Runtime         | Serialize              | item                                     | serialize item to byte array             |
| 34   | boa.interop.System.Runtime         | Deserialize            | bytes                                    | deserialize byte array to item           |
| 35   | boa.interop.System.Storage         | GetContext             |                                          | get the storage context                  |
| 36   | boa.interop.System.Storage         | Get                    | context, key                             | get the storage by key                   |
| 37   | boa.interop.System.Storage         | Put                    | context, key, value                      | put the key-value storage                |
| 38   | boa.interop.System.Storage         | Delete                 | context, key                             | delete storage by key                    |
| 39   | boa.interop.System.Transaction     | GetTXHash              | transaction                              | get transaction hash                     |
| 40   | boa.interop.System.Transaction     | GetType                | transaction                              | get transaction type                     |
| 41   | boa.interop.System.Transaction     | GetAttributes          | transaction                              | get transaction attributes               |
| 42   | boa.interop.System.Attribute       | GetUsage               | attribute                                | get transaction attribute usage          |
| 43   | boa.interop.System.Attribute       | GetData                | attribute                                | get transaction attribute data           |
| 44   | boa.interop.Ontology.Native        | Invoke                 | param, method, contractaddress, version  | invoke native contract                   |
| 45   | boa.interop.Ontology.Runtime       | Base58ToAddress        | arg                                      | transfer base58 address to byte array    |
| 46   | boa.interop.Ontology.Runtime       | AddressToBase58        | arg                                      | byte array address to base58             |
| 47   | boa.interop.Ontology.Runtime       | GetRandomHash          |                                          | get current block hash                   |
| 48   | boa.buildins                       | ToScriptHash           | arg                                      | const base58 address to byte array       |
| 49   | boa.buildins                       | concat                 | str1 , str2                              | concat 2 string                          |
| 50   | boa.buildins                       | sha1                   | data                                     | hash data with sha1                      |
| 51   | boa.buildins                       | sha256                 | data                                     | hash data with sha256                    |
| 52   | boa.buildins                       | hash160                | data                                     | hash data with hash160                   |
| 53   | boa.buildins                       | hash256                | data                                     | hash data with hash                      |
