import re
import ipaddress


def dec_to_bin(x):
    return int(bin(x)[2:])


patternIP = "^(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[0-9]{2}|[1-9])\.(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[0-9]{2}|[0-9])\.(25[" \
            "0-5]|2[0-4][0-9]|1[0-9]{2}|[0-9]{2}|[0-9])\.(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[0-9]{2}|[0-9])$"
#num = "(255|254|252|248|240|224|192|128|0+)"
#patternMask = "^" + num + "\." + num + "\." + num + "\." + num + "$"
patternMask="^\/([0-9]|[12][0-9]|3[0-2])$"
resultIp = None
resultMask = None
address = None
mask = None
while resultIp is None:
    print("Enter ip address: ", end='')
    #address = input()
    address="192.168.0.1"
    resultIp = re.match(patternIP, address)
    if resultIp is None:
        print('Invalid IP address format')

resultMask = None
while resultMask is None:
    print("Enter subnet mask: ", end='')
    #mask = input()
    mask="/24"
    resultMask = re.match(patternMask, mask)
    if resultMask is None:
        print('Invalid Subnet Mask format')

ipBin=[]
ipDec=[]
print()
for i in range(1, 5):
    ipDec.append(resultIp.group(i))
    next_part=str(dec_to_bin(int(resultIp.group(i))))
    while len(next_part)<8:
        next_part = "0"+next_part
    ipBin.append(next_part)

for i in range(0,4):
    spaces=" "*(10-len(ipDec[i]))
    print(ipDec[i]+spaces,end='')

print()
for i in range(0,4):
    print(ipBin[i]+"  ",end='')


ipAddress=ipaddress.ip_interface(address+mask)
network=ipAddress.network
broadcast=network.broadcast_address
print()
print("network address is: {}".format(str(network)))
print("broadcast address is: {}".format(str(broadcast)))