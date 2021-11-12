from urllib import request
import toml
from project import Project


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        # print(content)

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        data = toml.loads(content)
        poetry_data = data['tool']['poetry']
        name = poetry_data['name']
        description = poetry_data['description']
        dependencies = poetry_data['dependencies']
        dev_dependencies = data['tool']['poetry']['dev-dependencies']
        return Project(name, description, dependencies, dev_dependencies)
