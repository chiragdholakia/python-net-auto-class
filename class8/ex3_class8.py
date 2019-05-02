from jnpr.junos import Device
from jnpr.junos.utils.config import Config
from jnpr.junos.exception import LockError
from getpass import getpass

from jnpr_devices import srx2

jnpr_device = Device(**srx2)
jnpr_device.open()
jnpr_device.timeout = 60

config = Config(jnpr_device)
config.lock()

try:
    config.lock()
except LockError:
    print("Device is already locked")

config.load("set system host-name python4life", format="set", merge="True")
# Check diff of staged vs running config
print("Check diff of staged vs running config")
print(config.diff())

config.rollback(0)


print("Check diff of staged vs running config after rollback")
print(config.diff())
