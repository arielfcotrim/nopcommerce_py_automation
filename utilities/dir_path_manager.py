import os


class DirPathManager:
    @staticmethod
    def get_project_root_directory():
        return os.path.dirname(os.path.dirname(__file__))

    @staticmethod
    def get_relative_path(*args):
        root_path = DirPathManager.get_project_root_directory()
        return os.path.join(root_path, *args)
