from flask import Flask, render_template, redirect, url_for
import os
import logging

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)

PROJECTS_DATA = [
    {
        "title": "Digitizing Centuries of History with Computer Vision",
        "desc": "Developed a sophisticated computer vision pipeline to transcribe and digitize centuries-old handwritten records from the 18th century for the Hampden County Registry of Deeds. Our solution transformed 300-year-old documents into an easily searchable digital format, unlocking invaluable historical information.",
        "link": None
    },
    {
        "title": "AI-Powered Chest X-Ray Analysis for Enhanced Diagnostics",
        "desc": "Developed a cutting-edge computer vision model for interpreting chest X-rays, achieving an impressive average AUC-ROC of 0.85 (ranking second on Papers With Code) and a leading macro F1 score of 0.39. This publicly accessible tool provides radiologists with an efficient and accurate aid for timely patient diagnoses.",
        "link": "https://huggingface.co/spaces/cfgpp/Danny_Net_Demo"
    },
    {
        "title": "Empowering Education Through Technology: Website and Database for Volunteer Tutors",
        "desc": "Designed and built a comprehensive website and database platform for a volunteer organization dedicated to teaching underserved students. This platform streamlines operations, connects tutors with students, and facilitates effective learning.",
        "link": "https://volunteertutors.netlify.app/"
    },
    {
        "title": "Interactive Data Visualization for Federal Grant Distribution Analysis",
        "desc": "Created an interactive web application for Senator Edward Markey’s Office to analyze over $10 billion in federal grant distributions across Massachusetts. This tool enables in-depth exploration and visualization of complex data, supporting informed decision-making and policy analysis.",
        "link": None
    },
]

@app.route('/')
def home():
    mission = "Strick Data Solutions is a data science and AI consulting agency based in Boston, Massachusetts. We specialize in helping small and medium-sized businesses unlock the power of their data to drive smarter decisions, boost efficiency, and fuel growth. Founded on the belief that cutting-edge technology should be accessible to all businesses, not just Fortune 500s, we bring elite data science and AI expertise to organizations that need practical, scalable, and personalized solutions."
    team = "We're a team of highly skilled data scientists and AI engineers who thrive on solving complex challenges. Our size allows us to be agile, our focus keeps us efficient, and our passion ensures every project delivers real impact."
    value = ["Clarity over jargon", "Speed without compromise", "Partnership over transactions", "Results that matter"]
    quote = "Whether you're trying to make sense of messy data, automate workflows, build predictive models, or simply figure out where to start, we’re here to guide you."
    contact_email = "info@strickds.com"
    return render_template('home.html',
                           mission=mission,
                           team=team,
                           quote=quote,
                           value=value,
                           contact_email=contact_email)

@app.route('/about/')
def about():
    about = """
    Strick Data Solutions is a Boston-based data science and AI consulting agency
    dedicated to empowering small and medium-sized businesses across industries
    like healthcare, retail, finance, and marketing. Founded on the principle
    that expert data insights should be accessible to all, we bridge the gap
    for SMBs seeking to leverage their data for strategic advantage.

    Our team of elite AI engineers and data scientists delivers tailored solutions
    with agility and speed, understanding the urgency of data-driven decisions.
    We pride ourselves on providing top-tier talent and personalized service,
    building strong partnerships to ensure cost-effective solutions and measurable
    results for every client.

    Contact us to explore how our expertise can transform your operations and
    drive your growth in a data-driven future.
    """
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
    return render_template('projects.html', projects=PROJECTS_DATA)  # Use global PROJECTS_DATA

@app.route('/projects')
def projects_with_slash():
    return redirect(url_for('projects'))

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)

######## flask --debug run
