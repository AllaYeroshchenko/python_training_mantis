from model.project import Project
import time

class ProjectHelper:

    def __init__(self, app):
        self.app=app

    def open_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("my_view_page.php")):
            wd.find_element_by_xpath("//img[@alt='MantisBT']").click()

    def make(self, project):
        wd = self.app.wd
        self.go_to_project_page()
        wd.find_element_by_xpath("//input[@value='Create New Project']").click()
        wd.find_element_by_name("name").send_keys(project.name)
        wd.find_element_by_name("description").send_keys(project.description)
        wd.find_element_by_xpath("//input[@value='Add Project']").click()
        time.sleep(5)

    def go_to_project_page(self):
        wd = self.app.wd
        self.open_home_page()
        wd.find_element_by_link_text("Manage").click()
        wd.find_element_by_link_text("Manage Projects").click()

    def get_project_list(self):
        wd = self.app.wd
        list=[]
        self.go_to_project_page()
        project_table=wd.find_elements_by_xpath("//table[@class='width100']//tr[@class='row-category']/following-sibling::tr")
        for element in project_table:
            name=element.find_element_by_xpath(".//td[1]/a").text
            id=element.find_element_by_xpath(".//td[1]/a").get_attribute("href").split("project_id=", 1)[1]
            description=element.find_element_by_xpath(".//td[5]").text
            list.append(Project(id=id, name=name, description=description))
        return list

