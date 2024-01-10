# Lung-Disease-Detection

## How to run:

### Step 1: Get the model file into your system

**Drive link for model file: [model.h5](https://drive.google.com/file/d/15UNsIE3aIHudTiRVSqAT4S3AT3veFb2S/view?usp=sharing)**

**Note:** Save the model in the same directory that manage.py is located.

**Note:** Create a folder named **'media'** in the base directory of the Django-server (same directory that manage.py is located) and inside the media folder create another folder named **'downloads'**.

### Step 2: Open three terminal instances.

### Step 3: In one of them navigate inside tbase directory of the Django-server (folder where manage.py is located) and run:

`py manage.py runserver`

This starts our django-server that handles the backend.

### Step 4: In the second terminal, go inside the Frontend folder and run:

`npm run dev`

This starts our frontend react-vite app. If you want to host this web app into your LAN, run:

`npm run host`

### Step 5: In the last terminal, navigate to the python preds folder inside **'Frontend\src\Components\'** and in the mentioned location, create a folder named python_preds. Open it inside the terminal and run:

`http-server ./`

This runs a http server that hosts our files locally. This is required for react to fetch the images output by the model.

Then, open the react app into your browser to successfully use the app.
