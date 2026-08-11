from .scanitex_akamai import ProviderScanitexAkamai
from .scanitex_cdn77 import ProviderScanitexCdn77
from .scanitex_cloudflare import ProviderScanitexCloudflare
from .scanitex_fastly import ProviderScanitexFastly
from .scanitex_stackpath import ProviderScanitexStackpath

from .cloud_ip_ranges_akamai import ProviderCloudIPRangesAkamai
from .cloud_ip_ranges_bunny import ProviderCloudIPRangesBunny
from .cloud_ip_ranges_cachefly import ProviderCloudIPRangesCachefly
from .cloud_ip_ranges_cloudflare import ProviderCloudIPRangesCloudflare
from .cloud_ip_ranges_fastly import ProviderCloudIPRangesFastly
from .cloud_ip_ranges_g_core import ProviderCloudIPRangesGCore
from .cloud_ip_ranges_quic_cloud import ProviderCloudIPRangesQuicCloud



__all__ = [
    "ProviderCloudIPRangesAkamai",
    "ProviderCloudIPRangesBunny",
    "ProviderCloudIPRangesCachefly",
    "ProviderCloudIPRangesCloudflare",
    "ProviderCloudIPRangesFastly",
    "ProviderCloudIPRangesGCore",
    "ProviderCloudIPRangesQuicCloud",

    "ProviderScanitexAkamai",
    "ProviderScanitexCdn77",
    "ProviderScanitexCloudflare",
    "ProviderScanitexFastly",
    "ProviderScanitexStackpath",
]