#!/usr/bin/python3
import sys
import shutil
import subprocess
import os

"""
 Test if file test and file_storage are present
"""
if not os.path.exists("tests/test_models/test_amenity.py"):
    print("No file")
    exit(1)
if not os.path.exists("models/amenity.py"):
    print("No file")
    exit(1)

"""
 Restore
"""
try:
    shutil.copy("models/tmp_amenity.py", "models/amenity.py")
except Exception as e:
    pass

"""
 Backup
"""
try:
    shutil.copy("models/amenity.py", "models/tmp_amenity.py")
except Exception as e:
    pass

"""
 get fake and move to correct folder
"""
fake_amenity_name = sys.argv[1]
try:
    shutil.copy(fake_amenity_name, "models/amenity.py")
except Exception as e:
    pass

"""
 Run test
"""
process = subprocess.Popen(["python3", "-m", "unittest", "tests/test_models/test_amenity.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, error = process.communicate()
s_total = "{}{}".format(output, error)

if "FAIL" in s_total or "Traceback" in s_total:
    print("OK", end="")


"""
 Restore
"""
try:
    shutil.copy("models/tmp_amenity.py", "models/amenity.py")
except Exception as e:
    pass