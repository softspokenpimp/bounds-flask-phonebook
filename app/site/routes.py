from flask import Blueprint, render_template

# This is the idea of the site and when init.py calls for it, the site will exist 

site = Blueprint('site', __name__, template_folder='site_templates')

@site.route('/')
def home():
    return render_template('index.html')

@site.route('/profile')
def profile():
    return render_template('profile.html')


