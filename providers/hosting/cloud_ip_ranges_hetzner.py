from providers.base import BaseProvider
from providers.models import NetworkPrefix, ProviderResults

from ipaddress import ip_network

class ProviderCloudIPRangesHetzner(BaseProvider):
    name = "Hetzner"
    category = "hosting"
    source = "cloud-ip-ranges"

    url = "https://cloud-ip-ranges.com/download/hetzner.txt"



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
