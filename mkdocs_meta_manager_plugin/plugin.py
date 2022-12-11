import re
from os import environ
from datetime import datetime

from mkdocs.config import config_options
from mkdocs.plugins import BasePlugin

class MetaManagerPlugin(BasePlugin):
    config_scheme = (
        ('meta_filename', config_options.Type(str)),
    )

    def __init__(self):
        self.enabled = True

    def on_page_markdown(self, markdown, page, config, files):
        if not self.enabled:
            return markdown

        print(page.meta)

        return markdown