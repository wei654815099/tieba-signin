FROM python:3-slim

# Set destination for COPY

WORKDIR /app

# 使用aliyun的pip源安装
RUN pip3 install requests_html requests schedule -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com --no-cache-dir

# Copy the source code. Note the slash at the end, as explained in
# https://docs.docker.com/engine/reference/builder/#copy
COPY spider.py ./

# (Optional) environment variable that our dockerised
# application can make use of. The value of environment
# variables can also be set via parameters supplied
# to the docker command on the command line.
#ENV HTTP_PORT=8081

ENV tiebaCookies "BDUSS=xUMk9sRm5-QUNCSFQ0eFd0YzNUVW5pSG5MSlZ5RER0dzUzNXVqSFEyNkFncnBpSVFBQUFBJCQAAAAAAAAAAAEAAAArUb80tPO087ray6cAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAID1kmKA9ZJiaG; STOKEN=f3baa843a9331bbe0c1102d2df80a4e56e942a98d121f17469d3b9d0eb8bcff7;"
ENV tiebaLogLevel 20

# 设置时区
RUN ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && echo 'Asia/Shanghai' > /etc/timezone

# Run
CMD [ "python3", "spider.py" ]
