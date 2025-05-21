from flask import Flask, render_template, redirect, url_for
import os
import logging
from data import PROJECTS_DATA, TEAM_MEMBERS, ADVISORS

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)

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

@app.route('/team/')
def team():
    team_information = "Our team is composed of highly skilled data scientists and AI engineers who thrive on solving complex challenges. Founder Daniel Strick serves as a Principal AI/ML Engineer, bringing deep expertise in machine learning, deep learning, and robust data engineering to Strick Data Solutions."
    return render_template('team.html', team_members=TEAM_MEMBERS,
                           team_information = team_information,
                           advisors = ADVISORS)  # Use global TEAM_MEMBERS
@app.route('/team')
def team_with_slash():
    return redirect(url_for('team'))

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)

######## flask --debug run
