from typing import Generator, List

from src.loading import get_meetups
from src.const import RSTContent, SpeakerData


SPEAKER_RST_TEMPLATE = """{title}
=================
{description}

{linkedin}{github}{email}{photo}
"""

PHOTO_RST_TEMPLATE = """
.. image:: {photo}
    :alt: profile-photo
    :width: 200px
"""


def get_speakers_meetups(speaker_id: int) -> List[int]:
    meetups = get_meetups()
    meetup_ids = []
    for meetup in meetups:
        for talk in meetup["talks"]:
            if speaker_id in talk["speakers"]:
                meetup_ids.append(meetup["id"])

    return meetup_ids


def generate_speaker_rst(speaker: SpeakerData) -> RSTContent:
    if linkedin := speaker.get("linkedin"):
        linkedin = f"- :icon:`fa-brands fa-linkedin-in` `linkedin <{linkedin}>`_"
    linkedin = linkedin + "\n\n" if linkedin else ""

    if github := speaker.get("github"):
        github = f"- {github}"
    github = github + "\n\n" if github else ""

    if email := speaker["contact_info"].get("email"):
        email = f"- {email}\n"
    email = email + "\n\n" if email else ""

    if photo := speaker["photo"]:
        photo = PHOTO_RST_TEMPLATE.format(photo=photo)
    photo = photo + "\n\n" if photo else ""

    rst_content = SPEAKER_RST_TEMPLATE.format(
        id=speaker["id"],
        title=speaker["name"],
        description=(speaker.get("description") or "") + "\n\n",
        linkedin=linkedin,
        github=github,
        email=email,
        photo=photo,
    )

    meetups = get_speakers_meetups(speaker["id"])
    if meetups:
        rst_content += "Talks on meetups:\n\n"
        for meetup_id in meetups:
            rst_content += f"- :ref:`meetup_{meetup_id}`\n"

    rst_content += "\n"
    return rst_content
