# Write your testing or manipulation code here
# This script will be executed before packaging the layer
# Code below can be fully removed if not needed

from importlib.metadata import files
import sysconfig

print(sysconfig.get_config_var("EXT_SUFFIX"))
print([file for file in files('pydantic-core') if file.name.startswith('_pydantic_core')])
"""
[PackagePath('pydantic_core/_pydantic_core.pyi'), PackagePath('pydantic_core/_pydantic_core.cpython-312-x86_64-linux-gnu.so')]
"""