## Makku_Backend_Users

### Tech stack
- python
- django
- drf
- jwt
- swagger

### Layout

[![Figma](https://img.shields.io/badge/-Figma-black?style=flat-square&logo=figma)](https://www.figma.com/file/K6vy2Ewmb2hSN9bxOFnNGk/makku?node-id=1%3A2&t=JR3orsm7mB3LZErE-0)

### Installation

- Clone the repository on your computer: `git clone https://github.com/MakkuService/Makku_BackEnd_Users-.git`
- Install dependencies: `pip install -r requirements`
- Launch: `python manage.py runserver`

### Docker

- docker-compose build - 'create image'
- docker-compose up -d - 'run container in compose file'

### EndPoints

- [GET] EmailVerify, parametrers: token
- [POST] Login, parameters: Email, Password
- [POST] Register, parameters: Email, Username, Password
- 

#### Current 
- [X] Custum User Model
- [X] JWT autentification
- [X] User Registration
- [X] Sending Verification Email
- [X] VerifyEmail
- [X] LoginUser
- [ ] Logout
- [ ] Reset Password
- [ ] 

#### Bags
- [ ] Check Docker host/port
- [ ] Check JWT Token: not valid
