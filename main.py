#Decorator that saves stored functions and recalls them in case they are run again
import json

def logger(f):
    def wrapper(*args, **kwargs):
        result = ""
        #To check if the function has already been run
        try:
            with open("history.json", "r") as file:
                history_data = json.load(file)
        except FileNotFoundError:
            history_data = []
            with open("history.json", "w") as file:
                json.dump(history_data, file, indent=4)
        for i in range(len(history_data)-1):
            if f.__name__ == history_data[i]["name"] and kwargs == history_data[i]["kwargs"] and args == history_data[i]["args"]:
                result = history_data[i]["result"]

        if result == "":
            function_info = {
                "name": f.__name__,
                "args": args,
                "kwargs": kwargs,
                "result": f(*args, **kwargs)}
            result = f(*args, **kwargs)
            history_data.append(function_info)
            with open("history.json", "w") as file:
                json.dump(history_data, file, indent=4)
        return result
    return wrapper

@logger
def adder(x, y):
    print(int(x) + int(y))
    return(int(x) + int(y))


adder(55, 23)


