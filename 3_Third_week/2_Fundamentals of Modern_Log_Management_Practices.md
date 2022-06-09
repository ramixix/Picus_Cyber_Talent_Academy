First of all, I'd like to give you an overview of the Security Operations Center. A SOC refers to people, processes, and technologies responsible for monitoring, analyzing, maintaining, and improving an organization's cybersecurity. A SOC is not a room with large monitors on the wall; it is a capability composed of three building blocks; people, process,and technology.

- The first building block of a SOC is People. A SOC consists of different roles, including SOC analyst, incident responder, threat hunter, and SOC manager. Some mature Security Operations Centers also include compliance auditor and security architect roles.

- The second building block is Processes. Defining clear, robust, and repeatable processes brings a good foundation for the actions a SOC member takes. A SOC lacks guidance and produces inconsistent results if these processes aren't in place. We will see key SOC operations in the next slide. 

- The third building block is Technology. An effective SOC incorporates data from various sources and analyzes and manages data. The core technology of a successful SOC is an enterprise-wide data collection, management, detection, and analytics solution. 


**a log is a record of the events occurring within an organization's systems and networks.**
**Briefly, log management is the process for generating, transmitting, storing, analyzing, and disposing of log data.**

Log Management is the most fundamental SOC function as threat detection and mitigation, monitoring and troubleshooting, incident investigation and forensics, government and industry compliance, auditing, and threat hunting are entirely dependent on internal and external context, which is provided by logs. 


there are four categories of sources we can choose to collect logs from:

- The first one is Security Controls, which are safeguards or countermeasures to prevent, detect, correct, compensate, or counteract security risks to physical property, information, computer systems, or other assets.

- The second group of log sources is Network Infrastructure, the hardware and software resources of an entire network that enable network connectivity, communication, operations, and management of an enterprise network.

- The third one is Operating Systems Microsoft Windows, macOS, Linux distributions, and other operating systems are valuable log sources.

- The last group of log sources is Applications.


We can identify three criteria in defining the quality and performance factors of data provided by log management: 
1- If there are missing logs or not, 
2- If logs are relevant, and
3- If the logs are delivered to SIEMs with no delay.

- Firstly, the coverage should be comprehensive to ensure all required data from systems, security devices, and others are collected so that no critical events stay out of the SOC visibility.
- It is also important not to inflate the logging infrastructure with data that does not add good enough context. This would create complexity, performance issues, storage shortage, and unnecessarily taking away from the event per second (EPS) license capacity.
- Secondly, the level of detail logs contain is also very important. The SIEM may have received the log, but the event types and event attributes may be off to pinpoint an event. Or, conversely, logging maybe in the verbose level that contains unnecessary details. 
- Thirdly, the timing of a log delivery is a crucial factor in detecting incidents early on. Infrastructural issues or policy configurations may delay the log delivery.

So, to summarize, SIEM practitioners that are in charge of the log management needs to
- make sure that they strike the right balance on the number of sources they collect logs from. 
- logs should contain the required detail with no excess information, and
- logs are to be delivered and collected with no delay. 