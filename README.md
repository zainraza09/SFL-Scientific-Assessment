# SFL-Scientific-Assesment
## 1.	What is data lake?
   ### a.   Data Lake:
   **i.**	A data lake is a central location that holds a large amount of data in its native or raw format.<br/>
   **ii.** It often consolidates all of an organization’s data in one single central location, where it can be saved “as is” without the need to impose a schema.<br/>
   **iii.** It stores data from all stages of refinement process starting from staging layer to compute layers.<br/>
   **iv.**  And, it can store all types of data – including unstructured and semi-structured data like image, video, audio etc.<br/>
   **v.**  Example – Azure genlake 2.<br/>

  ###  b.   Benefits of Data lake and how it’s different from Datawarehouse.
  **i.**  Datawarehouse can process only structured data whereas datalake can store structured, semi-structured and unstructured data.<br/>
     &nbsp; **Benefit for client:** They need not to maintain different types of databases for structured and unstructured data.<br/>
  **ii.**	Datawarehouse can scale up to certain extent and becomes exponentially more expensive but datalake can scale to any amount with less cost.<br/>
    &nbsp; **Benefit for client:** Scalability with low cost<br/>
 **iii.**	Data ware house is mostly meant for business professional but datalake can we used by business professionals and data scientist.<br/>
    &nbsp;  **Benefit for client:** A unified space for everyone.<br/>
## 2.	What is serverless architecture? And what are pros and cons?
   ### a.	Serverless is a cloud computing execution model where the cloud provider dynamically manages the allocation and provisions of server.
**a.** serverless application runs in stateless compute containers that are event triggered and are fully managed by event triggers.<br/>
**b.**	The pricing is based on the number of executions rather than pre purchased compute capacity.<br/>
**c.**	Example: Azure functions, AWS Lambda.<br/>
**d.**	Pros: <br/>
 &nbsp; **i.**	Cheaper than traditional cloud<br/>
  &nbsp; **ii.**	It scalable to any capacity.<br/>
  &nbsp; **iii.**	It lowers human resource costs.<br/>
  &nbsp; **iv.**	It focuses more on user experience.<br/>
**e.**	Cons:<br/>
  &nbsp; **i.**	Third party has a control of the execution.<br/>
  &nbsp; **ii.**	It has learning curve.<br/>
  
  3.	ETL Flow:

4.	Modern ML Ops.
a.	ML Ops is the fusion of traditional devops process in the context of data science and machine learning.
b.	
 
c.	Steps Involved in Data:
i.	Identify and collect:
1.	First step in a dataOps enabled pipeline is identifying sources and source system where the target data lives.
ii.	Process:
1.	Once the source data is identified, it needs to be processed and transformed into a form that can be analyzed or explored.
iii.	Store:
1.	Choosing the technology that meets your organization access right, security and privacy needs. Using a dataware house or a datalake is a typical option.
d.	Steps involved in ML:
i.	Extract:
1.	The goal is to extract the feature that contains information about the data which can resolve the business problem.
ii.	Train:
1.	Training is fitting a model to your train dataset while maintaining optimal performance and meeting the requirement.
iii.	Optimize:
1.	Use appropriate method to optimize the model before going live.
e.	Steps involved in Continuous integration:
i.	Plan, package and develop:
1.	When the model is ready to be published, the underlying code, dependency will be pushed to repo and merged to main branch.
2.	The push will trigger the build for the model.
ii.	Test:
1.	Afte the build is generated and packaging is done and container is ready to be shipped, the process continues with performing unit test and integration testing.
f.	Steps involved in Continuous integration:
i.	Staging:
1.	Staging is a place where the artifact of CD will reside.
ii.	Release and configuration:
1.	In this step the mode will be deployed to the target system.
iii.	Validation and Monitoring.
1.	ML model will be validated in this step and monitored.




