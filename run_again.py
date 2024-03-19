#The following decorator runs the function again in case of any error.

def try_again(f):
    import time
    def wrapper(*args, **kwargs):
        failures = 0
        allowed_attempts = 5
        while failures < allowed_attempts:
            try:
                return f(*args, **kwargs)
            except Exception as error:
                print(f"We encountered the following error {error}.")
                failures += 1
                time.sleep(6)
    return wrapper



@try_again
def converter(variable):
    variable_type = type(variable)
    if variable_type.__name__ == "str":
        output = int(variable)
    elif variable_type.__name__ == "int":
        output = str(variable)
    print(output)
    return output


converter("r3")