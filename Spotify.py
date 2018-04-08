def get_artist_id(artist_name, sp):
    recs = sp.search(artist_name)
    print(recs)
    return recs["tracks"]["items"][2]["id"]

def get_reccomendations():
    pass