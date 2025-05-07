from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    projects = [
        {"name": "coffee rating website", "description": "this site enable us to share our experience of a coffee shop that we visited and rate it for others usage", "images": ["coffee1.png", "coffee2.png", "coffee3.png"],"link":"https://github.com/sampathkumar-l/coffeeshop-rating-provider"},
        {"name": "movie sharing site", "description": "this will work like the imbd site,that it will tell movie's description and also the rating of that movie", "images": ["movie1.png", "movie2.png", "movie3.png"],"link":"https://github.com/sampathkumar-l/movielist-and-it-review-site"},
        {"name": "quizler", "description": "this is simple quiz game that will show my begining of coding phase", "images": ["quiz1.png", "quiz2.png", "quiz3.png"],"link":"https://github.com/sampathkumar-l/quizzler-app-using-open-trivia-db"},
        {"name": "quotes generater", "description": "this is a simple quote generator to enable me unterstand the gui basics", "images": ["quotes1.png", "quotes2.png"],"link":"https://github.com/sampathkumar-l/kanye-quotes-start"},
        {"name": "rain notifier", "description": "this project will help you track the rain day in the morning by getting a sms about it ,so you take an umberlla when you leave the home", "images": ["mess.jpg"],"link":"https://github.com/sampathkumar-l/wheather-notifier"},
    ]
    return render_template('index.html', projects=projects)

if __name__ == '__main__':
    app.run(debug=True)
