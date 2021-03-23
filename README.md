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
[+] Total Keys Checked : 741  [ Speed : 847.35 Keys/s ]  Current words: ride pen disease certain isolate skate tiny iron time calm such congress
[+] Total Keys Checked : 755  [ Speed : 876.57 Keys/s ]  Current words: ramp someone afford salon side mule aspect east edge jump slush age
[+] Total Keys Checked : 811  [ Speed : 863.43 Keys/s ]  Current words: rural destroy basic priority police few prison mushroom mercy ten fantasy airport
[+] Total Keys Checked : 893  [ Speed : 863.44 Keys/s ]  Current words: sheriff price route limb clerk wink coral notice remain ethics link dutch
[+] Total Keys Checked : 1571  [ Speed : 903.94 Keys/s ]  Current words: fluid umbrella duck service typical demand urban carry elegant rich neck winter
[+] Total Keys Checked : 1573  [ Speed : 897.03 Keys/s ]  Current words: marriage express make income gift monitor cram inquiry around virtual series iron
[+] Total Keys Checked : 1596  [ Speed : 887.01 Keys/s ]  Current words: ten goddess faint fatal purchase zone use whale wagon super just hurdle
[+] Total Keys Checked : 1664  [ Speed : 896.37 Keys/s ]  Current words: time ship festival online drum frozen lamp stomach floor soon shrug fringe
[+] Total Keys Checked : 2316  [ Speed : 898.56 Keys/s ]  Current words: mercy wing dinosaur decide record firm rose unhappy prefer pelican accident session
[+] Total Keys Checked : 2386  [ Speed : 903.74 Keys/s ]  Current words: cluster soul sphere audit shoe hobby globe destroy twenty mimic critic brief
[+] Total Keys Checked : 2440  [ Speed : 892.59 Keys/s ]  Current words: ask hospital flame garment oval aunt cactus green notable crew monkey fish
[+] Total Keys Checked : 2472  [ Speed : 904.67 Keys/s ]  Current words: kiss wash flee soccer differ start alcohol nose enough cream grunt pull
[+] Total Keys Checked : 3080  [ Speed : 898.21 Keys/s ]  Current words: almost abuse muscle fall steak bulb all glove soccer galaxy chat hill
[+] Total Keys Checked : 3166  [ Speed : 903.01 Keys/s ]  Current words: book lyrics eager space shrug canyon elder old chunk nerve daughter swim
[+] Total Keys Checked : 3244  [ Speed : 894.72 Keys/s ]  Current words: brief cupboard motion shadow debate what veteran salmon slam cause prevent stadium
[+] Total Keys Checked : 3317  [ Speed : 902.15 Keys/s ]  Current words: merit exclude forest age list easily modify sand slow stone collect anger
[+] Total Keys Checked : 3870  [ Speed : 901.41 Keys/s ]  Current words: field snack antique please royal talk plug supreme birth crowd stumble cable
[+] Total Keys Checked : 3949  [ Speed : 905.72 Keys/s ]  Current words: document runway above suffer tuna essence cover rally correct bundle attitude powder
[+] Total Keys Checked : 4091  [ Speed : 906.90 Keys/s ]  Current words: catch board monkey prosper clever gorilla green oval situate disease orbit absorb
[+] Total Keys Checked : 4098  [ Speed : 900.22 Keys/s ]  Current words: utility grocery reject tree fortune height velvet weather cattle eternal term jump
[+] Total Keys Checked : 4633  [ Speed : 903.62 Keys/s ]  Current words: track educate novel end coach monkey fruit future trumpet invest canoe rabbit
[+] Total Keys Checked : 4792  [ Speed : 908.51 Keys/s ]  Current words: invite wire truth jacket bottom often horror wheat valve lake truck cattle
[+] Total Keys Checked : 4863  [ Speed : 902.86 Keys/s ]  Current words: riot essay shy chat balcony album female monitor amazing truck summer turkey
[+] Total Keys Checked : 4930  [ Speed : 908.71 Keys/s ]  Current words: believe hip sponsor degree echo flower squeeze before sail discover tape spice
[+] Total Keys Checked : 5426  [ Speed : 908.37 Keys/s ]  Current words: buffalo give engine strategy muscle tribe debris assume salmon concert word dad
[+] Total Keys Checked : 5617  [ Speed : 905.95 Keys/s ]  Current words: upgrade often leader quote spike outside mail below eagle razor torch boost
[+] Total Keys Checked : 5624  [ Speed : 910.19 Keys/s ]  Current words: actual poverty soft any shed silk pause sleep velvet mosquito hurry result
[+] Total Keys Checked : 5746  [ Speed : 912.15 Keys/s ]  Current words: glass tilt party client gold train brief economy supply rotate donkey myth
[+] Total Keys Checked : 6208  [ Speed : 911.98 Keys/s ]  Current words: setup odor dumb perfect obvious slight brick eight tip uncover visa sad
[+] Total Keys Checked : 6447  [ Speed : 911.36 Keys/s ]  Current words: fan endless muffin quick practice burger deliver bargain equip blush want hurry
[+] Total Keys Checked : 6450  [ Speed : 914.79 Keys/s ]  Current words: february laundry sail neither cash crystal regular south hedgehog close acoustic test
[+] Total Keys Checked : 6505  [ Speed : 915.80 Keys/s ]  Current words: cinnamon stumble goddess retreat final civil noise hole circle regret photo outdoor
[+] Total Keys Checked : 7024  [ Speed : 914.65 Keys/s ]  Current words: section tilt symptom recipe second regular siren ritual toilet flush draw window
[+] Total Keys Checked : 7238  [ Speed : 911.80 Keys/s ]  Current words: thank glad deny hen infant any brief sugar demise snap dinosaur hint
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
```

# Tips
```
BTC:	bc1q39meky2mn5qjq704zz0nnkl0v7kj4uz6r529at
ETH:	0xa74fC23f07A33B90d6848dF0bb409bEA5Ac16b28
DOGE:	D5Wh5bQMc3XVGdLbjJbGjryjNom5tZY6dD
```
