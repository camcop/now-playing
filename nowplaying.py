from sample import draw, lastfm_user_data, get_album_cover
import time
import logging
import os
import dotenv

try:
    dotenv.load_dotenv()
except:
    logging.warning("Dotenv error")

def main():
    logging.basicConfig(level=logging.DEBUG)
    
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
        try:
            lastplayed_track, lastplayed_artist, lastplayed_album, lastplayed_image = lastfm_user_data.lastplayed(requested_username)
        except:
            logging.info("Error fetching data. Trying again.")
        
        logging.info("Last played track: " + lastplayed_track)
        logging.info("Last played artist: " + lastplayed_artist)
        logging.info("Last played album: " + lastplayed_album)
        logging.info("Last played image: " + lastplayed_image)

        if lastplayed_track == previous_track_name:  #check if the track name is same as what we displayed last time
            logging.info("No change to data - not refreshing")
        else:
            refreshed_time = time.time()

            logging.info("New data found from api - refreshing screen...")

            # logging.info("Clearing screen")
            # draw.clear_screen()
            
            logging.info("Drawing: ")
            # draw.draw_text(lastplayed_artist + " - " + lastplayed_track)
            # draw.draw_text_position(lastplayed_artist, 'top')
            # draw.draw_text_position(lastplayed_track, 'bottom')
            # draw.text_top_bottom(lastplayed_track, lastplayed_artist)
            if lastplayed_image == previous_image_name:  #check if the track name is same as what we displayed last time
                logging.info("No change to album cover - using same image")
            else:
                try:
                    get_album_cover.fetch_image(lastplayed_image)
                except Exception as e:
                    logging.exception("Error fetching album cover. Showing previous cover", e)
                    pass
            # draw.image(album_cover)
            draw.image_and_text(album_cover, lastplayed_track, lastplayed_artist)
        
            previous_track_name = lastplayed_track
            previous_image_name = lastplayed_image


        if time.time() >= refreshed_time + refresh_slowdown_period:
            refresh_frequency = refresh_frequency_low
        else:
            refresh_frequency = refresh_frequency_default

        logging.info("Waiting " + str(refresh_frequency) + " seconds")
        time.sleep(refresh_frequency)

if __name__== "__main__":
    main()