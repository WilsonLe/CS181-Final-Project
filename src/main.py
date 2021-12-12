import os
import time
from dotenv import load_dotenv
from pprint import pprint
import requests
import redis

load_dotenv()


def main():
  r = redis.StrictRedis(host=os.getenv("redisHost"),
                        port=os.getenv("redisPort"),
                        password=os.getenv("redisPass"))
  for movieID in range(700000):
    try:
      if not r.exists(movieID):
        res = requests.get(
            f"https://api.themoviedb.org/3/movie/{movieID}?api_key={os.getenv('apiKey')}")
        if res.status_code == 200:
          r.set(res.json()["id"], res.text)
          print(f"{movieID} written to db")
        else:
          print(f"{movieID} not exist in API")
      else:
        print(f"{movieID} already in db")
    except Exception as e:
      print(e)


if __name__ == "__main__":
  main()
