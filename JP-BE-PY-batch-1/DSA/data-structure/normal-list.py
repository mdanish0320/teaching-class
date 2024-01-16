events = [
        "Patient Admission",
        "Patient Room Changed",
        "Patient Went on Leave",
        "Patient Returned from Leave",
        "Patient Discharged",
        
        "Patient Readmit",
        "Patient Discharged"
    ]




def process_event(event):
    print("process event:", event)

# print(events)
# process_event(events[0])
# process_event(events[1])
# process_event(events[2])
# process_event(events[3])
# process_event(events[4])
# process_event(events[5])
# process_event(events[6])
# print(events)



# improvement 
print(events)
process_event(events[0])
del events[0]
process_event(events[0])
del events[0]
process_event(events[0])
del events[0]
process_event(events[0])
del events[0]
process_event(events[0])
del events[0]
process_event(events[0])
del events[0]
process_event(events[0])
del events[0]
print(events)

# drawbacks
# 1. we have to delete the first element and therefore list will resize and shift data from one place to other by copying and pasting
# 2. when list grow on size, it resizes - copying data from one place to other

# solutions
# make a linked list
