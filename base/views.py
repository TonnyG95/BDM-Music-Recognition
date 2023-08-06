from django.shortcuts import render
import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import os
import boto3

# Rendering homepage
def home(request):
    return render(request, 'home.html')

if os.path.isfile("env.py"):
    import env

# API Call
def scan_song(request):
    if request.method == "POST":
        audio_link = request.POST.get('audio_link')
        audio_file = request.FILES.get('audio_file')

        if audio_link:
            response = requests.post(
                'https://api.audd.io/',
                data={
                    'url': audio_link,
                    'return': 'apple_music,spotify',
                    'api_token': os.environ.get('API_TOKEN'),
                },
            )
            response_data = response.json()
            result = response_data.get('result')
            if result:
                song_data = {
                    "artist": result.get('artist'),
                    "title": result.get('title'),
                    "album": result.get('album'),
                    "release_date": result.get('release_date'),
                    "label": result.get('label'),
                    "timecode": result.get('timecode'),
                    "song_link": result.get('song_link'),
                }
                return JsonResponse(song_data)
            else:
                return JsonResponse({"error": "No song data found."})
        elif audio_file:
            s3_url = upload_to_s3(audio_file)
            if s3_url:
                response = requests.post(
                    'https://api.audd.io/',
                    data={
                        'url': s3_url,
                        'return': 'apple_music,spotify',
                        'api_token': os.environ.get('API_TOKEN'),
                    },
                )
                response_data = response.json()
                result = response_data.get('result')
                if result:
                    song_data = {
                        "artist": result.get('artist'),
                        "title": result.get('title'),
                        "album": result.get('album'),
                        "release_date": result.get('release_date'),
                        "label": result.get('label'),
                        "timecode": result.get('timecode'),
                        "song_link": result.get('song_link'),
                    }
                    return JsonResponse(song_data)
                else:
                    return JsonResponse({"error": "No song data found."})
            else:
                return JsonResponse({"error": "Error uploading file to S3."})
        else:
            return JsonResponse({"error": "Please enter a URL or upload an audio file."})

    return JsonResponse({"error": "Invalid request"})

def upload_to_s3(file):
    aws_access_key_id = os.environ.get('AWS_ACCESS_KEY_ID')
    aws_secret_access_key = os.environ.get('AWS_SECRET_ACCESS_KEY')
    bucket_name = os.environ.get('AWS_STORAGE_BUCKET_NAME')
    s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)

    try:
        s3.upload_fileobj(file, bucket_name, file.name)
        s3_url = f"https://{bucket_name}.s3.amazonaws.com/{file.name}"
        return s3_url
    except Exception as e:
        print("Error uploading to S3:", e)
        return None
