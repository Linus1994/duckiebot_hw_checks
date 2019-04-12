FROM duckietown/rpi-duckiebot-base:master18

RUN [ "cross-build-start" ]

RUN [ "cross-build-end" ]

COPY hw_checks.py .

CMD [ "python3 hw_checks.py" ]
