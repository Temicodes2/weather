from flask import Flask, render_template, request
import requests
app = Flask(__name__)
@app.route("/")
def visitors():
    counter_read_file = open("count.txt","r")
    visitors_count = int(counter_read_file.read())
    counter_read_file.close()
    visitors_count = visitors_count + 1
    counter_write_file = open("count.txt","w")
    counter_write_file.write(str(visitors_count))
    counter_write_file.close()
    return render_template("index.html", count=visitors_count)
@app.route("/", methods=["POST"])
def weather_stats():
    counter_read_file = open("count.txt","r")
    visitors_count = int(counter_read_file.read())
    counter_read_file.close()
    lat=request.form["lat"]
    lon=request.form["lon"]
    api_url = 'https://weather-l6tl.onrender.com/api/getCurrentWeather/'+lat+"/"+lon
    response = requests.get(api_url)
    weather_data = response.json()
    print(weather_data)
    return render_template("index.html", weather=weather_data, count=visitors_count)
if __name__ == "main":
    app.run()