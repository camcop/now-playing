import lastfm_user_data
import draw
import time


logging.basicConfig(level=logging.DEBUG)
frequency = 5

while True:
    print ("Checking API for last played: ", end = '')
    lastplayed_track, lastplayed_artist, lastplayed_album, lastplayed_image = lastfm_user_data.lastplayed(requested_username)
    
    if lastplayed_track == previous_track_name:  #check if the track name is same as what we displayed last time
        logging.info("No change to data - not refreshing")
    else:
        logging.info("New data found from api - refreshing screen...")

        logging.info("Clearing screen")
        draw.clear_screen()
        
        logging.info("Drawing: ", end = '')
        draw.draw_text(lastplayed_artist + " - ", lastplayed_track)
    
        previous_track_name = lastplayed_track


    logging.info("Waiting " + str(frequency) + " seconds")
    time.sleep(frequency)