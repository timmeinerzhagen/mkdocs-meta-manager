# mkdocs-meta-manager

MkDocs plugin for managing meta tags across folders and files

## Setup

1. Install the plugin:
    ```bash
    pip install mkdocs-meta-manager
    ```
2. Add the plugin to your `mkdocs.yml`
    ```bash
    plugins:
        - search
        - meta-manager
    ```

## Usage

Add meta files with the name `.meta.yml` (can be configured) in your docs file structure.

All markdown files in the same folder and in subfolders automatically get all tags that are defined in the given meta file.

## Options

`meta_filename`
Change the default name of the meta file. (default=`.meta.yml`)

`merge_tags`
Merge the tags of all relevant meta files and pages for a page (default=`false`)
