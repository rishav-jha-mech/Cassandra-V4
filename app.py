from flask import Flask, jsonify,request, render_template
from pytube import YouTube

app = Flask(__name__,template_folder="templates",static_url_path='', static_folder='static')


@app.route("/", methods=['GET','POST'])
def api():

    if request.method == 'POST':
        uri = request.form['link']
        print(f"{uri} \n {uri} \n")
        try:
            video = YouTube(uri)
            a=video.streams.filter(progressive=False, only_video=True)
            b=video.streams.filter(only_audio=True)
            c=video.streams.filter(progressive=True)
        except:
            message = "Wrong URL Entered"
            render_template("index.html",message=message)

        return render_template("index.html",yobj=video,onlyVideo=a,onlyAudio=b,bothVideoAudio=c)

    return render_template("index.html") # For Handling GET Request

if __name__ == "__main__":
    app.run(debug=True,port=5050)