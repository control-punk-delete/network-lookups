import json

from exporters import ExporterBase

class ExporterIndex(ExporterBase):
    
    def export(self, results):
            
        index = [
            {
                "cidr": str(prefix.cidr),
                "provider": result.provider,
                "category": result.category,
                "version": prefix.family,
            }
            for result in results
            for prefix in result.prefixes
            ]

                  
        with open(self.output_dir /
                    "index.json", "w", encoding="utf8" ) as fp: json.dump( index, fp, indent=2,)