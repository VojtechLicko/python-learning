def movier_review(rating):
    return (
        "Avoid it at all costs!"
        if rating <= 5
        else ("This one was fun" if 9 > rating > 5 else "Outstanding")
    )
