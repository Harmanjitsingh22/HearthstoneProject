# Tests for Resource.py
from Resource import Resource

new_resource = Resource()
new_resource.set_resource_type("Gemstone")
assert new_resource.resource_type == "Gemstone"

new_resource2 = Resource()
new_resource2.set_resource_type("Gold")
assert new_resource2.resource_type == "Gold"