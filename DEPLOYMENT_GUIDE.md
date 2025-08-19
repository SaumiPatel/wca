# WhatsApp Chat Analyzer - Deployment Guide

This guide provides instructions for deploying the WhatsApp Chat Analyzer application to different platforms.

## Prerequisites

- Git repository with your application code
- GitHub account
- Streamlit Cloud account or Heroku account

## Option 1: Deploy to Streamlit Cloud (Recommended)

Streamlit Cloud is the easiest way to deploy Streamlit applications.

1. **Push your code to GitHub**
   - Create a new repository on GitHub
   - Initialize Git in your local project folder (if not already done):
     ```
     git init
     git add .
     git commit -m "Initial commit"
     git branch -M main
     git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
     git push -u origin main
     ```

2. **Sign up for Streamlit Cloud**
   - Go to [Streamlit Cloud](https://streamlit.io/cloud)
   - Sign in with your GitHub account

3. **Deploy your app**
   - Click "New app"
   - Select your repository, branch, and main file path (app.py)
   - Click "Deploy"
   - Wait for the deployment to complete

4. **Access your deployed app**
   - Once deployed, you'll get a URL to access your application
   - Share this URL with others to let them use your WhatsApp Chat Analyzer

## Option 2: Deploy to Heroku

1. **Create a Procfile**
   - Create a file named `Procfile` (no extension) in your project root with the following content:
     ```
     web: streamlit run app.py --server.port=$PORT
     ```

2. **Create a runtime.txt file**
   - Create a file named `runtime.txt` in your project root with the following content:
     ```
     python-3.9.16
     ```

3. **Push your code to GitHub**
   - Follow the same steps as in Option 1 if not already done

4. **Sign up for Heroku**
   - Go to [Heroku](https://www.heroku.com/) and create an account
   - Install the Heroku CLI on your computer

5. **Deploy to Heroku**
   - Login to Heroku CLI:
     ```
     heroku login
     ```
   - Create a new Heroku app:
     ```
     heroku create your-app-name
     ```
   - Push your code to Heroku:
     ```
     git push heroku main
     ```
   - Ensure at least one instance is running:
     ```
     heroku ps:scale web=1
     ```

6. **Access your deployed app**
   - Open your app with:
     ```
     heroku open
     ```
   - Or visit `https://your-app-name.herokuapp.com`

## Important Notes

1. **Environment Variables**: If your app uses any API keys or sensitive information, set them as environment variables in your deployment platform.

2. **File Upload Limits**: Be aware that both platforms have limits on file upload sizes. Streamlit Cloud has a limit of 200MB, while Heroku has a limit of 500MB for the entire application.

3. **Timeout Limits**: Heroku has a 30-second timeout for web requests. If your app takes longer to process data, consider implementing background processing.

4. **Sleeping Apps**: Free Heroku dynos sleep after 30 minutes of inactivity. The first request after sleeping will take longer to respond.

5. **Persistence**: Neither platform provides persistent storage by default. If you need to store user data, consider using a database service.

## Troubleshooting

- **Application Crashes**: Check the logs using `heroku logs --tail` for Heroku or the Streamlit Cloud dashboard for errors.
- **Dependency Issues**: Ensure all dependencies are correctly listed in `requirements.txt`.
- **Memory Errors**: If you encounter memory errors, consider optimizing your code or upgrading to a paid tier with more resources.