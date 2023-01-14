from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def location():
    return render_template('location.html')

@app.route('/size', methods=['POST'])
def size():
    location = request.form['location']
    return render_template('size.html', location=location)

@app.route('/building', methods=['POST'])
def building():
    location = request.form['location']
    size = request.form['size']
    return render_template('building.html', location=location, size=size)

@app.route('/rate', methods=['POST'])
def rate():
    location = request.form['location']
    size = request.form['size']
    building = request.form['building']
    return render_template('rate.html', location=location, size=size, building=building)

if __name__ == '__main__':
    app.run()


@app.route('/result', methods=['POST'])
def result():
    location = request.form['location']
    size = float(request.form['size'])
    building = request.form['building']
    rate = float(request.form['rate'])

    # Static inputs
    flex_rate = 487
    secondary_services_percent = 115/100
    density = 5.86
    fitout_cost = 128.64
    fm_cost = 162.88
    staffing_cost = 110.68

    # Calculate traditional revenues
    traditional_revenues = size * rate

    # Calculate flex revenues
    if building == "Grade A CBD":
        quality = "high quality city centre"
    elif building == "Grade A non-core":
        quality = "high quality non-core"
    elif building == "Grade B CBD":
        quality = "medium quality"
    elif building == "Grade B non-core":
        quality = "value based"
    else:
        quality = "Business Park"
    flex_revenues = size * flex_rate * density * secondary_services_percent

    # Calculate flex cost
    flex_cost = (fitout_cost + fm_cost + staffing_cost) * size
    flex_cost_amortized = flex_cost / 10

    return render_template('result.html', location=location, size=size, building=building, rate=rate, traditional_revenues=traditional_revenues, flex_revenues=flex_revenues, flex_cost_amortized=flex_cost_amortized, quality=quality)
