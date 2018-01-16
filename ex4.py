import re
access_template = ['switchport mode access',

                   'switchport access vlan {}',

                   'switchport nonegotiate',

                   'spanning-tree portfast',

                   'spanning-tree bpduguard enable']

trunk_template = ['switchport trunk encapsulation dot1q',

                  'switchport mode trunk',

                  'switchport trunk allowed vlan {}']

if_mode=input("Enter interface mode (access/trunk): ")


vlans_pattern="^((\s*)\d+(\s*),)*(\s*)\d+(\s*)$"

if if_mode== "access" or if_mode== "a":
    if_nr = input("Enter interface type and number: ")
    vlan=input("Enter VLAN number: ")
    try:
        vlan_int=int(vlan)
        print("\nOutput:" + "\n" * 2)
        print("interface "+if_nr)
        for i in range(0,access_template.__len__()):
            if i==1:
                print(access_template[i].format(vlan_int))
            else:
                print(access_template[i])
    except ValueError:
        print("You must enter a number.")

elif if_mode == "trunk" or if_mode=="t":
    if_nr = input("Enter interface type and number: ")
    vlans=""
    result=re.match(vlans_pattern,vlans)
    print("\nOutput:"+"\n"*2)
    while result is None:
        vlans=input("Enter allowed vlans: ")
        result = re.match(vlans_pattern, vlans)
    for i in range(0, trunk_template.__len__()):
        if i == 2:
            print(trunk_template[i].format(vlans))
        else:
            print(trunk_template[i])
else:
    print("not a correct option")