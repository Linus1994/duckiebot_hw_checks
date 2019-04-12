FROM duckietown/rpi-duckiebot-base:master18

COPY hw_checks.py .

CMD [ "./start_checks.sh" ]