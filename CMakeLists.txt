cmake_minimum_required(VERSION 2.8)
project (GPU_KCF)

#opencv should be re-built with OPENCL, VA and VA_Intel 
set(OPENCV_INCLUDE /home/lancer/opencv/build/include)
set(OPENCV_LIB /home/lancer/opencv/build/lib)


set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11 -g -O0 -I${CMAKE_SOURCE_DIR}/runtime/include -I/usr/include/python3.5m -I${OPENCV_INCLUDE} ")
#set(ENABLE_EXPORTS false)
#set(CMAKE_EXE_LINKER_FLAGS "-L$ENV{DL_SDK_LIB} -L${CMAKE_SOURCE_DIR}/3rdparty/gflags/lib")

link_directories(${OPENCV_LIB} ${CMAKE_SOURCE_DIR}/runtime/lib/x64)
add_executable(GPU_KCF src/intelscalar.cpp src/SetupSurface.cpp src/fhog.cpp src/kcftracker.cpp src/main.cpp)
SET(LIBRARY_OUTPUT_PATH ${CMAKE_SOURCE_DIR}/src)
add_library(_kcftracker SHARED src/intelscalar.cpp src/SetupSurface.cpp src/fhog.cpp src/kcftracker.cpp src/main.cpp src/kcftracker_wrap.cxx)
add_library(kcftracker SHARED src/intelscalar.cpp src/SetupSurface.cpp src/fhog.cpp src/kcftracker.cpp src/main.cpp src/kcftracker_wrap.cxx)
target_link_libraries(GPU_KCF X11 igfxcmrt64  va va-drm pthread rt  opencv_core opencv_video opencv_videoio opencv_imgproc opencv_photo opencv_highgui opencv_imgcodecs)
target_link_libraries(_kcftracker X11 igfxcmrt64  va va-drm pthread rt  opencv_core opencv_video opencv_videoio opencv_imgproc opencv_photo opencv_highgui opencv_imgcodecs python3.5m)
target_link_libraries(kcftracker X11 igfxcmrt64  va va-drm pthread rt  opencv_core opencv_video opencv_videoio opencv_imgproc opencv_photo opencv_highgui opencv_imgcodecs python3.5m)


