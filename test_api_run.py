import requests
import argparse

# insert api key generated from the day
API_KEY = ''
REGION = 'na'

# insert player puuid 
PUUID = ''

# insert match id
MATCH_ID = ''

# choose between puuid or match when calling the function
"""
example usage: 
"""


def matchvpuuid(method):
  # Method to get match data off of match id
  if method == 'match':
    url = f"https://{REGION}.api.riotgames.com/match/v1/matches/{match_id}"
    headers = {
      'X-Riot-Token' = API_KEY
    }
    response = requests.get(url, headers = headers)
    if response.status_code == 200:
      return response.json()
    else:
      print(f"Error: {response.status_code} - {response.text")
      return None
  match_details = get_match_details(MATCH_ID)
  print(match_details)

  # Method to get individual data off of puuid
  if method == 'puuid':
     url = f"https://{REGION}.api.riotgames.com/match/v1/matchlists/by-puuid/{puuid}"
    headers = {
      'X-Riot-Token' = API_KEY
    }
    response = requests.get(url, headers = headers)
    if response.status_code == 200:
      return response.json()
    else:
      print(f"Error: {response.status_code} - {response.text")
      return None
  match_details = get_match_details(PUUID)
  print(match_details)

def main():
  parser = argparse.ArgumentParser()
  parser.add_argument("method", type = str, help="the method used for api data from methods api")
  args = parser.parse_args()
  m = args[0]
  matchvpuuid(m)
