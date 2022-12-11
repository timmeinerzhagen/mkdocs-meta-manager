import yaml

from mkdocs.config import config_options
from mkdocs.plugins import BasePlugin

class MetaManagerPlugin(BasePlugin):
    config_scheme = (
        ('meta_filename', config_options.Type(str, default='.meta.yml')),
    )

    meta_files = {}

    def __init__(self):
        self.enabled = True

    def on_files(self, files, config):
        for file in files:
            if file.src_path.endswith(self.config['meta_filename']):
                print(file)
                with open(file.src_path, "r") as stream:
                    try:
                        self.meta_files[file.src_path] = yaml.safe_load(stream)
                    except yaml.YAMLError as exc:
                        print(exc)
                print(self.meta_files[file.src_path])
                files.remove(file)
        return files
        

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