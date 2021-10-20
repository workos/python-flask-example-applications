# python-flask-sso-example
An example Flask application demonstrating how to use the [WorkOS Python SDK](https://github.com/workos-inc/workos-python) to authenticate users via SSO.

## Prerequisites
- Python 3.6+


## Flask Project Setup

1. In your CLI, navigate to the directory into which you want to clone this git repo.
   ```bash
   $ cd ~/Desktop/
   ```

2. Clone the main git repo for these Python example apps using your preferred secure method (HTTPS or SSH).
   ```bash
   # HTTPS
   $ git clone https://github.com/workos-inc/python-flask-example-applications.git
   ```

   or

   ```bash
   # SSH
   $ git clone git@github.com:workos-inc/python-flask-example-applications.git
   ```

3. Navigate to the sso app within the cloned repo.
   ```bash
   $ cd python-flask-example-applications/python-flask-sso-example
   ```

4. Create and source a Python virtual environment. You should then see `(env)` at the beginning of your command-line prompt.
   ```bash
   $ python3 -m venv env
   $ source env/bin/activate
   (env) $
   ```

5. Install the cloned app's dependencies.
   ```bash
   (env) $ pip install -r requirements.txt
   ```

6. Obtain and make note of the following values. In the next step, these will be set as environment variables.
   - Your [WorkOS API key](https://dashboard.workos.com/api-keys)
   - Your [SSO-specific, WorkOS Client ID](https://dashboard.workos.com/configuration)

7. Ensure you're in the root directory for the example app, `python-flask-sso-example/`. Create a `.env` file to securely store the environment variables. Open this file with the Nano text editor. (This file is listed in this repo's `.gitignore` file, so your sensitive information will not be checked into version control.)
   ```bash
   (env) $ touch .env
   (env) $ nano .env
   ```

8. Once the Nano text editor opens, you can directly edit the `.env` file by listing the environment variables:
   ```bash
   export WORKOS_API_KEY=<value found in step 6>
   export WORKOS_CLIENT_ID=<value found in step 6>
   ```

   To exit the Nano text editor, type `CTRL + x`. When prompted to "Save modified buffer", type `Y`, then press the `Enter` or `Return` key.

9. Source the environment variables so they are accessible to the operating system.
   ```bash
   (env) $ source .env
   ```

   You can ensure the environment variables were set correctly by running the following commands. The output should match the corresponding values.
   ```bash
   (env) $ echo $WORKOS_API_KEY
   (env) $ echo $WORKOS_CLIENT_ID
   ```

10. In `python-flask-sso-example/app.py` change the `CUSTOMER_EMAIL_DOMAIN` string value to an email domain that makes sense for your testing purposes if the default `gmail.com` isn't relevant. If you'd like to establish auth connection via Connection_ID instead, please change the `CUSTOMER_CONNECTION_ID` to your organization's connectionID. 

11. The final setup step is to start the server.
   ```bash
   (env) $ flask run
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

   Navigate to `localhost:5000` in your web browser. You should see a "Login" button. If you click this link, you'll be redirected to an HTTP `404` page because we haven't set up SSO yet!

   You can stop the local Flask server for now by entering `CTRL + c` on the command line.


## SSO Setup with WorkOS

Follow the [SSO authentication flow instructions](https://workos.com/docs/sso/guide/introduction) to set up an SSO connection.

When you get to the step where you provide the `REDIRECT_URI` value, use http://localhost:5000/auth/callback.

If you get stuck, please reach out to us at support@workos.com so we can help.

## Testing the Integration

1. Naviagte to the `python-flask-sso-example` directory. Source the virtual environment we created earlier, if it isn't still activated from the steps above. Start the Flask server locally.

   ```bash
   $ cd ~/Desktop/python-flask-sso-example/
   $ source env/bin/activate
   (env) $ flask run
   ```

   Once running, navigate to http://localhost:5000 to test out the SSO workflow.

   Hooray!

## Need help?

If you get stuck and aren't able to resolve the issue by reading our API reference or tutorials, you can reach out to us at support@workos.com and we'll lend a hand.
