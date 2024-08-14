def badge_maker(name):
    return f"Hello, my name is {name}."


def batch_badge_creator(names):
    return [badge_maker(name) for name in names]


def assign_rooms(speakers):
    room_assignments = []
    for index, speaker in enumerate(speakers):
        room_assignments.append(f"Hello, {speaker}! You'll be assigned to room {index + 1}!")
    return room_assignments


def printer(speakers):
    badges = batch_badge_creator(speakers)
    room_assignments = assign_rooms(speakers)
    
    for badge in badges:
        print(badge)
        
    for assignment in room_assignments:
        print(assignment)
