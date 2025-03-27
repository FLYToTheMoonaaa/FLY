import requests
import json
import time
url = "https://graphigo.prd.galaxy.eco/query"

def send_graphql_request(url, query, variables):
  headers = {
    'accept': '*/*',
    'accept-language': 'zh-HK,zh;q=0.9',
    'authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJEZXZpY2VJRCI6ImdhLXVzZXItMTg2NzkzMjM5Mi4xNzA5MjIwMDI1IiwiR2FseGVJRCI6InhVTEFKNmNyNXVoTWVoaWRWN3AyNUgiLCJleHAiOjE3NDEyMzUxNzIsImp0aSI6ImZkZDJjNjk5MGRmMzhmMzA4MWFmYWVhOTUzZmE4YTJjYmJhMzNkMTZmOTQ2ZGZmNDE3ZTYwYzg3NDhiZDE4ZmEiLCJBZGRyZXNzIjoiMHhENUEwNWExNjk2RTAxNjdjZjE1Mjk4NGQwMzA5MURBRDQ2MjFBNTQ2IiwiQWRkcmVzc1R5cGUiOjEsIkFjY291bnRVc2VybmFtZSI6IiJ9.cF5KtLfJ7wU2eLqODnO8pMLWsIBIDdTcZTwQ_hTECno',
    'content-type': 'application/json',
    'device-id': 'ga-user-1867932392.1709220025',
    'origin': 'https://app.galxe.com',
    'platform': 'web',
    'priority': 'u=1, i',
    'request-id': '4f84af35-c401-49a0-a9e6-3798c2862e66',
    'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
    'x-unique-client-id': 'ga-user-1867932392.1709220025',
    'x-unique-link-id': '4247d1980e4925b4ed12b9baad48bf2c6c51bc35940655270d1f16177026ff63'
  }

  payload = {
    "query": query,
    "variables": variables
  }

  response = requests.post(url, headers=headers, json=payload)
  return response
def jiankong():
  query = """
          query CampaignList($input: ListCampaignInput!, $address: String!) {
            campaigns(input: $input) {
              pageInfo {
                endCursor
                hasNextPage
                __typename
              }
              list {
                ...CampaignSnap
                boost(address: $address) {
                  golden
                  __typename
                }
                isBookmarked(address: $address)
                id
                numberID
                name
                airdrop {
                  rewardType
                  rewardAmount
                  rewardInfo {
                    custom {
                      name
                      icon
                      __typename
                    }
                    token {
                      address
                      symbol
                      decimals
                      icon
                      __typename
                    }
                    __typename
                  }
                  claimDetail(address: $address) {
                    amount
                    __typename
                  }
                  __typename
                }
                childrenCampaigns {
                  id
                  type
                  rewardName
                  rewardInfo {
                    discordRole {
                      guildId
                      guildName
                      roleId
                      roleName
                      inviteLink
                      __typename
                    }
                    __typename
                  }
                  __typename
                }
                whitelistInfo(address: $address) {
                  usedCount
                  __typename
                }
                watchlistPro {
                  watchListId
                  rewardIconGif
                  rewardIcon
                  rewardCampaign
                  __typename
                }
                info
                useCred
                formula
                thumbnail
                gasType
                createdAt
                requirementInfo
                description
                enableWhitelist
                chain
                startTime
                status
                requireEmail
                requireUsername
                distributionType
                endTime
                rewardName
                cap
                loyaltyPoints
                tokenRewardContract {
                  id
                  address
                  chain
                  __typename
                }
                tokenReward {
                  userTokenAmount
                  tokenAddress
                  depositedTokenAmount
                  tokenRewardContract
                  tokenDecimal
                  tokenLogo
                  tokenSymbol
                  __typename
                }
                space {
                  id
                  name
                  thumbnail
                  alias
                  isVerified
                  __typename
                }
                rewardInfo {
                  discordRole {
                    guildId
                    guildName
                    roleId
                    roleName
                    inviteLink
                    __typename
                  }
                  premint {
                    startTime
                    endTime
                    chain
                    price
                    totalSupply
                    contractAddress
                    banner
                    __typename
                  }
                  __typename
                }
                participants {
                  participantsCount
                  bountyWinnersCount
                  __typename
                }
                recurringType
                __typename
              }
              __typename
            }
          }

          fragment CampaignMedia on Campaign {
            thumbnail
            rewardName
            type
            gamification {
              id
              type
              __typename
            }
            __typename
          }

          fragment CampaignSnap on Campaign {
            id
            name
            inWatchList
            inNewYearWatchList
            ...CampaignMedia
            __typename
          }
          """

  variables = {
    "address": '',
    "input": {
      "listType": "Newest",
      "gasTypes": ["Gasless"],
      "types": None,
      "rewardTypes": None,
      "chains": ["GRAVITY_ALPHA"],
      "isVerified": None,
      "statuses": ["Active", "NotStarted"],
      "spaceCategories": None,
      "backers": None,
      "first": 200,
      "after": "-1",
      "searchString": None,
      "claimableByUser": None,
      "ecosystem": None
    }
  }
  response5 = send_graphql_request(url, query, variables)
  aa=response5.json()
  return aa

def fetch_campaigns():
  aa = jiankong()
  campaigns = aa["data"]["campaigns"]["list"]
  return {campaign["id"]: campaign["name"] for campaign in campaigns}

initial_campaigns = fetch_campaigns()
print(initial_campaigns)

while True:
  try:
    time.sleep(60)

    # 第二次请求，获取新数据
    print("获取新数据...")
    new_campaigns = fetch_campaigns()
    new_ids = set(new_campaigns.keys()) - set(initial_campaigns.keys())

    # 找出新增的 ID

    # 打印新增的活动名称
    if new_ids:
      print("\n\033[94m发现新的活动-------------------------------：\033[0m")  # 这行变蓝色
      for new_id in new_ids:
        print(f"- {new_campaigns[new_id]}")
    else:
      print(f"没有发现新的活动---------------------------------------")
  except  Exception as e:
    print(e)

# 等待 100 秒










