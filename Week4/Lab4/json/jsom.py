import json

with open("/Users/a../Desktop/ProgrammingPrinciples2/Week4/Lab4/json/txt.json") as f:
    data = json.load(f)

print("Interface Status")
print("=" * 80)
print("{:<50}{:<25}{:<8}{}".format("DN", "Description", "Speed", "MTU"))
print("-" * 80)

for interface in data['imdata']:
    dn = interface['l1PhysIf']['attributes']['dn']
    description = interface['l1PhysIf']['attributes']['descr']
    speed = interface['l1PhysIf']['attributes']['speed']
    mtu = interface['l1PhysIf']['attributes']['mtu']
    print("{:<50}{:<25}{:<8}{}".format(dn, description, speed, mtu))