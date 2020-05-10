import shutil
import subprocess

p = subprocess.Popen('build.bat')
p.wait()
shutil.copyfile("source/pygments.css", "build/html/_static/pygments.css")