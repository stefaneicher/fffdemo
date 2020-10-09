add_library(calculator
        DISPLAY.h
        SYSTEM.h
        UI.c
        UI.h)

target_include_directories(calculator PUBLIC ${CMAKE_CURRENT_LIST_DIR})