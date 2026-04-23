from django import forms
from .models import Game

class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = [
            'appid', 'name', 'release_date', 'price', 'dlc_count',
            'windows', 'mac', 'linux', 'metacritic_score', 'achievements',
            'recommendations', 'supported_languages', 'full_audio_languages',
            'genres', 'developers', 'publishers', 'categories', 'score_rank',
            'positive', 'negative', 'average_playtime_forever', 'average_playtime_2weeks',
            'median_playtime_forever', 'median_playtime_2weeks', 'discount',
            'peak_ccu', 'tags', 'pct_pos_total', 'num_reviews_total',
            'pct_pos_recent', 'num_reviews_recent'
        ]