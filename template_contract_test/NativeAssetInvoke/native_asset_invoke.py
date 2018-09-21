from boa.interop.Ontology.Native import Invoke
from boa.builtins import ToScriptHash

OntContract = ToScriptHash("AFmseVrdL9f9oyCzZefL9tG6UbvhUMqNMV")
OngContract = ToScriptHash("AFmseVrdL9f9oyCzZefL9tG6UbvhfRZMHJ")


def Main(operation, args):
    if operation == "RecycleAsset":
        return RecycleAsset()


def RecycleAsset(from_acct, to_acct, ont, ong):
    ret = bytearray()
    transfer = state(from_acct, to_acct, ont)
    ret = Invoke(0, OntContract, "transfer", [transfer])
    if ret != b'\x01':
        raise Exception("tansfer ont error.")
    transfer = state(from_acct, to_acct, ong)
    ret = Invoke(0, OngContract, "transfer", [transfer])
    if ret != b'\x01':
        raise Exception("tansfer ont error.")
    return True