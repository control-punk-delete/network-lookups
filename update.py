import asyncio
import httpx

from providers import load_providers
from exporters import ExporterMeta, ExporterIndex

ExporterMeta = ExporterMeta()
ExporterIndex = ExporterIndex()

async def main():

    async with httpx.AsyncClient(timeout=30, follow_redirects=True) as session:

        providers = load_providers(session)
        results = await asyncio.gather(*(provider.fetch() for provider in providers))

        ExporterMeta.export(results)
        ExporterIndex.export(results)
        

if __name__ == "__main__":
    asyncio.run(main())