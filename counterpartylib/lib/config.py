"""Variables prefixed with `DEFAULT` should be able to be overridden by
configuration file and command‐line arguments."""

UNIT = 100000000        # The same across assets.


# Versions
VERSION_MAJOR = 9
VERSION_MINOR = 55
VERSION_REVISION = 4
VERSION_STRING = str(VERSION_MAJOR) + '.' + str(VERSION_MINOR) + '.' + str(VERSION_REVISION)


# Counterparty protocol
TXTYPE_FORMAT = '>I'
SHORT_TXTYPE_FORMAT = 'B'

TWO_WEEKS = 2 * 7 * 24 * 3600
MAX_EXPIRATION = 4 * 2016   # Two months

MEMPOOL_BLOCK_HASH = 'mempool'
MEMPOOL_BLOCK_INDEX = 9999999


# SQLite3
MAX_INT = 2**63 - 1


# Bitcoin Core
OP_RETURN_MAX_SIZE = 80  # bytes


# Currency agnosticism
BTC = 'LTC'
XCP = 'XLP'

BTC_HALFTIME = 840000

BTC_NAME = 'Litecoin'
XCP_NAME = 'Liteparty'
APP_NAME = XCP_NAME.lower()

DEFAULT_RPC_PORT_TESTNET = 14000
DEFAULT_RPC_PORT = 4000

DEFAULT_BACKEND_PORT_TESTNET = 19332
DEFAULT_BACKEND_PORT = 9332
DEFAULT_BACKEND_PORT_TESTNET_BTCD = 19335
DEFAULT_BACKEND_PORT_BTCD = 9335

UNSPENDABLE_TESTNET = 'myLitepartyXXXXXXXXXXXXXXXXXVHTF2S'
UNSPENDABLE_MAINNET = 'LitepartyXXXXXXXXXXXXXXXXXXXYbYgpf'

ADDRESSVERSION_TESTNET = b'\x6f'
P2SH_ADDRESSVERSION_TESTNET = b'\xc4'
PRIVATEKEY_VERSION_TESTNET = b'\xef'
ADDRESSVERSION_MAINNET = b'\x30'
P2SH_ADDRESSVERSION_MAINNET = b'\x05'
PRIVATEKEY_VERSION_MAINNET = b'\xb0'
MAGIC_BYTES_TESTNET = b'\xfd\xd2\xc8\xf1' 
#MAGIC_BYTES_TESTNET = b'\xfa\xbf\xb5\xda'   # For bip-0010
MAGIC_BYTES_MAINNET = b'\xfb\xc0\xb6\xdb'   # For bip-0010

BLOCK_FIRST_TESTNET_TESTCOIN = 449684
BURN_START_TESTNET_TESTCOIN = 449685
BURN_END_TESTNET_TESTCOIN = 4017708    
BLOCK_FIRST_TESTNET = 449684 #2018-03-08
BLOCK_FIRST_TESTNET_HASH = 'b9f00078e1c27097329a7d48d939d2695540c507817a6b975ef89dff152dbace'
BURN_START_TESTNET = 449685 #2018-03-08 
BURN_END_TESTNET = 9000000 # A long time.

BLOCK_FIRST_MAINNET_TESTCOIN = 1381242
BURN_START_MAINNET_TESTCOIN = 1381245
BURN_END_MAINNET_TESTCOIN = 2500000     # A long time.

BLOCK_FIRST_MAINNET = 1381242
BLOCK_FIRST_MAINNET_HASH = '8f908d66a22c71ad2b35205d3bdb284e208d6b4764edc15ad1aa58cd917b1dc3'
BURN_START_MAINNET = 1381245
BURN_END_MAINNET = 139000 


# Protocol defaults
# NOTE: If the DUST_SIZE constants are changed, they MUST also be changed in counterblockd/lib/config.py as well
    # TODO: This should be updated, given their new configurability.
# TODO: The dust values should be lowered by 90%, once transactions with smaller outputs start confirming faster: <https://github.com/mastercoin-MSC/spec/issues/192>
DEFAULT_REGULAR_DUST_SIZE = 5430         # TODO: This is just a guess. I got it down to 5530 satoshis.
DEFAULT_MULTISIG_DUST_SIZE = 7800        # <https://bitcointalk.org/index.php?topic=528023.msg7469941#msg7469941>
DEFAULT_OP_RETURN_VALUE = 0
DEFAULT_FEE_PER_KB = 250000               # sane/low default, also used as minimum when estimated fee is used
ESTIMATE_FEE_PER_KB = True               # when True will use `estimatefee` from bitcoind instead of DEFAULT_FEE_PER_KB
ESTIMATE_FEE_NBLOCKS = 3

# UI defaults
DEFAULT_FEE_FRACTION_REQUIRED = .009   # 0.90%
DEFAULT_FEE_FRACTION_PROVIDED = .01    # 1.00%


DEFAULT_REQUESTS_TIMEOUT = 20   # 20 seconds
DEFAULT_RPC_BATCH_SIZE = 20     # A 1 MB block can hold about 4200 transactions.

# Custom exit codes
EXITCODE_UPDATE_REQUIRED = 5


DEFAULT_CHECK_ASSET_CONSERVATION = True

BACKEND_RAW_TRANSACTIONS_CACHE_SIZE = 20000
BACKEND_RPC_BATCH_NUM_WORKERS = 6

UNDOLOG_MAX_PAST_BLOCKS = 100 #the number of past blocks that we store undolog history

DEFAULT_UTXO_LOCKS_MAX_ADDRESSES = 1000
DEFAULT_UTXO_LOCKS_MAX_AGE = 3.0 #in seconds

ADDRESS_OPTION_REQUIRE_MEMO = 1
ADDRESS_OPTION_MAX_VALUE = ADDRESS_OPTION_REQUIRE_MEMO # Or list of all the address options

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
