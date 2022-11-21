FROM 812206152185.dkr.ecr.us-west-2.amazonaws.com/latch-base:6839-main

# RUN apt-get update
# RUN apt-get install -y wget

# ENV MUSCLEVERSION='3.8.31'
# # MUSCLE ========================================
# RUN wget http://drive5.com/muscle/downloads"$MUSCLEVERSION"/muscle"$MUSCLEVERSION"_i86linux64.tar.gz &&\
#   tar -xvf muscle* &&\
#   rm muscle*.tar.gz &&\
#   mv muscle* /usr/local/bin/muscle

# STOP HERE:
# The following lines are needed to ensure your build environement works
# correctly with latch.
RUN python3 -m pip install --upgrade latch
COPY wf /root/wf
ARG tag
ENV FLYTE_INTERNAL_IMAGE $tag
WORKDIR /root
