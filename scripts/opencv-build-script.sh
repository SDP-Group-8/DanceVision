ffmpeg_path=$1
opencv_directory=$2

export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:~/$ffmpeg_path/lib
export PKG_CONFIG_PATH=$PKG_CONFIG_PATH:~/$ffmpeg_path/lib/pkgconfig
export PKG_CONFIG_LIBDIR=$PKG_CONFIG_LIBDIR:~/$ffmpeg_path/lib

cmake \
    -D BUILD_EXAMPLES=ON \
    -D BUILD_TESTS=OFF \
    -D OPENCV_EXTRA_EXE_LINKER_FLAGS="-Wl,-rpath,~/$ffmpeg_path/lib" \
    -D CMAKE_BUILD_TYPE=RELEASE \
    -D WITH_QT=ON \
    -D BUILD_OPENJPEG=ON \
    -D CMAKE_INSTALL_PREFIX=~/opencv_install $opencv_directory
