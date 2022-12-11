import yaml
from pathlib import Path

from mkdocs.config import config_options
from mkdocs.plugins import BasePlugin

class MetaManagerPlugin(BasePlugin):
    config_scheme = (
        ('meta_filename', config_options.Type(str, default='**/.meta.yml')),
    )

    meta_files = {}

    def __init__(self):
        self.enabled = True

    def on_pre_build(self, config):
        print(config)

        pathlist = Path(config.docs_dir).glob(self.config['meta_filename'])
        print(pathlist)
        for path in pathlist:
            filepath = str(path)
            print(filepath)
            with open(filepath, "r") as stream:
                try:
                    self.meta_files[filepath] = yaml.safe_load(stream)
                except yaml.YAMLError as exc:
                    print(exc)
            print(self.meta_files[file.src_path])
        print(self.meta_files)
        

    def on_page_markdown(self, markdown, page, config, files):
        if not self.enabled:
            return markdown

        print(page)

        for part in page.file.src_path.split('/'):
            if part in self.meta_files:
                for key, value in self.meta_files[part].items():
                    print(key, value)
                    if not page.meta[key]:
                        page.meta[key] = value

        print(page)
        return markdown