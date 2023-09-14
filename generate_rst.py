import os

from src.loading import get_meetups, get_speakers
from src.meetups import generate_meetup_rst
from src.speakers import generate_speaker_rst
from src.const import MEETUPS_DIR, SPEAKERS_DIR


def main() -> None:
    meetups_data = get_meetups()
    speakers_data = get_speakers()

    os.makedirs(MEETUPS_DIR, exist_ok=True)
    os.makedirs(SPEAKERS_DIR, exist_ok=True)

    for meetup in meetups_data:
        meetup_id = meetup["id"]
        meetup_rst = generate_meetup_rst(meetup)
        with open(os.path.join(MEETUPS_DIR, f"meetup_{meetup_id}.rst"), "w") as file:
            file.write(meetup_rst)

    for speaker in speakers_data:
        speaker_id = speaker["id"]
        speaker_rst = generate_speaker_rst(speaker)
        with open(os.path.join(SPEAKERS_DIR, f"speaker_{speaker_id}.rst"), "w") as file:
            file.write(speaker_rst)


if __name__ == "__main__":
    main()
