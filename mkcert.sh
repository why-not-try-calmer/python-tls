#!/usr/bin/bash
read -p "Email:" email
read -p "CN:" CN
read -p "Country:" C
read -p "Province:" ST
read -p "City:" L
read -p "Organization:" O
read -p "Organization unit:" OU

openssl req -new -x509 -days 365 -nodes -out cert.pem -keyout key.pem -subj "/C=${C}/ST=${ST}/L=${L}/O=${O}/OU=${OU}/CN=${CN}/emailAddress=${email}"