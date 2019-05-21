# Sensu Agent
## Introduction
    The Workload Manager supports integration to various third party services. This document briefs down information 
    on integration with Sensu Server by creating a Virtual Machine (VM) with Agent service in Workload Manager.
    
    Sensu agent is a lightweight client that runs on the infrastructure components you want to monitor. Agents register 
    with the Sensu backend as monitoring entities with type: "agent". Agent entities are responsible for creating 
    check and metrics events to send to the backend event pipeline. 
    
    Please refer the below link for more details.
    https://docs.sensu.io/sensu-go/5.3/reference/agent/

# Pre-Requisites
#### CloudCenter
- CloudCenter 5.0.1 and above
- Knowledge on how to use Workload Manager 
- Supported OS: CentOS 7
	
# Download the service bundles
   Step 1 : Fetch sensu agent File by copying & pasting the contents from [here](https://github.com/datacenter/cloudcentersuite/raw/master/Content/Monitoring/Sensu-Agent/WorkloadManager/src/sensu-agent/sensu-agent) into a new file named "sensu-agent". Place the file in a repository and its location is http://YourIP/services/sensu-agent/sensu-agent.
   
   Step 2 : With any existing App Profile, this agent script can be configured by defining value with proper repository path like  "services/sensu-agent/sensu-agent" under "Post Start script" in service Initialization  Actions  OR "Initialization script" in Node Initialization. Sample App Profile has been given for demo.
   
   Step 3 : Download the Sample Modelled Application Profiles with sensu agent pre-configured in Service lifecycle action, from [here](https://github.com/datacenter/cloudcentersuite/raw/master/Content/Monitoring/Sensu-Agent/WorkloadManager/sensuagent_iu.zip?raw=true).
   
   Step 4 : Verify the location of the application packages and Agent File in file Repository. Make sure its placed correctly, By default Application Package will be under apps/your-packages and Node Lifecycle Agent file will be under services/sensu-agent/<sensu-agent-file>.
   
   Step 5 : Login into your Cloud Center Suite with your credentials namely IP address, Email address, Password & Tenant ID. Navigate to App profiles section under Workload Manager. Click on "Import" button found on the top right corner of App profiles section. You will be prompted to choose the application profile that needs to be imported. Choose the Modelled Application Profile Zip file downloaded from Step-3. Then You will be prompted to map your file repository in which you have placed the Node Lifecycle Agent file. Map your file repository.
   
You will be presented with a message saying "Application Profile Imported Successfully".
   
# Service Package Bundle

The Package of Service bundle consists of the following files:

Shell script:
 - sensu-agent: This script will install agent and configure the sensu agent with sensu server.


# Service Initialization actions / Node Initialization & Clean Up
   - Under "Pre-Start Script" lifecycle action, agent script would be configured like services/sensu-agent/sensu-agent

# Minimum Resource Specifications

     
S.No    | Resource    |  Value   | Remarks
----    | ----------  | ---------| ------- 
 1      |  CPU        | 1        |        
 2      |  Memory     | 1 GB     |     
  
 
 # Global Parameters in Application Profile
 
   - If sensu server deployment uses default values and credentials,  then add only the below global variable and skip/ignore 2nd table data.

| Parameter Name	| Type	 | Description | Allowed Value |Default Value |
| ------ | ------ | ------ |------ | ------ |
| sensuServerHost | String | Sensu Server Host IP Address |   |  |  |

   - If sensu server deployment is not using the default values, then add the following details in App Profile as Global Parameters in addition with the above variable.
   - If the sensu agent needs to point to external sensu server, add the following parameters.

| Parameter Name	| Type	 | Description | Allowed Value |Default Value |
| ------ | ------ | ------ |------ | ------ |
| rabbitmqPort | Number | Port for connecting to Sensu Server  |  | 5672 | 


