from contracts.libs.Utils import Revert
from boa.interop.System.Runtime import CheckWitness

def Require(condition):
	"""
	If condition is not satisfied, return false
	:param condition: required condition
	:return: True or false
	"""
	if not condition:
		Revert()
	return True

def RequireScriptHash(key):
    """
    Checks the bytearray parameter is script hash or not. Script Hash
    length should be equal to 20.
    :param key: bytearray parameter to check script hash format.
    :return: True if script hash or revert the transaction.
    """
    Require(len(key) == 20)
    return True

def RequireWitness(witness):
	"""
	Checks the transaction sender is equal to the witness. If not
	satisfying, revert the transaction.
	:param witness: required transaction sender
	:return: True if transaction sender or revert the transaction.
	"""
	Require(CheckWitness(witness))
	return True