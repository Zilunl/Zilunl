# year_progress.py

import datetime
import pytz  # Import the pytz library for timezone support

def calculate_year_progress():
    now = datetime.datetime.now(pytz.timezone('Australia/Melbourne')).replace(tzinfo=None)
    year_start = datetime.datetime(now.year, 1, 1)
    year_end = datetime.datetime(now.year + 1, 1, 1)
    total_days = (year_end - year_start).days
    passed_days = (now - year_start).days
    progress_percentage = (passed_days / total_days) * 100
    return progress_percentage

def generate_progress_bar(progress_percentage):
    bar_length = 30
    num_filled = int(progress_percentage / (100 / bar_length))
    num_empty = bar_length - num_filled
    return '{ ' + '█' * num_filled + '▁' * num_empty + ' }'

progress = calculate_year_progress()
progress = round(progress, 2)
progress_bar = generate_progress_bar(progress)
current_date = (datetime.datetime.now()+datetime.timedelta(days=1)).strftime("%d-%b-%Y")

print(f"⏳ **Year Progress** {progress_bar} {progress}% as on ⏰ {current_date}")