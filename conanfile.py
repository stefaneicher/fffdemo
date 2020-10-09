from conans import ConanFile, CMake, tools
import os

class FFFDemo(ConanFile):
    name = "FFFDemo"
    version = "0.1"
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"
    exports_sources = "src/*", "CMakeLists.txt", "test/*"
    requires = "gtest/1.10.0"

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
        cmake.test()

    def package(self):
        self.copy("*.h", dst="include", src="src")
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)


if __name__ == "__main__":
    conan_file_path = os.path.dirname(os.path.realpath(__file__))
    os.system(f"conan create --build=missing . eicher/development ")
