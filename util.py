import re


def format_tag_name(name):
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!", name)
    return name
    # If tag has name like "release/1.2.3", take only "1.2.3" part
    pattern = re.compile(r"(?P<tag>[^\d.]+)")

    match = pattern.search(name)
    if match:
        return match.group("tag")

    # just left properly named tags intact
    if name.startswith("v"):
        return name

    # fail in case of wrong tag names like "release/unknown"
    raise ValueError(f"Wrong tag name: {name}")