# python-flask-mfa-example
An example Flask application demonstrating how to use the [WorkOS MFA API](https://workos.com/docs/mfa/guide) using the [Python SDK](https://github.com/workos/workos-python) to authenticate users.

## Prerequisites
- Python 3.6+


## Flask Project Setup

1. Clone the main git repo for these Python example apps using your preferred secure method (HTTPS or SSH).
   ```bash
   # HTTPS
   $ git clone https://github.com/workos/python-flask-example-applications.git
   ```

   or

   ```bash
   # SSH
   $ git clone git@github.com:workos/python-flask-example-applications.git
   ```

2. Navigate to the sso app within the cloned repo.
   ```bash
   $ cd python-flask-example-applications/python-flask-mfa-example
   ```

3. Create and source a Python virtual environment. You should then see `(env)` at the beginning of your command-line prompt.
   ```bash
   $ python3 -m venv env
   $ source env/bin/activate
   (env) $
   ```

4. Install the cloned app's dependencies.
   ```bash
   (env) $ pip install -r requirements.txt
   ```

5. Obtain and make note of the following values. In the next step, these will be set as environment variables.
   - Your [WorkOS API key](https://dashboard.workos.com/api-keys)
   - Your [SSO-specific, WorkOS Client ID](https://dashboard.workos.com/configuration)

6. Ensure you're in the root directory for the example app, `python-flask-sso-example/`. Create a `.env` file to securely store the environment variables. Open this file with the Nano text editor. (This file is listed in this repo's `.gitignore` file, so your sensitive information will not be checked into version control.)
   ```bash
   (env) $ touch .env
   (env) $ nano .env
   ```

7. Once the Nano text editor opens, you can directly edit the `.env` file by listing the environment variables:
   ```bash
   WORKOS_API_KEY=<value found in step 6>
   WORKOS_CLIENT_ID=<value found in step 6>
   APP_SECRET_KEY=<any string value you\'d like>
   ```

   To exit the Nano text editor, type `CTRL + x`. When prompted to "Save modified buffer", type `Y`, then press the `Enter` or `Return` key.

8. Source the environment variables so they are accessible to the operating system.
   ```bash
   (env) $ source .env
   ```

   You can ensure the environment variables were set correctly by running the following commands. The output should match the corresponding values.
   ```bash
   (env) $ echo $WORKOS_API_KEY
   (env) $ echo $WORKOS_CLIENT_ID
   (env) $ echo $APP_SECRET_KEY
   ```


9. The final setup step is to start the server.
   ```bash
   (env) $ flask run
   ```

   If you are using macOS Monterey, port 5000 is not available and you'll need to start the app on a different port with this slightly different command. 
   ```bash
   (env) $ flask run -p 5001
   ```

   You'll know the server is running when you see no errors in the CLI, and output similar to the following is displayed:

   ```bash
   * Tip: There are .env or .flaskenv files present. Do "pip install python-dotenv" to use them.
   * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
   * Debug mode: off
   * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
   ```

   Navigate to `localhost:5000`, or `localhost:5001` depending on which port you launched the server, in your web browser. You should see a "Login" button. If you click this link, you'll be redirected to an HTTP `404` page because we haven't set up SSO yet!

   You can stop the local Flask server for now by entering `CTRL + c` on the command line.


## Using the MFA application

11. This application is meant to showcase the MFA API and how to interact with it using the WorkOS Python SDK. It is not meant to show a real-life example of how MFA should be implemented. 

   The app supports two types of MFA flows, SMS and Time-based One Time Password (TOTP). 

   SMS: The SMS flow requires you to send a code via text message. You can customize this message, but the message must include the string "{{code}}". This string of characters tells the WorkOS API to generate a random code that will be populated automatically. If "{{code}}" is not included in the message, the authentication cannot be completed. 

   TOTP: This type of authentication requires the use of a 3rd party authentication app (1Password, Authy, Google Authenticator, Microsoft Authenticator, Duo, etc). Scan the QR code from the Factor Details page to create the corresponding factor in the 3rd party app, then enter the time-based password when prompted in this MFA application.  

   TOTP NOTE - Since all storage is being done via browser cookies, only 1 TOTP type connection can be added at a time to this app due to limitations on the size of the cookies that browsers can store. This is due to the size of the QR code. 

## Need help?

First, make sure to reference the MFA docs at https://workos.com/docs/mfa/guide. 

If you get stuck and aren't able to resolve the issue by reading our API reference or tutorials, you can reach out to us at support@workos.com and we'll lend a hand.
