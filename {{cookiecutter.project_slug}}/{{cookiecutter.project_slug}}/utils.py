import os

def load_pkg_file(pkg_filename, filename, default):
    """Load file content under package folder

    """
    pkg_dir = os.path.dirname(pkg_filename)
    filepath = os.path.join(pkg_dir, filename)
    try:
        with open(filepath, 'rt') as pkg_file:
            return pkg_file.read().strip()
    except IOError:
        return default
