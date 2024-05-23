from flask import Flask, render_template, jsonify, request
from flask_sqlalchemy import SQLAlchemy
#from database import load_jobs_from_db, load_job_from_db, add_application_to_db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


from models import jobs, application, load_jobs_from_model, load_job_from_model, add_application_to_db

@app.route("/")
def hello_jovian():

  #jobs = load_jobs_from_db()
  jobs = load_jobs_from_model()
  return render_template('home.html', 
                         jobs=jobs)


@app.route("/api/jobs")
def list_jobs():
  jobs = load_jobs_from_model()
  return jsonify(jobs)


@app.route("/job/<id>")
def show_job(id):
  job = load_job_from_model(id)
  
  if not job:
    return "Not Found", 404
  
  return render_template('jobpage.html', 
                         job=job)


@app.route("/api/job/<id>")
def show_job_json(id):
  job = load_job_from_model(id)
  return jsonify(job)

@app.route("/job/<id>/apply", methods=['post'])
def apply_to_job(id):
  data = request.form
  print(data)
  job = load_job_from_model(id)
  add_application_to_db(id, data)
  return render_template('application_submitted.html', 
                         application=data,
                         job=job)


if __name__ == "__main__":
  app.run(debug=True)
