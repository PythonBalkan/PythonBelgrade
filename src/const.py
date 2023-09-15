from enum import Enum
from typing import Dict, List, Optional, TypedDict


JSON_DATA_DIR = "docs/source/json-data"
MEETUPS_DIR = "docs/source/meetups"
SPEAKERS_DIR = "docs/source/speakers"


class JSONType(str, Enum):
    MEETUPS = "meetups"
    SPEAKERS = "speakers"


class SpeakerData(TypedDict):
    id: int
    name: str
    linkedin: Optional[str]
    github: Optional[str]
    description: Optional[str]
    contact_info: Dict[str, str]
    photo: Optional[str]


class LocationData(TypedDict):
    name: str
    url: str


class TalkReferenceData(TypedDict):
    title: str
    url: str


class TalkData(TypedDict):
    title: str
    abstract: str
    speakers: List[int]
    references: List[TalkReferenceData]


class LightningTalkData(TypedDict):
    title: str
    speaker: str


class MeetupData(TypedDict):
    id: int
    title: str
    location: LocationData
    start: str
    talks: List[TalkData]
    youtube: Optional[str]
    lightning_talks: List[LightningTalkData]


RSTContent = str
