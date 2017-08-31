import tweepy #Import Library Tweepy
import credentials
class TwitterAPI:
    """Clase principal que contiene el metodo para conectarse mediante OAuth a la API de Twitter
    utilizando cuatro atributos"""
    __consumer_key= credentials.CONSUMER_KEY
    __consumer_secret= credentials.CONSUMER_SECRET
    __access_token=credentials.ACCESS_TOKEN
    __access_token_secret=credentials.ACCESS_TOKEN_SECRET
    
    def main():
        auth = tweepy.OAuthHandler(TwitterAPI.__consumer_key, TwitterAPI.__consumer_secret)
        auth.set_access_token(TwitterAPI.__access_token, TwitterAPI.__access_token_secret)
        api = tweepy.API(auth)
        return api


class ActionsAPI(TwitterAPI):
    """Clase que ereda de TwitterAPI el metodo para conectarse a la API de Twitter
    y que cuenta con dos metodos: update_status y get_info_user los cuales reciben
    message y name como parametros."""
    __action=TwitterAPI.main()
    user_info = []
    def __init__(self, message=None, name=None):
        self.message = message
        self.name = name
        
    def update_status(self):
        """ Recibe el Tweet a Twittear"""
        ActionsAPI.__action.update_status(status=self.message)
        return print("Listo!")

    def get_info_user(self):
        """Retorna la informacion principal del usuario de Twitter espcificado"""
        data=ActionsAPI.__action.get_user(self.name)
        ActionsAPI.user_info.append(data._json['name'])
        ActionsAPI.user_info.append(data._json['description'])
        ActionsAPI.user_info.append(data._json['location'])
        ActionsAPI.user_info.append(data._json['followers_count'])
        ActionsAPI.user_info.append(data._json['friends_count'])
        ActionsAPI.user_info.append(data._json['statuses_count'])
        ActionsAPI.user_info.append(data._json['favourites_count'])
        return print(ActionsAPI.user_info)

a=ActionsAPI(name='MarcoA_Rod')
a.get_info_user()