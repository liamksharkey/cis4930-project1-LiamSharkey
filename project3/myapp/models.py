from django.db import models
from django.forms import ModelForm

class Game(models.Model):
        appid = models.IntegerField(primary_key=True)
        name = models.CharField(max_length=255)
        release_date = models.DateTimeField()
        price = models.FloatField()
        dlc_count = models.IntegerField()
        windows = models.BooleanField()
        mac = models.BooleanField()
        linux = models.BooleanField()
        metacritic_score = models.FloatField(null=True)
        achievements = models.IntegerField(null=True)
        recommendations = models.IntegerField(null=True)
        supported_languages = models.JSONField()
        full_audio_languages = models.JSONField()
        developers = models.JSONField()
        publishers = models.JSONField()
        categories = models.JSONField()
        genres = models.JSONField()
        score_rank = models.IntegerField()
        positive = models.IntegerField()
        negative = models.IntegerField()
        average_playtime_forever = models.FloatField()
        average_playtime_2weeks = models.FloatField()
        median_playtime_forever = models.FloatField()
        median_playtime_2weeks = models.FloatField()
        discount = models.FloatField()
        peak_ccu = models.IntegerField()
        tags = models.JSONField()
        pct_pos_total = models.FloatField()
        num_reviews_total = models.IntegerField()
        pct_pos_recent = models.FloatField()
        num_reviews_recent = models.IntegerField()
        def __str__(self):
                return f"{self.title} ({'done' if self.is_done else 'pending'})"
        
class GameDetail(ModelForm):
        class Meta:
                model =  Game
                fields = '__all__'
                

class WeatherRecord(models.Model):
        latitude = models.FloatField()
        longitude = models.FloatField()
        date = models.DateField()

        temp_max = models.FloatField(null=True)
        temp_min = models.FloatField(null=True)
        precipitation = models.FloatField(null=True)
        wind_speed = models.FloatField(null=True)

        class Meta:
                unique_together = ("latitude", "longitude", "date")

        def __str__(self):
                return f"{self.latitude}, {self.longitude} @ {self.date}"