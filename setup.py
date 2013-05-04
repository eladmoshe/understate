from distutils.core import setup

files = ["uslib/*"]

REQUIREMENTS = [
    "pygments == 0.6.1",
    "pyfiglet == 1.6"
    ]

setup(name = "understate",
        version = "200",
        description = "markdown presentations using ncurses",
        author = "Ithai Levi",
        author_email = "ithai.levi@gmail.com",
        url = "http://github.com/L3V3L9",
        packages = ['uslib'],
        package_data = {'uslib' : files },
        scripts = ["understate"],
        long_description = """Create stunnig terminal presentations user markdown and some ncurses magic""",
        classifiers=[
            'Development Status :: 4 - Beta',
            'Environment :: Console :: Curses',
            'Intended Audience :: End Users/Desktop',
            'License :: OSI Approved :: GNU General Public License v3(GPLv3)',
            'Operating System :: POSIX :: Linux',
            'Operating System :: MacOS',
            'Programming Language :: Python',
            'Topic :: Text Processing :: Markup'
            ],
        install_requires=REQUIREMENTS
        )