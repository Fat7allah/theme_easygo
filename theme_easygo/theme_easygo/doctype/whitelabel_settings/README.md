# Whitelabel Settings for Theme EasyGo

This module provides comprehensive whitelabeling capabilities for your Frappe application, allowing you to customize the appearance and branding of your site.

## Features

- **App Logo**: Change the application logo that appears in the navbar
- **App Logo Width**: Adjust the size of the app logo (20px-200px)
- **Favicon**: Change the browser favicon
- **Splash Image**: Change the splash/loading image
- **Login Page Title**: Customize the title shown on the login page
- **Hide "Powered By" Text**: Remove the "Powered by Frappe" text from the footer
- **Navbar Background Color**: Change the color of the navigation bar
- **Custom Navbar Title**: Set a custom title for the navbar
- **Navbar Title CSS**: Apply custom CSS to style the navbar title
- **Hide Help Menu**: Remove the help menu from the navbar
- **Remove Welcome Page**: Disable the default welcome page
- **Update Welcome Blog**: Update the default welcome blog post

## Usage

1. Navigate to **Whitelabel Settings** in your Frappe application
2. Configure the desired whitelabel options
3. Click **Save** to apply the changes
4. Click **Preview Changes** to see the changes immediately

## Technical Details

The whitelabel settings work by:
1. Storing configuration in the Whitelabel Settings doctype
2. Generating custom CSS based on these settings
3. Loading the custom CSS in both desk and web templates
4. Applying JavaScript enhancements where needed

## Version Compatibility

- For Version 13+: Includes the ability to update onboarding steps to remove video and documentation links

## Troubleshooting

If changes don't appear immediately:
1. Clear your browser cache
2. Run `bench clear-cache` on the server
3. Restart the Frappe server with `bench restart`
