# btc_words
Search Mnemonic words for BTC address (offline check in file). Python3 implementation Using _multi cpu_.
The script could be helpful to target the BTC Puzzle Transaction >100 BTC unsolved currently. 

# Info
The script generate randomly the English Mnemonic words and calculates the BTC derivation path BTC address and compare them in the input btc address file. If match is found the script will stop and print the corresponding mnemonic words on screen along with the matching btc Address.

Default Value used, can be changed if required. Currently they are set to make 12 words, using 4 cpu and checking the first address only in the derived path of the words.
```
cores=4
entropy_bits = 128                      # [128, 160, 192, 224, 256]
derivation_total_path_to_check = 1      # default = 1
```
_entropy_bits_to_mnemonic_ function can be modified if any other language words are needed. Currenly the default is English Words only.

# Run
```
(base) C:\anaconda3>python bip44_words_mcpu.py
[+] Starting.........Wait.....
[+] Loaded 256 address from file: btc_address.txt
Starting thread:  2
Starting thread:  1
Starting thread:  3
Starting thread:  0
[+] Total Keys Checked : 7247  [ Speed : 915.38 Keys/s ]  Current words: tooth slot lion flip cruise vibrant peace bone keen task turn crouch
[+] Total Keys Checked : 7308  [ Speed : 916.11 Keys/s ]  Current words: talent long toilet coil stove bring machine enforce drip gate front remind
[+] Total Keys Checked : 7808  [ Speed : 913.70 Keys/s ]  Current words: pattern cave school daring sting talk daughter then assume position humor custom
[+] Total Keys Checked : 8034  [ Speed : 916.18 Keys/s ]  Current words: grab swamp ginger popular broken modify thing fiscal agent drama wine question
[+] Total Keys Checked : 8047  [ Speed : 913.15 Keys/s ]  Current words: rich quit until enemy rough cute minor boss napkin practice tiger kit
[+] Total Keys Checked : 8112  [ Speed : 915.64 Keys/s ]  Current words: apple coyote edge demise goat garbage journey inch diet chicken outdoor glory
[+] Total Keys Checked : 8534  [ Speed : 915.75 Keys/s ]  Current words: select captain alarm dish damage next flag detect good tenant trade burger
[+] Total Keys Checked : 8834  [ Speed : 914.81 Keys/s ]  Current words: rebuild bacon talent fragile renew report angle resemble scene toward dignity soda
[+] Total Keys Checked : 8882  [ Speed : 917.98 Keys/s ]  Current words: brave version music earn marble artefact option index pilot lift excite juice
[+] Total Keys Checked : 8952  [ Speed : 918.53 Keys/s ]  Current words: stove hood lemon daughter icon deputy share erupt keen alcohol tiger imitate
[+] Total Keys Checked : 9339  [ Speed : 917.99 Keys/s ]  Current words: wolf august pause canyon claw witness height announce sing night swallow choose
[+] Total Keys Checked : 9612  [ Speed : 917.32 Keys/s ]  Current words: spoon occur virtual verify dumb guard marble dice crack trend alcohol narrow
[+] Total Keys Checked : 9713  [ Speed : 919.82 Keys/s ]  Current words: hunt online under quality spin govern flavor faculty thing loop law endorse
[+] Total Keys Checked : 9752  [ Speed : 919.14 Keys/s ]  Current words: goat tiny betray assist diesel discover mutual praise trick skin fluid lend
[+] Total Keys Checked : 10155  [ Speed : 916.69 Keys/s ]  Current words: thumb neither twenty claim ethics ice check coast near away lawn scorpion
[+] Total Keys Checked : 10376  [ Speed : 914.74 Keys/s ]  Current words: tide test approve elite slice cake scrap palace intact drastic hurt prevent
[+] Total Keys Checked : 10492  [ Speed : 916.79 Keys/s ]  Current words: panther mixture candy fitness unable report find moment distance dose usual rhythm


(base) C:\anaconda3>python seed_puzzle.py
BIP44 Searched Mnemonics : 150800   with Total Derivation Path 20 to 30 each
SIGINT or CTRL-C detected. Exiting gracefully. BYE
```

# Tips
```
BTC:	bc1q39meky2mn5qjq704zz0nnkl0v7kj4uz6r529at
ETH:	0xa74fC23f07A33B90d6848dF0bb409bEA5Ac16b28
DOGE:	D5Wh5bQMc3XVGdLbjJbGjryjNom5tZY6dD
```
