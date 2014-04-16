This Django project allows to browse a large base of XML documents
using faceted browsing. It relies on Django-haystack to manage the
faceting.  Several search-indexing systems can be used in
Django-haystack, such as Solr or ElasticSearch.

## Installation

xmlfacets requires Python 2.7 and PostgreSQL.

To set up a local development environment, install [Fabric](http://fabfile.org/)

and make sure you have the following dependencies

* libxml2
* libxslt
* Optional: [Watchdog](http://packages.python.org/watchdog/), for use with the `fab watch_static` command to automatically collect and compile static files as they are changed.
1. Run the command `fab setup` inside the project directory
2. Edit the generated "editorsnotes/settings\_local.py" file with your database information
3. Run `fab sync_database`
4. Start the development server with `fab runserver`

More specifically, for Ubuntu Linux 12.04TLS:

2. Postgresql  
     sudo apt-get install postgresql
     sudo apt-get install pgadmin3

     sudo -u postgres psql postgres
     sudo apt-get install postgresql-client
     sudo apt-get install postgresql-server-dev-9.1

     sudo -u postgres createuser -P -s xmlfacets
     sudo -u postgres createdb -O xmlfacets xmlfacets

3. Fabric
          sudo pip install fabric
4.   libxml2 + libxslt
          sudo apt-get install libxml2

          sudo apt-get install libxml2-dev libxslt-dev

5.   Elastic Search

          wget https://download.elasticsearch.org/elasticsearch/elasticsearch/elasticsearch-1.1.0.deb
          sudo dpkg -i elasticsearch-1.1.0.deb
          sudo service elasticsearch start

6.    Watchdog (optional)

           sudo pip install watchdog

7.  Virtual Environment

          sudo pip install virtualenv

8. Install flup

   To use it with Apache2/fcgi, install flup

   	   sudo pip install flup

9. Inside xmlfacets directory

   	  fab setup

10. Database

    edit xmlfacets/settings_local.py with database info, then:
    	 fab sync_database

    you will be asked the name of the administrator login/pw, let's call it
    "admin" 


11. Start the debug server and check the site:

    	  fab runserver

    open on a web browser http://localhost:8000/

12. Import existing XML documents

    Importing one XML document in /SVN-REPOS/ALBANIA/AL/ImportMe.xml
    	   bin/python manage.sh import -u admin -p /SVN-REPOS/ /SVN-REPOS/ALBANIA/AL/ImportMe.xml

    Assume all the documents are at directory /SVN-REPOS, to import the all, type:

	   ./import.sh /SVN-REPOS admin
