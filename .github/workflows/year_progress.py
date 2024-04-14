import datetime

def get_year_progress():
    # Get current date
    current_date = datetime.date.today()

    # Get the first day of the year
    start_of_year = datetime.date(current_date.year, 1, 1)

    # Get the last day of the year
    end_of_year = datetime.date(current_date.year, 12, 31)

    # Calculate total days in the year
    total_days_in_year = (end_of_year - start_of_year).days + 1

    # Calculate elapsed days
    elapsed_days = (current_date - start_of_year).days

    # Calculate year progress percentage
    year_progress = (elapsed_days / total_days_in_year) * 100

    return year_progress

def generate_progress_bar(progress):
    # Create a progress bar with 20 segments
    bar_length = 20
    filled_segments = int(progress / 100 * bar_length)
    remaining_segments = bar_length - filled_segments

    # Create the progress bar string
    progress_bar = '█' * filled_segments + '▁' * remaining_segments

    return progress_bar

# Get current year progress
year_progress = get_year_progress()

# Generate progress bar
progress_bar = generate_progress_bar(year_progress)

# Get current date
current_date = datetime.date.today()

# Print Year Progress with progress bar
print(f"⏳ **Year Progress** {{ {progress_bar} }} {year_progress:.2f} % as on ⏰ {current_date.strftime('%d-%b-%Y')}")
