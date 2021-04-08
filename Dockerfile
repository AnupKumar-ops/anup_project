FROM tomcat
MAINTAINER anup_kumar
ARG path_to_war=/var/
COPY $path_to_war/webapp.war /usr/local/tomcat/webapps/
