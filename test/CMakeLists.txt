include(GoogleTest)
add_executable(unitTestGuideLinesTest
        UI_test_cpp.cpp
        fff.h
        )
target_link_libraries(unitTestGuideLinesTest PUBLIC calculator ${CONAN_LIBS})
target_include_directories(unitTestGuideLinesTest PUBLIC ${CMAKE_CURRENT_LIST_DIR})
gtest_discover_tests(unitTestGuideLinesTest TEST_PREFIX new:)