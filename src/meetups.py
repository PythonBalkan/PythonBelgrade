from src.const import MeetupData, RSTContent
from src.loading import get_speakers


MEETUP_RST_TEMPLATE = """.. _meetup_{id}:

{title}
=================

- Location: `{location_name} <{location_url}>`_
- Date: {start}
{youtube}
"""

TALK_RST_TEMPLATE = """{title}
---

.. toctree::
"""

ABSTRACT_TEMPLATE = "- Abstract:\n{abstract}"

LIGHTNING_TALK_RST_TEMPLATE = """- {title} | {speaker}"""


def generate_meetup_rst(meetup: MeetupData) -> RSTContent:
    if youtube := meetup.get("youtube"):
        youtube = f"..  youtube:: {youtube.split('?v=')[-1]}"
    youtube = youtube if youtube else ""

    rst_content = MEETUP_RST_TEMPLATE.format(
        id=meetup["id"],
        title=meetup["title"],
        location_name=meetup["location"]["name"],
        location_url=meetup["location"]["url"],
        start=meetup["start"],
        youtube=youtube,
    )

    if talks := meetup.get("talks"):
        rst_content += "Talks:\n-----\n\n"
        for talk in talks:
            rst_content += TALK_RST_TEMPLATE.format(title=talk.get("title" or "No title"))
            rst_content += (
                "\n".join(
                    [
                        "  ../speakers/speaker_{id}".format(id=speaker["id"])
                        for speaker in get_speakers(*talk["speakers"])
                    ]
                )
                + "\n\n"
            )

            if abstract := talk.get("abstract"):
                rst_content += ABSTRACT_TEMPLATE.format(abstract=abstract)

            if references := talk.get("references"):
                rst_content += "References:\n" + "\n".join(
                    [f"- `{reference['title']} <{reference['url']}>`_" for reference in references]
                )

            rst_content += "\n\n"

    if lightning_talks := meetup.get("lightning_talks"):
        rst_content += "Lightning Talks:\n-----\n\n"
        for talk in lightning_talks:
            rst_content += LIGHTNING_TALK_RST_TEMPLATE.format(title=talk["title"], speaker=talk["speaker"]) + "\n"

    return rst_content
