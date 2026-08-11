
import httpx

from providers.cdn import (

    ProviderCloudIPRangesAkamai,
    ProviderCloudIPRangesBunny,
    ProviderCloudIPRangesCachefly,
    ProviderCloudIPRangesCloudflare,
    ProviderCloudIPRangesFastly,
    ProviderCloudIPRangesGCore,
    ProviderCloudIPRangesQuicCloud,


    ProviderScanitexAkamai,
    ProviderScanitexCdn77,
    ProviderScanitexCloudflare,
    ProviderScanitexFastly,
    ProviderScanitexStackpath
)

from providers.cloud import (
    ProviderScanitexAlibaba,
    ProviderScanitexAmazon,
    ProviderScanitexAmazonLeo,
    ProviderScanitexAzure,
    ProviderScanitexDigitalOcean,
    ProviderScanitexGoogle,
    ProviderScanitexIBMCloud,
    ProviderScanitexLinodeAkamai,
    ProviderScanitexOracle,
    ProviderScanitexTencent,
    ProviderScanitexVultr
)


from providers.hosting import (
    ProviderScanitexBluehost,
    ProviderScanitexContabo,
    ProviderScanitexGoDaddy,
    ProviderScanitexHetzner,
    ProviderScanitexHostinger,
    ProviderScanitexIONOS,
    ProviderScanitexNamecheap,
    ProviderScanitexOVH,
    ProviderScanitexScaleway
)

def load_providers(session: httpx.AsyncClient,):

    return (
        # cdn
            ProviderCloudIPRangesAkamai(session),
            ProviderCloudIPRangesBunny(session),
            ProviderCloudIPRangesCachefly(session),
            ProviderCloudIPRangesCloudflare(session),
            ProviderCloudIPRangesFastly(session),
            ProviderCloudIPRangesGCore(session),
            ProviderCloudIPRangesQuicCloud(session),

            ProviderScanitexAkamai(session),
            ProviderScanitexCdn77(session),
            ProviderScanitexCloudflare(session),
            ProviderScanitexFastly(session),
            ProviderScanitexStackpath(session),

        # cloud
            ProviderScanitexAlibaba(session),
            ProviderScanitexAmazon(session),
            ProviderScanitexAmazonLeo(session),
            ProviderScanitexAzure(session),
            ProviderScanitexDigitalOcean(session),
            ProviderScanitexGoogle(session),
            ProviderScanitexIBMCloud(session),
            ProviderScanitexLinodeAkamai(session),
            ProviderScanitexOracle(session),
            ProviderScanitexTencent(session),
            ProviderScanitexVultr(session),
        # hosting
            ProviderScanitexBluehost(session),
            ProviderScanitexContabo(session),
            ProviderScanitexGoDaddy(session),
            ProviderScanitexHetzner(session),
            ProviderScanitexHostinger(session),
            ProviderScanitexIONOS(session),
            ProviderScanitexNamecheap(session),
            ProviderScanitexOVH(session),
            ProviderScanitexScaleway(session)
        )