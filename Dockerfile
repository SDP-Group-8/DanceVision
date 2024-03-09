FROM ros:noetic-robot

SHELL ["/bin/bash", "-c"]

ADD . /dancevision

WORKDIR /dancevision

RUN apt-get update
RUN apt-get install -y vim git python3-pip wget qt5-default

WORKDIR /ffmpeg

RUN wget https://github.com/PyAV-Org/pyav-ffmpeg/releases/download/6.1.0-1/ffmpeg-manylinux_x86_64.tar.gz
RUN tar -xzf ffmpeg-manylinux_x86_64.tar.gz

WORKDIR /opencv-build

RUN sh /dancevision/scripts/opencv-build-script.sh /ffmpeg /dancevision/src/base-opencv && make -j4
RUN cd python_loader && python3 setup.py develop
RUN pip3 install --upgrade numpy
RUN pip3 install src/pose_tracking/ src/dancevision_app/server/
