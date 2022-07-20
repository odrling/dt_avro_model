from commands import StartProcess
from monitor_requests import send_model
from utils import time


if __name__ == "__main__":
    send_model(StartProcess(timestamp=time()))
