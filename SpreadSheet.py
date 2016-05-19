import gspread
from oauth2client.service_account import ServiceAccountCredentials
class Document:


    #OAuth2 Authorization
    def get_user(self):
        scope = ['https://spreadsheets.google.com/feeds']

        credentials = ServiceAccountCredentials.from_json_keyfile_name('TvShowDoc-2a3b4b8070e7.json', scope)

        gc = gspread.authorize(credentials)

        return gc

    #open Spreadsheet, then worksheet
    def Setup(self,token):

        sh = token.open_by_url('https://docs.google.com/spreadsheets/d/1llo-gQx8D8w4Y2aZfPaYylDArekriwcEn7lbC2lV34c/edit?usp=sharing')

        worksheet = sh.get_worksheet(0)

        return worksheet








