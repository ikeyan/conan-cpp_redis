from contextlib import contextmanager
from conans import ConanFile, CMake, tools
import os

@contextmanager
def in_dir(directory):
    last_dir = os.getcwd()
    try:
        os.makedirs(directory)
    except OSError:
        pass

    try:
        os.chdir(directory)
        yield directory
    finally:
        os.chdir(last_dir)

class CppRedisConan(ConanFile):
    name = "cpp_redis"
    version = "master"
    settings = "os", "compiler", "build_type", "arch"
    requires = (
            "Boost/1.60.0@lasote/stable"
            )
    FOLDER_NAME = "cpp_redis"
    BUILD_FOLDER_NAME = "cpp_redis/build"

    def source(self):
        repository = "https://github.com/Cylix/cpp_redis.git"
        self.run("git clone --recursive %s" % repository)
#        zip_name = "gtest-%s.zip" % self.version
#        url = "https://github.com/Cylix/cpp_redis/archive/master.zip"
#        self.output.info("Downloading %s..." % url)
#        tools.download(url, zip_name)
#        tools.unzip(zip_name)
#        os.unlink(zip_name)

    def build(self):
        cmake = CMake(self.settings)
            
        self.run("cmake %s/%s %s" % (self.conanfile_directory, self.FOLDER_NAME, cmake.command_line))
        self.run("cmake --build . %s" % cmake.build_config)

#        self.run('mkdir %s' % self.BUILD_FOLDER_NAME)
#        self.run('cd %s && cmake .. %s' % (self.BUILD_FOLDER_NAME, cmake.command_line))
#        self.run("cd %s && make -j" % self.BUILD_FOLDER_NAME)

    def package(self):
        self.copy("*", dst="include", src=self.FOLDER_NAME+"/includes")
        self.copy("*", dst="include", src=self.FOLDER_NAME+"/tacopie/includes")
        self.copy("*.lib", dst="lib", src="lib")
        self.copy("*.so", dst="lib", src="lib")
        self.copy("*.a", dst="lib", src="lib")

    def package_info(self):
        self.cpp_info.libs = ["cpp_redis", "tacopie"]

