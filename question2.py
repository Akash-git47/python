# YouTube Playlist Analysis

videos = [12, 4, 8, 15, 3, 20]

# Total watch time
total_time = sum(videos)

# Longest video
longest_video = max(videos)

# Average video duration
average_duration = total_time / len(videos)

# Videos shorter than 5 minutes
short_videos = []

for video in videos:
    if video < 5:
        short_videos.append(video)

print("Total Watch Time:", total_time, "minutes")
print("Longest Video:", longest_video, "minutes")
print("Average Video Duration:", average_duration, "minutes")
print("Videos shorter than 5 minutes:", short_videos)