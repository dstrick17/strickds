from flask import Flask, render_template
import os
import logging

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)

@app.route('/')
def home():
    projects = [
        {"title": "Hampden County Registry of Deeds", "desc": "Leveraged a powerful computer vision model to transcribe 300 year old documents into a digitized format. This data was then indexed, making search much more efficient."},
        {"title": "Radiologist Level Computer Vision Model", "desc": "We developed and trained a Computer Vision Model to read chest X-Rays, with an accuracy of x.xx %. This model has been made publically available in order to help trained professionals to be able to diagnose patients more efficiently. ", "link" : "https://huggingface.co/spaces/cfgpp/Danny_Net_Demo"}
    ]
    mission = "Strick Data Solutions is a data science and AI consulting agency based in Boston, Massachusetts. We specialize in helping small and medium-sized businesses unlock the power of their data to drive smarter decisions, boost efficiency, and fuel growth. Founded on the belief that cutting-edge technology should be accessible to all businesses, not just Fortune 500s, we bring elite data science and AI expertise to organizations that need practical, scalable, and personalized solutions."
    team = "We're a team of highly skilled data scientists and AI engineers who thrive on solving complex challenges. Our size allows us to be agile, our focus keeps us efficient, and our passion ensures every project delivers real impact."
    value = ["Clarity over jargon", "Speed without compromise", "Partnership over transactions", "Results that matter"]
    quote = "Whether you're trying to make sense of messy data, automate workflows, build predictive models, or simply figure out where to start, we’re here to guide you."
    contact_email = "strickds@proton.me"
    return render_template('home.html',
                           mission=mission,
                           team=team,
                           quote=quote,
                           value=value,
                           contact_email=contact_email,
                           projects=projects)

@app.route('/about')
def about():
    about = "We are a team of Data Science Consultants eager to work on varying projects. From Healthcare to Computer Vision, Strick Data Solutions is here to help. Contact us to collaborate or consult!"
    return render_template('about.html',
                           about=about)

@app.route('/contact')
def contact():
    contact_email = "strickds@proton.me"
    print("Contact page accessed") 
    return render_template('contact.html',
                           contact_email=contact_email) 

@app.route('/projects')
def projects():
    projects = [
        {"title": "Hampden County Registry of Deeds", "desc": "Leveraged a powerful computer vision model to transcribe 300 year old documents into a digitized format. This data was then indexed, making search much more efficient."},
        {"title": "Radiologist Level Computer Vision Model", "desc": "We developed and trained a Computer Vision Model to read chest X-Rays, with an accuracy of x.xx %. This model has been made publically available in order to help trained professionals to be able to diagnose patients more efficiently. ", "link" : "https://huggingface.co/spaces/cfgpp/Danny_Net_Demo"}
    ]
    return render_template('projects.html',
                            projects=projects)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
