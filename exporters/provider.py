import json
import re

from ipaddress import ip_network
from pathlib import Path

from .base import ExporterBase
from providers.models import NetworkPrefix, ProviderResults


def slugify(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-")


class ExporterProvider(ExporterBase):

    def _path(self, category: str, source: str, name: str) -> Path:
        directory = self.output_dir / "providers" / slugify(category)
        directory.mkdir(parents=True, exist_ok=True)

        filename = f"{slugify(source)}-{slugify(name)}.json"
        return directory / filename

    def export(self, result: ProviderResults) -> None:

        path = self._path(result.category, result.source, result.provider)

        payload = {
            "provider": result.provider,
            "category": result.category,
            "source": result.source,
            "prefixes": [prefix.cidr for prefix in result.prefixes],
        }

        with open(path, "w", encoding="utf8") as fp:
            json.dump(payload, fp, indent=2)

    def load(self, category: str, source: str, name: str) -> ProviderResults | None:

        path = self._path(category, source, name)

        if not path.exists():
            return None

        with open(path, "r", encoding="utf8") as fp:
            payload = json.load(fp)

        result = ProviderResults(
            payload["provider"], payload["category"], payload["source"]
        )

        for cidr in payload["prefixes"]:
            result.add_item(NetworkPrefix(ip_network(cidr)))

        return result
