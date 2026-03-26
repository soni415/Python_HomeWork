from attendees_list import attendees_list


def who_checked_in(attendees_list):
    att_list=[]
    for attendee in attendees_list:
        att_dict={}
        if attendee["checked_in"]:
            att_dict["name"]=attendee["name"]
            att_dict["ticket_type"]=attendee["ticket_type"]
            att_list.append(att_dict)
            att_dict={}

    return att_list


final_attendees_list = who_checked_in(attendees_list)
for person in final_attendees_list:
    for key, value in person.items():
        print(key,":",value)
    print()

def count_VIP(final_attendees_list):
    VIP_Count=0
    for person in final_attendees_list:
        if person["ticket_type"]=="VIP":
            VIP_Count+=1
    return VIP_Count

VIP_Count=count_VIP(final_attendees_list)
print("The VIP count is: ",VIP_Count)
print()

def is_vip(person):
    if person["ticket_type"]=="VIP":
        return True
    else:
        return False

person = final_attendees_list[0]
VIP_status=is_vip(person)
print("Is",person["name"]," a VIP? ",VIP_status)