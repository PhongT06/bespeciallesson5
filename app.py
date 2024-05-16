from flask import Flask, request

app = Flask(__name__)

videos = [
    {'id': 1, 'title': 'The Art of Coding', 'duration': 32},
    {'id': 2, 'title': 'Exploring the Cosmos', 'duration': 44},
    {'id': 3, 'title': 'Cooking Masterclass: Italian Cuisine', 'duration': 76},
    {'id': 4, 'title': 'History Uncovered: Ancient Civilizations', 'duration': 77},
    {'id': 5, 'title': 'Fitness Fundamentals: Strength Training', 'duration': 59},
    {'id': 6, 'title': 'Digital Photography Essentials', 'duration': 45},
    {'id': 7, 'title': 'Financial Planning for Beginners', 'duration': 40},
    {'id': 8, 'title': "Nature's Wonders: National Geographic", 'duration': 45},
    {'id': 9, 'title': 'Artificial Intelligence Revolution', 'duration': 87},
    {'id': 10, 'title': 'Travel Diaries: Discovering Europe', 'duration': 78}
]

def merge_sort(lst):
    # Check if our list can be split
    if len(lst) > 1:
        # Find the midway point
        midway = len(lst) // 2
        # Split the list into a left and right half
        left_half = lst[:midway]
        right_half = lst[midway:]

        # Call merge_sort on left half 
        merge_sort(left_half)
        # Call the merge_sort on right half
        merge_sort(right_half)

        # Merge the left and right half lists back into the original list
        # index pointers for the three lists
        l = 0 # pointer for left half
        r = 0 # pointer for right half
        m = 0 # pointer for main list

        # While the left and right pointers are still pointing at valid indices
        while l < len(left_half) and r < len(right_half):
            # if the element at the left half pointer is less than the right half pointer
            if left_half[l]['title'] < right_half[r]['title']:
                # Place the left half value in the original list
                lst[m] = left_half[l]
                # Move our left half pointer right one spot
                l += 1
            else:
                # Place the right half value in the original list
                lst[m] = right_half[r]
                # Move our right half pointer right one spot
                r += 1
            # Either way, always increase the main pointer one spot
            m += 1

        # When one of the half finishes (can be right or left first), copy the rest of the other half into the original
        while l < len(left_half):
            lst[m] = left_half[l]
            l += 1
            m += 1
        while r < len(right_half):
            lst[m] = right_half[r]
            r += 1
            m += 1

    return lst

merge_sort(videos)

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid]['title'] == target:
            return arr[mid]
        elif arr[mid]['title'] < target:
            low = mid + 1
        else:
            high = mid - 1
    return None

@app.route('/')
def index():
    return 'Hello World!!'

@app.route('/sorted-videos')
def sorted_videos():
    return videos

@app.route('/videos')
def search_videos():
    search = request.args.get('search')
    if not search:
        return {'error': "Must have the 'search' query param"}, 400
    video = binary_search(videos, search)
    if video:
        return video
    else:
        return {'error': f"No video with the title '{search}'"}, 404
