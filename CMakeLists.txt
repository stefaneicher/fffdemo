cmake_minimum_required(VERSION 3.16 FATAL_ERROR)

project(FFFDemo)

set(CMAKE_CXX_STANDARD 14)

include(${CMAKE_CURRENT_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

add_subdirectory(src)

enable_testing()
add_subdirectory(test)
