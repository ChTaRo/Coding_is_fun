import bitcoin

#generate a random private key
valid_private_key = False
while not valid_private_key:
    private_key = bitcoin.random_key()
    decode_private_key = bitcoin.decode_privkey(private_key, 'hex')
    valid_private_key = 0 < decode_private_key < bitcoin.N

print('Private key (hex is):', private_key)
print('private key (deciaml is:)', decode_private_key)