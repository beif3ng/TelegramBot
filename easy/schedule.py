week = [
    {
        "id": "Mon",
        "lessons": [" ", "react", "python", "python", "database", "database", "philosophy"]
    },
    {
        "id": "Tue",
        "lessons": ["algorithms lecture", "database lecture", "database lecture"]
    },
    {
        "id": "Wed",
        "lessons": ["math lecture", "react lecture", "manasovedenie lecture", "react", " ", "pe", "pe"]
    },
    {
        "id": "Thu",
        "lessons": [" ", " ", "info", "info lecture", "python", "python"]
    },
    {
        "id": "Fri",
        "lessons": [" ", "math", "russian", "russian", "react lecture", "english", "english"]
    },
    {
        "id": "Sat",
        "lessons": ["algorithms", "algorithms", "manasovedenie", "python lecture", "pyhton lecture", "python", "python"]
    }
]


def get_schedule(day_name: str = None) -> str:
    schedule_text = ""
    for day in week:
        if day["id"] == day_name:
            num = 0
            for lesson in day["lessons"]:
                num += 1
                schedule_text += f"{num}. {lesson}\n"
    return schedule_text



