# mono integrated crm for local business

This idea for project created when i visiting a local barbershop and communicating with a barber.
It little django full stack crm that come's integration for monobank.ua(`its one of the most popular web based bank in Ukraine`) API.

[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter-django/)
[![Black code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

## Project description

This project provide booking for a clients, email notifications for stuff and clients. Monthly notification for staff salary payments, based on their activities. Its can be likely automaticly create transaction for staff sallaryes.

## TODO
 - [ ] Create own business profile for user
 - [ ] Adding staff members for company
 - [ ] Pages with contains booking information for company and for staff members
 - [ ] Notification for staff members
 - [ ] Integrated form that can give access for clients booking some company services
 - [ ] Notification for clients
 - [ ] Access for FOP account in monobank
 - [ ] Transactions in bank account
## Settings

## Basic Commands
Just for start project you need docker.
For build dev envs its uses command 
`docker-compose -f local.yml build --no-cache && docker-compose -f local.yml up -d` 

### Setting Up Your Users
