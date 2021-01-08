import subprocess
this_is_a_very_very_long_variable = 10
this_is_an_another_very_very_long_variable = 11
short_variable = 1
little = 0
if (this_is_a_very_very_long_variable > this_is_an_another_very_very_long_variable
        and this_is_a_very_very_long_variable - this_is_an_another_very_very_long_variable > 5):
    pass
if (short_variable > little or this_is_a_very_very_long_variable > this_is_an_another_very_very_long_variable
        and this_is_a_very_very_long_variable - this_is_an_another_very_very_long_variable > 5):
    pass


class MyClass(object):
    class InnerClass(object):
        pass

    def function1(self):
        def inner_function(self):
            pass

        pass
