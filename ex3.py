import re

patternIP = "((25[0-5]|2[0-4][0-9]|1[0-9]{2}|[0-9]{2}|[1-9])\.(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[0-9]{2}|[0-9])\.(25[" \
            "0-5]|2[0-4][0-9]|1[0-9]{2}|[0-9]{2}|[0-9])\.(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[0-9]{2}|[0-9]))"

whole_pattern = "^(.*)\s" + patternIP + "\s+\[(.*)\]\s+via\s+" + patternIP + ".*(\d{1,2}:\d{1,2}:\d{1,2}),\s(.*)$"

symbol_to_name={"L":"local","C":"Connected","S":"Static","R":"Rip","M":"mobile","B":"BGP","D":"EIGRP","EX":"EIGRP external","O":"OSPF","IA":"OSPF inter area",
                "N1":"OSPF NSSA external type 1","N2":"OSPF NSSA external type 2","E1":"OSPF external type 1","E2":"OSPF external type 2","E":"EGP",
                "i":"IS-IS","su":"IS-IS summary","L1":"IS-IS level-1","L2":"IS-IS level-2","ia":"IS-IS inter area","*":"candidate default","U":"per-user static route",
                "o":"ODR","P":"periodic downloaded static route","H":"NHRP","l":"LISP","a":"application route","+":"replicated route","%":"next hop override"}

file=open("ShowIpRoute.txt","r")

for line in file.readlines():
    result=re.match(whole_pattern, line)
    if result is not None:
        protocol=result.group(1)
        protocol.strip()
        symbols=protocol.split(' ')
        firstIp=result.group(2)
        adMetric=result.group(7)
        secondIp =result.group(8)
        time =result.group(13)
        interface = result.group(14)
        print("Protocol:"+"\t"*4,end='')
        #last index, due to main protocol duplicates otherwise


        print(symbol_to_name[symbols[symbols.__len__()-1]])
        print("Prefix:"+"\t"*5+firstIp)
        print("Ad/Metric:"+"\t"*4+adMetric)
        print("Next-Hop:"+"\t"*4+secondIp)
        print("Last Update:"+"\t"*3+time)
        print("Outbound interface:"+"\t"*2+interface)
        print("--------------------------------------------")



