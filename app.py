from flask import Flask, render_template, redirect, url_for
import os
import logging

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)

@app.route('/')
def home():
    projects = [
        {"title": "Hampden County Registry of Deeds", "desc": "Transformed centuries of historical records for the Hampden County Registry of Deeds by applying advanced computer vision. Our model digitized 300-year-old documents, enabling efficient search and access to invaluable information"},
        {"title": "Developed a cutting-edge Computer Vision Model for chest X-Ray analysis", "desc": "Achieving an average AUC-ROC of 0.85, this publicly available tool empowers radiologists with an efficient aid for more accurate and timely patient diagnoses.", "link": "https://huggingface.co/spaces/cfgpp/Danny_Net_Demo"},
    ]
    mission = "Strick Data Solutions is a data science and AI consulting agency based in Boston, Massachusetts. We specialize in helping small and medium-sized businesses unlock the power of their data to drive smarter decisions, boost efficiency, and fuel growth. Founded on the belief that cutting-edge technology should be accessible to all businesses, not just Fortune 500s, we bring elite data science and AI expertise to organizations that need practical, scalable, and personalized solutions."
    team = "We're a team of highly skilled data scientists and AI engineers who thrive on solving complex challenges. Our size allows us to be agile, our focus keeps us efficient, and our passion ensures every project delivers real impact."
    value = ["Clarity over jargon", "Speed without compromise", "Partnership over transactions", "Results that matter"]
    quote = "Whether you're trying to make sense of messy data, automate workflows, build predictive models, or simply figure out where to start, we’re here to guide you."
    contact_email = "info@strickds.com"
    return render_template('home.html',
                           mission=mission,
                           team=team,
                           quote=quote,
                           value=value,
                           contact_email=contact_email,
                           projects=projects)

@app.route('/about/')
def about():
    about = "We are a team of Data Science Consultants eager to work on varying projects. From Healthcare to Computer Vision, Strick Data Solutions is here to help. Contact us to collaborate or consult!"
    return render_template('about.html',
                           about=about)

@app.route('/about')
def about_with_slash():
    return redirect(url_for('about'))

@app.route('/contact/')
def contact():
    contact_email = "info@strickds.com"
    print("Contact page accessed") 
    return render_template('contact.html',
                           contact_email=contact_email) 

@app.route('/contact')
def contact_with_slash():
    return redirect(url_for('contact'))

@app.route('/projects/')
def projects():
    projects = [
        {"title": "Hampden County Registry of Deeds", "desc": "Transformed centuries of historical records for the Hampden County Registry of Deeds by applying advanced computer vision. Our model digitized 300-year-old documents, enabling efficient search and access to invaluable information"},
        {"title": "Developed a cutting-edge Computer Vision Model for chest X-Ray analysis", "desc": "Achieving an average AUC-ROC of 0.85, this publicly available tool empowers radiologists with an efficient aid for more accurate and timely patient diagnoses.", "link": "https://huggingface.co/spaces/cfgpp/Danny_Net_Demo"},
    ]
    return render_template('projects.html',
                            projects=projects)

@app.route('/projects')
def projects_with_slash():
    return redirect(url_for('projects'))

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
