from conans import ConanFile, CMake
import os

username = os.getenv("CONAN_USERNAME", "sbis")
channel = os.getenv("CONAN_CHANNEL", "testing")

class TestConan(ConanFile):
    generators = "cmake"
    settings = "os", "compiler", "build_type", "arch"

    requires = "event/2.0.22a@%s/%s"%(username, channel)

    def build(self):
        cmake = CMake(self.settings)
        command_line = cmake.command_line

        # Workaround with cmake + msys: https://github.com/conan-io/conan/issues/625
        if self.settings.os == "Windows" and self.settings.compiler == "gcc":
            command_line += ' -G "MSYS Makefiles"'

        self.run('cmake "%s" %s'%(self.conanfile_directory, command_line))
        self.run("cmake --build . %s"%cmake.build_config)

    def imports(self):
        self.copy(pattern="*.dll", dst="bin", src="bin")
        self.copy(pattern="*.so", dst="bin", src="lib")
        self.copy(pattern="*.dylib", dst="bin", src="lib")

    def test(self):
        self.run(os.path.join("bin", "test_exec"))
