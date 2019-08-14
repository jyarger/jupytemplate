__version__ = '0.5.1'


def _jupyter_nbextension_paths():
    # src & dest are os paths, and so must use os.path.sep to work correctly on Windows.
    # In contrast, require is a requirejs path, and thus must use `/` as the path separator.
    return [dict(
        section='notebook',
        # src is relative to current module
        src='jupytemplate',
        # dest directory is in the `nbextensions/` namespace
        dest='jupytemplate',
        # require is also in the `nbextensions/` namespace
        # must use / as path.sep
        require='jupytemplate/main',
    )]