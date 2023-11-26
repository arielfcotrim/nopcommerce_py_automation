import os


# Define a class to manage directory paths
class DirPathManager:
    @staticmethod
    def get_project_root_directory():
        """
        Get the root directory of the project.

        :return: The absolute path of the project's root directory.
        """
        # Use os.path.dirname twice to go up two levels from the current file,
        # which gives the project's root directory
        return os.path.dirname(os.path.dirname(__file__))

    @staticmethod
    def get_relative_path(*args):
        """
        Construct a path relative to the project's root directory.

        :param args: A sequence of directory names or path segments.
        :return: An absolute path, constructed by joining the project root
                 with the provided path segments.
        """
        # Retrieve the project's root directory
        root_path = DirPathManager.get_project_root_directory()

        # Join the root directory with the provided path segments
        return os.path.join(root_path, *args)
