from suds.client import Client
from suds import WebFault
from fixture.project import Project

class SoapFixture:

    def __init__(self, client, username, password):
        self.username=username
        self.password=password
        self.client=Client(client)
        if self.can_login()==True:
            pass

    def can_login(self):
   #     self.client = Client("http://localhost/mantisbt-1.2.20/api/soap/mantisconnect.php?wsdl")
        try:
            self.client.service.mc_login(self.username, self.password)
            return True
        except WebFault:
            return False


    def get_project_list(self):
        list = []
        try:
            listdata = self.client.service.mc_projects_get_user_accessible(self.username, self.password)
            for row in listdata:
                list.append(Project(id=str(row.id), name=row.name.strip(), description=row.description.strip()))
            return list
        except WebFault:
            return False

    def destroy(self):
        pass
