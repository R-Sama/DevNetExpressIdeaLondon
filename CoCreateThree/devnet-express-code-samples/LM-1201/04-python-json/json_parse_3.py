# food={"vegetables":["carrots","kale","cucumber","tomato"]}
# print(food["vegetables"][1])
# for veg in food["vegetables"]:
# 	print(veg)
#
# cars={"sports":{"Porsche":"Volkswagon","Viper":"Dodge","Corvette":"Chevy"}}
# print(cars["sports"]["Corvette"])
# for auto in cars["sports"]:
# 	print(auto,cars["sports"][auto])
#

dessert={"iceCream":["Rocky-Road","strawberry","Pistachio-Cashew","Pecan-Praline"]}
for pengTing in dessert["iceCream"]:
    if(pengTing=="Rocky-Road"):
        print(pengTing)

print(dessert["iceCream"])

soup={"soup":{"tomato":"healthy","onion":"bleh!","vegetable":"goodForYou"}}

for liquidFood in soup["soup"]:
    print(liquidFood, "is", soup["soup"][liquidFood])

ticket={"response": {"serviceTicket": "ST-16891-ugqKRVvCfPJcEaGXnGEN-cas","idleTimeout": 1800,"sessionTimeout": 21600},"version": "1.0"}
for TT in ticket["response"]:
    print(TT,"+", ticket["response"][TT])



network={"Network":{"router":{"ipaddress":"192.168.1.21","mac_address":"08:56:27:6f:2b:9c"}}}

hosts={"response": [{"id": "4c60d6a7-4812-40d6-a337-773af2625e56","hostIp": "65.1.1.86","hostMac": "00:24:d7:43:59:d8","hostType": "wireless"},{"id": "3ef5a7c3-7f74-4e57-a5cb-1448fbda5078","hostIp": "207.1.10.20","hostMac": "5c:f9:dd:52:07:78","hostType": "wired"},{"id": "12f9c920-24fa-4d32-bf39-4c63813aecd8","hostIp": "212.1.10.20","hostMac": "e8:9a:8f:7a:22:99","hostType": "wired"}],"version": "1.0"}

# for item in hosts["response"]:
# 	print(item["id"])
# 	print(item["hostIp"])
# 	print(item["hostMac"])
# 	print(item["hostType"])


devices={"response": [
    {
      "family": "Switches and Hubs",
      "type": "Cisco Catalyst 2960C-8PC-L Switch",
      "serialNumber": "FOC1637Y3FJ",
      "role": "CORE",
      "reachabilityStatus": "Reachable",    
      "instanceUuid": "2dc30cac-072e-4d67-9720-cc302d02695a",
      "id": "2dc30cac-072e-4d67-9720-cc302d02695a"
    },
    {
      "family": "Unified AP",
      "type": "Cisco 3500I Unified Access Point",
      "serialNumber": "FGL1548S2YF",
      "role": "ACCESS",
      "reachabilityStatus": "Reachable",
      "instanceUuid": "17184480-2617-42c3-b267-4fade5f794a9",
      "id": "17184480-2617-42c3-b267-4fade5f794a9"
    }
  ],
  "version": "1.0"
}
# print(devices["response"][0]["id"])