
# Python PIP
# PIP is a package manager for Python packages, or modules if you like.

# Python Package
# A package contains all the files you need for a module.

# Modules are Python code libraries you can include in your project.

# Check if PIP is Installed

"""!pip3 --version """   

# For terminal
# pip --version

"""pip 20.0.2 from /usr/lib/python3/dist-packages/pip (python 3.8)
"""
# Download a Package
"""
!pip3 install camelcase """

# pip install camelcase  (For terminal)
# Requirement already satisfied: camelcase in /home/fenil/.local/lib/python3.8/site-packages (0.2)
# Using a Package
"""
import camelcase

cc = camelcase.CamelCase()

text = "hello, universe!"

print(cc.hump(text))
"""
# Find Packages
"""
https://pypi.org/
"""
# Remove a Package
"""
!pip3 uninstall camelcasey
"""
# pip uninstall camelcase   (For Terminal)

# List Packages
"""
!pip3 list
 """