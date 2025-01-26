# -*- coding: utf-8 -*-
"""
Usage: python p2sh_brute.py

@author: iceland
"""
from tqdm import tqdm
import time, os
import secp256k1 as ice
# =============================================================================
print('\n[+] Program Starting ... Please Wait')

Funded = [line.split()[0] for line in open('bitcoin_addresses_and_balance.tsv','r') if line[0]=='3']
print(f'[+] Loaded {len(Funded)} p2sh Address.   Last: {Funded[-1]}')
Funded = [bytes.fromhex(ice.address_to_h160(line)) for line in tqdm(Funded)]
Funded = set(Funded)
print('[+] Converted back to HASH160 bytes and loaded in a SET...')


k = 0
st = time.time()
while True:
    try:
        script = b'\x00\x14' + os.urandom(20)
        h = ice.hash160(script)
        
        if k%200000 == 0: print(f'[Completed {k:>12}]  [{k/(0.0001+time.time()-st):.2f} Key/s]  Script= {script.hex():>50}', end='\r')
    
        if h in Funded:
            print(f'Script= {script.hex():>50}  {h.hex():>36}  {ice.hash_to_address(1, True, h)}')
            with open('Results_p2sh_FoundScripts.txt','a') as fw:
                fw.write(f'Script= {script.hex()}  {h.hex()}  {ice.hash_to_address(1, True, h)}\n')
        k += 1
    except(KeyboardInterrupt, SystemExit):
        exit('\nSIGINT or CTRL-C detected. Exiting gracefully. BYE')
