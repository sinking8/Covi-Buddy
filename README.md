## Welcome

The world is now in the midst of a dire pandemic and everyone could use a friend. CoviBuddy is your friendly web application that has been designed to make your life easier during this tough and testing pandemic period. Features include a Covid Severity Quiz which will tell you how symptomatic you are, Face Mask Detector, Weekly Newsletter which will be emailed to your mail ID containing the latest news and updates on Covid-19 and a Covid Cases Tracker which has live data displayed in a graphical form about the cases, recoveries and deaths of all the countries around the world.  All of these features have been created using Machine Learning Algorithms thereby making them adaptable and dynamic. They are also easy to use and are hosted on a responsive web page. We aim to add more amazing features in the future like a Covid based chatbot, a mobile application and so on.


<hr>


## Built With
* [Bootstrap](https://getbootstrap.com)
* [Flask](https://flask.palletsprojects.com/en/2.0.x/)
* [OpenCV](https://docs.opencv.org/4.5.2/d6/d00/tutorial_py_root.html)


## Screenshots

### Covid Mask Detector
![Covid_Mask_Detector](https://github.com/sinking8/Covi-Buddy/blob/main/screenshots/face_mask.jpeg)

### Covid Tracker
![Covid_Mask_Detector](https://github.com/sinking8/Covi-Buddy/blob/main/screenshots/covid_tracker.png)

### Covid Detector Quiz
![Covid_Mask_Detector](https://github.com/sinking8/Covi-Buddy/blob/main/screenshots/quiz.png)

Project Structure
--------

  ```sh
  ├── Procfile
  ├── Procfile.dev
  ├── README.md
  ├── app.py
  ├── config.py
  ├── requirements.txt
  ├── covid_detector
  │   ├── saved_models
  │   ├── Covid_Detect.py
  │   ├── Mask_detect.py
  │   ├── Haarcascades
  ├── static
  │   ├── css
  │   ├── font
  │   ├── ico
  │   ├── img
  │   └── js
  └── templates
      ├── errors
      │   ├── 404.html
      │   └── 500.html
      └── pages
          ├── API.html
          └── CoviBuddy.html
          └── index.pug
          └── webcam.html
  ```


### Screenshots




### Quick Start

1. Clone the repo
  ```
  $ git clone https://github.com/sinking123/Covi-Buddy.git
  $ cd Covi-Buddy
  ```

2. Initialize and activate a virtualenv:
  ```
  $ virtualenv --no-site-packages env
  $ source env/bin/activate
  ```

3. Install the dependencies:
  ```
  $ pip install -r requirements.txt
  ```

5. Run the development server:
  ```
  $ python app.py
  ```

6. Navigate to [http://localhost:5000](http://localhost:5000)

