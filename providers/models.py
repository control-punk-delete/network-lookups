from dataclasses import dataclass, field
from ipaddress import IPv4Network,IPv6Network, ip_network


Network = IPv4Network | IPv6Network

@dataclass
class NetworkPrefix:
    prefix: Network

    @property
    def cidr(self) -> str:
        return str(self.prefix)

    @property
    def family(self) -> int:
        return self.prefix.version

    def contains(self, ip) -> bool:
        return ip in self.prefix



@dataclass(slots=True)
class ProviderResults:
    provider: str
    category: str
    prefixes: list[NetworkPrefix] = field(
        default_factory=list
    )

    def add_item(self, prefix: ip_network) -> None:
        
        exists = any(item.prefix == prefix.prefix for item in self.prefixes)
        if exists:
            return

        self.prefixes.append(prefix)


    def __len__(self) -> int: return len(self.prefixes)
