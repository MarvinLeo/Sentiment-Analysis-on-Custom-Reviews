import time
import json
import readFromTweeter as rft

## Comsumer Key and Secret
ckey = 'R0cJeuxEIplHpkjplJBD5TKaX'
csecret = 'EvvXLxWmB7dC9TYXqp4ay7MHt75Jl393M6lorMly1t4xhzEtko'

## Access Key and Secret
atoken = '3016058258-R4FBHd675L82SiG8nrkG3NVCbDOCMDV5sD3DehC'
asecret = 'q5hpnQIXw3oroJdQiA9fD6UBtBfp7QrqWK201E1q8WaSY'

rft.readTweet(ckey, csecret, atoken, asecret, 'whisky')