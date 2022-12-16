from flask import render_template
from app import app
from sqlalchemy.ext.automap import automap_base
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)
print(db)
Base = automap_base()
Base.prepare(db.engine, reflect=True)
cert_table = Base.classes.cert
comm_table = Base.classes.comm
con_table = Base.classes.contact
education_table = Base.classes.education
experience_table = Base.classes.experience
program_table = Base.classes.program
project_table = Base.classes.projects
technique_table = Base.classes.technique
tool_table = Base.classes.tools

@app.route('/')
def index():
    certs = db.session.query(cert_table).all()
    comm = db.session.query(comm_table).all()
    con = db.session.query(con_table).all()
    edu = db.session.query(education_table).all()
    exp = exp_format(db.session.query(experience_table).all())
    program = db.session.query(program_table).all()
    project = project_format(db.session.query(project_table).all())
    technique = db.session.query(technique_table).all()
    tool = db.session.query(tool_table).all()
    
    return render_template(
        'index.html',
        title='Hoang Xuan Bui',
        cert_list=certs,
        comm_list=comm,
        con_list=con,
        edu_list=edu,
        exp_list=exp,
        program_list=program,
        project_list=project,
        technique_list=technique,
        tool_list=tool
    )


def exp_format(tab):
    tab_list = []

    for field in tab:
        tab_list.insert(0, {
            'company': field.company,
            'location': field.location,
            'title': field.title,
            'start': field.start,
            'end': field.end,
            'bullets': data_split(field.bullets),
            'urls': data_split(field.urls),
            'desc': field.desc
        })

    return tab_list


def project_format(tab):
    tab_list = [None] * len(tab)

    for field in tab:
        tab_list[field.id-1] = {
            'title': field.title,
            'urls': data_split(field.urls),
            'summary': field.summary,
            'pics': data_split(field.pics),
            'start_date': field.start_date,
            'end_date': field.end_date,
        }
    return tab_list[::-1]

def data_split(d):
    if d != None:
        return d.split('>>>')
    else:
        return d