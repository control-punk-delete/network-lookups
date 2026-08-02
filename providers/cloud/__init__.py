from .alibaba import ProviderAlibaba
from .amazon_leo import ProviderAmazonLeo
from .amazon import ProviderAmazon
from .azure import ProviderAzure
from .digitalocean import ProviderDigitalOcean
from .google import ProviderGoogle
from .ibmcloud import ProviderIBMCloud
from .linkhole_akamai import ProviderLinodeAkamai
from .oracle import ProviderOracle
from .tencent import ProviderTencent
from .vulrt import ProviderVultr


__all__ = [
    "ProviderAlibaba",
    "ProviderAmazonLeo",
    "ProviderAmazon",
    "ProviderAzure",
    "ProviderDigitalOcean",
    "ProviderGoogle",
    "ProviderIBMCloud",
    "ProviderLinodeAkamai",
    "ProviderOracle",
    "ProviderTencent",
    "ProviderVultr"
]