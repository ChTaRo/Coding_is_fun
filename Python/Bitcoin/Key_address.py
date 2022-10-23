import bitcoin
import qrcode

#generate a random private key
valid_private_key = False
while not valid_private_key:
    private_key = bitcoin.random_key()
    decode_private_key = bitcoin.decode_privkey(private_key, 'hex')
    valid_private_key = 0 < decode_private_key < bitcoin.N

print('Private key (hex) is:', private_key)
print('private key (deciaml) is:', decode_private_key)

#convert private key to WIF format
wif_encoded_private_key  = bitcoin.encode_privkey(decode_private_key, 'wif')
print('private key (WIF) is:', wif_encoded_private_key)

#add suffix "01" to indicate a compress private key
compress_private_key = private_key + '01'
print("Private key compress(hex) is:",  compress_private_key)

#generate a WIF format from the compress private key (WIF-compressed)
wif_compress_private_key = bitcoin.encode_privkey(bitcoin.decode_privkey(compress_private_key, 'hex'), 'wif')
print('private key (WIF-compressed) is:', wif_compress_private_key)

#multiply the EC generator point G with the private key to get public key point
public_key = bitcoin.fast_multiply(bitcoin.G, decode_private_key)
print('public key (x, y) coordinate is:', public_key)

#encode as hex, prefix 04
hex_encoded_public_key = bitcoin.encode_pubkey(public_key, 'hex')
print('public key(hex) is:', hex_encoded_public_key)

#compress public ke, adjust prefix depending on whether y is even or odd
(public_key_x, public_key_y) = public_key
if (public_key_y % 2) == 0:
    compress_prefix = '02'
else:
    compress_prefix = '03'
hex_compress_public_key = compress_prefix + bitcoin.encode(public_key_x, 16)
print('Compress public key (hex) is:', hex_compress_public_key)

#generate compressed bitcoin address from public key
print('Bitcoin address (b58check)', bitcoin.pubkey_to_address(public_key))

print('Compressed Bitcoin address (b58check) is:', bitcoin.pubkey_to_address(hex_compress_public_key))

img = qrcode.make(bitcoin.pubkey_to_address(hex_compress_public_key))
 
# Saving as an image file
img.save('MyQRCode1.png')