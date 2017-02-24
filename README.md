## Set up:

1. pip is required

```
$ sudo apt-get install python-pip
```

2. Now that pip is installed we need to install virtualenv

```
$ sudo pip install virtualenv
```

3. Create a virtualenv

```
$ virtualenv -p python3 env
```

4. Activate the virtualenv

```
$ source env/bin/activate
```

5. Install dependencies

```
$ pip install -r requirements.txt
```


## Once the enviroment is activated:

1. Run migrations (Only to prevent warning messages from third party libraries. There are no models in the winclap project.)

```
$ python manage.py migrate
```
      
 2. Start the server.

```
$ python manage.py runserver
```
      
### 1 - Campaigns classificator

For this	exercise I decided to build a real API functionality using Django REST Framework. For that, I created:

1. The `campaignclassificator.api.serializers.UserDataSerializer` serializer, which allows to automatically validate the incoming parameters and return a 400 error if necessary.

2. The `campaignclassificator.api.views.CurrencyProblemAPIView` view that validates the parameters using the serializer and looks for the best campaign match. If there is more than one match it takes one of those at random. It was built this way to allow dynamic parameters instead of using the `user.json` data alone.

The actual function that tests this view using the `user.json` file is in the API unit tests file `campaignsclassificator.api.tests.py` (the test checks if the result is one of the two possible matches for best campaign). Besides that, there are unit tests for checking that a 400 error is raised if a parameter is missing or invalid.


#### To run the test that sends the `user.json` data to the API

```
$ python manage.py test campaignclassificator.api.tests
```

#### To test the API endpoint using other parameters

Go to the following URL passing parameters as query string. It will return the best campaign from the given list.

```
http://127.0.0.1:8000/clasificator/api/best_campaign/?gender=Male&age=16&platform=Android&connection=WiFi
```


### 2 - Currency Problem

The code for this exercise is in the `currencyproblem.api.views.py` file, the dataset used is in `currencyproblem.datasets.campaigns.json`

Going to the following URL will return a list of campaigns with the profits converted to USD in JSON format.

```
http://127.0.0.1:8000/currency/api/currency/
```

### 3 - Sheep

The code for this exercise is in the `sheep.sheep.py` file, the dataset used is in ``sheep.c-input.in``

Type in terminal:

```
$ python winclap/sheep/sheep.py 
```
