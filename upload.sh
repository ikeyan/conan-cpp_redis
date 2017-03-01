#!/usr/bin/env bash
conan user ikeshita_katsuhiko -r conan.io
conan export ikeshita_katsuhiko/stable
conan upload cpp_redis/master@ikeshita_katsuhiko/stable --all -r=conan.io
conan remove -f cpp_redis/master@ikeshita_katsuhiko/stable

