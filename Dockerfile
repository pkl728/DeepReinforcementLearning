FROM python:3.6

# Install miniconda to /miniconda
RUN curl -LO http://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
RUN bash Miniconda3-latest-Linux-x86_64.sh -p /miniconda -b
RUN rm Miniconda3-latest-Linux-x86_64.sh
ENV PATH=/miniconda/bin:${PATH}
RUN conda update -y conda

# Python packages from conda
RUN conda install -y \
    tensorflow==1.8.0 \
    numpy \
    pydot \
    keras==2.1.6 \
    matplotlib \
    ipython \
    graphviz \
    pyqt=5 
ADD main.py /
ADD MCTS.py /
ADD agent.py /
ADD config.py /
ADD funcs.py /
ADD helper_funcs.py /
ADD game.py /
ADD initialise.py /
ADD loggers.py /
ADD loss.py /
ADD memory.py /
ADD model.py /
ADD settings.py /
ADD utils.py /

RUN mkdir -p /run
RUN mkdir -p /run/logs
RUN mkdir -p /run/models
RUN mkdir -p /run/memory
RUN conda create --name connect4 python=3
CMD ["source", "activate", "connect4"]
RUN pip install --upgrade pip
RUN pip install git+https://github.com/apple/coremltools
CMD [ "python", "./main.py" ]
