"""
An Example on domain auction
"""
from boa.interop.System.Storage import *
from boa.interop.System.Runtime import *
from boa.interop.System.ExecutionEngine import *
from boa.builtins import concat
from boa.interop.Ontology.Native import *

ctx = GetContext()
selfAddr = GetExecutingScriptHash()

def Main(operation, args):

    if operation == 'register':
        acct = args[0]
        url = args[1]
        if CheckWitness(acct) == True:
            return register(acct,url)
        Notify('CheckWitness failed!')
        return False
    
    if operation == 'sell':
        acct = args[0]
        url = args[1]
        price = args[2]
        if CheckWitness(acct) == True:
            return sell(acct,url,price)
        Notify('CheckWitness failed!')
        return False

    if operation == 'query':
        url = args[0]
        return query(url)

    if operation == 'buy':
        acct = args[0]
        url = args[1]
        price = args[2]
        if CheckWitness(acct) == True:
            return buy(acct,url,price)
        Notify('CheckWitness failed!')
        return False

    if operation == 'transfer':
        fromacct = args[0]
        amount = args[1]
        return transferONT(fromacct,selfAddr,amount)

    Notify('Not a supported operation!')
    return True


def register(account,domain):

    if not Get(ctx,domain):
        Put(ctx,domain,account)
        Notify('register succeed!')
        return True
    Notify('already registered!')
    return False

def sell(account,url, price):
    owner = Get(ctx,url)
    if owner == account :
        Put(ctx,concat('Original_Owner_',url),account)
        Put(ctx,concat('Price_',url),price)
        Put(ctx,url,selfAddr)
        Notify('sell succeed!')
        return True
    Notify('Not a owner')
    return False

def query(url):
    owner = Get(ctx,url)
    Notify(concat('owner is ',owner))
    return owner

def buy(acct,url,price):
    owner = Get(ctx,url)
    if owner != selfAddr:
        Notify("url not in sale!")
        return False

    prevBuyer = Get(ctx,concat('TP_',url))
    currentPrice = Get(ctx,concat('Price_',url))
    if not prevBuyer:
        if price >= currentPrice:
            if transferONT(acct,selfAddr,price) == True:
                Put(ctx,concat('TP_',url),acct)
                if price > currentPrice:
                    Put(ctx,concat('Price_',url),price)
                Notify('buy succeed!')
                return True
            else:
                Notify('Transfer Failed')
                return False
        Notify('Price is lower than current price')
        return False

    if price <= currentPrice:
        Notify('Price is lower than current price')
        return False
    #todo refund current price to prevbuyer
    if transferONT(selfAddr,acct,currentPrice) == True:
        Put(ctx,concat('TP_',url),acct)
        Put(ctx,concat('Price_',url),price)
        Notify('buy succeed!')
        return True
    else:
        Notify('refund failed')
        return False

def transferONT(fromacct,toacct,amount):
    if CheckWitness(fromacct) == True:
        contractAddress = bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01')
        param = [fromacct,toacct,amount]
        res = Invoke(param,'transfer',contractAddress,1)
        if res and res[0] == b'x01':
            return True
        else:
            return False

    else:
        Notify('checkWitness failed')
        return False

