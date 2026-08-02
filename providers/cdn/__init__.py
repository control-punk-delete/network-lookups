from .akamai import ProviderAkamai
from .cloudflare import ProviderCloudflare
from .stackpath import ProviderStackpath
from .cdn77 import ProviderCdn77
from .fastly import ProviderFastly


__all__ = [
    "ProviderAkamai",
    "ProviderCloudflare",
    "ProviderStackpath",
    "ProviderCdn77",
    "ProviderFastly"


]