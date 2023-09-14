import json

from src.const import JSON_DATA_DIR, JSONType, MeetupData, SpeakerData


def get_json_objects(type_: JSONType, *ids) -> list:
    with open(f"{JSON_DATA_DIR}/{type_}.json", "r") as file:
        data = json.load(file)

    if len(ids) == 0:
        return data

    return [instance for instance in data if instance["id"] in ids]


def get_meetups(*ids) -> list[MeetupData]:
    return get_json_objects(JSONType.MEETUPS, *ids)


def get_speakers(*ids) -> list[SpeakerData]:
    return get_json_objects(JSONType.SPEAKERS, *ids)
