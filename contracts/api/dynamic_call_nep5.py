from boa.interop.Neo.App import RegisterAppCall
from boa.interop.System.Runtime import Log

YouLeContract = RegisterAppCall('731aa306346c486c126d86b17624f8e970b097ee', 'operation', 'a', 'b', 'c')


def Main(operation, args):
    if operation == "CallNep5Contract":
        Log("1111111111")
        if len(args) != 4:
            return False
        from_acct = args[0]
        to_acct = args[1]
        value = args[2]
        hash_a = args[3]
        return CallNep5Contract(from_acct, to_acct, value, hash_a)


def CallNep5Contract(from_acct, to_acct, value, contractHash):
    Log("222222222")
    res = YouLeContract("transfer", from_acct, to_acct, value)
    if res != "\x01":
        raise Exception()
    return True


