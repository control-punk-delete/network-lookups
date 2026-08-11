from providers.base import BaseProvider
from providers.models import NetworkPrefix, ProviderResults

from ipaddress import ip_network


class ProviderScanitexAmazon(BaseProvider):
    name = "Amazon AWS"
    category = "cloud"
    source = "scanitex"
    url = "https://scanitex.com/en/resources/asn-database/amazon-aws/download/txt"



    async def fetch(self) -> ProviderResults:

        response = await self.session.get(self.url)

        if response.status_code != 200:
            return

        for cidr in response.text.splitlines():
            cidr = cidr.strip()

            if not cidr:
                continue

            if cidr.startswith("#"):
                continue
            self.results.add_item(NetworkPrefix(ip_network(cidr)))

        return self.results

    
