import os

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup  # NOQA



def fullsplit(path, result=None):
    """
    Split a pathname into components (the opposite of os.path.join) in a
    platform-neutral way.
    """
    if result is None:
        result = []
    head, tail = os.path.split(path)
    if head == '':
        return [tail] + result
    if head == path:
        return result
    return fullsplit(head, [tail] + result)

# Compile the list of packages available, because distutils doesn't have
# an easy way to do this.
packages, package_data = [], {}

root_dir = os.path.dirname(__file__)
if root_dir != '':
    os.chdir(root_dir)
extensions_dir = 'django_extensions'

for dirpath, dirnames, filenames in os.walk(extensions_dir):
    # Ignore PEP 3147 cache dirs and those whose names start with '.'
    dirnames[:] = [d for d in dirnames if not d.startswith('.') and d != '__pycache__']
    parts = fullsplit(dirpath)
    package_name = '.'.join(parts)
    if '__init__.py' in filenames:
        packages.append(package_name)
    elif filenames:
        relative_path = []
        while '.'.join(parts) not in packages:
            relative_path.append(parts.pop())
        relative_path.reverse()
        path = os.path.join(*relative_path)
        package_files = package_data.setdefault('.'.join(parts), [])
        package_files.extend([os.path.join(path, f) for f in filenames])



setup(
    name='django_extension_commands',
    version='0.1.0',
    description="Extension Commands for Django",
    long_description="""Extension Commands for Django""",
    author='@okwrtdsh',
    author_email='okwrtdsh@gmail.com',
    maintainer='@okwrtdsh',
    maintainer_email='okwrtdsh@gmail.com',
    url='ssh://git@github.com:okwrtdsh/django_extension_commands.git',
    platforms=['any'],
    packages=packages,
    package_data=package_data,
    install_requires=['six>=1.2'],
)

