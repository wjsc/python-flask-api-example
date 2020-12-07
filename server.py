from flask import Flask, request, jsonify, make_response, abort
import my_math
app = Flask(__name__)

@app.route('/sum')
def sum():
    """ Calculate X + Y """
    x, y = int(request.args.get('x')), int(request.args.get('y'))
    return jsonify({"result": my_math.sum(x, y) })

@app.route('/minus')
def minus():
    """ Calculate X - Y """
    x, y = int(request.args.get('x')), int(request.args.get('y'))
    return jsonify({"result": my_math.minus(x, y) })

@app.route('/mult')
def mult():
    """ Calculate X * Y """
    x, y = int(request.args.get('x')), int(request.args.get('y'))
    return jsonify({"result": my_math.mult(x, y) })

@app.route('/divide')
def divide():
    """ Calculate X / Y """
    try:
        x, y = int(request.args.get('x')), int(request.args.get('y'))
        return jsonify({"result": my_math.divide(x, y) })
    except ZeroDivisionError as e:
        abort(make_response(jsonify({ "message": "Y parameter can't be zero"}), 400))

if __name__ == "__main__":
    print("ready to run...")
    app.run(host="0.0.0.0", port=3000)