
from boa.interop.System.Runtime import Notify, CheckWitness, Log


def Main(operation, args):
    if operation == "RunTimeTest":
        user = args[0]
        return RunTimeTest(user)


def RunTimeTest(user):
    Log("11111111")
    res = CheckWitness(user)
    Log(res)
    Notify("Hi BlockChain")
    Notify("s1", "s2", 1, 2, 3)
    Log("log message")
