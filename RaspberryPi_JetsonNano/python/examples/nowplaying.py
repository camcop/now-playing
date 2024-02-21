import lastfm_user_data
import draw
import time
import logging
import sys
import os
from dotenv import load_dotenv

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
            draw.text_top_bottom(lastplayed_track, lastplayed_artist)
            draw.image(lastplayed_image)
        
            previous_track_name = lastplayed_track


        logging.info("Waiting " + str(frequency) + " seconds")
        time.sleep(frequency)

if __name__== "__main__":
    main()