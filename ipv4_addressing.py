#program to shaw characteristics of IPv4 addressins schemes

import random

def decimal_to_hex(n):
    return "%X" % n

def hex_to_decimal(s):
    return int(s, 16)

def decimal_to_binary(n):
    '''convert denary integer n to binary string bStr'''
    bStr = ''
    if n < 0:  return 'Must be positive integer'
    if n == 0: return '0'
    while n > 0:
        bStr = str(n % 2) + bStr
        n = n >> 1
    return bStr

def int2bin(n, count=24):
    """returns the binary of integer n, using count number of digits"""
    return "".join([str((n >> y) & 1) for y in range(count-1, -1, -1)])

def special_ipv4_address():
    print("IPv4 Special Addresses")
    print("0.0.0.0/8       Current network (only as source address)")
    print("10.0.0.0/8      Private network (16,777,216 addresses)")
    print("100.64.0.0/10   Shared Address Space")
    print("127.0.0.0/8     Loopback address (local host)")
    print("169.254.0.0/16  Link-local")
    print("172.16.0.0/12   Private network (1,048,576 addresses)")
    print("192.0.0.0/24    IETF Protocol Assignments")
    print("192.0.2.0/24    TEST-NET-1")
    print("192.88.99.0/24  IPv6 to IPv4 relay")
    print("192.168.0.0/16  Private network (65,536 addresses)")
    print("192.168.5.0     Private network (Broadcast to entire subnet)")
    print("192.168.5.255   Private network (Broadcast address)")
    print("198.51.100.0/24 TEST-NET-2")
    print("203.0.113.0/24  TEST-NET-3")
    print("224.0.0.0/4     IP Multicast (former class D network)")
    print("240.0.0.0/4     Reserved (former class E network")
    print("255.255.255.255 Broadcast address")
    print("x.x.x.0         Network ID in class C or CIDR with subnet mask > 24")
    print("x.x.x.255       Broadcast in class C or CIDR with subnet mask > 24")
    print()

def classful_ipv4_address():
    print("IPv4 Classful Addresses  (not Classless Internet Domain Routing")
    print("Class  Leading Bits  Networks   Addresses  Start     End Address")
    print("A      0        8/24       128 16,677,216   0.0.0.0  127.255.255.254")
    print("B      10      16/16    16,384     65,536 128.0.0.0  191.255.255.254")
    print("C      110     24/8  2,097,152        256 192.0.0.0  223.255.255.254")
    print("Multi  1110                               224.0.0.0  239.255.255.255")
    print()

def random_ipv4_address(type):
    address = []
    if type == 'a' or type == 'A':
        address.append(random.randrange(0, 128, 1))
        address.append(random.randrange(0, 256, 1))
        address.append(random.randrange(0, 256, 1))
        address.append(random.randrange(1, 255, 1))
    elif type == 'b' or type == 'B':
        address.append(random.randrange(128, 192, 1))
        address.append(random.randrange(0, 256, 1))
        address.append(random.randrange(0, 256, 1))
        address.append(random.randrange(1, 255, 1))
    elif type == 'c' or type == 'C':
        address.append(random.randrange(192, 224, 1))
        address.append(random.randrange(0, 256, 1))
        address.append(random.randrange(0, 256, 1))
        address.append(random.randrange(1, 255, 1))
    elif type == 'm' or type == 'M':
        address.append(random.randrange(224, 240, 1))
        address.append(random.randrange(0, 256, 1))
        address.append(random.randrange(0, 256, 1))
        address.append(random.randrange(1, 256, 1))
    return address

def print_dotted_decimal(addr):
    print(str(addr[0]) + '.' + str(addr[1]) + '.' + str(addr[2]) + '.' + str(addr[3]))

def dotted_to_binary(addr):
    s = ""
    for n in range(4):
        s1 = decimal_to_binary(addr[n])
        while len(s1) < 8:
            s1 = '0' + s1
        s += s1
    print(s)

special_ipv4_address()
classful_ipv4_address()
print("Random Class A address")
A = random_ipv4_address('a')
print_dotted_decimal(A)
dotted_to_binary(A)
print("Random Class B address")
B = random_ipv4_address('B')
print_dotted_decimal(B)
dotted_to_binary(B)
print("Random Class C address")
C = random_ipv4_address('c')
print_dotted_decimal(C)
dotted_to_binary(C)
print("Random Multicast address")
M = random_ipv4_address('M')
print_dotted_decimal(M)
dotted_to_binary(M)
