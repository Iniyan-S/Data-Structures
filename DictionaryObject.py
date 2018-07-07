class_names = ["jack", "bob", "mary", "jeff", "ann", "pierre", "martha", "clause", "pablo", "susan", "gustav"]

def create_dataset():
    import randon
    num_entries = 5000000
    f = open("data.txt", "w")
    for i in range(num_entries):
        current = random.choice(class_names)
        f.write(current+"\n")

    f.close()
