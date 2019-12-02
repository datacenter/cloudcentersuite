#!/usr/bin/env python

import os,time
from subprocess import STDOUT, check_call
import pip
import sys
from util import *
from error_utils import ErrorUtils


'''
    Required Azure Python Packages
'''
pip_sources = [
    "azure-mgmt-resource~=2.0",
    "azure-mgmt-sql~=0.11.0",
    'haikunator'
]

cmd = sys.argv[1]

# Install Python Packages
try:
    from pip import main
except ImportError as err:
    from pip._internal.main import main

def install_packages():
    global pip_sources
    main(['install'] + pip_sources)

# Validate Mandatory parameters
# Invoke External LifeCyle Actions

try:
    print_log('check prequisite environments')
    print('check prequisite environments')
    from service_parameter_util import create_params_json
    status = create_params_json()

    if bool(status):

        print_log("Initializing")
        install_packages()

        from main import start, stop

        if cmd in "start":
            start()
        elif cmd in "stop":
            stop()
    else:
        print_error(ErrorUtils.internal_error())
        sys.exit(127)

except Exception as e:
    print_error(ErrorUtils.internal_error(e.message))
    write_error(e)

    sys.exit(127)
