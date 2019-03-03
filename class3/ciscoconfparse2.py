from ciscoconfparse import CiscoConfParse



bgp_obj=CiscoConfParse("bgp_input.txt")



match=bgp_obj.find_objects_w_child(parentspec=r"router bgp", childspec=r"^\s+neighbor")

fin_list=[]
for children in match[0].children:
    if "neighbor" in children.text:
        nei_ip=children.text.split()[1]
        match_as=bgp_obj.find_objects_w_child(parentspec=children.text,childspec=r"^\s+remote-as")
        for sub_child in match_as[0].children:
            if "remote-as" in sub_child.text:
                rem_as=sub_child.text.split()[1]
        fin_list.append((nei_ip,rem_as))


print ("\n\n")
print(fin_list)
