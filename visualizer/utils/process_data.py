import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


class YoutubeWatchHistory:

    def __init__(self, path):
        self.path = path
        self.watch_history = pd.read_json(path)


    def process_history(self):
        """Processes the watch history of the user where unavailable videos,
        YouTube Music rows are removed from the data frame.
        Additionally, columns "description", "products, "details", "activityControls", and 
        "header are dropped.
        """
        try: 
            # Remove deleted/unavailable videos
            self.watch_history = self.watch_history[self.watch_history['subtitles'].notna()]

            # Drop Titles with 'Visited Youtube Music'
            self.watch_history = self.watch_history[~self.watch_history['title'].str.contains('Visited YouTube Music')]

            # Drop titles with Answered survey question
            self.watch_history = self.watch_history[~self.watch_history['title'].str.contains('Answered survey question')]

            # Drop description
            self.watch_history = self.watch_history.drop(columns=['description'])

            # Drop products
            self.watch_history = self.watch_history.drop(columns=['products'])

            # Drop details
            self.watch_history = self.watch_history.drop(columns=['details'])

            # Drop activityControls
            self.watch_history = self.watch_history.drop(columns=['activityControls'])

            # Drop header
            self.watch_history = self.watch_history.drop(columns=['header'])
        except:
            print("Error processing history")

    def get_watch_history(self):
        """Returns the watch history as a data frame.
        """
        return self.watch_history