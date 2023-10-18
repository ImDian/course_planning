courses = input().split(", ")
command = input()

while command != "course start":
    command_list = command.split(":")
    action = command_list[0]
    title = command_list[1]

    if action == "Add":
        if title not in courses:
            courses.append(title)

    elif action == "Insert":
        index = int(command_list[2])
        if title not in courses:
            courses.insert(index, title)

    elif action == "Remove":
        if title in courses:
            courses.remove(title)
        if f"{title}-Exercise" in courses:
            courses.remove(f"{title}-Exercise")

    elif action == "Swap":
        title2 = command_list[2]
        if title in courses and title2 in courses:
            title_index = courses.index(title)
            title2_index = courses.index(title2)

            courses[title_index], courses[title2_index] = courses[title2_index], courses[title_index]

            if f"{title}-Exercise" in courses:
                temp = courses.pop(title_index + 1)
                courses.insert(title2_index + 1, temp)
            if f"{title2}-Exercise" in courses:
                temp = courses.pop(title2_index + 1)
                courses.insert(title_index + 1, temp)

    elif action == "Exercise":
        if title in courses and f"{title}-Exercise" not in courses:
            courses.insert(courses.index(title) + 1, f"{title}-Exercise")

        elif title not in courses:
            courses.extend([title, f"{title}-Exercise"])

    command = input()

for i, lesson in enumerate(courses):
    print(f"{i + 1}.{lesson}")