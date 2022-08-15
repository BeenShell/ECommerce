
# This is a simple scripts with the commands to run.
# If the languge has dashes they must be written as underlines, and the country code
# must be capitalized.
# e.g en-us becomes en_US
# The commands must be run at the root directory.

# 1. django-admin makemessages -l LANGUAGE_CODE_HERE --ignore venv
# This command will create a file named django.po for each language, that will contain the messages
# and their respective translations for the languages

# 2. django-admin compilemessages --ignore venv
# This will compile the .po files to django.mo which are binary optimized translation files.
# This is the content visible in page

# To see things take action, change the webpage language in your browser settings.

# todo: turn this into an actual python script
