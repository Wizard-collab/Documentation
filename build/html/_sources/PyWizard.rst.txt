^^^^^^^^
PyWizard
^^^^^^^^

PyWizard is executable file that allows you to use the wizard API without the interface.

It is extremely similar to a python.exe executable

You can use it in command line or give a python file in argument.

===================
Python and PyWizard
===================

Let's try some python base libraries in PyWizard.

Launch PyWizard from the installation directory of wizard or from the ui ( tools>PyWizard ) and write this simple command ::

	>>> print("Hello world")
	>>> Hello world

Now let's create a python file with some code inside ::

	from datetime import datetime
	import time

	for a in range(100):
		print(datetime.now())
		time.sleep(0.1)

And run this script with PyWizard ( using the command line )::

	PyWizard myscript.py
	>>> 2020-05-09 23:40:37.421579
	>>> 2020-05-09 23:40:37.521589
	>>> 2020-05-09 23:40:37.622466

