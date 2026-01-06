# Secure Web Application Using NGINX Reverse Proxy

## Project Title
Secure Web Server with SSL and Reverse Proxy on Linux

## Objective
The main goal of this project is to secure a backend web application by placing it behind an NGINX reverse proxy and enabling HTTPS using SSL. The backend server should not be directly accessible by users.

## Technologies Used
- Linux (RHEL / Rocky Linux)
- NGINX Web Server
- Python Flask
- OpenSSL
- FirewallD

## Project Description
In this project, a Flask backend application is created and runs on localhost port 5000. NGINX is configured as a reverse proxy to forward requests securely to the backend. HTTPS is enabled using a self-signed SSL certificate to encrypt data between the client and server.

## Architecture
Client Browser → HTTPS (Port 443) → NGINX Reverse Proxy → HTTP (Port 5000) → Flask Backend

## Security Implementation
- HTTPS encryption using SSL certificate
- Reverse proxy hides backend server
- Firewall allows only required ports
- Backend server accessible only via NGINX

## Outcome
The website is secured using HTTPS and the backend Flask application is protected from direct access.

## Note
SSL private keys are not uploaded to GitHub for security reasons.
