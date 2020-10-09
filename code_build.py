import os


def code_build():
    conan_file_path = os.path.dirname(os.path.realpath(__file__))
    os.system(f"conan create --build=missing {conan_file_path} eicher/development ")


if __name__ == "__main__":
    code_build()
