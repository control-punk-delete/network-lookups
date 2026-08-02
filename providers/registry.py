
import httpx

from providers.cdn import (
    ProviderAkamai,
    ProviderCloudflare,
    ProviderCdn77,
    ProviderFastly,
    ProviderStackpath
)

from providers.cloud import (
    ProviderAlibaba,
    ProviderAmazonLeo,
    ProviderAmazon,
    ProviderAzure,
    ProviderDigitalOcean,
    ProviderGoogle,
    ProviderIBMCloud,
    ProviderLinodeAkamai,
    ProviderOracle,
    ProviderTencent,
    ProviderVultr
)


from providers.hosting import (
    ProviderGoDaddy
)

def load_providers(session: httpx.AsyncClient,):

    return (
        # cdn
             ProviderAkamai(session),
             ProviderCloudflare(session),
             ProviderCdn77(session),
             ProviderFastly(session),
             ProviderStackpath(session),
        # cloud
            ProviderAlibaba(session),
            ProviderAmazonLeo(session),
            ProviderAmazon(session),
            ProviderAzure(session),
            ProviderDigitalOcean(session),
            ProviderGoogle(session),
            ProviderIBMCloud(session),
            ProviderLinodeAkamai(session),
            ProviderOracle(session),
            ProviderTencent(session),
            ProviderVultr(session),
        # hosting
            ProviderGoDaddy(session)
        )