# python-flask-admin-portal-example
An example Flask application demonstrating how to use the [WorkOS Python SDK](https://github.com/workos-inc/workos-python) so your customers can access the WorkOS Admin Portal from your application.

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

2. Navigate to the Admin Portal example app within the cloned repo.
   ```bash
   $ cd python-flask-example-applications/python-flask-admin-portal-example
   ````

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
   - Your `WORKOS_CLIENT_ID`, in the format `client_<random-alphanumeric-string>`, retrievable from WorkOS dashboard under "Configuration".

6. Ensure you're in the root directory for the example app, `python-flask-admin-portal-example/`. Create a `.env` file to securely store the environment variables. Open this file with the Nano text editor. (This file is listed in this repo's `.gitignore` file, so your sensitive information will not be checked into version control.)
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

9. Update the Admin Portal Redirect Link in the "Configuration" page of your WorkOS Dashboard. The URL should be http://localhost:5000. If you are using macOS Monterey, set this to localhost:5001. 

After an Admin Portal user creates an SSO connection using the Admin Portal, they need to be redirected to a webpage within your application (usually this webpage confirms successful creation of the connection). To configure which webpage this is, enter the webpage’s URL in the Configuration section of your WorkOS dashboard under the “Admin Portal Redirect Link” header. For production usage this URL must begin with HTTPS, but for development purposes the URL can begin with HTTP.

## Start the server

10. The final setup step is to start the server.
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

   Navigate to `localhost:5000`, or `localhost:5001` depending on which port you launched the server, in your web browser to view the homepage of the Admin Portal example app. Enter the name of the new Organization to be created and the names of all of the Organization's associated domains.

   - The Organization must be a new Organization that doesn't yet exist in your WorkOS dashboard
   - The domains should be entered as space-separated values, e.g. "domain1.com domain2.com domain3.com"

   Then, click the buttons to either create a new SSO connection or a new Directory Sync connection.
   
   Hooray!

## Need help?

If you get stuck and aren't able to resolve the issue by reading our API reference or tutorials, you can reach out to us at support@workos.com and we'll lend a hand.
