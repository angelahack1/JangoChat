FROM python:3.12-slim-bookworm

RUN useradd --create-home appuser
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
ENV PORT=8000

WORKDIR /home/appuser/app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
ENV PYTHONUNBUFFERED=1
RUN chown -R appuser:appuser /home/appuser
USER appuser

# Make it executable
RUN chmod +x /home/appuser/app/entrypoint.sh

# Set the entrypoint
ENTRYPOINT ["/home/appuser/app/entrypoint.sh"]

EXPOSE $PORT
# The command to run when the container starts
CMD ["daphne", "-b", "0.0.0.0", "-p", "8000", "JangoChat.asgi:application"]


