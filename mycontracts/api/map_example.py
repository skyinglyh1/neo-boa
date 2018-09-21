
from boa.interop.System.Runtime import Notify, Serialize, Deserialize
from boa.interop.System.Storage import GetContext, Put, Get

ctx = GetContext()


def Main(operation, args):
    if operation == "MapTest":
        return MapTest()


def MapTest():
    m = {}
    m["k1"] = 100
    m["k2"] = 200
    Notify(m["k1"])
    Notify(m["k2"])
    b = Serialize(m)
    Put(ctx, "mapexample", b)

    v = Get(ctx, "mapexample")
    m2 = Deserialize(v)
    Notify(m2["k1"])
    Notify(m2["k2"])
    return True


