from conan import ConanFile
from conan.tools.cmake import CMake, CMakeToolchain, cmake_layout


class StructoptConan(ConanFile):
    name = "structopt"
    settings = "os", "arch", "compiler", "build_type"
    generators = "CMakeDeps"

    def layout(self):
        cmake_layout(self)

    def requirements(self):
        self.requires("magic_enum/0.9.6")
        self.requires("visit_struct/1.1.0")
        self.test_requires("doctest/2.4.11")

    def generate(self):
         tc = CMakeToolchain(self)
         tc.variables["STRUCTOPT_TESTS"] = True
         tc.variables["STRUCTOPT_SAMPLES"] = True
         tc.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
