
# BDM Music Recognition WebApp

BDM Music Recognition is a web application that allows users to scan and identify songs using the [audd.io](https://audd.io/) API. It is built with Django for the backend, Bootstrap for the frontend, and uses AWS S3 Bucket for file storage. The app is built with a focus on assisting businesses and professionals in the music industry. Please note that this application necessitates the use of certain APIs, for which paid subscriptions may be required. 

![Screenshot_2](https://github.com/TonnyG95/BDM-Music-Recognition/assets/47572512/443f6e04-4a1a-4fe4-95b6-7416431967ce)

## Table of Contents
1. [Features](#features)
2. [Technologies](#technologies)
3. [Setup](#setup)
4. [Usage](#usage)
5. [Deployment](#deployment)

## Features

- **Song Recognition**: Upload a snippet or full song to find out its title, artist, label, and release date.
- **Mobile-Friendly Interface**: Thanks to Bootstrap, the app is user-friendly on all devices.
- **Secure File Storage**: All uploaded files are stored in AWS S3, ensuring fast and secure access.

### Song Recognition

BDM Quality Control Buddy is a free and open-source app which you can integrate with your service to speed up your QC process. The app uses the Audd.io API to gather all information about songs you scan. Audd.io is a professional service that many music professionals, such as music labels, distributors, producers, etc., rely on. Audd.io can access all kinds of information about a song, from the ISRC to the link to the song on each and every DSP that is currently available. But for our use, we decided just to show the most important information for us, which includes:

- Release Title
- Artists
- Album
- Release Date
- Label
- Smart Link

For more information about the audd.io API, [visit their website](https://audd.io/).

**As you can see in this screenshot (We had to blur information about clients due to data protection policy by BDM Network):**

![Screenshot_3](https://github.com/TonnyG95/BDM-Music-Recognition/assets/47572512/e6948998-436d-473e-909b-daa8b8215a02)

**In case Audd.io has no information about the song, it will return that the song is clear and ready for distribution, as you can see in this screenshot:**

![Screenshot_4](https://github.com/TonnyG95/BDM-Music-Recognition/assets/47572512/1154689f-83ba-4ae9-8e48-b6cec7b10233)

### Responsive Design

Since we used [Bootstrap 5](https://getbootstrap.com/) as our CSS framework/library, the web application is fully responsive and looks good on all screens, from PCs to smartphones. The UI in this project was not our priority, so we used pre-made bootstrap elements/components for rapid development.

### Secure File Storage

BDM's Quality Control Buddy uses an Amazon S3 bucket for storage of the uploaded files that are sent for scanning. The reason for this was that we wanted to ensure that our server won't be affected by users uploading songs for scanning and that we won't be limited by storage for our web application. Another advantage of using an Amazon S3 bucket is that files are secured, available, and quickly uploaded, which will help users to scan as many songs as possible without having to wait a few minutes for the song to upload. Keep in mind that Amazon S3 can get expensive with a lot of uploads and it's important to remember that your bucket must be public for this to work.

Our Amazon S3 Settings:

The bucket is publicly accessible and here you can see our settings in the bucket's "Permissions" tab:
- Permissions > **Bucket Policy**:

```
{
    "Version": "2012-10-17",
    "Id": "Policy1650556415415",
    "Statement": [
        {
            "Sid": "Stmt1650556411764",
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::your-bucket-name/*"
        }
    ]
}

```

- Permissions > **Cross-origin resource sharing (CORS)**:

```
[
    {
        "AllowedHeaders": [
            "*"
        ],
        "AllowedMethods": [
            "PUT",
            "GET",
            "POST",
            "DELETE"
        ],
        "AllowedOrigins": [
            "*"
        ],
        "ExposeHeaders": []
    },
    {
        "AllowedHeaders": [
            "*"
        ],
        "AllowedMethods": [
            "PUT",
            "GET",
            "POST",
            "DELETE"
        ],
        "AllowedOrigins": [
            "*"
        ],
        "ExposeHeaders": []
    },
    {
        "AllowedHeaders": [],
        "AllowedMethods": [
            "GET"
        ],
        "AllowedOrigins": [
            "*"
        ],
        "ExposeHeaders": []
    }
]

```

- Permissions > **Access control list (ACL) Settings**:

![Screenshot_5](https://github.com/TonnyG95/BDM-Music-Recognition/assets/47572512/781fdb43-740c-4027-9f32-d42c9d95bb13)

## Technologies

- **Backend**: [Django](https://www.djangoproject.com/)
- **Frontend**: [Bootstrap](https://getbootstrap.com/)
- **Song Recognition**: [audd.io API](https://audd.io/)
- **File Storage**: [AWS S3 Bucket](https://aws.amazon.com/s3/)

### Backend Technologies

As we mentioned before, this web application is built on Django. Django is a high-level Python web framework that enables rapid development of secure and maintainable websites and web applications. It follows the model-template-view (MTV) architectural pattern, which is similar to the model-view-controller (MVC) pattern. Django was designed to make it easy for developers to build web applications with less code and follows the "Don't Repeat Yourself" (DRY) principle. [More information here](https://www.djangoproject.com/)

---

### Frontend Technologies

As we mentioned before, this web application uses Bootstrap 5 for our frontend framework/library. Bootstrap is a popular front-end web development framework that provides pre-designed HTML, CSS, and JavaScript components for building responsive and mobile-friendly websites and web applications. [More information here](https://getbootstrap.com/)

---

### Audd.io API

Audd.io is an online audio recognition service that allows users to identify songs by analyzing audio clips. It uses advanced algorithms to recognize music from various sources, such as recordings, radio, or even humming. Users can upload a short audio clip or provide a URL to identify a song. Audd.io is particularly helpful when you come across a song and want to know its title, artist, and other relevant details. [More information here](https://audd.io/)


---

### Amazon S3

Amazon S3 (Simple Storage Service) is a popular cloud-based storage service provided by Amazon Web Services (AWS). S3 is an object storage service that offers highly scalable, durable, and secure cloud storage. It is designed to store and retrieve any amount of data at any time. The service is commonly used for hosting static website content, storing backups, archiving data, and enabling data-driven applications. [More information here](https://aws.amazon.com/s3/)
 

## Setup

Follow these steps to set up and run the application:

1. **Clone the repository**:
```
git clone https://github.com/TonnyG95/BDM-Music-Recognition
```

2. **Set up a virtual environment and install dependencies**:
```bash
python -m venv venv
source venv/bin/activate  # for Linux/Mac
venv\Scripts\activate  # for Windows
pip install -r requirements.txt
```

3. **Configure AWS and audd.io settings**:
Add your keys and secrets for AWS S3 and audd.io in `settings.py` or through environment variables.

4. **Run migrations**:
```
python manage.py migrate
```

5. **Start the server**:
```
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` to access the application.

## Usage

1. **Upload**: Click the upload button and select the audio file you wish to identify.
2. **Recognition**: Once uploaded, the app will automatically identify the song and display the results.

## Deployment

### Where to deploy this application?

Since this is a Django application, you can't deploy it simply like you would with PHP applications. It can be complicated, so please check a few tutorials on the topic before you try to deploy it on your own. Depending on the service you choose, deployment can be simple or very complicated. We have successfully deployed this application on the cloud platforms listed below, but please do some research before you attempt to deploy:
- [Render](https://render.com/) 
- [Amazon Lightsail](https://aws.amazon.com/lightsail/)
- [Vercel](https://vercel.com/)
- [Heroku](https://www.heroku.com/) 

**From all platforms we deployed this app on, the easiest and simplest solution was Render, which also has a free tier. The 2nd place was Vercel, followed by Heroku. As you would expect, deployment to Amazon Web Services was the most complicated. Check a few tutorials and give it a try.**

### Step by Step

1. Select your cloud platform.
2. Clone this repo.
3. Create `env.py` or rename **"env-example.py"** to **"env.py"**.
4. Add your API credentials.

```
import os

# Main Settings

os.environ["SECRET_KEY"] = "Your secret key"

# Audd.io API Key
os.environ["api_token"] = "Your API token"

# S3 Upload
os.environ["AWS_ACCESS_KEY_ID"] = 'Your AWS access key'
os.environ["AWS_SECRET_ACCESS_KEY"] = 'Your AWS secret key'
os.environ["AWS_STORAGE_BUCKET_NAME"] = 'Your AWS bucket name'
os.environ["AWS_S3_REGION_NAME"] = 'Your AWS region'
```

5. Run 
``` 
pip install -r requirements.txt
```

6. Run
```
python manage.py makemigrations
```
7. Run 
```
python manage.py migrate
```
8. Run 
```
python manage.py collectstatic
```
9. Now you should be able to run the development server to test the app 
```
python manage.py runserver
```
- Note: If you are using Mac OS or Linux, you need to use `python3` instead of `python`.

```
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py collectstatic
python3 manage.py runserver
```

### Conclusion

Thanks to everyone who checked out our app. We hope you find it useful and enjoy using it as much as we enjoyed building it



