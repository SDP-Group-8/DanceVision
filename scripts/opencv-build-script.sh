export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:~/ffmpeg/ffmpeg-manylinux_x86_64/lib
export PKG_CONFIG_PATH=$PKG_CONFIG_PATH:~/ffmpeg/ffmpeg-manylinux_x86_64/lib/pkgconfig
export PKG_CONFIG_LIBDIR=$PKG_CONFIG_LIBDIR:~/ffmpeg/ffmpeg-manylinux_x86_64/lib

cmake \
    -D BUILD_EXAMPLES=ON \
    -D BUILD_TESTS=OFF \
    -D OPENCV_EXTRA_EXE_LINKER_FLAGS="-Wl,-rpath,~/ffmpeg/ffmpeg-manylinux_x86_64/lib" \
    -D CMAKE_BUILD_TYPE=RELEASE \
    -D WITH_QT=ON \
    -D BUILD_OPENJPEG=ON \
    -D CMAKE_INSTALL_PREFIX=~/opencv_install \
    /home/alex-webb03/opencv-python/opencv
