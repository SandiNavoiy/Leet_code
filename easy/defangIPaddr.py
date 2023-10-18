import ipaddress
class Solution(object):
    """Изменение и проверка IP адреса"""
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        try:
            ip_new = str(ipaddress.ip_address(address))
            return ip_new.replace(".", "[.]")
        except:
            print("This ip-address is not IP-4 ")


solution = Solution()
new_adress = solution.defangIPaddr("1.1.1.1")
print(f'"{new_adress}"')