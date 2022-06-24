# DevNet_Instructor
DevNet Associate training for Instructor Accreditation

Task 1 -- GitHub Skills Test !

1. Task name => Github
2. Task preparation => Create a folder in which a git repository is initialized. Then create a readme file in which the different task steps are described.
3. Task implementation => the task is implemented by running standard git commands in a terminal for setting up the repository both locally and remotely in a cloud-based server like Github.
4. Task troubleshooting => No issues were faced in setting up the repo.
5. Task verification => refer to the present repo.

Task 2 -- Ansible Skills Test !

1. Task name => Ansible
2. Task preparation => Create an Ansible playbook that retrieves information on a remote devices, in the specific case it is a Cisco router CSR1kv. The playbook is under the Ansible folder.
3. Task implementation => Create a folder on which the Ansible directory will be defined. Then, edit the Ansible config file in which the location of hosts (inventory), host key checking and other config parameters will be defined. Finally, create the ansible playbook with which we will be able to retrieve the IOS version, the interfaces, and set the buffer size. This step requires an .yaml file, i.e., the playbook in whcih all the commands for retrieving such information will be defined. In this task, the playbook is called ios_facts.
4. Task troubleshooting => no issues were faced. Just a need to choose the right tasks.
5. Task verification => refer to the uploaded screenshot in the Ansible folder. 

Task 3 -- Docker !

1. Task name => Docker
2. Task preparation => Refer to Ansible playbook given for building a docker image that spins up a webserver (web app) for which the service is exposed to port 8088. All scripts are under the Docker folder.
3. 
a) Task implementation => A dockerfile is created and contains all instructions for setting up the service. Specifically, flask framework is used to develop the app. The app is a very simple Python script that will display some html title and body text, in addition to a current date through a javascript in the localhost (0.0.0.0:8088). This script is exploited and a docker image is build with necessary commands to setup the app and download the image. The bash script "web-app.sh" contains all the commands that perform such actions and finally executes the docker run command which actually creates the docker container from the built image and exposes the service on the virtual/localhost on port 8088, as requested by the task.

b) very similalry to the a) part, apache2 can be used instead of flask. Specifically, the official image from [https://hub.docker.com/_/httpd_](url) is used to pull the image and then build and run the container with the same settings. Check the specific folder apache_webserver for verification.

5. Task troubleshooting => no issues encountered.
6. Task verification => refer to the two screenshots uploaded un the task folder. The screenshots show the docker container deployment and the web application runing on the localhost:8088.


Task 4 -- Jenkins !

1. Task name => jenkins
2. Task preparation => A working docker application is required.
3. Task implementation => Jenskins server is downloaded and run in a docker container. Jenkins is configured by setting the right git repository and access credentials. The web app of task 3 is then used for executing a build of the application through Jenkins jobs (refer to dockerwebapp_jenkins_build.png). Again, Jenkins is used to test the application by executing a check of the application. Finally, CI/CD pipeline job is configured for building the application. The essence of the pipeline is to stop and remove any existing web app container, then building it again, and finally verifying it works. This way, any chode changes in the application will be continuously integrated and the app will be build automatically and ready for deployment.
4. Task troubleshooting => No issues were faced in setting up Jenkins and the specific jobs.
5. Task verification => Refer to screenshots uploaded under the same task directory.


Task 5 -- REST API & RESTCONF !

1. Task name => restconf
2. Task preparation => No specific requirements beside having a running image of the virtual router CSR1kv.
3. Task implementation => The task consists of transforming curl commands into python scripts that achieve the same goal, i.e., performing configuration commands on the virtual router CSR1kv, by using the RESTCONF protocol. Various python scripts have been created for achieving different goals like creating loopback interfaces, fetching all configured interfaces, and deleting the loopback. Each of these tasks corresponds to a specific python file under the Restconf folder.
Task troubleshooting => No major issues were faced during the task implementation.
Task verification => Refer to screenshots uploaded under the RESTCONF_python_verifications directory.


Task 6 -- WEBEX TEAMS API !

1. Task name => webex
2. Task preparation => The usual DEVASC VM running. Retrieve a personal token from developer.webex.com .
3. Task implementation => The task consists of developing python scripts that perform REST requests to the Webex Teams API. In particular, the implementation includes the creation of a specific Room (or Space), add a specific memeber (Yvan) , post a few messages, and the upload screenshot attachments of the other tasks implementations.
4. Task troubleshooting => No issues were faced during the task implementation.
5. Task verification => Refer to screenshots uploaded under the relative directory.
