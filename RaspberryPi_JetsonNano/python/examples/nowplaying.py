import lastfm_user_data
import draw
import time
import logging
import os
from dotenv import load_dotenv
import get_album_cover

try:
    load_dotenv()
except ImportError:
    logging.warning("No dotenv found")

def main():
    logging.basicConfig(level=logging.DEBUG)
    frequency = 5
    previous_track_name = ""

    requested_username = os.environ.get("LAST_FM_USERNAME")
    if requested_username is None:
        logging.error("No username specified. Exiting")
        return
    logging.info("Requesting currently playing for username: " + requested_username)

    # try:
    #     requested_username = sys.argv[1]
    # except IndexError:
    #     logging.error("No username provided")

    logging.info("Clearing screen")
    draw.clear_screen()

    while True:
        logging.info("Checking API for last played: ")
        lastplayed_track, lastplayed_artist, lastplayed_album, lastplayed_image = lastfm_user_data.lastplayed(requested_username)
        logging.info("Last played track: " + lastplayed_track)
        logging.info("Last played artist: " + lastplayed_artist)
        logging.info("Last played album: " + lastplayed_album)
        logging.info("Last played image: " + lastplayed_image)

        if lastplayed_track == previous_track_name:  #check if the track name is same as what we displayed last time
            logging.info("No change to data - not refreshing")
        else:
            logging.info("New data found from api - refreshing screen...")

            # logging.info("Clearing screen")
            # draw.clear_screen()
            
            logging.info("Drawing: ")
            # draw.draw_text(lastplayed_artist + " - " + lastplayed_track)
            # draw.draw_text_position(lastplayed_artist, 'top')
            # draw.draw_text_position(lastplayed_track, 'bottom')
            # draw.text_top_bottom(lastplayed_track, lastplayed_artist)
        
            album_cover = get_album_cover.fetch_image(lastplayed_image)
            draw.image(album_cover)
        
            previous_track_name = lastplayed_track


        logging.info("Waiting " + str(frequency) + " seconds")
        time.sleep(frequency)

if __name__== "__main__":
    main()