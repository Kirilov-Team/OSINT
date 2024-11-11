from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
build_options = {'packages': [], 'excludes': []}

base = 'console'

executables = [
    Executable('main.py', base=base, target_name = 'Project_OSINT', icon="icon.ico")
]

setup(name='project_osint',
      version = '1.0',
      description = "Made By Kirilov Technology",
      options = {'build_exe': build_options},
      executables = executables)
