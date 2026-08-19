import asyncio
import httpx

from providers import load_providers
from exporters import ExporterMeta, ExporterIndex, ExporterProvider

ExporterMeta = ExporterMeta()
ExporterIndex = ExporterIndex()
ExporterProvider = ExporterProvider()

# async def main():

#     async with httpx.AsyncClient(timeout=300, follow_redirects=True) as session:

#         providers = load_providers(session)
#         results = await asyncio.gather(*(provider.fetch() for provider in providers))

#         ExporterMeta.export(results)
#         ExporterIndex.export(results)
        

# if __name__ == "__main__":
#     asyncio.run(main())


async def main():

    async with httpx.AsyncClient(timeout=300, follow_redirects=True) as session:

        providers = load_providers(session)

        fetched = await asyncio.gather(
            *(provider.fetch() for provider in providers),
            return_exceptions=True,
        )

        results = []

        for provider, result in zip(providers, fetched):

            label = f"{provider.category}/{provider.source}/{provider.name}"

            if isinstance(result, Exception):
                print(f"[warn] {label}: fetch raised {result!r}", file=sys.stderr)
                result = None

            if result is None or len(result) == 0:
                fallback = ExporterProvider.load(
                    provider.category, provider.source, provider.name
                )

                if fallback is None:
                    print(
                        f"[warn] {label}: no data returned and no previous "
                        f"export available, skipping",
                        file=sys.stderr,
                    )
                    continue

                print(
                    f"[warn] {label}: no data returned, falling back to "
                    f"previous export ({len(fallback)} prefixes)",
                    file=sys.stderr,
                )
                results.append(fallback)
                continue

            ExporterProvider.export(result)
            results.append(result)

        ExporterMeta.export(results)
        ExporterIndex.export(results)


if __name__ == "__main__":
    asyncio.run(main())
