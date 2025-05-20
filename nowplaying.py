import os
import time
import logging
from dotenv import load_dotenv
from sample import draw, lastfm_user_data, get_album_cover

load_dotenv()
LOG_FILENAME = 'log.txt'

logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(name)s - %(message)s',
    level=logging.DEBUG,
    handlers=[
        logging.FileHandler(LOG_FILENAME),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

def main():
    refresh_frequency_default = 5
    refresh_frequency_low = 60
    refresh_frequency = refresh_frequency_default
    refresh_slowdown_period = 120 * refresh_frequency
    refreshed_time = 0

    previous_track_name = ''
    previous_image_name = ''
    album_cover = 'images/album_cover.jpg'
    lastplayed_track = ''
    lastplayed_artist = ''
    lastplayed_album = ''
    lastplayed_image = ''

    requested_username = os.environ.get("LAST_FM_USERNAME")
    if requested_username is None:
        logger.error("No username specified. Exiting")
        return
    logger.debug("Requesting currently playing for username: %s", requested_username)
    # try:
    #     requested_username = sys.argv[1]
    # except IndexError:
    #     logging.error("No username provided")
    logger.info("Clearing screen")
    draw.clear_screen()

    while True:
        logger.info("Checking API for last played: ")
        try:
            lastplayed_track, lastplayed_artist, lastplayed_album, lastplayed_image = lastfm_user_data.lastplayed(requested_username)
        except Exception as e:  # Replace with actual exceptions
            logger.warning(f"Error fetching data: {e}. Trying again.")
        logger.info("Checking API for last played: ")

        logger.info("Last played track: %s", lastplayed_track)
        logger.info("Last played artist: %s", lastplayed_artist)
        logger.info("Last played album: %s", lastplayed_album)
        logger.info("Last played image: %s", lastplayed_image)

        if lastplayed_track == previous_track_name:
            logger.info("No change to data - not refreshing")
        else:
            refreshed_time = time.time()

            logger.info("New data found from API - refreshing screen...")

            if lastplayed_image == previous_image_name:
                logger.info("No change to album cover - using same image")
            else:
                try:
                    get_album_cover.fetch_image(lastplayed_image)
                except Exception as e:
                    logger.exception("Error fetching album cover. Showing previous cover: %s", e)
            draw.image_and_text(album_cover, lastplayed_track, lastplayed_artist)

            previous_track_name = lastplayed_track
            previous_image_name = lastplayed_image

        if time.time() >= refreshed_time + refresh_slowdown_period:
            refresh_frequency = refresh_frequency_low
        else:
            refresh_frequency = refresh_frequency_default

        logger.info("Waiting %d seconds", refresh_frequency)
        time.sleep(refresh_frequency)

if __name__ == "__main__":
    main()
