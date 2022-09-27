
**odoo**
========
_A great option to make software-dev apps_
------------------------------------------
       
<br/>

1. **Scaffolding new Odoo Module.**
2. **Docker Compose file.**
3. **References.**

<br/><br/>

**1. SCAFFOLDING NEW ODOO MODULE**
----------------------------------

<br/>

```docker
docker run -it --rm --user root -v "${PWD}/custom-addons-15:/mnt/extra-addons" odoo:15.0 /usr/bin/odoo scaffold library_ed /mnt/extra-addons
```
<br/>

> **WARNING**
> ${PWD} is the enviroment variable to get current working directory in Microsoft Power Shell, if you're not working with that shell, replace it with your CURRENT-DIRECTORY enviroment variable.

<br/><br/>

**2. DOCKER COMPOSE FILE**
--------------------------

<br/>

```docker
version: '3.1'
services:
  
  odoo:
    container_name: odoo15
    image: odoo:15.0
    env_file: .env
    ports:
      - "127.0.0.1:8069:8069"
    # WARNING: For update/install modules inside the container, overwrites COMMAND 
    # command: odoo -c /etc/odoo/odoo.conf -u library_ed -d test15
    depends_on:
      - postgres
    volumes:
      - odoo15-data:/var/lib/odoo
      - ./config-15:/etc/odoo
      - ./custom-addons-15:/mnt/extra-addons

  postgres:
    container_name: postgres-for-odoo15
    image: postgres
    env_file: .env
    volumes:
      - postgres-db:/var/lib/postgresql/data/pgdata

volumes:
  odoo15-data:
  postgres-db:
```

<br/><br/>

**3. REFERENCES**
-----------------

<br/>

1. (2022). Home. odoo. Retrieved July 31, 2022 from https://www.odoo.com/es_ES 
2. (2022). Compara las ediciones de Odoo. odoo. Retrieved July 31, 2022 from https://www.odoo.com/es_ES/page/editions 
3. (2022). Odoo Open Source Apps To Grow Your Business. GitHub. Retrieved 31 July, 2022 from https://github.com/odoo/odoo 
4. Reis, Daniel. (2022). Odoo 15 Development Essentials. Editorial Packt. (5ta Ed.). www.packt.com
5. Jamon Camisso. (mayo 11, 2022) Tutorial How To Install Odoo on Ubuntu 20.04 with Docker. Digital Ocean Community. Retrieved August 14, 2022 from https://www.digitalocean.com/community/tutorials/how-to-install-odoo-on-ubuntu-20-04-with-docker
6. Emerald Digital SC. (2022). Curso de "Fundamentos de Docker“. Youtube. Retrieved August 12, 2022 from https://www.youtube.com/watch?v=jxt1DGnTqoQ&t=164s&ab_channel=EmeraldDigital 
7. odoo. (2022) odoo Docker Official Image. Docker. Retrieved August 14, 2022 from https://hub.docker.com/_/odoo 
8. odoo/Docker. (enero 10, 2018) [10.0] docker odoo scaffold (Permission denied) #159. Github. Retrieved August 14, 2022 de  https://github.com/odoo/docker/issues/159 
9. (2022) Odoo Documentación. odoo. Retrieved August 14, 2022 from https://www.odoo.com/documentation/15.0/ 
10. (2022) Developer Documentation. Odoo. Retrieved August 14, 2022 from https://www.odoo.com/documentation/15.0/developer.html 
11. slipymp. (2022). IBO - Icon Builder for Odoo. Retrieved August 18, 2022 from https://spilymp.github.io/ibo/ 

