import input_handler as ih
import request_handler as rh
import soup_handler as sh
import spotify_handler as spotify

date = ih.prompt_for_date()
billboard_page_source = rh.get_billboard_page(str(date))
track_list = sh.get_billboard_song_list(billboard_page_source)
spotify.setup()
spotify.create_playlist(date)
spotify.add_tracks_to_playlist(track_list, date.year)


