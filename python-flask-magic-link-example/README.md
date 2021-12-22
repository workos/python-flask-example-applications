# python-flask-magic-link-example
An example Flask application demonstrating how to use the [WorkOS Python SDK](https://github.com/workos-inc/workos-python) to authenticate users via Magic Link.

## Prerequisites
- Python 3.6+


## Flask Project Setup

1. Clone the main git repo for these Python example apps using your preferred secure method (HTTPS or SSH).
   ```bash
   # HTTPS
   $ git clone https://github.com/workos-inc/python-flask-example-applications.git
   ```

   or

   ```bash
   # SSH
   $ git clone git@github.com:workos-inc/python-flask-example-applications.git
   ```

2. Navigate to the Magic Link example app within the cloned repo.
   ```bash
   $ cd python-flask-example-applications/python-flask-magic-link-example
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
   export WORKOS_API_KEY=<value found in step 6>
   export WORKOS_CLIENT_ID=<value found in step 6>
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
   ```

9. The final setup step is to start the server.
   ```bash
   (env) $ flask run
   ```

   If you are using Mac OS Monterey, port 5000 is not available and you'll need to start the app on a different port with this slightly different command. 
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

   Navigate to `localhost:5000`, or `localhost:5001` depending on which port you launched the server, in your web browser.  You should see a "Login" button. 

   You can stop the local Flask server for now by entering `CTRL + c` on the command line.


## Magic Link Setup with WorkOS

Change the default REDIRECT_URI value in the "Configuration" page of your WorkOS dashboard to `http://localhost:5000/success`, or `http://localhost:5001/success` depending on which port you launched the server.

## Testing the Integration

1. Naviagte to http://localhost:5000, or `http://localhost:5001/success` depending on which port you launched the server, to test out the Magic Link flow!

## Need help?

If you get stuck and aren't able to resolve the issue by reading our API reference or tutorials, you can reach out to us at support@workos.com and we'll lend a hand.
