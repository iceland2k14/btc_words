# -*- coding: utf-8 -*-
"""
Usage :
 > python bip44_words_mcpu.py
 
@author: iceland
"""

import hashlib
import bitcoinlib
import time
import sys
import hmac, struct
import bit
from multiprocessing import Event, Process, Queue, Value, cpu_count

################################################################
order	= 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141

fl = 'btc_address.txt'      # file containing all address to be matched by mnemonics

btc_list = [line.split()[0] for line in open(fl,'r')]
btc_list = set(btc_list)

screen_print_after_keys = 200
################################################################
def check_address(addr):
    flag = False
    if addr in btc_list:
        flag = True
    return flag
################################
# valid_entropy_bits = [128, 160, 192, 224, 256]

def entropy_bits_to_mnemonic(entropy_bits):
    words = bitcoinlib.mnemonic.Mnemonic().generate(entropy_bits)
# bitcoinlib.keys.HDKey.from_passphrase(Mnemonic().generate(256)).address()  # very slow
# seed = bitcoinlib.mnemonic.Mnemonic().to_seed(words)                       # hashlib is faster
    return words

################################ x100 faster 
def mnem_to_seed(words):
	salt = 'mnemonic'
	seed = hashlib.pbkdf2_hmac("sha512",words.encode("utf-8"), salt.encode("utf-8"), 2048)
	return seed

################################
def bip39seed_to_bip32masternode(seed):
#    k = seed
    h = hmac.new(b'Bitcoin seed', seed, hashlib.sha512).digest()
    key, chain_code = h[:32], h[32:]
    return key, chain_code

################################
def parse_derivation_path(str_derivation_path="m/44'/60'/0'/0/0"):      # 60' is for ETH 0' is for BTC
    path = []
    if str_derivation_path[0:2] != 'm/':
        raise ValueError("Can't recognize derivation path. It should look like \"m/44'/0'/0'/0\".")
    for i in str_derivation_path.lstrip('m/').split('/'):
        if "'" in i:
            path.append(0x80000000 + int(i[:-1]))
        else:
            path.append(int(i))
    return path

def derive_bip32childkey(parent_key, parent_chain_code, i):
    assert len(parent_key) == 32
    assert len(parent_chain_code) == 32
    k = parent_chain_code
    if (i & 0x80000000) != 0:
        key = b'\x00' + parent_key
    else:
#        key = bytes(PublicKey(parent_key))
        key = bit.Key.from_bytes(parent_key).public_key
    d = key + struct.pack('>L', i)
    while True:
        h = hmac.new(k, d, hashlib.sha512).digest()
        key, chain_code = h[:32], h[32:]
        a = int.from_bytes(key, byteorder='big')
        b = int.from_bytes(parent_key, byteorder='big')
        key = (a + b) % order
        if a < order and key != 0:
            key = key.to_bytes(32, byteorder='big')
            break
        d = b'\x01' + h[32:] + struct.pack('>L', i)
    return key, chain_code

def bip39seed_to_private_key(bip39seed):
    str_derivation_path = "m/44'/0'/0'/0/0"
    derivation_path = parse_derivation_path(str_derivation_path)
    master_private_key, master_chain_code = bip39seed_to_bip32masternode(bip39seed)
    private_key, chain_code = master_private_key, master_chain_code
    for i in derivation_path:
        private_key, chain_code = derive_bip32childkey(private_key, chain_code, i)
    return private_key
################################
# =============================================================================
# def seed_to_privatekey(seed, n=1):
#     b = bitcoinlib.keys.HDKey.from_seed(seed)
#     flg = False
#     const = "m/44'/0'/0'/0/"
#     for k in range(n):
#         b0=b.subkey_for_path(const + str(k))
#         flg = check_address(b0.address())
#         if flg == True:
#             break
# #    b0=b.subkey_for_path("m/44'/0'/0'/0/0")
# #    b0.address()
# #    b0.hash160.hex()
# #    b0.private_hex
# #    b1=b.subkey_for_path("m/44'/0'/0'/0/1")
# #    b2=b.subkey_for_path("m/44'/0'/0'/0/2")
# #    b3=b.subkey_for_path("m/44'/0'/0'/0/3")
# #    b4=b.subkey_for_path("m/44'/0'/0'/0/4")
#     return flg
# =============================================================================


def do_work_loop(entropy_bits):
    mnem = entropy_bits_to_mnemonic(entropy_bits)
    seed = mnem_to_seed(mnem)
#    flg = seed_to_privatekey(seed,derivation_total_path_to_check)
    pvk = bip39seed_to_private_key(seed)
    addr = bit.Key.from_bytes(pvk).address
    flg = check_address(addr)
    return mnem, flg, addr

###############################################################################
# Things which can be changed in code
entropy_bits = 128                      # [128, 160, 192, 224, 256]
derivation_total_path_to_check = 1      # default = 1
###############################################################################
def hunt_BTC_mnemonics(cores='all'):  # pragma: no cover

    available_cores = cpu_count()

    if cores == 'all':
        cores = available_cores
    elif 0 < int(cores) <= available_cores:
        cores = int(cores)
    else:
        cores = 1

    counter = Value('i')
    match = Event()
    queue = Queue()

    workers = []
    for r in range(cores):
        p = Process(target=generate_mnem_address_pairs, args=(counter, match, queue, r))
        workers.append(p)
        p.start()

    for worker in workers:
        worker.join()
    
    keys_generated = 0
    while True:
        time.sleep(1)
        current = counter.value
        if current == keys_generated:
            if current == 0:
                continue
            break
        keys_generated = current
        s = 'Total Mnemonics generated: {}\r'.format(keys_generated)

        sys.stdout.write(s)
        sys.stdout.flush()

    mnem_words, address = queue.get()
    print('\n\nFinal Mnemonics Words (English): ', mnem_words)
    print('BTC Address: {}'.format(address))

#==============================================================================
def generate_mnem_address_pairs(counter, match, queue, r):
    st = time.time()
    print('Starting thread: ', r)
    k = 1
    while True:
        if match.is_set():
            return

        with counter.get_lock():
            counter.value += 1
            
        mnem, flg, addr = do_work_loop(entropy_bits)
        
        if k % screen_print_after_keys == 0:
#            print('  {:0.2f} Keys/s    :: Total Key Searched: {}'.format(k/(time.time() - st), k), end='\n')
            print('[+] Total Keys Checked : {0}  [ Speed : {1:.2f} Keys/s ]  Current words: {2}'.format(counter.value, counter.value/(time.time() - st), mnem))
            
        if flg == True:
            match.set()
            queue.put_nowait((mnem, addr))
            return
        
        k += 1

###############################################################################
if __name__ == '__main__':
    print('[+] Starting.........Wait.....')
    print('[+] Loaded ' + str(len(btc_list)) +' address from file:' + fl)
    hunt_BTC_mnemonics(cores=4)