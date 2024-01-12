from ipaddress import IPv4Address, AddressValueError

class IpAddressList:

    def __init__(self, ipList):
        self.ipList = ipList

    def printIpList(self):
        print(self.ipList)

    def orderIpList(self):
        self.ipList = sorted(list(set(line for line in self.ipList)), reverse=True)
        
    def removeIpV6Addr(self):
        updatedList = []
        for address in self.ipList:
            if is_ipv4(address):
                updatedList.append(address)
        
        self.ipList = updatedList

def is_ipv4(addr):
    try:
        IPv4Address(addr.split('/')[0])
        return True
    except AddressValueError:
        return False
