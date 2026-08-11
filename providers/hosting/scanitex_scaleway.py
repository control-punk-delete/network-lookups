from providers.base import BaseProvider
from providers.models import NetworkPrefix, ProviderResults

from ipaddress import ip_network

class ProviderScanitexScaleway(BaseProvider):
    name = "Scaleway"
    category = "hosting"
    source = "scanitex"
    url = "https://scanitex.com/en/resources/asn-database/scaleway/download/txt"

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