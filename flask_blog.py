from flask import Flask, render_template, url_for

posts = [
    {
    'author': 'Aish',
    'content': 'My First Blog - wohoo',
    'title': 'My Intro',
    'date_posted': '07/09/2022'
    },
    {
    'author': 'Akshay',
    'Blog': 'Food Blog',
    'title': 'Visit to Saravana Bhavan',
    'date_posted': '11/09/2022'
    }
]

app = Flask(__name__) #__name__ -> name of the module -> to inform flask which module we are gonna run

@app.route('/') #route we type in our browser to go to different pages
@app.route('/home')
def home():
    return render_template('home.html', template_var = posts, page_name = "Home page")
    # ^ Having the entire HTML code makes the overall code look ugly -> templates
    
@app.route('/about')
def about():
    return render_template('about.html', template_var = posts, page_name = "About")

if __name__ == "__main__":
    app.run(debug=True)


