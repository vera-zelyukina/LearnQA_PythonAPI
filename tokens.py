import requests
import time

response = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job")
token = response.json()["token"]
time_seconds = response.json()["seconds"]

response = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params={"token": token})
if response.json()["status"] == "Job is NOT ready":
    print("status is correct")

time.sleep(time_seconds)

response = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params={"token": token})
if (response.json()["status"] == "Job is ready") and ("result" in response.json()):
    print("status is correct and result is exist")
