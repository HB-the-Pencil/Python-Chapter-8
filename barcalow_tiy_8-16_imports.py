# PyCharm is going to hate me for all these import statements...
import user_profile
method_1 = user_profile.build_profile("import", "module", item="first")
print(method_1)

from user_profile import build_profile
method_2 = build_profile("from module", "import function", item="second")
print(method_2)

from user_profile import build_profile as build
method_3 = build("from module", "import function as x", item="third")
print(method_3)

import user_profile as u
method_4 = u.build_profile("import module", "as x", item="fourth")
print(method_4)

from user_profile import *
method_5 = build_profile("from module", "import *", item="fifth")
print(method_5)
# Surprisingly, no errors.
