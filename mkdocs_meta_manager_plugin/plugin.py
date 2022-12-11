import re
import yaml
from pathlib import Path

from mkdocs.config import config_options
from mkdocs.plugins import BasePlugin

class MetaManagerPlugin(BasePlugin):
    config_scheme = (
        ('meta_filename', config_options.Type(str, default='.meta.yml')),
    )

    meta_files = {}

    def __init__(self):
        self.enabled = True

    def on_pre_build(self, config):
        pathlist = Path(config.docs_dir).rglob(self.config['meta_filename'])
        for path in pathlist:
            filepath = str(path)
            raw_path = filepath \
                .replace('/' + self.config['meta_filename'], '') \
                .replace(config.docs_dir + "/", '') \
                .replace(config.docs_dir, '')
            with open(filepath, "r") as stream:
                try:
                    self.meta_files[raw_path] = yaml.safe_load(stream)
                except yaml.YAMLError as exc:
                    print(exc)
        print(self.meta_files)
        

    def on_page_markdown(self, markdown, page, config, files):
        if not self.enabled:
            return markdown

        path_parts = page.file.src_path.split('/')
        for i in reversed(range(len(path_parts))):
            part = '/'.join(path_parts[0:i])
            if part in self.meta_files:
                for key, value in self.meta_files[part].items():
                    if not key in page.meta:
                        page.meta[key] = value

        print(page.meta)
        return markdown
