
import json

from datetime import UTC, datetime

from .base import ExporterBase


class ExporterMeta(ExporterBase):

    SCHEMA = 1
    LOOKUP_VERSION = "0.1.0"

    def export(self, results):

        categories = {r.category for r in results}

        metadata = {

            "schema":
                self.SCHEMA,

            "lookup_version":
                self.LOOKUP_VERSION,

            "generated":
                datetime.now(UTC).isoformat(),

            "providers":
                len(results),

            "categories":
                len(categories),

            "prefixes":
                sum(len(r) for r in results),

            "providers_stats": [

                {

                    "provider":
                        r.provider,

                    "category":
                        r.category,

                    "prefixes":
                        len(r.prefixes),
                }

                for r in results

            ],

        }

        with open(self.output_dir /
                   "metadata.json", "w", encoding="utf8" ) as fp: json.dump( metadata, fp, indent=2,)