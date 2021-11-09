# python-flask-directory-sync-example
A basic Flask app that uses the [WorkOS Python SDK](https://github.com/workos-inc/workos-python) to support Directory Sync.

## Prerequisites
- Python 3.6+

## Directory Sync Setup with WorkOS
First, follow the [Create a New Directory Connection](https://workos.com/docs/directory-sync/guide/create-new-directory-connection) step in the WorkOS Directory Sync guide.

If you get stuck, please reach out to us at support@workos.com so we can help.

## Flask Project Setup

### Clone Directory

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

3. Navigate to the Directory Sync example app within the cloned repo.
   ```bash
   $ cd python-flask-example-applications/python-flask-directory-sync-example
   ```

4. Create and source a Python virtual environment. You should then see `(env)` at the beginning of your command-line prompt.
   ```bash
   $ python3 -m venv env
   $ source env/bin/activate
   (env) $
   ```

### Install Dependencies

5. Install the cloned app's dependencies.
   ```bash
   (env) $ pip install -r requirements.txt
   ```

### Set Environment Variables

6. Obtain and make note of the following values. In the next step, these will be set as environment variables.
   - Your [WorkOS API key](https://dashboard.workos.com/api-keys)
   - Your `WEBHOOKS_SECRET`, retrievable from the URL in the WEBHOOKS area of the WorkOS dashboard. This is only required if you are utilizing the webhooks route of this application to receive and validate webhook events. 


7. Ensure you're in the root directory for the example app, `python-flask-directory-sync-example/`. Create a `.env` file to securely store the environment variables. Open this file with the Nano text editor. (This file is listed in this repo's `.gitignore` file, so your sensitive information will not be checked into version control.)
   ```bash
   (env) $ touch .env
   (env) $ nano .env
   ```

 8. Once the Nano text editor opens, you can directly edit the `.env` file by listing the environment variables:
    ```bash
    export WORKOS_API_KEY=<value found in step 6>
    export WEBHOOKS_SECRET=<value found in step 6>
    ```

    To exit the Nano text editor, type `CTRL + x`. When prompted to "Save modified buffer", type `Y`, then press the `Enter` or `Return` key.

9. Source the environment variables so they are accessible to the operating system.
   ```bash
   (env) $ source .env
   ```

   You can ensure the environment variables were set correctly by running the following commands. The output should match the corresponding values.
   ```bash
   (env) $ echo $WORKOS_API_KEY
   (env) $ echo $WEBHOOKS_SECRET
   ```

## Start the server

1. Use this command to run the app:
   ```bash
   flask run
   ```

2. Once the server is running, navigate to http://localhost:5000 to view the home page of the app where you can then select the view for users or groups. 

    - The `/users` URL corresponds to the WorkOS API's [List Directory Users endpoint](https://workos.com/docs/reference/directory-sync/user/list)
    - The `/groups` URL corresponds to the WorkOS API's [List Directory Groups endpoint](https://workos.com/docs/reference/directory-sync/group/list)
    - You can extend this Django example app by adding views to `directory_sync/views.py` for the other available [Directory Sync API endpoints](https://workos.com/docs/reference/directory-sync).

## Need help?

When you clone this repo, the `DEBUG` setting is `False` by default in `app.py`. You can set `DEBUG = True` if you need to troubleshoot something during the tutorial, but you must use `DEBUG = False` in order to successfully connect to the WorkOS API.

If you get stuck and aren't able to resolve the issue by reading our API reference or tutorials, please  reach out to us at support@workos.com and we'll help you out.
