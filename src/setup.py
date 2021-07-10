from cx_Freeze import setup, Executable

base = None

executables = [Executable("main.py", base=base)]

packages = ["idna"]
options = {
    'build_exe': {
        'packages': packages,
    },
}

setup(
    name="OSM Telegram Scrapper",
    options=options,
    version="2.0.0",
    description='OSM Telegram Scrapper',
    executables=executables
)
