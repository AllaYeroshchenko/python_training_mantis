from suds.client import Client
from suds import WebFault
from fixture.project import Project

class SoapHelper:

    def __init__(self, app):
        self.app = app


    def can_login(self, username, password):
        client = Client("http://localhost/mantisbt-1.2.20/api/soap/mantisconnect.php?wsdl")
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False


    def get_project_list(self, username, password):
        list = []
        client = Client("http://localhost/mantisbt-1.2.20/api/soap/mantisconnect.php?wsdl")
        try:
            listdata = client.service.mc_projects_get_user_accessible(username, password)
            for row in listdata:
                list.append(Project(id=str(row.id), name=row.name.strip(), description=row.description.strip()))
            return list
        except WebFault:
            return False

