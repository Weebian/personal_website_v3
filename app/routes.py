from flask import render_template
from app import app
from sqlalchemy.ext.automap import automap_base
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)
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
cosplay_table = Base.classes.cosplay
panels_table = Base.classes.panels
gunpla_table = Base.classes.gunpla
gardening_table = Base.classes.gardening
woodworking_table = Base.classes.woodworking

app.add_url_rule

@app.route('/')
def index():
    con = db.session.query(con_table).all()
    
    return render_template(
        'index.html',
        title='Home',
        con_list=con
    )

@app.route('/resume')
def resume():
    certs = cert_format(db.session.query(cert_table).all())
    comm = db.session.query(comm_table).all()
    con = db.session.query(con_table).all()
    edu = db.session.query(education_table).all()
    exp = exp_format(db.session.query(experience_table).all())
    program = db.session.query(program_table).all()
    project = project_format(db.session.query(project_table).all())
    technique = db.session.query(technique_table).all()
    tool = db.session.query(tool_table).all()
    
    return render_template(
        'resume.html',
        title='Resume',
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

@app.route('/cosplay')
def cosplay():
    con = db.session.query(con_table).all()
    cos = yr_format(db.session.query(cosplay_table).all())

    return render_template(
        'cosplay.html',
        title='Cosplay',
        con_list=con,
        cos_list = cos
    )

@app.route('/gunpla')
def gunpla():
    con = db.session.query(con_table).all()
    gunpla = yr_format(db.session.query(gunpla_table).all())

    return render_template(
        'gunpla.html',
        title='Gunpla',
        con_list=con,
        gunpla_list = gunpla
    )

@app.route('/panels')
def panels():
    con = db.session.query(con_table).all()
    panels = panels_format(db.session.query(panels_table).all())

    return render_template(
        'panels.html',
        title='Panels',
        con_list=con,
        panels_list = panels
    )

@app.route('/gardening')
def gardening():
    con = db.session.query(con_table).all()
    gar = gardening_format(db.session.query(gardening_table).all())

    return render_template(
        'gardening.html',
        title='Gardening',
        con_list=con,
        gar_list = gar
    )

@app.route('/photography')
def photography():
    con = db.session.query(con_table).all()

    return render_template(
        'photography.html',
        title='Photography',
        con_list=con
    )

@app.route('/woodworking')
def woodworking():
    con = db.session.query(con_table).all()
    wood = wood_format(db.session.query(woodworking_table).all())

    return render_template(
        'woodworking.html',
        title='Woodworking',
        con_list=con,
        wood_list= wood 
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

def cert_format(tab):
    tab_list = [None]*len(tab)

    for field in tab:
        tab_list[field.id-1] = {
            'name': field.name,
            'date': field.date,
        }

    return tab_list[::-1]

def yr_format(tab):
    curr_date = 0
    tab_list = []

    for field in tab:
        if curr_date == field.date:
            tab_list[-1]['arr'].append(field)
        else:
            curr_date = field.date
            tab_list.append({ 'arr': [field], 'date': field.date })
    
    return tab_list[::-1]

def panels_format(tab):
    curr_date = 0
    tab_list = []

    for field in tab:
        field.copanelists = data_split(field.copanelists)

        if curr_date == field.date:
            tab_list[-1]['arr'].append(field)
        else:
            curr_date = field.date
            tab_list.append({ 'arr': [field], 'date': field.date })
    
    return tab_list[::-1]

def gardening_format(tab):
    curr_date = 0
    tab_list = []

    for field in tab:
        f_field = {
            'plants': field.plants,
            'pic': field.pic,
            'date': field.date
            }

        if curr_date == field.date:
            tab_list[-1]['arr'].append(f_field)
        else:
            curr_date = field.date
            tab_list.append({ 'arr': [f_field], 'date': field.date })
    
    return tab_list[::-1]

def wood_format(tab):
    curr_date = 0
    tab_list = []

    for field in tab:
        f_field = {
            'project': field.project,
            'pics': data_split(field.pictures),
            'desc': field.desc,
            'date': field.date
            }

        if curr_date == field.date:
            tab_list[-1]['arr'].append(f_field)
        else:
            curr_date = field.date
            tab_list.append({ 'arr': [f_field], 'date': field.date })
    
    return tab_list[::-1]

def data_split(d):
    if d != None:
        return d.split('>>>')
    else:
        return d