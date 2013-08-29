'''
Configuration Settings

Includes keys for Twilio, etc.  Second stanza intended for Heroku deployment.
'''

# Uncommet to configure in file.
ACCOUNT_SID = "AC4e4ae505f911752bc0a334a1d9bb9c52"
AUTH_TOKEN = "069d7b07d22be81b0a216e5e5f1f7b33"
BSSSPAM_APP_SID = "AP4d53354dcb4588a65f39b6355435e5c1"
BSS_SPAM_ID = "+19787352571"


# Begin Heroku configuration - configured through environment variables.
import os
ACCOUNT_SID = os.environ['ACCOUNT_SID']
AUTH_TOKEN = os.environ['AUTH_TOKEN']
BSSSPAM_APP_SID = os.environ['BSSSPAM_APP_SID']
BSS_SPAM_ID = os.environ['BSS_SPAM_ID']


