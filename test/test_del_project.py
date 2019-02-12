from model.project import Project
import random
import string


def test_del_project(app, db):
    old_projects = app.project.get_project_list()
    if len(old_projects) == 0:
        project = Project(name="name", description="description")
        app.project.make(project)
        old_projects = app.project.get_project_list()
    old_projects_db=db.get_project_list()
    assert sorted(old_projects, key=Project.id_or_max) == sorted(old_projects_db, key=Project.id_or_max)
    project=random.choice(old_projects)
    app.project.delete_by_id(project.id)
    old_projects.remove(project)
    new_projects_db=db.get_project_list()
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects_db, key=Project.id_or_max)


