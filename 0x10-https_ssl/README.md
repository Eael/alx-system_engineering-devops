Configuring SSL on my domain

Problems Encountered
haproxy.cfg gave errors because of the letsencrypt certifcate
To solve, combine `fullchain.pem` file and `privkey.pem`

`sudo cat /etc/letsencrypt/live/your_domain/fullchain.pem /etc/letsencrypt/live/your_domain/privkey.pem > your_domain.pem`
Then make a certs directory in your haproxy files to keep the cert
`sudo mkdir /etc/haproxy/certs`
Next copy your pem file to the certs directory
`sudo cp your_domain.pem /etc/haproxy/certs/`
