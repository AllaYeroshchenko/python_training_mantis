from model.project import Project
import pytest
import random
import string

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [Project(random_string("name", 10), random_string("description", 15)) for i in range(1)]

@pytest.mark.parametrize("project", testdata, ids=[repr(x) for x in testdata])
def test_make_project(app, soap, project):
    old_projects = app.project.get_project_list()
    old_projects_soap=soap.get_project_list()
    assert sorted(old_projects, key=Project.id_or_max) == sorted(old_projects_soap, key=Project.id_or_max)
    app.project.make(project)
    old_projects.append(project)
    new_projects_soap=soap.get_project_list()
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects_soap, key=Project.id_or_max)


