# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div

@app.route('/add')
def do_add(a, b):
    """Add a and b parameters."""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = add(a,b)

    return str(result)

@app.route('/subtract')
def do_sub(a, b):
    """Substract b from a parameters."""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = sub(a,b)

    return str(result)

@app.route('/multiply')
def do_mult(a, b):
    """Multiply a and b parameters."""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = mult(a,b)

    return str(result)

@app.route('/divide')
def do_div(a, b):
    """Divide a by b parameters."""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = div(a,b)

    return str(result)

# Part two
operators = {
        "add": add,
        "sub": sub,
        "mult": mult,
        "div": div,
        }


@app.route("/math/<oper>")
def do_math(oper):
    """Do math on a and b."""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = operators[oper](a, b)

    return str(result)
