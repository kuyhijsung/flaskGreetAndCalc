from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)
# Put your app in here.


@app.route("/add")
def add_math():
    """Add a and b parameters."""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = add(a, b)

    return str(result)


@app.route("/sub")
def sub_math():
    """Subtract and b parameters."""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = sub(a, b)

    return str(result)


@app.route("/mult")
def mult_math():
    """Multiply a and b parameters."""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = mult(a, b)

    return str(result)


@app.route("/div")
def div_math():
    """Divide a and b parameters."""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = div(a, b)

    return str(result)


# solution code for refractoring

# operators = {          adding class methods into a dict.
#     "add": add,
#     "sub": sub,
#     "mult": mult,
#     "div": div,
# }


# @app.route("/math/<oper>")           creating a route that uses <> in the route to use it as arguments to be passed into the parameter of the do_math method.
# def do_math(oper):
#     """Do math on a and b."""

#     a = int(request.args.get("a"))      get request of the query string.
#     b = int(request.args.get("b"))
#     result = operators[oper](a, b)      calling the operators dict and passing in the argument as the key, which calls the method that matches with that key and then passing in the initialized values from the get request
#                                         in order to execute the said method.

#     return str(result)                  returning the total as a string to be passed into the body of the page.
