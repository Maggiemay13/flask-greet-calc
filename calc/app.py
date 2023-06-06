# Put your app in here.
from flask import Flask, request

from operations import add, sub, mult, div

app = Flask(__name__)


@app.route("/add")
def add_numbers():
    """Add a and b parameters"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = add(a, b)

    return str(result)


@app.route("/sub")
def subtract_numbers():
    """Subtract a and b parameters"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = sub(a, b)

    return str(result)


@app.route("/mult")
def multiply_numbers():
    """Multiply a and b parameters"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = mult(a, b)

    return str(result)


@app.route("/div")
def divide_numbers():
    """Divide a and b parameters"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = div(a, b)

    return str(result)

# use a dictionary to map operation names to the functions that do the underlying math
operators = {
    "add": add,
    "sub": sub,
    "mult": mult,
    "div": div
}


@app.route("/math/<oper>")
def dp_math(oper):
    """Do math with paramater a and b"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = operators[oper](a, b)

    return str(result)
