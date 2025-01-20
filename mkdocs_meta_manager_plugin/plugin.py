import re
import yaml
from pathlib import Path
import logging
import os

from mkdocs.config import config_options
from mkdocs.plugins import BasePlugin

log = logging.getLogger(f"mkdocs.plugins.{__name__}")

class MetaManagerPlugin(BasePlugin):
    config_scheme = (
        ('meta_filename', config_options.Type(str, default='.meta.yml')),
        ('merge_entries', config_options.Type(list, default=[])),
    )
    meta_files = {}

    def __init__(self):
        self.enabled = True

    def on_pre_build(self, config):
        pathlist = Path(config.docs_dir).rglob(self.config['meta_filename'])
        for path in pathlist:
            filepath = str(path)
            raw_path = filepath \
                .replace(os.path.sep + self.config['meta_filename'], '') \
                .replace(config.docs_dir + os.path.sep, '') \
                .replace(config.docs_dir, '')
            with open(filepath, "r") as stream:
                try:
                    self.meta_files[raw_path] = yaml.safe_load(stream)
                except yaml.YAMLError as exc:
                    print(exc)
        log.debug("[meta-manager] All '%s' files: %s", self.config["meta_filename"], self.meta_files)

    def on_page_markdown(self, markdown, page, config, files):
        if not self.enabled:
            return markdown

        path_parts = page.file.src_path.split(os.path.sep)
        for i in reversed(range(len(path_parts))):
            part = os.path.sep.join(path_parts[0:i])
            if part in self.meta_files:
                for key, value in self.meta_files[part].items():
                    if not key in page.meta:
                        page.meta[key] = value
                    elif key in self.config['merge_entries']:
                        if not isinstance(page.meta[key], list):
                            page.meta[key] = [page.meta[key]]
                        page.meta[key].extend(value)

        log.debug("[meta-manager] %s: %s", page.file.src_path, page.meta)
        return markdown
