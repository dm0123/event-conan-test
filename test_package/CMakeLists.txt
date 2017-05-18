cmake_minimum_required(VERSION 2.8.11)

project(test_exec)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

add_executable(test_exec main.cpp)
target_link_libraries(test_exec ${CONAN_LIBS})
