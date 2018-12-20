import os
import platform

from twisted.internet import defer

from .. import data, helper
from p2pool.util import pack


P2P_PREFIX = 'ba3c2bef'.decode('hex')
P2P_PORT = 9838
ADDRESS_VERSION = 68
SCRIPT_ADDRESS_VERSION = 18
RPC_PORT = 9338
RPC_CHECK = defer.inlineCallbacks(lambda uniod: defer.returnValue(
            'unioaddress' in (yield uniod.rpc_help()) and
            not (yield uniod.rpc_getinfo())['testnet']
        ))
BLOCKHASH_FUNC = lambda data: pack.IntType(256).unpack(__import__('unio_hash').getPoWHash(data))
POW_FUNC = lambda data: pack.IntType(256).unpack(__import__('unio_hash').getPoWHash(data))
BLOCK_PERIOD = 150 # s
SYMBOL = 'UOC'
CONF_FILE_FUNC = lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'UnioCore') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/UnioCore/') if platform.system() == 'Darwin' else os.path.expanduser('~/.uniocore'), 'unio.conf')
BLOCK_EXPLORER_URL_PREFIX = 'https://explorer.dash.org/block/'
ADDRESS_EXPLORER_URL_PREFIX = 'https://explorer.dash.org/address/'
TX_EXPLORER_URL_PREFIX = 'https://explorer.dash.org/tx/'
SANE_TARGET_RANGE = (2**256//2**32//1000000 - 1, 2**256//2**32 - 1)
DUST_THRESHOLD = 0.001e8
