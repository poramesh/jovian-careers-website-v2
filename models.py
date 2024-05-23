from app import db
import datetime


class jobs(db.Model):
    id = db.Column(db.Integer, primary_key=True) #So, id = db.Column(db.Integer, primary_key=True) in SQLAlchemy is a direct equivalent of id INT NOT NULL AUTO_INCREMENT in SQL. It creates an integer primary key column that auto-increments with each new record, ensuring it is always unique and not null.
    title = db.Column(db.String(250), nullable=False)
    location = db.Column(db.String(50), nullable=False)
    salary = db.Column(db.Integer)
    currency = db.Column(db.String(10))
    responsibilities = db.Column(db.String(2000))
    requirements = db.Column(db.String(2000))



class application(db.Model):
      id = db.Column(db.Integer, primary_key = True)
      job_id = db.Column(db.Integer, nullable = False) 
      full_name = db.Column(db.String(100),nullable =False)
      email = db.Column(db.String(100), unique =True)
      linkedin_url = db.Column(db.String(50))
      education = db.Column(db.String(50))
      work_experience = db.Column(db.String(100))
      resume_url = db.Column(db.String(40))
      created_at = db.Column(db.DateTime, default=datetime.datetime.now())
      updated_at = db.Column(db.DateTime, default=datetime.datetime.now(), onupdate=datetime.datetime.now())


def load_jobs_from_model():
    jobsFromTheSqliteDatabase = jobs.query.all()
    jobList = []
    for job in jobsFromTheSqliteDatabase:
        job_data = {
            'id':job.id,
            'title':job.title,
            'location':job.location,
            'salary':job.salary,
            'currency':job.currency,
            'responsibilities':job.responsibilities,
            'requirements':job.requirements
        }
        jobList.append(job_data)
        print(job_data)
    return jobList


def load_job_from_model(id):
    jobFromTheSqliteDatabase = jobs.query.get(id)
    if(jobFromTheSqliteDatabase):
        jobList = {
                 'id':jobFromTheSqliteDatabase.id,
                 'title':jobFromTheSqliteDatabase.title,
                 'location':jobFromTheSqliteDatabase.location,
                 'salary':jobFromTheSqliteDatabase.salary,
                 'currency':jobFromTheSqliteDatabase.currency,
                 'responsibilities':jobFromTheSqliteDatabase.responsibilities,
                 'requirements':jobFromTheSqliteDatabase.requirements
            }
        print(jobList)
    return jobList

def add_application_to_db(id,data):
    app = application(job_id=id,
                    full_name =data['full_name'], 
                    email =data['email'], 
                    linkedin_url = data['linkedin_url'],
                    education = data['education'], 
                    work_experience =data['work_experience'], 
                    resume_url=data['resume_url'])
    db.session.add(app)
    db.session.commit()





     
 



