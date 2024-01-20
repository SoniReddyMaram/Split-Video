from moviepy.video.io.VideoFileClip import VideoFileClip
import math

# Function to split video into 1-minute segments
def split_video(video_path):
    clip = VideoFileClip(video_path)
    duration = clip.duration
    
    # Calculate the number of segments (rounded up)
    num_segments = math.ceil(duration / 60)
    
    # Generate 1-minute clips
    for i in range(num_segments):
        start_time = i * 60  # Start time in seconds
        end_time = min((i + 1) * 60, duration)  # End time in seconds (not exceeding the video duration)
        
        # Create a subclip from start_time to end_time
        subclip = clip.subclip(start_time, end_time)
        
        # Write the subclip to a file
        subclip.write_videofile(f'output_clip_{i + 1}.mp4')  # Change the file format if needed

# Replace 'video_path' with the path to your video file
video_path = 'C:/Users/sonir/OneDrive/Desktop/Research Work/300.mp4'
split_video(video_path)
