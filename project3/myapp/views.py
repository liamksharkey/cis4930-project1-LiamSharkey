import os
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.contrib import messages
import pandas as pd
from project3 import settings
from .forms import GameForm
from .models import Game
import json
from django.contrib.admin.views.decorators import staff_member_required
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from django.core.management import call_command

def base(request):
        return render(request, 'myapp/base.html')


def home(request):
        return render(request, 'myapp/home.html')


def games_home(request):
        game_qs = Game.objects.all().order_by('appid')
        paginator = Paginator(game_qs, 25) 
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'myapp/games_home.html', {
                'page_obj': page_obj
        })


def games_detail(request, pk):
        game = get_object_or_404(Game, pk=pk)
        return render(request, 'myapp/games_detail.html', {'game': game})
    
 
def games_edit(request, pk):
        game = get_object_or_404(Game, pk=pk)
        
        if request.method == 'POST':
                form = GameForm(request.POST, instance=game)
                if form.is_valid():
                        form.save()
                        return redirect('games_detail', pk=game.pk)
        else:
                form = GameForm(instance=game)

        return render(request, 'myapp/games_edit.html', {'form': form, 'game': game})
 

def games_delete(request, pk):
        game = get_object_or_404(Game, pk=pk)

        if request.method == 'POST':
                game.delete()
                messages.success(request, 'The game has been deleted successfully.')
                return redirect('games_home')

        return render(request, 'myapp/games_delete.html', {'game': game})


FIGURE_DIR = os.path.join(settings.MEDIA_ROOT, 'figures')
if not os.path.exists(FIGURE_DIR):
    os.makedirs(FIGURE_DIR)
   

def games_analytics(request):
        from django.shortcuts import render
import json
import pandas as pd
from .models import Game


def games_analytics(request):
        games = Game.objects.all()
        df = pd.DataFrame(list(games.values()))
        df['accessibility_score'] = (
                df['windows'] + df['mac'] + df['linux'] + 
                df['supported_languages'].apply(len) +
                df['full_audio_languages'].apply(len)
        )

        filtered_df = df[df['pct_pos_total'] > 0]

        scatter_data = [
                {"x": row['accessibility_score'], "y": row['pct_pos_total']}
                for _, row in filtered_df.iterrows()
        ]
        df_genres = df.explode('genres')
        df_genres = df_genres[df_genres['pct_pos_total'] >= 0]

        genre_grouped = (
                df_genres.groupby('genres')['pct_pos_total']
                .median()
                .sort_values()
        )

        genres = genre_grouped.index.tolist()
        genre_values = genre_grouped.values.tolist() 

        context = {
                "scatter_data": json.dumps(scatter_data),
                "genres": json.dumps(genres),
                "genre_values": json.dumps(genre_values),
        }

        return render(request, "myapp/games_analytics.html", context)

@staff_member_required 
@require_POST
def fetch_data(request): 
        call_command("fetch_data")
        return JsonResponse({"status": "success", "message": "Data fetched"})