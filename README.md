Simple flask project that uses two external network (one for nginx, one for having static ip)

To create nginx network
docker network create --gateway 172.25.0.1 --subnet 172.25.0.0/16 nginx-proxy

To create flask network
docker network create --gateway 100.100.0.1 --subnet 100.100.0.0/16 flask_network

