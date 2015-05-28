from electrum import wallet
import socket
import json
import time
import electrum


def get_from_electrum(method, params=[]):
    params = [params] if type(params) is not list else params
    s = socket.create_connection(('ecdsa.net', 50001))
    s.send(json.dumps({"id": 0, "method": method, "params": params}).encode() + b'\n')
    return json.loads(s.recv(99999)[:-1].decode())

print get_from_electrum('blockchain.address.get_balance', '1CGWVknXB2V5qb6Gj7LZdkrT7hNiQgpXTo')

xpub = '3793dc8b1e6b6eb97f8e1365f1c06048590cf0096116b61b0e0933f59b84d78f81f20ec0b916a39f3c4386ab61bc669b1832b4735eb61de5e4282f0cd273a11b'


c = electrum.SimpleConfig({'wallet_path' : '/home/civilizedgravy/.electrum/wallets/magic_word_wallet'})
s = electrum.daemon.get_daemon(c, True)
network = electrum.NetworkProxy(s, c)
network.start()

while network.is_connecting():
	time.sleep(0.1)

if not network.is_connected():
	print "daemon is not connected"
	sys.exit(1)

wallet_path = str(c.get_wallet_path())
storage = electrum.wallet.WalletStorage(path=wallet_path)



if not storage.file_exists:
	wallet = electrum.wallet.Wallet.from_xpub(xpub, storage)
	
else:
	wallet = electrum.wallet.Wallet(storage)

