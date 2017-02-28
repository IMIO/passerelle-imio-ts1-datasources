Passerelle connector : Import ts1 datasources and method to add, update or delete new records
=============================================================================================

Installation
------------

 - add to Passerelle installed apps settings:
   INSTALLED_APPS += ('passerelle_imio_ts1_datasources',)

 - enable module:
   PASSERELLE_APP_PASSERELLE_IMIO_TS1_DATASOURCES_ENABLED = True


Usage
-----

 - create and configure new connector
   - Title/description: whatever you want
   - URL: https://e-services.liege.be:8443/
   - Certificate check: uncheck if the service has no valid certificate

 - test service by clicking on the available links
   - the /voies/ endpoint may take some time as it will query for everything
     (but will be cut at 51 items)
   - the /voies/?q=... endoint is set with an example string, feel free to
     change it.


Usage in w.c.s.
---------------

 - configure a list field with a jsonp datasource, with the "/voies/" endpoint
   URL as value.
