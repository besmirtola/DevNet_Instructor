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
3. Task implementation => A dockerfile is created and contains all instructions for setting up the service. Specifically, flask framwork is used to develop the app. The app is a very simple Python script that will display some html title and body text, in addition to a current date through a javascript in the localhost (0.0.0.0:8088). This script is exploited and a docker image is build with necessary commands to setup the app and download the image. The bash script "sample-app.sh" contains all the commands that perform such actions and finally carries out the docker run command which actually creates the docker container from the built image and exposes the service on the virtual/local host on port 8088 as requested by the task.
4. Task troubleshooting => no issues encountered.
5. Task verification => refer to the two screenshots uploaded un the task folder. The screenshots show the docker container deployment and the web application runing on the localhost:8088.
