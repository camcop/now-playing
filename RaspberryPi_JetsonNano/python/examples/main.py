import lastfm_user_data
import draw
import time


frequency = 5

while True:
    print ("Checking API for last played: ", end = '')
    lastplayed_track, lastplayed_artist, lastplayed_album, lastplayed_image = lastfm_user_data.lastplayed(requested_username)
    
    if lastplayed_track == previous_track_name:  #check if the track name is same as what we displayed last time
        print ("no change to data - not refreshing")
    else:
        print ("new data found from api - refreshing screen")
        previous_track_name = lastplayed_track

    print ("Drawing : ", end = '')
    draw.draw_text(lastplayed_artist + " - ", lastplayed_track)
    
    print ("Waiting " + str(frequency) + " seconds")
    time.sleep(frequency)