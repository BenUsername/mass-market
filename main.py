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


