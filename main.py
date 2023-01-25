"""
Simple User Settings
"""
import time
import usersettings

# Identify your application - 'settings.cfg' will be saved in %AppData%\my_test_app\my_test_app
s = usersettings.Settings('my_test_app')

# Specify settings
s.add_setting('counter', int, default=0)
s.add_setting('animal', str, default='turtle')
s.add_setting('runtimes', list, [])
s.add_setting('my_dict', dict, {'firstkey':1,'secondkey':2,'thirdkey':3})

# load any previously saved values for those settings
s.load_settings()

# use those settings
s.counter += 1
if s.counter > 2:
    # switch a setting
    s.animal = 'gold fish'
s.runtimes.append(time.time())

# save setting changes
s.save_settings()

print(
    (
        "I've run {0.counter} time(s).\n"
        "Animal is set to {0.animal}.\n"
        "I've been launched at these times:\n {0.runtimes}"
    ).format(s)
)

print(list(s.my_dict.values()))