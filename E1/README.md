
**odoo**
========
_A great option to make software-dev_
-------------------------------------
       
<br/>

**E1 - CUSTOMIZING APPS**
1. **About odoo.conf (odoo 16.0).**
2. **Install / Update odoo modules through odoo command.**
3. **Docker compose file.**
4. **Check DB data with psql.**
5. **References.**

<br/><br/><br/><br/>

**1. ABOUT ODOO.CONF (ODOO 16.0)**
----------------------------------

When you start from zero a docker container with odoo v16.0 image and create your db, the generated odoo.conf only will have one parameter (admin_passwd). To save all the configuration the server runs, you must set this _command_ at odoo section (see topic 3):

```docker
command: odoo --save --stop-after-init
```

> **NOTE**
> When you start the containers with _**docker-compose up**_ you'll watch the message _**[odoo image name] exited with code 0**_, so your must delete or comment the added command  and do over _docker-compose up_ to take in count your odoo.conf.


<br/><br/>

**2. INSTALL / UPDATE ODOO MODULES THROUGH ODOO COMMAND**
---------------------------------------------------------

You can use "**-i your_module**" (install) or "**-u your_module**" (update) odoo command flag after set the "**-d db_name**" flag. To indicate this bash codeline to docker, add / modify your docker-compose.yml at the odoo image section with this _command_ (see topic 3):
<br/>

```docker
command: odoo -c [odoo.conf] -d [db_name] -i [your_module]
command: odoo -c [odoo.conf] -d [db_name] -u [your_module]
```
<br/><br/>

> **NOTE**
> These commands are to enhance your productivity developing odoo modules, e.g. decreasing time gaps between do changes, navigate to Apps screen and restarting odoo server.

<br/><br/>

**3. DOCKER COMPOSE FILE**
--------------------------

The recommended file content to follow this lesson:
<br/>

```docker
version: '3.1'
services:
  
  odoo:
    container_name: odoo16
    image: odoo:16.0
    env_file: .env
    ports:
      - "127.0.0.1:8069:8069"
    # WARNING: For saving all the running config of server,
    # once saved it comment again with "#"
    # command: odoo --save --stop-after-init
    # WARNING: For update/install modules inside the container, also enable 
    # the unit-testing of the indicated module (quit # before --test-enable)
    # command: odoo -c /etc/odoo/odoo.conf -d test16 -u create_project_from_sale_order #--test-enable
    depends_on:
      - postgres
    volumes:
      - odoo16-data:/var/lib/odoo
      - ./config-16:/etc/odoo
      - ./custom-addons-16:/mnt/extra-addons

  postgres:
    container_name: postgres-for-odoo16
    image: postgres
    env_file: .env
    volumes:
      - postgres-db:/var/lib/postgresql/data/pgdata

volumes:
  odoo16-data:
  postgres-db:
```
<br/><br/><br/>

**4. CHECK DB DATA WITH PSQL**
------------------------------

To watch you odoo db, you can use the **psql** postgres tool, with the next docker command:
```
docker exec -it --env-file [envfile] [postgres_container] psql -U [postgres_user] -d [postgres_db]
```

_Example:_

```
docker exec -it --env-file .env postgres-for-odoo16 psql -U odoo -d test16
```

<br/><br/>

**5. REFERENCES**
-----------------

1. (2022). Home. odoo. Retrieved July 31, 2022 from https://www.odoo.com/es_ES 
2. (2022). Compara las ediciones de Odoo. odoo. Retrieved July 31, 2022 from https://www.odoo.com/es_ES/page/editions 
3. (2022). Odoo Open Source Apps To Grow Your Business. GitHub. Retrieved 31 July, 2022 from https://github.com/odoo/odoo 
4. Reis, Daniel. (2022). Odoo 15 Development Essentials. Editorial Packt. (5ta Ed.). www.packt.com
5. Jamon Camisso. (mayo 11, 2022) Tutorial How To Install Odoo on Ubuntu 20.04 with Docker. Digital Ocean Community. Retrieved August 14, 2022 from https://www.digitalocean.com/community/tutorials/how-to-install-odoo-on-ubuntu-20-04-with-docker
6. Emerald Digital SC. (2022). Curso de "Fundamentos de Docker“. Youtube. Retrieved August 12, 2022 from https://www.youtube.com/watch?v=jxt1DGnTqoQ&t=164s&ab_channel=EmeraldDigital 
7. odoo. (2022) odoo Docker Official Image. Docker. Retrieved August 14, 2022 from https://hub.docker.com/_/odoo 
8. odoo/Docker. (enero 10, 2018) [10.0] docker odoo scaffold (Permission denied) #159. Github. Retrieved August 14, 2022 de  https://github.com/odoo/docker/issues/159 
9. (2022) Odoo Documentación. odoo. Retrieved August 14, 2022 from https://www.odoo.com/documentation/15.0/ 
10. Odoo. (2022) Developer Documentation. Odoo. Retrieved August 14, 2022 from https://www.odoo.com/documentation/15.0/developer.html 
11. slipymp. (2022). IBO - Icon Builder for Odoo. Retrieved August 18, 2022 from https://spilymp.github.io/ibo/
12. MDN Web Docs community. (2023) Xpath. Retrieved February 14, 2023 from https://developer.mozilla.org/es/docs/Web/XPath
13. Odoo. (2023) ORM API. Retrieved February 10, 2023 from https://www.odoo.com/documentation/16.0/es/developer/reference/backend/orm.html
14. Odoo. (2023) How to fill many2many or many2one fields while creating a record in another model. Retrieved February 11, 2023 from https://www.odoo.com/es_ES/forum/ayuda-1/how-to-fill-many2many-or-many2one-fields-while-creating-a-record-in-another-model-128503
15. Odoo. (2023) Views. Retrieved February 22, 2023 from https://www.odoo.com/documentation/16.0/developer/reference/backend/views.html
16. Cuaderno de Cultura Científica. (February 13, 2019) La notación polaca, la de Jan Łukasiewicz. Matemoción.  Retrieved February 23, 2023 from https://culturacientifica.com/2019/02/13/la-notacion-polaca-la-de-jan-lukasiewicz/
17. GitHub Pages. postgres - psql command line tutorial and cheat sheet. Tomcat.Retrieved April 15, 2023 from https://tomcam.github.io/postgres/
