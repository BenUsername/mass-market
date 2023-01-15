from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/location", methods=["POST"])
def location():
    location = request.form["location"]
    return render_template("location.html", location=location)

@app.route("/size", methods=["POST"])
def size():
    location = request.form["location"]
    size = request.form["size"]
    return render_template("size.html", location=location, size=size)

@app.route("/building", methods=["POST"])
def building():
    location = request.form["location"]
    size = request.form["size"]
    building = request.form["building"]
    return render_template("building.html", location=location, size=size, building=building)

@app.route("/rate", methods=["POST"])
def rate():
    location = request.form["location"]
    size = request.form["size"]
    building = request.form["building"]
    rate = request.form["rate"]
    return render_template("rate.html", location=location, size=size, building=building, rate=rate)

@app.route("/result", methods=["POST"])
def result():
    location = request.form["location"]
    size = request.form["size"]
    building = request.form["building"]
    rate = request.form["rate"]
    flex_rate = 487
    secondary_services = 115
    average_density = 5.86
    fit_out = 128.64
    fm = 162.88
    staffing = 110.68
    traditional = (int(size) * int(rate))
    flex = (int(size) * int(rate)) + (int(size) * flex_rate)
    flex_cost = (int(size) * fit_out) + (int(size) * fm) + staffing
    return render_template("result.html", location=location, size=size, building=building, rate=rate, traditional=traditional, flex=flex, flex_cost=flex_cost)

if __name__ == "__main__":
    app.run(debug=False)
