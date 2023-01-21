# FLASK APP WITH OPENAI

Start in project:
1. Get a openai API key: https://beta.openai.com/account/api-keys
2. Install pycharm comunity edition IDE (You can use another IDE if you want): https://www.jetbrains.com/help/pycharm/installation-guide.html#requirements
3. Clone this repository in your system
4. Open the proyect and install requirements via terminal:
```python -m pip install -r requirements.txt```
5. Once the requirements are installed, tu start the web app, run in terminal: 
```python -m flask --app app run```
6. Go to your web browser and search http://localhost:5000

Docker container:
1. Install docker
2. Enter to proyect directory and run: ```docker build -t app_name .```
3. Then run: ```docker run -d -p 5000:5000 <app_name>```
4. Go to your web browser and search http://localhost:5000