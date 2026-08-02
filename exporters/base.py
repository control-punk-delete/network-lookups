from pathlib import Path


class ExporterBase:

    def __init__(self, output_dir: Path = Path("lookpus")):
        self.output_dir = output_dir
        self.output_dir.mkdir(parents=True, exist_ok=True)