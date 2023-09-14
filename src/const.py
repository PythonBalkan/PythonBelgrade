from enum import StrEnum
from typing import TypedDict


JSON_DATA_DIR = "docs/source/json-data"
MEETUPS_DIR = "docs/source/meetups"
SPEAKERS_DIR = "docs/source/speakers"


class JSONType(StrEnum):
    MEETUPS = "meetups"
    SPEAKERS = "speakers"


class SpeakerData(TypedDict):
    id: int
    name: str
    linkedin: str | None
    github: str | None
    description: str | None
    contact_info: dict[str, str]
    photo: str | None


class LocationData(TypedDict):
    name: str
    url: str


class TalkReferenceData(TypedDict):
    title: str
    url: str


class TalkData(TypedDict):
    title: str
    abstract: str
    speakers: list[int]
    references: list[TalkReferenceData]


class LightningTalkData(TypedDict):
    title: str
    speaker: str


class MeetupData(TypedDict):
    id: int
    title: str
    location: LocationData
    start: str
    talks: list[TalkData]
    youtube: str | None
    lightning_talks: list[LightningTalkData]


RSTContent = str
