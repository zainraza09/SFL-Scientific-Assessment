# SFL-Scientific-Assesment
## 1.	What is data lake?
   ### a.   Data Lake:
  &nbsp; &nbsp; **i.**	A data lake is a central location that holds a large amount of data in its native or raw format.<br/>
  &nbsp; &nbsp; **ii.** It often consolidates all of an organization’s data in one single central location, where it can be saved “as is” without the need to impose a schema.<br/>
  &nbsp; &nbsp; **iii.** It stores data from all stages of refinement process starting from staging layer to compute layers.<br/>
 &nbsp; &nbsp;  **iv.**  And, it can store all types of data – including unstructured and semi-structured data like image, video, audio etc.<br/>
  &nbsp; &nbsp; **v.**  Example – Azure genlake 2.<br/>

  ###  b.   Benefits of Data lake and how it’s different from Datawarehouse.
&nbsp; &nbsp;  **i.**  Datawarehouse can process only structured data whereas datalake can store structured, semi-structured and unstructured data.<br/>
   &nbsp; &nbsp;  &nbsp; **Benefit for client:** They need not to maintain different types of databases for structured and unstructured data.<br/>
&nbsp; &nbsp;  **ii.**	Datawarehouse can scale up to certain extent and becomes exponentially more expensive but datalake can scale to any amount with less cost.<br/>
&nbsp; &nbsp;    &nbsp; **Benefit for client:** Scalability with low cost<br/>
&nbsp; &nbsp; **iii.**	Data ware house is mostly meant for business professional but datalake can we used by business professionals and data scientist.<br/>
  &nbsp; &nbsp;  &nbsp;  **Benefit for client:** A unified space for everyone.<br/>
## 2.	What is serverless architecture? And what are pros and cons?
&nbsp; &nbsp;**a.**	Serverless is a cloud computing execution model where the cloud provider dynamically manages the allocation and provisions of server.A serverless application runs in stateless compute containers that are event triggered and are fully managed by event triggers.<br/>
&nbsp; &nbsp;**b.**	The pricing is based on the number of executions rather than pre purchased compute capacity.<br/>
&nbsp; &nbsp;**c.**	Example: Azure functions, AWS Lambda.<br/>
&nbsp; &nbsp;**d.Pros:** <br/>
 &nbsp;&nbsp; &nbsp; **i.**	Cheaper than traditional cloud<br/>
  &nbsp;&nbsp; &nbsp; **ii.**	It scalable to any capacity.<br/>
  &nbsp;&nbsp; &nbsp; **iii.**	It lowers human resource costs.<br/>
  &nbsp;&nbsp; &nbsp; **iv.**	It focuses more on user experience.<br/>
**e.	Cons:**<br/>
  &nbsp; &nbsp;&nbsp; **i.**	Third party has a control of the execution.<br/>
&nbsp; &nbsp;  &nbsp; **ii.**	It has learning curve.<br/>
  
### 3.	ETL Flow:
<img width="901" alt="image" src="https://github.com/zainraza09/SFL-Scientific-Assesment/blob/main/ETL_Flow%20Diagram.PNG">

### 4.	Modern ML Ops.<br/>
**a.**	ML Ops is the fusion of traditional devops process in the context of data science and machine learning.<br/>
**b.**	<br/>
 <img width="901" alt="image" src="https://github.com/zainraza09/SFL-Scientific-Assesment/blob/main/MLOPS_Diagram.PNG"><br/>

**c.	Steps Involved in Data:**<br/>
&nbsp; **i.	Identify and collect:**<br/>
&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;First step in a dataOps enabled pipeline is identifying sources and source system where the target data lives.<br/>
&nbsp; **ii.	Process:**<br/>
&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;Once the source data is identified, it needs to be processed and transformed into a form that can be analyzed or explored.<br/>
&nbsp; **iii.	Store:**<br/>
&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;	Choosing the technology that meets your organization access right, security and privacy needs. Using a dataware house or a datalake is a typical option.<br/>

**d.	Steps involved in ML:**<br/>
&nbsp; **i.	Extract:**<br/>
&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;The goal is to extract the feature that contains information about the data which can resolve the business problem.<br/>
&nbsp; **ii.	Train:**<br/>
&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;Training is fitting a model to your train dataset while maintaining optimal performance and meeting the requirement.<br/>
&nbsp; **iii.	Optimize:**<br/>
&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;Use appropriate method to optimize the model before going live.<br/>
**e.	Steps involved in Continuous integration:**<br/>
**i.	Plan, package and develop:**<br/>
&nbsp;&nbsp;&nbsp; **1**&nbsp;When the model is ready to be published, the underlying code, dependency will be pushed to repo and merged to main branch.<br/>
&nbsp;&nbsp;&nbsp;&nbsp;**2** &nbsp;The push will trigger the build for the model.<br/>
&nbsp;**ii.	Test:**<br/>
&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;Afte the build is generated and packaging is done and container is ready to be shipped, the process continues with performing unit test and integration testing.<br/>
**f.	Steps involved in Continuous integration:**<br/>
&nbsp;**i.	Staging:**<br/>
&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;Staging is a place where the artifact of CD will reside.<br/>
&nbsp;**ii.	Release and configuration:**<br/>
&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;In this step the mode will be deployed to the target system.<br/>
&nbsp;**iii.	Validation and Monitoring.**<br/>
&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;ML model will be validated in this step and monitored.<br/>
