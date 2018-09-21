
from boa.interop.System.Contract import Destroy


def Main(operation, args):
    if operation == "Destroy":
        return DestroyContract()
    if operation == "Migrate":
        code = args[0]
        return Migrate(code)


def DestroyContract():
    Destroy()
    return True


def Migrate(code):
    Migrate(code, True, "", "", "", "", "")
    return True
