from setuptools import setup, find_packages


with open('README.md') as readme_file:
    README = readme_file.read()


setup_args = dict(
    name='db-by-josh',
    version='0.0.3',
    description='A thread safe DSL for sqlite3.',
    long_description_content_type="text/markdown",
    long_description=README,
    license='MIT',
    packages=find_packages(),
    author='Josh Arnold',
    author_email='dev@josharnold.me',
    keywords=['Sqlite3', 'Thread', 'Safe', 'DSL', 'Wrapper'],
    python_requires='>=3.6',
    url='https://github.com/josharnoldjosh/thread_safe_sqlite',    
)


if __name__ == '__main__':
    setup(**setup_args)