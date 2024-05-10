FROM python:alpine
WORKDIR /var/project
COPY pyproject.toml /var/project/
COPY README.md /var/project/
COPY syslogserver_to_cloudwatch /var/project/syslogserver_to_cloudwatch
RUN python -m pip install wheel
RUN python -m venv /var/project_venv
RUN /var/project_venv/bin/python -m pip install .

ENV PORT 5140
EXPOSE 5140/udp

CMD ["/var/project_venv/bin/python", "-m", "syslogserver_to_cloudwatch"]
