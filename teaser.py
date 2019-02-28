import webbrowser

class lovedfilms():
    def __init__(self,caption,design,picture,clip):
        self.title=caption
        self.storyline=design
        self.poster_image_url=picture
        self.trailer_youtube_url=clip
    def show_film_clip(self):
        webbrowser.open(self,trailer_youtube_url)
