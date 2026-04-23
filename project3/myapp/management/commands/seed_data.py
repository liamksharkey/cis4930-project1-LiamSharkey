# yourapp/management/commands/load_games.py
import pandas as pd
import ast
from django.core.management.base import BaseCommand
from myapp.models import Game

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        useful_cols = ['appid', 'name', 'release_date', 'price', 'dlc_count',
                'windows', 'mac', 'linux', 'metacritic_score',
               'achievements','recommendations','supported_languages',
               'full_audio_languages','developers','publishers','categories',
               'genres','score_rank','positive','negative','average_playtime_forever',
               'average_playtime_2weeks','median_playtime_forever',
               'median_playtime_2weeks','discount','peak_ccu','tags',
               'pct_pos_total','num_reviews_total','pct_pos_recent',
               'num_reviews_recent']
        
        df = pd.read_csv(
            'data/raw/games_march2025_full.csv',
            on_bad_lines='skip',
            engine='python',
            usecols=useful_cols
        )

        df = df.fillna(df.mean(numeric_only=True))

        string_columns = df.select_dtypes(include=['object']).columns
        df[string_columns] = df[string_columns].fillna('MISSING')

        df['windows'] = df['windows'].astype(bool)
        df['mac'] = df['mac'].astype(bool)
        df['linux'] = df['linux'].astype(bool)

        df["supported_languages"] = df["supported_languages"].apply(ast.literal_eval)
        df["full_audio_languages"] = df['full_audio_languages'].apply(ast.literal_eval)
        df["developers"] = df["developers"].apply(ast.literal_eval)
        df["publishers"] = df["publishers"].apply(ast.literal_eval)
        df['genres'] = df['genres'].apply(ast.literal_eval)

        df['release_date'] = pd.to_datetime(df['release_date'])

        games = []
        for _, row in df.iterrows():
                games.append(Game(
                appid=row['appid'],
                name=row['name'],
                release_date=row['release_date'],
                price=row['price'],
                dlc_count=row['dlc_count'],
                windows=row['windows'],
                mac=row['mac'],
                linux=row['linux'],
                metacritic_score=row['metacritic_score'],
                achievements=row['achievements'],
                recommendations=row['recommendations'],
                supported_languages=row['supported_languages'],
                full_audio_languages=row['full_audio_languages'],
                genres=row['genres'],
                developers=row['developers'],
                publishers=row['publishers'],
                categories = row['categories'],
                score_rank = row['score_rank'],
                positive = row['positive'],
                negative = row['negative'],
                average_playtime_forever = row['average_playtime_forever'],
                average_playtime_2weeks = row['average_playtime_2weeks'],
                median_playtime_forever = row['median_playtime_forever'],
                median_playtime_2weeks = row['median_playtime_2weeks'],
                discount = row['discount'],
                peak_ccu = row['peak_ccu'],
                tags = row['tags'],
                pct_pos_total = row['pct_pos_total'],
                num_reviews_total = row['num_reviews_total'],
                pct_pos_recent = row['pct_pos_recent'],
                num_reviews_recent = row['num_reviews_recent'],
        ))

        Game.objects.bulk_create(games, batch_size=1000, ignore_conflicts=True)