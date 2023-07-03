## Installation
To install and run, follow these steps:
1. Clone the repository:
   

   git clone https://github.com/alex23090/tech_exercise_ds.git
   
2. Navigate to the project directory:
   

   cd tech_exercise
   
3. Create a virtual environment:
   

   python3 -m venv env
   
4. Activate the virtual environment:
   * For Windows:
     

     .\env\Scripts\activate
     
   * For macOS/Linux:
     

     source env/bin/activate
     
5. Install the dependencies:
   

   pip install -r requirements.txt
   
6. Perform database migrations:
   

   python manage.py migrate
   
7. Start the development server:
   

   python manage.py runserver
   
9. Open your web browser and navigate to http://localhost:8000 to access the application.
