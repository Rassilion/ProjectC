FROM python:2.7.13-onbuild
RUN apt-get update && \
    apt-get -y install gcc mono-mcs coreutils
CMD [ "python","-m", "CodeJudge.judge" ]