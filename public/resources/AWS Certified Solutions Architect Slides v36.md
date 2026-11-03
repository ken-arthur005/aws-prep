AWS Certified Solutions Architect Associate By Stéphane Maarek aws% certified <u>https://links.data cumulus.com/aw</u> ~~Solutions~~ ir <u>sArchitect certified</u> ~~<u>htt</u>~~ -sa- <u>ps://links.da</u> <mark>if .</mark> <u>associate</u> ASSOCIATE -coupon d ) <u>https://links.dat</u> ~~<u>tac</u>~~ <u>umulus.com |</u> ~~=e~~ <u>acumulus.com/ /aws-certifiedaws-certsa-associatesolutioncoupon architect-pthttps://links.datacumulus.com/aw https://links.datacumulus.com/aws</u> ~~COURSE > EXTRA PRACTICE EXAMS >~~ <u>s-certified-sa-associate-coupon</u> -cert-solution ~~<u>coupon</u>~~ -architect-pt-coupon 

© Stephane Maarek 

Disclaimer: These slides are copyrighted and strictly for personal use only 

- This document is reserved for people enrolled into the <u>Ultimate AWS Solutions Architect Associate Course</u> 

- Please do not share this document , it is intended for personal use and exam preparation only, thank you. 

- If you’ve obtained these slides for free on a website that is not the course’s website, please reach out to piracy@datacumulus.com. Thanks! 

- Best of luck for the exam and happy learning! 

© Stephane Maarek 

#### Table of Contents 

- <u>Getting Started with AWS</u> 

- <u>AWS Identity & Access Management (AWS IAM)</u> 

- <u>Amazon EC2 – Basics</u> 

- <u>Amazon EC2 – Associate</u> 

- <u>Amazon EC2 – Instance Storage</u> 

- <u>High Availability & Scalability</u> 

- <u>RDS, Aurora & ElastiCache</u> 

- <u>Amazon Route 53</u> 

- <u>Classic Solutions Architecture</u> 

- <u>Amazon S3</u> 

© Stephane Maarek 

#### Table of Contents 

- <u>Amazon S3 – Advanced</u> 

- <u>Amazon S3 – Security</u> 

- <u>CloudFront & Global Accelerator</u> 

- <u>AWS Storage Extras</u> 

- <u>AWS Integration & Messaging</u> 

- <u>Containers on AWS</u> 

- <u>Serverless Overview</u> 

- <u>Serverless Architectures</u> 

- <u>Databases in AWS</u> 

- <u>Data & Analytics</u> 

© Stephane Maarek 

#### Table of Contents 

- <u>Machine Learning</u> 

- <u>AWS Monitoring, Audit & Performance</u> 

- <u>Advanced Identity in AWS</u> 

- <u>AWS Security & Encryption</u> 

- <u>Amazon VPC</u> 

- <u>Disaster Recovery & Migrations</u> 

- <u>More Solutions Architecture</u> 

- <u>Other Services</u> 

- <u>White Papers & Architectures</u> 

- <u>Exam Preparation</u> 

- <u>Congratulations</u> 

© Stephane Maarek 

### AWS Certified Solutions Architect Associate Course SAA-C03 

© Stephane Maarek 

Welcome! We’re starting in 5 minutes 



<!-- Start of picture text -->
~~<br><!-- End of picture text -->

- We’re going to prepare for the Solutions Architect exam - SAA-C03 

- It’s a challenging certification, so this course will be long and interesting 

- Basic IT knowledge is necessary 

- This course contains videos… 

   - From the Cloud Practitioner, Developer and SysOps course - shared knowledge 

   - Specific to the Solutions Architect exam - exciting ones on architecture! 

- We will cover over 30 AWS services 

- AWS / IT Beginners welcome! (but take your time, it’s not a race) 

© Stephane Maarek 

My SAA-C03 certification: 96.1% 



<!-- Start of picture text -->
AWS Certified Solutions Architect - Associate<br>Notice of Exam Results<br><!-- End of picture text -->

© Stephane Maarek > 

#### About me 

- I’m Stephane! 

- Worked as in IT consultant and AWS Solutions Architect, Developer & SysOps 

- Worked with AWS many years: built websites, apps, streaming platforms 

- Veteran Instructor on AWS (Certifications, CloudFormation, Lambda, EC2…) 

- You can find me on 

   - GitHub: https://github.com/simplesteph ~~<u>OO</u>~~ 

   - • LinkedIn: https://www.linkedin.com/in/stephanemaarek ~~<u>EE</u>~~ 

   - • Medium: https://medium.com/@stephane.maarek ~~<u>EE</u>~~ 

   - • Twitter: https://twitter.com/stephanemaarek 



<!-- Start of picture text -->
% 4.7 Instructor Rating<br>R 473,642 Reviews<br>@. 1,553,489 Students<br>oy pp iZ © 39Courses<br><!-- End of picture text -->

© Stephane Maarek 

#### What’s AWS? 

- AWS (Amazon Web Services) is a Cloud Provider 



<!-- Start of picture text -->
~~<br><!-- End of picture text -->

- <u>on</u> 

- • They provide you with servers and services that you can use <u>demand and scale easily</u> 

- AWS has revolutionized IT over time 

- AWS powers some of the biggest websites in the world 

   - Amazon.com 

   - Netflix 

© Stephane Maarek 

What we’ll learn in this course (and more!) 



Amazon EC2 



**Amazon ECR** 



**Amazon ECS** 



**AWS Elastic Beanstalk** 





**AWS Auto Scaling Lambda** 



**IAM** 





**Amazon AWS KMS S3** 

















**Amazon Amazon Amazon SES RDS Aurora** 

**Amazon DynamoDB** 

**Amazon ElastiCache** 

**Amazon SQS** 

**Amazon AWS Step Functions SNS** 





**Amazon AWS CloudWatch CloudFormation** 









**AWS Amazon API Elastic Load Amazon CloudTrail Gateway Balancing CloudFront** 





**Amazon Amazon Kinesis Route 53** 

© Stephane Maarek 

#### Navigating the AWS spaghetti bowl 



© Stephane Maarek 

### Udemy Tips 

© Stephane Maarek 

### Getting started with AWS 

© Stephane Maarek 

es 

#### AWS Cloud History 

2002: 2004: 2007: Internally Launched publicly Launched in launched with SQS Europe 



2003: 2006: Amazon infrastructure is Re-launched one of their core strength. publicly with Idea to market SQS, S3 & EC2 

© Stephane Maarek SE 

#### AWS Cloud Number Facts 

- In 2019, AWS had $35.02 billion in annual revenue 

- AWS accounts for 47% of the market in 2019 (Microsoft is 2nd with 22%) 

- Pioneer and Leader of the AWS Cloud Market for the 9th consecutive year 

- Over 1,000,000 active users 



<!-- Start of picture text -->
Figure 1. Magic Quadrant for Cloud Infrastructure asa Service, Worldwide<br>CHALLENGERS LEADERS.<br>‘Amazon Web Services@<br>@ Microsoft<br>@ Google<br>| Alibaba Cloud @ Oracle @<br>5 'M@<br>5<br>3<br>ie<br>Pd<br>fa<br>°<br>2<br>><br>i=<br>aEI NICHE PLAYERS VISIONARIES<br>COMPLETENESS OF VISION ——_—_> As of July 2019 © Gartner, Inc<br>‘Source: Gartner (July 2019)<br><!-- End of picture text -->

**Gartner Magic Quadrant** 

© Stephane Maarek 

#### AWS Cloud Use Cases 

- AWS enables you to build sophisticated, scalable applications 

- Applicable to a diverse set of industries 

- Use cases include 

   - Enterprise IT, Backup & Storage, Big Data analytics 

   - • Website hosting, Mobile & Social Apps • Gaming 







© Stephane Maarek 

#### AWS Global Infrastructure 

- AWS Regions 

- AWS Availability Zones • AWS Data Centers • AWS Edge Locations / Points of Presence 

- • <u>https://infrastructure.aws/</u> 



<!-- Start of picture text -->
N. California<br>Jas<br>DISCOVER London<br>[okie Fs Mian]<br>HOW WE DO IT GovCloud (US-East) e_Paris_|<br>;<br>Pvaiabiy Zones<br>ane<br><!-- End of picture text -->

© Stephane Maarek 

#### AWS Regions 

- AWS has Regions all around the world 

- Names can be us-east-1, eu-west-3… 

- A region is a cluster of data centers • Most AWS services are region-scoped 



<!-- Start of picture text -->
°<br>8 ° °%60<br>co ° 0° 0 60<br>- °<br>\<br>><br>.<br>f<br>s 4<br>ora‘© coming Soon<br><!-- End of picture text -->

<u>https://aws.amazon.com/about-aws/global-infrastructure/</u> 



<!-- Start of picture text -->
| Us East (N. Virginia) us-east-1<br>US East (Ohio) us-east-2<br>US West (N. California) us-west-1<br>US West (Oregon) us-west-2<br>Africa (Cape Town) af-south-1<br>Asia Pacific (Hong Kong) ap-east-1<br>Asia Pacific (Mumbai) ap-south-1<br>Asia Pacific (Seoul) ap-northeast-2<br>Asia Pacific (Singapore) ap-southeast-1<br>Asia Pacific (Sydney) ap-southeast-2<br>Asia Pacific (Tokyo) ap-northeast-t<br>Canada (Central) ca-central-1<br>Europe (Frankfurt) eu-central-1<br>Europe (Ireland) eu-west-1<br>Europe (London) eu-west-2<br>Europe (Paris) eu-west-3<br>Europe (Stockholm) eu-north-1<br>Middle East (Bahrain) me-south-1<br>South America (Sao Paulo) sa-east-1<br><!-- End of picture text -->

© Stephane Maarek 

#### How to choose an AWS Region? 

If you need to launch a new application, where should you do it? 



<!-- Start of picture text -->
? te ? #<br>? ?<br><!-- End of picture text -->

- Compliance with data governance and legal requirements: data never leaves a region without your explicit permission 

- Proximity to customers: reduced latency 

- Available services within a Region: new services and new features aren’t available in every Region 

- • Pricing: pricing varies region to region and is transparent in the service pricing page 

© Stephane Maarek 

#### AWS Availability Zones 

- Each region has many availability zones (usually 3, min is 3, max is 6). Example: • ap-southeast-2a 

AWS Region Sydney: ap-southeast-2 

- ap-southeast-2b 

ap-southeast-2a ap-southeast-2b ap-southeast-2c 

   - ap-southeast-2c 

- Each availability zone (AZ) is one or more discrete data centers with redundant power, networking, and connectivity 

- They’re separate from each other, so that they’re isolated from disasters 









- They’re connected with high bandwidth, ultra-low latency networking 

- © Stephane Maarek 

- I'”TS Ol <mark>E</mark> ns 

#### AWS Points of Presence (Edge Locations) 

- Amazon has 400+ Points of Presence (400+ Edge Locations & 10+ Regional Caches) in 90+ cities across 40+ countries 

- Content is delivered to end users with lower latency 

<u>https://aws.amazon.com/cloudfront/features/</u> 

© Stephane Maarek 

#### Tour of the AWS Console 



- AWS has Global Services: 

   - Identity and Access Management (IAM) 

   - Route 53 (DNS service) 

   - CloudFront (Content Delivery Network) 



   - WAF (Web Application Firewall) 

- Most AWS services are Region-scoped : 

   - Amazon EC2 (Infrastructure as a Service) 

   - Elastic Beanstalk (Platform as a Service) 

   - Lambda (Function as a Service) 



- Rekognition (Software as a Service) 

• Region Table: <u>https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services</u> © Stephane Maarek I ~~E~~ '”TS Ol ~~ns~~ 

~~ns~~ 

### AWS Identity and Access Management (AWS IAM) 

© Stephane Maarek 

IAM: Users & Groups • IAM  = Identity and Access Management, Global service • Root account created by default, shouldn’t be used or shared • Users are people within your organization, and can be grouped • Groups only contain users, not other groups • Users don’t have to belong to a group, and user can belong to multiple groups **Group: Developers Group: Operations Group Audit Team Alice Bob Charles David Edward Fred** © Stephane Maarek 6<sup>af]</sup> [aa Ja IE'”TS Ol ns 

#### IAM: Permissions 

- Users or Groups can be assigned JSON documents called policies 

- These policies define the permissions of the users 

- In AWS you apply the least privilege principle : don’t give more permissions than a user needs 

{ "Version": "2012-10-17", "Statement": [ { "Effect": "Allow", "Action": "ec2:Describe*", "Resource": "*" }, { "Effect": "Allow", "Action": "elasticloadbalancing:Describe*", "Resource": "*" }, { "Effect": "Allow", "Action": [ "cloudwatch:ListMetrics", "cloudwatch:GetMetricStatistics", "cloudwatch:Describe*" ], "Resource": "*" } ] } 

© Stephane Maarek 

|IAM Policies<br>**Developers**<br>o|inheritance<br>**Audit Team**<br>|ld|**Operations**<br>s|A|**FOR DISTRIBUTION © Stephane Maarekwww.da**<br>**inline**<br>|
|---|---|---|---|---|---|
|© Stephane Maarek<br>**Alice**<br>**Bob**<br><br>I|**Charles**<br> <br><br>'”TSOl|**David**<br><br>|**Edward**<br> <br><br>|**Fred**<br> <br><br>n|**tacumulus.com**<br><br><br>s|



#### IAM Policies Structure 

- Consists of 

   - Version: policy language version, always include “2012-1017” 

   - Id: an identifier for the policy (optional) 

   - Statement: one or more individual statements (required) 

- Statements consists of 

   - Sid: an identifier for the statement (optional) 

   - Effect: whether the statement allows or denies access (Allow, Deny) 

   - Principal: account/user/role to which this policy applied to 

   - Action: list of actions this policy allows or denies 

   - Resource: list of resources to which the actions applied to 

   - Condition: conditions for when this policy is in effect (optional) 



<!-- Start of picture text -->
{<br>"Version": "2012-10-17",<br>"Id": "S3-Ac t-Permissions",<br>"Statement": [<br>{<br>"Sid": "1",<br>"Effect": "Allow",<br>"Principal": {<br>"AWS": ["“arn:aws:iam: :123456789012 ty<br>js<br>"Action": [<br>iB<br>"Resource": ["“arn:aws:s3::: et/*"]<br>}<br>]<br>}<br><!-- End of picture text -->

© Stephane Maarek 

#### IAM – Password Policy 

- Strong passwords = higher security for your account • In AWS, you can setup a password policy: • Set a minimum password length • Require specific character types: • including uppercase letters • lowercase letters • numbers • non-alphanumeric characters 

- • Allow all IAM users to change their own passwords • Require users to change their password after some time (password expiration) • Prevent password re-use 

© Stephane Maarek 

#### Multi Factor Authentication - MFA 



- Users have access to your account and can possibly change configurations or delete resources in your AWS account 

- You want to protect your Root Accounts and IAM users 

- MFA = password _you know_ + security device _you own_ 

> **Password** + => **Successful login Alice** 

- Main benefit of MFA: <u>if a password is stolen or hacked, the account is not compromised</u> 

© Stephane Maarek ~~IE~~ '”TS Ol ns 

#### MFA devices options in AWS 

###### **Virtual MFA device** 

###### **Universal 2nd Factor (U2F) Security Key** 



<!-- Start of picture text -->
or 208<br>222 104<br>ce<br>140 359<br>‘<br>364 218<br>enki ctemb «<br><!-- End of picture text -->



<!-- Start of picture text -->
«amazon<br>204009<br>eMo ge<br>os aioe<br>mes «<br><!-- End of picture text -->



**Authy** (multi-device) 

**Google Authenticator Authy** (phone only) (multi-device) Support for multiple tokens on a single device. 

**YubiKey** by Yubico (3<sup>rd</sup> party) Support for multiple root and IAM users using a single security key 

© Stephane Maarek 

#### MFA devices options in AWS 

###### **Hardware Key Fob MFA Device** 

**Hardware Key Fob MFA Device for AWS GovCloud (US)** 





Provided by Gemalto (3<sup>rd</sup> party) 

Provided by SurePassID (3<sup>rd</sup> party) 

© Stephane Maarek SE 

es 

#### How can users access AWS ? 



<!-- Start of picture text -->
ex<br><!-- End of picture text -->

- To access AWS, you have three options: 

   - AWS Management Console (protected by password + MFA) 

   - AWS Command Line Interface (CLI): protected by access keys 

   - AWS Software Developer Kit (SDK) - for code: protected by access keys 

- Access Keys are generated through the AWS Console 

- Users manage their own access keys 

- <u>Access Keys are secret, just like a password. Don’t share them</u> 

• Access Key ID ~= username • Secret Access Key ~= password © Stephane Maarek IE'”TS Ol ns 

#### Example (Fake) Access Keys 



<!-- Start of picture text -->
Access keys<br>Use access keys to make secure REST or HTTP Query protocol requests to AWS service APIs. For your protection, you should never share your secret keys with<br>anyone. As a best practice, we recommend frequent key rotation. Learn more<br>Create access key<br>Access key ID Created Last used Status<br>AKIASK4E37PV4TU3RD6C 2020-05-25 15:13 UTC+0100 N/A Active | Make inactive x<br><!-- End of picture text -->

- Access key ID: AKIASK4E37PV4983d6C 

- Secret Access Key: AZPN3zojWozWCndIjhB0Unh8239a1bzbzO5fqqkZq • <u>Remember: don’t share your access keys</u> 

© Stephane Maarek 

#### What’s the AWS CLI? 

- A tool that enables you to interact with AWS services using commands in your command-line shell 

- Direct access to the public APIs of AWS services 

- You can develop scripts to manage your resources 

- It’s open-source <u>https://github.com/aws/aws-cli</u> 

- Alternative to using AWS Management Console 



<!-- Start of picture text -->
s3 cp myfile.txt s3://ccp-mybucket/myfile.txt<br>upload: ./myfile.txt to s3://ccp-mybucket/myfile.txt<br>s3 ls s3://ccp-mybucket<br>a on O3°22.52 @ myfile.txt<br><!-- End of picture text -->

© Stephane Maarek 

#### What’s the AWS SDK? 



- AWS Software Development Kit (AWS SDK) 

- Language-specific APIs (set of libraries) 

- Enables you to access and manage AWS services programmatically 

AWS SDK 

- Embedded within your application 

- Supports 

   - SDKs (JavaScript, Python, PHP, .NET, Ruby, Java, Go, Node.js, C++) 

   - Mobile SDKs (Android, iOS, …) 

Your Application 

• IoT Device SDKs (Embedded C, Arduino, …) • Example: AWS CLI is built on AWS SDK for Python © Stephane Maarek SE’”Oh es 

#### IAM Roles for Services 

- Some AWS service will need to perform actions on your behalf 

- • To do so, we will assign permissions to AWS services with IAM Roles 

- Common roles: 

   - EC2 Instance Roles 

   - Lambda Function Roles 

   - Roles for CloudFormation 



<!-- Start of picture text -->
IAM Role<br>EC2 Instance<br>(virtual server)<br>Access AWS<br><!-- End of picture text -->



<!-- Start of picture text -->
=<br><!-- End of picture text -->

© Stephane Maarek 

#### IAM Security Tools 

- IAM Credentials Report (account-level) 

   - a report that lists all your account's users and the status of their various credentials 

- IAM Access Advisor (user-level) 

   - Access advisor shows the service permissions granted to a user and when those services were last accessed. 

   - You can use this information to revise your policies. 

© Stephane Maarek 

#### IAM Guidelines & Best Practices 



- Don’t use the root account except for AWS account setup 

- One physical user = One AWS user 

- Assign users to groups and assign permissions to groups 

- Create a strong password policy 

- Use and enforce the use of Multi Factor Authentication (MFA) 

- Create and use Roles for giving permissions to AWS services 

- Use Access Keys for Programmatic Access (CLI / SDK) 

• Audit permissions of your account using IAM Credentials Report & IAM Access Advisor • <u>Never share IAM users & Access Keys</u> © Stephane Maarek ~~Oee~~ e 

#### IAM Section – Summary 



• Users: mapped to a physical user, has a password for AWS Console 

- Groups: contains users only 

- Policies: JSON document that outlines permissions for users or groups 

- Roles: for EC2 instances or AWS services 

- Security: MFA + Password Policy 

- AWS CLI: manage your AWS services using the command-line 

- AWS SDK: manage your AWS services using a programming language 

- Access Keys: access AWS using the CLI or SDK 

- Audit: IAM Credential Reports & IAM Access Advisor 

© Stephane Maarek 

Amazon EC2 – Basics 

© Stephane Maarek 

#### Amazon EC2 



- EC2 is one of the most popular of AWS’ offering 

- EC2 = Elastic Compute Cloud = Infrastructure as a Service 

- It mainly consists in the capability of : 

   - Renting virtual machines (EC2) 

   - Storing data on virtual drives (EBS) 

   - Distributing load across machines (ELB) 

   - Scaling the services using an auto-scaling group (ASG) 

- Knowing EC2 is fundamental to understand how the Cloud works 

© Stephane Maarek 

EC2 sizing & configuration options 

- Operating System ( OS ): Linux, Windows or Mac OS • How much compute power & cores ( CPU ) • How much random-access memory ( RAM ) • How much storage space: • Network-attached ( EBS & EFS ) • hardware ( EC2 Instance Store ) 

- • Network card: speed of the card, Public IP address • Firewall rules: security group 

- Bootstrap script (configure at first launch): EC2 User Data 

© Stephane Maarek 

#### EC2 User Data 

- It is possible to bootstrap our instances using an EC2 User data script. 

- bootstrapping means launching commands when a machine starts 

- That script is only run once at the instance first start 

- EC2 user data is used to automate boot tasks such as: 

   - Installing updates 

   - Installing software 

   - Downloading common files from the internet 

   - Anything you can think of 

- The EC2 User Data Script runs with the root user 

© Stephane Maarek 

Hands-On: Launching an EC2 Instance running Linux 

- We’ll be launching our first virtual server using the AWS Console 

- We’ll get a first high-level approach to the various parameters 

- We’ll see that our web server is launched using EC2 user data 

- We’ll learn how to start / stop / terminate our instance. 

© Stephane Maarek 

|EC2 Instance Types - Overview|
|---|
|•You can use different types of EC2 instances that are optimised for<br>different use cases(<br>https://aws.amazon.com/ec2/instance-types/)<br>•AWS has the following naming convention:<br>General Purpo|
|m5.2xlarge<br>Compute Opti<br>Memory Opti|
|•m: instance class<br>•5: generation (AWS improves them over time)<br>•2xlarge: size within the instance class<br>Accelerated C<br>HPC Optimize|



© Stephane Maarek a 

EC2 Instance Types – General Purpose 

- Great for a diversity of workloads such as web servers or code repositories 

- Balance between: 

   - Compute 

   - Memory 

   - Networking 

- In the course, we will be using the t2.micro which is a General Purpose EC2 instance 



<!-- Start of picture text -->
General Purpose<br>General purpose instances provide a balance of compute, memory and networking resources, and can be used for a variety of diverse<br>workloads. These instances are ideal for applications that use these resources in equal proportions such as web servers and code<br>repositories.<br>Mac T4g 3 T3a T2 M6g M5 M5a M5n M5zn M4 Al<br><!-- End of picture text -->

- _this list will evolve over time, please check the AWS website for the latest information_ 

© Stephane Maarek 

EC2 Instance Types – Compute Optimized 

- Great for compute-intensive tasks that require high performance processors: 

   - Batch processing workloads 

   - Media transcoding 

   - High performance web servers 

   - • High performance computing (HPC) • Scientific modeling & machine learning • Dedicated gaming servers 



<!-- Start of picture text -->
Compute Optimized<br>Compute Optimized instances are ideal for compute bound applications that benefit from high performance processors. Instances<br>belonging to this family are well suited for batch processing workloads, media transcoding, high performance web servers, high<br>performance computing (HPC), scientific modeling, dedicated gaming servers and ad server engines, machine learning inference and<br>other compute intensive applications.<br>Cég Cégn cs cSa csn C4<br><!-- End of picture text -->

- _this list will evolve over time, please check the AWS website for the latest information_ 

© Stephane Maarek 

EC2 Instance Types – Memory Optimized 

- Fast performance for workloads that process large data sets in memory 

- • Use cases: 

   - High performance, relational/non-relational databases 

   - • Distributed web scale cache stores 

   - In-memory databases optimized for BI (business intelligence) 

   - • Applications performing real-time processing of big unstructured data 



<!-- Start of picture text -->
Memory Optimized<br>Memory optimized instances are designed to deliver fast performance for workloads that process large data sets in memory.<br>R6g RS R5a R5b R5n R4 Xle x1 High Memory zid<br><!-- End of picture text -->

- _this list will evolve over time, please check the AWS website for the latest information_ 

© Stephane Maarek 

EC2 Instance Types – Storage Optimized 

- Great for storage-intensive tasks that require high, sequential read and write access to large data sets on local storage 

- Use cases: 

   - High frequency online transaction processing (OLTP) systems 

   - • Relational & NoSQL databases 

   - Cache for in-memory databases (for example, Redis) 

   - • Data warehousing applications 

   - Distributed file systems 



<!-- Start of picture text -->
Storage Optimized<br>Storage optimized instances are designed for workloads that require high, sequential read and write access to very large data sets on<br>local storage. They are optimized to deliver tens of thousands of low-latency, random I/O operations per second (IOPS) to applications.<br>13 \3en b2 D3 D3en H1<br><!-- End of picture text -->

- _this list will evolve over time, please check the AWS website for the latest information_ 

© Stephane Maarek 

EC2 Instance Types: example 

|Instance|vCPU|Mem (GiB)|Storage|Network<br>Performance|EBS Bandwidth<br>(Mbps)|
|---|---|---|---|---|---|
|t2.micro|1|1|EBS-Only|Low to Moderate||
|t2.xlarge|4|16|EBS-Only|Moderate||
|c5d.4xlarge|16|32|1 x 400 NVMe SSD|Up to 10 Gbps|4,750|
|r5.16xlarge|64|512|EBS Only|20 Gbps|13,600|
|m5.8xlarge|32|128|EBS Only|10 Gbps|6,800|



**t2.micro is part of the AWS free tier (up to 750 hours per month)** 

Great website: https://instances.vantage.sh 

© Stephane Maarek 

es 

#### Introduction to Security Groups 



<!-- Start of picture text -->
• Security Groups are the fundamental of network security in AWS<br>• They control how traffic is allowed into or out of our EC2 Instances.<br>Inbound traffic<br>WWW Outbound traffic EC2 Instance<br>• Security groups only contain   rules<br>Group<br>Security<br><!-- End of picture text -->

- Security groups rules can reference by IP or by security group 

© Stephane Maarek EES 

#### Security Groups Deeper Dive 

- Security groups are acting as a “firewall” on EC2 instances • They regulate: 

   - Access to Ports 

   - Authorised IP ranges – IPv4 and IPv6 

   - • Control of inbound network (from other to the instance) 

   - Control of outbound network (from the instance to other) 

© Stephane Maarek 



<!-- Start of picture text -->
Security Groups<br>Diagram<br>Your Computer - IP XX.XX.XX.XX<br>Security Group 1 Port 22 (authorised port 22)<br>Inbound<br>Filter IP / Port with Rules Port 22 Other computer<br>(not authorised port 22)<br>EC2 Instance<br>IP XX.XX.XX.XX<br>Security Group 1<br>WWW<br>Outbound<br>Any Port<br>Any IP – Any Port<br>Filter IP / Port with Rules<br>NOT FOR DISTRIBUTION © Stephane Maarek www.datacumulus.com<br><!-- End of picture text -->

© Stephane Maarek 

#### Security Groups Good to know 

- Can be attached to multiple instances 

- Locked down to a region / VPC combination 

- Does live “outside” the EC2 – if traffic is blocked the EC2 instance won’t see it 

- It’s good to maintain one separate security group for SSH access 

- If your application is not accessible (time out), then it’s a security group issue 

- If your application gives a “connection refused“ error, then it’s an application error or it’s not launched 

- All inbound traffic is blocked by default 

- All outbound traffic is authorised by default 

© Stephane Maarek 

#### Referencing other security groups Diagram 



<!-- Start of picture text -->
Security<br>EC2 Instance<br>Port 123 Group 2<br>IP XX.XX.XX.XX<br>(attached)<br>Security Group 1<br>Security<br>EC2 Instance Inbound EC2 Instance<br>Port 123 Group 1<br>IP XX.XX.XX.XX<br>Authorising Security Group 1 IP XX.XX.XX.XX<br>(attached)<br>Authorising Security Group 2<br>Security<br>EC2 Instance<br>Port 123     Group 3<br>IP XX.XX.XX.XX<br>(attached)<br><!-- End of picture text -->

© Stephane Maarek 

#### Classic Ports to know 

- 22 = SSH (Secure Shell) - log into a Linux instance 

- 21 = FTP (File Transfer Protocol) – upload files into a file share • 22 = SFTP (Secure File Transfer Protocol) – upload files using SSH 

- 80 = HTTP – access unsecured websites 

- 443 = HTTPS – access secured websites 

- 3389 = RDP (Remote Desktop Protocol) – log into a Windows instance 

© Stephane Maarek 



<!-- Start of picture text -->
SSH Summary Table<br>EC2 Instance<br>SSH Putty<br>Connect<br>a ee<br>Mac<br>i wv Vv<br>Linux<br>W w Vv<br>Windows < 10<br>| | vv<br>Windows >= 10<br>v w yvy<br>© Stephane Maarek<br>SE ’”- Oh es<br>NOT FOR DISTRIBUTION © Stephane Maarek www.datacumulus.com<br><!-- End of picture text -->

es 

#### Which Lectures to watch 

|• Mac / Linux:|
|---|
|• SSH on Mac/Linux lecture|
|• Windows:|
|• Putty Lecture|
|• If Windows 10:SSH on Windows 10 lecture|
|• All:|
|• EC2 Instance Connect lecture|



© Stephane Maarek 

#### SSH troubleshooting 

- Students have the most problems with SSH 

- If things don’t work… 1. Re-watch the lecture. You may have missed something 2. Read the troubleshooting guide 3. Try EC2 Instance Connect 

- <u>If one method works (SSH, Putty or EC2 Instance Connect) you’re good</u> 

- If no method works, that’s okay, the course won’t use SSH much 

© Stephane Maarek 

How to SSH into your EC2 Instance Linux / Mac OS X 

- We’ll learn how to SSH into your EC2 instance using Linux / Mac 

- SSH is one of the most important function. It allows you to control a remote machine, all using the command line. 



<!-- Start of picture text -->
EC2 Instance<br>WWW<br>Linux<br>Public IP<br>SSH – Port 22<br><!-- End of picture text -->



- We will see how we can configure OpenSSH ~/.ssh/config to facilitate the SSH into our EC2 instances 

© Stephane Maarek 

How to SSH into your EC2 Instance Windows 

- We’ll learn how to SSH into your EC2 instance using Windows 

- SSH is one of the most important function. It allows you to control a remote machine, all using the command line. 



<!-- Start of picture text -->
EC2 Instance<br>WWW<br>Linux<br>Public IP<br>SSH – Port 22<br><!-- End of picture text -->



- We will configure all the required parameters necessary for doing SSH on Windows using the free tool Putty. 

© Stephane Maarek 

#### EC2 Instance Connect 

- Connect to your EC2 instance within your browser 

- No need to use your key file that was downloaded 

- The “magic” is that a temporary key is uploaded onto EC2 by AWS 

- <u>Works only out-of-the-box with Amazon Linux 2</u> 

- Need to make sure the port 22 is still opened! 

© Stephane Maarek 

#### EC2 Instances Purchasing Options 

- On-Demand Instances – short workload, predictable pricing, pay by second 

- Reserved (1 & 3 years) 

   - Reserved Instances – long workloads 

   - Convertible Reserved Instances – long workloads with flexible instances 

- Savings Plans (1 & 3 years) –commitment to an amount of usage, long workload 

- Spot Instances – short workloads, cheap, can lose instances (less reliable) 

- Dedicated Hosts – book an entire physical server, control instance placement 

- Dedicated Instances – no other customers will share your hardware 

- Capacity Reservations – reserve capacity in a specific AZ for any duration 

© Stephane Maarek 

#### EC2 On Demand 

- Pay for what you use: 

   - Linux or Windows - billing per second, after the first minute 

   - All other operating systems - billing per hour 

- Has the highest cost but no upfront payment 

- No long-term commitment 

- Recommended for short-term and un-interrupted workloads , where you can't predict how the application will behave 

© Stephane Maarek 

#### EC2 Reserved Instances 

- Up to 72% discount compared to On-demand 

- You reserve a specific instance attributes (Instance Type, Region, Tenancy, OS) 

- Reservation Period – 1 year (+discount) or 3 years (+++discount) 

- Payment Options – No Upfront (+), Partial Upfront (++), All Upfront (+++) 

- Reserved Instance’s Scope – Regional or Zonal (reserve capacity in an AZ) 

- Recommended for steady-state usage applications (think database) 

- You can buy and sell in the Reserved Instance Marketplace 

- Convertible Reserved Instance 

   - Can change the EC2 instance type, instance family, OS, scope and tenancy 

   - Up to 66% discount 

**<u>Note:</u>** the % discounts are different from the video as AWS change them over time – the exact numbers are not needed for the exam. This is just for illustrative purposes J 

© Stephane Maarek 

#### EC2 Savings Plans 

• Get a discount based on long-term usage (up to 72% - same as RIs) 

- Commit to a certain type of usage ($10/hour for 1 or 3 years) 

- Usage beyond EC2 Savings Plans is billed at the On-Demand price 

- Locked to a specific instance family & AWS region (e.g., M5 in us-east-1) • Flexible across: 

   - Instance Size (e.g., m5.xlarge, m5.2xlarge) 

   - OS (e.g., Linux, Windows) 

   - Tenancy (Host, Dedicated, Default) 

© Stephane Maarek 

#### EC2 Spot Instances 



<!-- Start of picture text -->
re=oO74<br>(0h)<br><!-- End of picture text -->

- Can get a discount of up to 90% compared to On-demand 

- • Instances that you can “lose” at any point of time if your max price is less than the current spot price 

- The MOST cost-efficient instances in AWS 

- Useful for workloads that are resilient to failure 

   - Batch jobs 

   - • Data analysis 

   - Image processing 

   - Any distributed workloads 

   - Workloads with a flexible start and end time 

- Not suitable for critical jobs or databases 

© Stephane Maarek 

#### EC2 Dedicated Hosts 

- A physical server with EC2 instance capacity fully dedicated to your use 

- • Allows you address compliance requirements and use your existing serverbound software licenses (per-socket, per-core, pe—VM software licenses) 

- Purchasing Options: 

   - On-demand – pay per second for active Dedicated Host 

   - • Reserved - 1 or 3 years (No Upfront, Partial Upfront, All Upfront) 

- The most expensive option 

- Useful for software that have complicated licensing model (BYOL – Bring Your Own License) 

- Or for companies that have strong regulatory or compliance needs 

© Stephane Maarek 

#### EC2 Dedicated Instances 

   - Instances run on hardware that’s dedicated to you 

   - • May share hardware with other instances in same account 

- No control over instance placement (can move hardware after Stop / Start) 

- © Stephane Maarek 

- IE '”TS Ol 

ns 

#### EC2 Capacity Reservations 

- Reserve On-Demand instances capacity in a specific AZ for any duration 

- You always have access to EC2 capacity when you need it 

- No time commitment (create/cancel anytime), no billing discounts 

- Combine with Regional Reserved Instances and Savings Plans to benefit from billing discounts 

- You’re charged at On-Demand rate whether you run instances or not 

- Suitable for short-term, uninterrupted workloads that needs to be in a specific AZ 

© Stephane Maarek 

Which purchasing option is right for me? 



- On demand: coming and staying in resort whenever we like, we pay the full price 

- • Reserved: like planning ahead and if we plan to stay for a long time, we may get a good discount. 

- • Savings Plans: pay a certain amount per hour for certain period and stay in any room type (e.g., King, Suite, Sea View, …) 

- Spot instances: the hotel allows people to bid for the empty rooms and the highest bidder keeps the rooms. You can get kicked out at any time 

- Dedicated Hosts: We book an entire building of the resort 

- Capacity Reservations: you book a room for a period with full price even you don’t stay in it 

© Stephane Maarek 

Price Comparison Example – m4.large – us-east-1 

|**Price Type**|**Price (per hour)**|
|---|---|
|On-Demand|$0.10|
|Spot Instance (Spot Price)|$0.038 - $0.039 (up to 61% off)|
|Reserved Instance (1 year)|$0.062 (No Upfront) - $0.058 (All Upfront)|
|Reserved Instance (3 years)|$0.043 (No Upfront) - $0.037 (All Upfront)|
|EC2 Savings Plan (1 year)|$0.062 (No Upfront) - $0.058 (All Upfront)|
|Reserved**Convertible**Instance (1 year)|$0.071 (No Upfront) - $0.066 (All Upfront)|
|Dedicated Host|On-Demand Price|
|Dedicated Host Reservation|Up to 70% off|
|Capacity Reservations|On-Demand Price|



© Stephane Maarek 

#### EC2 Spot Instance Requests 



<!-- Start of picture text -->
re=a4<br>(ch)<br><!-- End of picture text -->

- Can get a discount of up to 90% compared to On-demand 

- Define max spot price and get the instance while current spot price < max • The hourly spot price varies based on offer and capacity 

   - If the current spot price > your max price you can choose to stop or terminate your instance with a 2 minutes grace period. 

- Other strategy: Spot Block 

   - “block” spot instance during a specified time frame (1 to 6 hours) without interruptions 

   - • In rare situations, the instance may be reclaimed 

- Used for batch jobs, data analysis, or workloads that are resilient to failures. 

- Not great for critical jobs or databases 

© Stephane Maarek 

#### EC2 Spot Instances Pricing 

User-defined max price wee eee ee ee ele 

<u>https://console.aws.amazon.com/ec2sp/v1/spot/home?region=us-east-1#</u> 

© Stephane Maarek 

#### How to terminate Spot Instances? 



<!-- Start of picture text -->
start <— Stop<br>(persistent) (persistent)<br>Interrupt<br>(persistent)<br>Spot request<br>Create Maximum price Launch<br>request Desired number of instances instances<br>q Launch specification<br>Request type: one-time | persistent<br>Valid from, Valid until<br>(one-time)<br>Request<br>failed<br><!-- End of picture text -->



<!-- Start of picture text -->
Create<br>request<br>.<br>=<br>persistent<br>i<br>active<br>persistent one-time<br>persistent<br><!-- End of picture text -->

You can only cancel Spot Instance requests that are **open, active, or disabled.** Cancelling a Spot Request does not terminate instances 

You must first cancel a Spot Request, and then terminate the associated Spot Instances 

<u>https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-requests.html</u> 

© Stephane Maarek 

#### Spot Fleets 

- Spot Fleets = set of Spot Instances + (optional) On-Demand Instances 

- The Spot Fleet will try to meet the target capacity with price constraints • Define possible launch pools: instance type (m5.large), OS, Availability Zone • Can have multiple launch pools, so that the fleet can choose 

   - Spot Fleet stops launching instances when reaching capacity or max cost 

- Strategies to allocate Spot Instances: 

   - lowestPrice: from the pool with the lowest price (cost optimization, short workload) 

   - diversified: distributed across all pools (great for availability, long workloads) 

   - capacityOptimized: pool with the optimal capacity for the number of instances 

   - • priceCapacityOptimized (recommended): pools with highest capacity available, then select the pool with the lowest price (best choice for most workloads) 

- <u>Spot Fleets allow us to automatically request Spot Instances with the lowest price</u> 

© Stephane Maarek 

### Amazon EC2 – Associate 

© Stephane Maarek 

#### Private vs Public IP (IPv4) 

- Networking has two sorts of IPs. IPv4 and IPv6: • IPv4: **`1.160.10.240`** 

   - IPv6: **`3ffe:1900:4545:3:200:f8ff:fe21:67cf`** 

- In this course, we will only be using IPv4. 

- IPv4 is still the most common format used online. 

- IPv6 is newer and solves problems for the Internet of Things (IoT). 

- IPv4 allows for 3.7 billion different addresses in the public space 

- IPv4: [0-255].[0-255].[0-255].[0-255]. 

© Stephane Maarek 

#### Private vs Public IP (IPv4) Example 



<!-- Start of picture text -->
Web Server (public): Server (public):<br>79.216.59.75 211.139.37.43<br>_ 7 oS<br>WWW<br>Internet Gateway (public): Internet Gateway (public):<br>149.140.72.10 253.144.139.205<br>Company A Company B<br>Private Network Private Network<br>192.168.0.1/22 192.168.0.1/22<br>:<br><!-- End of picture text -->

© Stephane Maarek 

#### Private vs Public IP (IPv4) Fundamental Differences 

- Public IP: 

   - Public IP means the machine can be identified on the internet (WWW) 

   - Must be unique across the whole web (not two machines can have the same public IP). 

   - Can be geo-located easily 

- Private IP: 

   - Private IP means the machine can only be identified on a private network only 

   - The IP must be unique across the private network 

   - BUT two different private networks (two companies) can have the same IPs. 

   - Machines connect to WWW using a NAT + internet gateway (a proxy) 

   - Only a specified range of IPs can be used as private IP 

© Stephane Maarek 

#### Elastic IPs 

- When you stop and then start an EC2 instance, it can change its public IP. 

- If you need to have a fixed public IP for your instance, you need an Elastic IP 

- An Elastic IP is a public IPv4 IP you own as long as you don’t delete it 

- You can attach it to one instance at a time 

© Stephane Maarek 

#### Elastic IP 

- With an Elastic IP address, you can mask the failure of an instance or software by rapidly remapping the address to another instance in your account. 

- You can only have 5 Elastic IP in your account (you can ask AWS to increase that). 

- Overall, try to avoid using Elastic IP: 

   - They often reflect poor architectural decisions 

   - Instead, use a random public IP and register a DNS name to it 

   - Or, as we’ll see later, use a Load Balancer and don’t use a public IP 

© Stephane Maarek 

- Private vs Public IP (IPv4) In AWS EC2 – Hands On • By default, your EC2 machine comes with: • A private IP for the internal AWS Network • A public IP, for the WWW. 

- When we are doing SSH into our EC2 machines: • We can’t use a private IP, because we are not in the same network • We can only use the public IP. 

- If your machine is stopped and then started, the public IP can change 

© Stephane Maarek 

#### Placement Groups 

- Sometimes you want control over the EC2 Instance placement strategy 

- That strategy can be defined using placement groups 

- When you create a placement group, you specify one of the following strategies for the group: 

   - _Cluster_ —clusters instances into a low-latency group in a single Availability Zone 

   - • _Spread_ —spreads instances across underlying hardware (max 7 instances per group per AZ) 

   - _Partition_ —spreads instances across many different partitions (which rely on different sets of racks) within an AZ. Scales to 100s of EC2 instances per group (Hadoop, Cassandra, Kafka) 

© Stephane Maarek 

#### Placement Groups Cluster 



<!-- Start of picture text -->
EC2 EC2 EC2<br>Placement group<br>Cluster<br>Same AZ<br>Low latency<br>10 Gbps network<br>EC2 EC2 EC2<br><!-- End of picture text -->

- Pros: Great network (10 Gbps bandwidth between instances with Enhanced Networking enabled - recommended) 

- • Cons: If the AZ fails, all instances fails at the same time 

- Use case: 

   - Big Data job that needs to complete fast 

   - Application that needs extremely low latency and high network throughput 

© Stephane Maarek 

#### Placement Groups Spread 

Us-east-1a 

###### Us-east-1b 



<!-- Start of picture text -->
Us-east-1c<br><!-- End of picture text -->

- Pros: 

   - Can span across Availability Zones (AZ) 



<!-- Start of picture text -->
EC2<br><!-- End of picture text -->



<!-- Start of picture text -->
EC2<br><!-- End of picture text -->



<!-- Start of picture text -->
EC2<br><!-- End of picture text -->

Hardware 1 

Hardware 3 

Hardware 5 



<!-- Start of picture text -->
EC2 EC2 EC2<br>Hardware 2 Hardware 4 Hardware 6<br><!-- End of picture text -->

   - Reduced risk is simultaneous failure 

   - EC2 Instances are on different physical hardware 

- Cons: 

   - Limited to 7 instances per AZ per placement group 

- Use case: 

   - Application that needs to maximize high availability 

   - Critical Applications where each instance must be isolated from failure from each other 

© Stephane Maarek 

#### Placements Groups Partition 



<!-- Start of picture text -->
us-east-1a us-east-1b<br>EC2 EC2 EC2<br>EC2 EC2 EC2<br>EC2 EC2 EC2<br>EC2 EC2 EC2<br>Partition 1 Partition 2 Partition 3<br><!-- End of picture text -->

- Up to 7 partitions per AZ 

- • Can span across multiple AZs in the same region 

- Up to 100s of EC2 instances 

- The instances in a partition do not share racks with the instances in the other partitions 

- A partition failure can affect many EC2 but won’t affect other partitions 

- EC2 instances get access to the partition information as metadata 

- <u>Use cases: HDFS, HBase, Cassandra, Kafka</u> 

© Stephane Maarek 

#### Elastic Network Interfaces (ENI) 

- Logical component in a VPC that represents a virtual network card 

- The ENI can have the following attributes: 

   - Primary private IPv4, one or more secondary IPv4 

   - One Elastic IP (IPv4) per private IPv4 

   - One Public IPv4 

   - One or more security groups 

   - A MAC address 

- You can create ENI independently and attach them on the fly (move them) on EC2 instances for failover 

Availability Zone Eth0 – primary ENI 192.168.0.31 **EC2** Eth1 – secondary ENI 192.168.0.42 **Can be moved** Eth0 – primary ENI **EC2** 



- Bound to a specific availability zone (AZ) 

© Stephane Maarek 

#### EC2 Hibernate 

- We know we can stop, terminate instances 

   - Stop – the data on disk (EBS) is kept intact in the next start 

   - Terminate – any EBS volumes (root) also set-up to be destroyed is lost 

- On start, the following happens: 

   - First start: the OS boots & the EC2 User Data script is run 

   - Following starts: the OS boots up 

   - Then your application starts, caches get warmed up, and that can take time! 

© Stephane Maarek 

#### EC2 Hibernate 

- Introducing EC2 Hibernate : 

   - The in-memory (RAM) state is preserved 

   - The instance boot is much faster! (the OS is not stopped / restarted) 

   - Under the hood: the RAM state is written to a file in the root EBS volume 

   - The root EBS volume must be encrypted 

- Use cases: 

   - Long-running processing 

   - Saving the RAM state 

   - Services that take time to initialize 

###### EC2 Instance 



<!-- Start of picture text -->
Running<br>RAM<br>Root EBS Volume<br>(Encrypted)<br>Hibernate<br>Stopping<br>RAM<br>RAM<br>Shutdown<br>Hibernation<br>Stopped<br>RAM<br>Start<br>Running<br>RAM<br>NOT FOR DISTRIBUTION © Stephane Maarek www.datacumulus.com<br><!-- End of picture text -->

© Stephane Maarek 

#### EC2 Hibernate – Good to know 

- Supported Instance Families – C3, C4, C5, I3, M3, M4, R3, R4, T2, T3, … 

- Instance RAM Size – must be less than 150 GB. 

- Instance Size – not supported for bare metal instances. 

- AMI – Amazon Linux 2, Linux AMI, Ubuntu, RHEL, CentOS & Windows… 

- Root Volume – must be EBS, encrypted, not instance store, and large 

- Available for On-Demand , Reserved and Spot Instances 

- An instance can NOT be hibernated more than 60 days 

© Stephane Maarek 

Amazon EC2 – Instance Storage 

© Stephane Maarek 

#### What’s an EBS Volume? 



- An EBS (Elastic Block Store) Volume is a network drive you can attach to your instances while they run 

- It allows your instances to persist data, even after their termination 

- They can only be mounted to one instance at a time (at the CCP level) 

- They are bound to a specific availability zone 

- Analogy: Think of them as a “network USB stick” 

- Free tier: 30 GB of free EBS storage of type General Purpose (SSD) or Magnetic per month 

© Stephane Maarek 

#### EBS Volume 

- It’s a network drive (i.e. not a physical drive) 

   - It uses the network to communicate the instance, which means there might be a bit of latency 

   - • It can be detached from an EC2 instance and attached to another one quickly 

- It’s locked to an Availability Zone (AZ) 

   - An EBS Volume in us-east-1a cannot be attached to us-east-1b 

   - To move a volume across, you first need to snapshot it 

- Have a provisioned capacity (size in GBs, and IOPS) • You get billed for all the provisioned capacity 

   - You can increase the capacity of the drive over time 

© Stephane Maarek 

#### EBS Volume - Example 



<!-- Start of picture text -->
US-EAST-1A US-EAST-1B<br>‘a<br>L] Oh Ld<br>EBS EBS EBS EBS EBS<br>(10 GB) (100 GB) (50 GB) (50 GB) (10 GB)<br>unattached<br>IE '”TS Ol ns<br>NOT FOR DISTRIBUTION © Stephane Maarek www.datacumulus.com<br><!-- End of picture text -->

© Stephane Maarek IE '”TS Ol 

#### EBS – Delete on Termination attribute 



<!-- Start of picture text -->
Volume Type (i) Device (i) Snapshot (i) Size (GiB) (i) Volume Type (i) 1OPs (i) Throughput(pie) TerminationDeleteon @ cryption (i)<br>Root /dev/xvda snap-09f18f682fd23a1b1 General Purpose SSD (gp2) v] 100/3000 NA Nbt Encrypted ~<br>General Purpose SS0(@52)») 100/000 N/A a sbreneyptes +) @<br>Add New Volume<br><!-- End of picture text -->

- Controls the EBS behaviour when an EC2 instance terminates 

   - By default, the root EBS volume is deleted (attribute enabled) 

   - By default, any other attached EBS volume is not deleted (attribute disabled) 

- This can be controlled by the AWS console / AWS CLI 

- Use case: preserve root volume when instance is terminated 

© Stephane Maarek 

#### EBS Snapshots 

- Make a backup (snapshot) of your EBS volume at a point in time 

- Not necessary to detach volume to do snapshot, but recommended 



<!-- Start of picture text -->
• Can copy snapshots across AZ or Region<br>US-EAST-1A US-EAST-1B<br>EBS Snapshot<br>oe<br>snapshot restore<br>EBS EBS<br>(50 GB) (50 GB)<br>A | 8 A<br><!-- End of picture text -->

© Stephane Maarek IE '”TS Ol 

ns 

#### EBS Snapshots Features 

- EBS Snapshot Archive 

   - Move a Snapshot to an ”archive tier” that is 75% cheaper 

   - Takes within 24 to 72 hours for restoring the archive 

**EBS Snapshot Archive** 

**EBS Snapshot** 

archive Se & 

• Recycle Bin for EBS Snapshots **EBS Snapshot Recycle Bin** • Setup rules to retain deleted snapshots so you can recover them after an accidental deletion delete • Specify retention (from 1 day to 1 year) fis" • Fast Snapshot Restore (FSR) • Force full initialization of snapshot to have no latency on the first use ($$$) © Stephane Maarek IE'”TS Ol ns 

es 

#### AMI Overview 



- AMI = Amazon Machine Image 

- AMI are a customization of an EC2 instance 

   - You add your own software, configuration, operating system, monitoring… 

   - Faster boot / configuration time because all your software is pre-packaged 

- AMI are built for a specific region (and can be copied across regions) 

- You can launch EC2 instances from: 

   - A Public AMI: AWS provided 

   - Your own AMI: you make and maintain them yourself 

   - An AWS Marketplace AMI: an AMI someone else made (and potentially sells) 

© Stephane Maarek EES 



<!-- Start of picture text -->
AMI Process (from an EC2 instance)<br>• Start an EC2 instance and customize it<br>• Stop the instance (for data integrity)<br>• Build an AMI – this will also create EBS snapshots<br>• Launch instances from other AMIs<br>Custom AMI<br>US-EAST-1A US-EAST-1B<br>Launch<br>Create AMI from AMI<br>oO )<br>®@ oO<br>© Stephane Maarek NOT FOR DISTRIBUTION © Stephane Maarek www.datacumulus.com<br><!-- End of picture text -->

es 

#### EC2 Instance Store 



<!-- Start of picture text -->
co<br><!-- End of picture text -->

- EBS volumes are network drives with good but “limited” performance • <u>If you need a high-performance hardware disk, use EC2 Instance Store</u> 

- Better I/O performance 

- EC2 Instance Store lose their storage if they’re stopped (ephemeral) 

- Good for buffer / cache / scratch data / temporary content 

- Risk of data loss if hardware fails 

- Backups and Replication are your responsibility 

© Stephane Maarek EES 

#### Local EC2 Instance Store 

###### **Very high IOPS** 



<!-- Start of picture text -->
Instance Size 100% Random Read IOPS Write lIOPS<br>i3.large* 100,125 35,000<br>i3.xlarge* 206,250 70,000<br>i3.2xLarge 412,500 180,000<br>13.4xLarge 825,000 360,000<br>13.8xLarge 1.65 million 720,000<br>i13.16xLarge 3.3 million 1.4 million<br>i3.metal 3.3 million 1.4 million<br>i3en.Large* 42,500 32,500<br>i3en.xLarge* 85,000 65,000<br>i3en.2xlarge* 170,000 130,000<br>i3en.3xlarge 250,000 200,000<br>i3en.6xLarge 500,000 400,000<br>i3en.12xLarge 1 million 800,000<br>i3en.24xLarge 2 million 1.6 million<br>i3en.metal 2 million 1.6 million<br><!-- End of picture text -->

© Stephane Maarek 

#### EBS Volume Types 

- EBS Volumes come in 6 types 

   - gp2 / gp3 (SSD): General purpose SSD volume that balances price and performance for a wide variety of workloads 

   - io1 / io2 Block Express (SSD): Highest-performance SSD volume for mission-critical low-latency or high-throughput workloads 

   - st1 (HDD): Low cost HDD volume designed for frequently accessed, throughputintensive workloads 

   - sc1 (HDD): Lowest cost HDD volume designed for less frequently accessed workloads 

- EBS Volumes are characterized in Size | Throughput | IOPS (I/O Ops Per Sec) 

- When in doubt always consult the AWS documentation – it’s good! 

- Only gp2/gp3 and io1/io2 Block Express can be used as boot volumes 

© Stephane Maarek 

#### EBS Volume Types Use cases General Purpose SSD 

- Cost effective storage, low-latency 

- System boot volumes, Virtual desktops, Development and test environments 

- 1 GiB - 16 TiB 

- gp3: 

   - Baseline of 3,000 IOPS and throughput of 125 MiB/s 

   - Can increase IOPS up to 16,000 and throughput up to 1000 MiB/s independently 

- gp2: 

   - Small gp2 volumes can burst IOPS to 3,000 

   - Size of the volume and IOPS are linked, max IOPS is 16,000 

   - 3 IOPS per GB, means at 5,334 GB we are at the max IOPS 

© Stephane Maarek 

EBS Volume Types Use cases Provisioned IOPS (PIOPS) SSD 

• Critical business applications with sustained IOPS performance • Or applications that need more than 16,000 IOPS 

• Great for databases workloads (sensitive to storage perf and consistency) • io1 (4 GiB - 16 TiB): • Max PIOPS: 64,000 for Nitro EC2 instances & 32,000 for other • Can increase PIOPS independently from storage size • io2 Block Express (4 GiB – 64 TiB): • Sub-millisecond latency 

• Max PIOPS: 256,000 with an IOPS:GiB ratio of 1,000:1 • Supports EBS Multi-attach 

© Stephane Maarek 

- EBS Volume Types Use cases Hard Disk Drives (HDD) • Cannot be a boot volume • 125 GiB to 16 TiB • Throughput Optimized HDD (st1) • Big Data, Data Warehouses, Log Processing • Max throughput 500 MiB/s – max IOPS 500 

- • Cold HDD (sc1): • For data that is infrequently accessed • Scenarios where lowest cost is important • Max throughput 250 MiB/s – max IOPS 250 

© Stephane Maarek 

#### EBS – Volume Types Summary 



<!-- Start of picture text -->
General Purpose Provisioned IOPS SSD volumes<br>SSD volumes<br>Volumetype gp3 gp2 io2 Block Express iol<br>3<br>Durability 99.8% - 99.9% 99,999% durability 99.8% - 99.9%<br>durability (0.1%- (0.001% annual durability (0.1% -<br>0.2% annual failure failure rate) 0.2% annual failure<br>rate) rate)<br>Use cases * Transactional ‘Workloads that + Workloads that<br>workloads require: require sustained<br>+ Virtual desktops sub. 1ops<br>+ Medium-sized, millisecond performance or<br>single-instancedatabases latency 16,000 10PS<br>+ uLowlatency * performanceSustained OPS. 1/0intensive<br>interactive database<br>applications + 64.000More than1OPS or workloads<br>+ Boot volumes 11,000 MiB/s of<br>+ Development ‘throughput<br>and test<br>environments<br>Volume size 1 GiB - 16 TiB GiB - 64 TiB* 4GiB-16TiB<br>Max 1OPS per 16,000 256,000 ° 64,000<br>volume (16<br>KIBO)<br>Max 1000 250 4,000 MiB/s 1,000 miB/s?<br>throughput MiB/s. MiB/siB/s?<br>per volume<br>‘Amazon EBS Not supported Supported<br>Multi-attach<br>NvMe Not supported Supported Not supported<br>reservations<br>Boot volume Supported<br><!-- End of picture text -->



<!-- Start of picture text -->
ThroughputHDD elames Optimized Cold HDD volumes<br>Volume type stl scl<br>Durability 99.8% - 99.9% durability (0.1% - 0.2% annual failure rate)<br>Use cases * Big data * Throughput-oriented storage for<br>+ Data warehouses data that is infrequently<br>+ Log processing accessed<br>* Scenarios where the lowest<br>storage cost is important<br>Volume size 125 GiB - 16 TiB<br>Max IOPS per 500 250<br>volume (1 MiB I/O)<br>Max throughput 500 MiB/s 250 MiB/s<br>per volume<br>,<br>Amazon EBS Multi- Not supported<br>attach<br>Boot volume Not supported<br>A<br>i<br><!-- End of picture text -->

<u>https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-volume-types.html#solid-state-drives</u> 

© Stephane Maarek 

#### EBS Multi-Attach – io1/io2 family 

- Attach the same EBS volume to multiple EC2 instances in the same AZ 

Availability Zone 1 

- Each instance has full read & write permissions to the high-performance volume 

- Use case: 

   - Achieve higher application availability in clustered Linux applications (ex: Teradata) 

   - Applications must manage concurrent write operations 

- Up to 16 EC2 Instances at a time 











<!-- Start of picture text -->
:<br><!-- End of picture text -->

io2 volume with Multi-Attach • Must use a file system that’s cluster-aware (not XFS, EXT4, etc…) © Stephane Maarek es 

#### EBS Encryption 

- When you create an encrypted EBS volume, you get the following: 

   - Data at rest is encrypted inside the volume 

   - All the data in flight moving between the instance and the volume is encrypted 

   - All snapshots are encrypted 

   - All volumes created from the snapshot 

- Encryption and decryption are handled transparently (you have nothing to do) 

- Encryption has a minimal impact on latency 

- EBS Encryption leverages keys from KMS (AES-256) 

- Copying an unencrypted snapshot allows encryption 

- Snapshots of encrypted volumes are encrypted 

© Stephane Maarek 

#### Encryption: encrypt an unencrypted EBS volume 

- Create an EBS snapshot of the volume 

- Encrypt the EBS snapshot ( using copy ) 

- Create new ebs volume from the snapshot ( the volume will also be encrypted ) 

- Now you can attach the encrypted volume to the original instance 

© Stephane Maarek 

#### Amazon EFS – Elastic File System 

- Managed NFS (network file system) that can be mounted on many EC2 

- EFS works with EC2 instances in multi-AZ 

- Highly available, scalable, expensive (3x gp2), pay per use 



<!-- Start of picture text -->
us-east-1a us-east-1b us-east-1c<br>EC2 Instances EC2 Instances EC2 Instances<br>Security Group<br>EFS FileSystem<br>nS<br>© Stephane Maarek<br><!-- End of picture text -->

#### Amazon EFS – Elastic File System 

- Use cases: content management, web serving, data sharing, Wordpress 

- Uses NFSv4.1 protocol 

- Uses security group to control access to EFS 

- Compatible with Linux based AMI (not Windows) 

- Encryption at rest using KMS 

- POSIX file system (~Linux) that has a standard file API 

- File system scales automatically, pay-per-use, no capacity planning! 

© Stephane Maarek 

#### EFS – Performance & Storage Classes 

- EFS Scale 

   - 1000s of concurrent NFS clients, 10 GB+ /s throughput 

   - Grow to Petabyte-scale network file system, automatically 

- Performance Mode (set at EFS creation time) 

   - General Purpose (default) – latency-sensitive use cases (web server, CMS, etc…) 

   - Max I/O – higher latency, throughput, highly parallel (big data, media processing) 

- Throughput Mode 

   - Bursting – 1 TB = 50MiB/s + burst of up to 100MiB/s 

   - Provisioned – set your throughput regardless of storage size, ex: 1 GiB/s for 1 TB storage 

   - Elastic – automatically scales throughput up or down based on your workloads 

      - Up to 3GiB/s for reads and 1GiB/s for writes 

      - Used for unpredictable workloads 

© Stephane Maarek 

#### EFS – Storage Classes 

- Storage Tiers (lifecycle management feature – move file after N days) • Standard: for frequently accessed files • Infrequent access (EFS-IA): cost to retrieve files, lower price to store. Enable EFS-IA with a Lifecycle Policy 

- Availability and durability • Standard: Multi-AZ, great for prod • One Zone: One AZ, great for dev, backup enabled by default, compatible with IA (EFS One Zone-IA) 

- Over 90% in cost savings 





<!-- Start of picture text -->
no access<br>for 60 days<br>EFS Standard<br>move Lifecycle Policy<br>EFS IA<br>Amazon EFS File System<br><!-- End of picture text -->

© Stephane Maarek 

#### EBS vs EFS – Elastic Block Storage 

- EBS volumes… 

   - one instance (except multi-attach io1/io2) 

   - are locked at the Availability Zone (AZ) level 

   - gp2: IO increases if the disk size increases 

|• gp3 & io1: can increase IO independently|
|---|



- To migrate an EBS volume across AZ 

   - Take a snapshot 

   - Restore the snapshot to another AZ 

   - EBS backups use IO and you shouldn’t run them while your application is handling a lot of traffic 

Availability Zone 1 Availability Zone 2 

**EBS** oO Oo 

**EBS EBS** 

snapshot restore • Root EBS Volumes of instances get terminated by default if the EC2 instance ~~—~~ 8 ~~-~~ gets terminated. (you can disable that) **EBS Snapshot** © Stephane Maarek I'”TS Ol ~~E~~ ns 

#### EBS vs EFS – Elastic File System 

- Mounting 100s of instances across AZ • EFS share website files (WordPress) • Only for Linux Instances (POSIX) 

- EFS has a higher price point than EBS 

- Can leverage EFS-IA for cost savings 

- Remember: EFS vs EBS vs Instance Store 



<!-- Start of picture text -->
Availability Zone 1 Availability Zone 2<br>Linux Linux<br>oO 0<br>EFS EFS<br>Mount Mount<br>Target Target<br><!-- End of picture text -->



<!-- Start of picture text -->
EFS<br><!-- End of picture text -->

© Stephane Maarek _ 

### High Availability & Scalability 

© Stephane Maarek 

Scalability & High Availability 

- Scalability means that an application / system can handle greater loads by adapting. 

- There are two kinds of scalability: 

   - Vertical Scalability 

   - Horizontal Scalability (= elasticity) 

- Scalability is linked but different to High Availability 

- Let’s deep dive into the distinction, using a call center as an example 

© Stephane Maarek 

#### Vertical Scalability 

- Vertically scalability means increasing the size of the instance 

- • For example, your application runs on a t2.micro 

- • Scaling that application vertically means running it on a t2.large 

- • Vertical scalability is very common for non distributed systems, such as a database. 

- • RDS, ElastiCache are services that can scale vertically. 

- There’s usually a limit to how much you can vertically scale (hardware limit) 



junior operator senior operator 

© Stephane Maarek 

#### Horizontal Scalability 

- Horizontal Scalability means increasing the number of instances / systems for your application 

- Horizontal scaling implies distributed systems. 

- • This is very common for web applications / modern applications 

- • It’s easy to horizontally scale thanks the cloud offerings such as Amazon EC2 



<!-- Start of picture text -->
operator operator operator<br><!-- End of picture text -->









operator operator operator 

© Stephane Maarek 

#### High Availability 

- High Availability usually goes hand in hand with horizontal scaling 

- High availability means running your application / system in at least 2 data centers (== Availability Zones) 

- The goal of high availability is to survive a data center loss 

###### first building in New York 





###### second building in San Francisco 

   - The high availability can be passive (for RDS Multi AZ for example) 

- The high availability can be active (for horizontal scaling) 

- © Stephane Maarek 

- N> <mark>N</mark> ee 

High Availability & Scalability For EC2 

• Vertical Scaling: Increase instance size (= scale up / down) 

   - From: t2.nano - 0.5G of RAM, 1 vCPU 

   - To: u-12tb1.metal – 12.3 TB of RAM, 448 vCPUs 

- Horizontal Scaling: Increase number of instances (= scale out / in) 

   - Auto Scaling Group 

   - Load Balancer 

- High Availability: Run instances for the same application across multi AZ • Auto Scaling Group multi AZ 

   - Load Balancer multi AZ 

© Stephane Maarek 

#### What is load balancing? 

• Load Balances are servers that forward traffic to multiple servers (e.g., EC2 instances) downstream **Elastic Load Balancer** EC2 Instance gp EC2 Instance <u>Se</u> @ ~~r~~ ree EC2 Instance © Stephane Maarek ~~I~~ '”TS OlEns 

|Why use a load balancer?|
|---|
|•Spread load across multiple downstream instances|
|•Expose a single point of access (DNS) to your application|
|•Seamlessly handle failures of downstream instances|
|•Do regular health checks to your instances|
|•Provide SSL termination (HTTPS) for your websites|
|•Enforce stickiness with cookies|
|•High availability across zones<br>•Separate public traffic from private traffic|



© Stephane Maarek 

#### Why use an Elastic Load Balancer? 

- An Elastic Load Balancer is a managed load balancer 

   - AWS guarantees that it will be working 

   - AWS takes care of upgrades, maintenance, high availability 

   - AWS provides only a few configuration knobs 

- It costs less to setup your own load balancer but it will be a lot more effort on your end 

- It is integrated with many AWS offerings / services 

   - EC2, EC2 Auto Scaling Groups, Amazon ECS 

   - AWS Certificate Manager (ACM), CloudWatch 

   - Route 53, AWS WAF, AWS Global Accelerator 

© Stephane Maarek 

#### Health Checks 

- Health Checks are crucial for Load Balancers 

- They enable the load balancer to know if instances it forwards traffic to are available to reply to requests 

- The health check is done on a port and a route (/health is common) 

- If the response is not 200 (OK), then the instance is unhealthy 

###### **Protocol:** HTTP 

**Port:** 4567 Health Checks **Endpoint:** /health ea @ cy EC2 Instance Elastic Load Balancer 

© Stephane Maarek IE '”TS Ol 

ns 

|Types of load balancer on AWS|
|---|





|• AWS has4 kinds of managed Load Balancers|
|---|



|• Classic Load Balancer(v1 - old generation) – 2009 – CLB|
|---|



|• HTTP,  HTTPS, TCP, SSL (secure TCP)|
|---|



|• Application Load Balancer(v2 - new generation) – 2016 – ALB|
|---|



|• HTTP,  HTTPS, WebSocket|
|---|



|• Network Load Balancer(v2 - new generation) – 2017 – NLB|
|---|



|• TCP,  TLS (secure TCP), UDP|
|---|



- Gateway Load Balancer – 2020 – GWLB 

   - Operates at layer 3 (Network layer) – IP Protocol 

• Overall, it is recommended to use the newer generation load balancers as they provide more features • Some load balancers can be setup as internal (private) or external (public) ELBs © Stephane Maarek IE'”TS Ol ns 



<!-- Start of picture text -->
Load Balancer Security Groups<br>LOAD BALANCER<br>HTTPS / HTTP HTTP Restricted<br>From anywhere to Load balancer<br>Users EC2<br><< <<<br>— Oo i:<br>Load Balancer Security Group:<br>Type (i) Protocol (i) Port Range (i) Source (i) Description (i)<br>HTTP TCP 80 0.0.0.0/0 Allow HTTP from an...<br>HTTPS TCP 443 0.0.0.0/0 Allow HTTPS from a...<br>Application Security Group: Allow traffic only from Load Balancer<br>Type (i) Protocol (i) Port Range (i) Source (i) Description (i)<br>HTTP TCP 80 sg-054b5ff5ea02f2b6e (load-b Allow Traffic only...<br>© Stephane Maarek NOT FOR DISTRIBUTION © Stephane Maarek www.datacumulus.com<br><!-- End of picture text -->

© Stephane Maarek 

Classic Load Balancers (v1) 

• Supports TCP (Layer 4), HTTP & HTTPS (Layer 7) listener internal • Health checks are TCP or HTTP based • Fixed hostname Client CLB EC2 XXX.region.elb.amazonaws.com<sup>Oo@2</sup> © Stephane Maarek IE'”TS Ol ns 

|Application Load Balancer (v2)|
|---|



|•Application load balancers is Layer 7 (HTTP)|
|---|





- Load balancing to multiple HTTP applications across machines (target groups) 

- Load balancing to multiple applications on the same machine (ex: containers) 

• Support for HTTP/2 and WebSocket • Support redirects (from HTTP to HTTPS for example) © Stephane Maarek IE'”TS Ol ns 

Application Load Balancer (v2) 

- Routing tables to different target groups: 



   - Routing based on path in URL   (example.com /users & example.com/ posts ) 

   - Routing based on hostname in URL  ( one.example.com & other.example.com ) 

   - Routing based on Query String, Headers (example.com/users? id=123&order=false ) 

- ALB are a great fit for micro services & container-based application (example: Docker & Amazon ECS) 

- Has a port mapping feature to redirect to a dynamic port in ECS 

• In comparison, we’d need multiple Classic Load Balancer per application © Stephane Maarek IE'”TS Ol ns 

Application Load Balancer (v2) HTTP Based Traffic Route /user HTTP **WWW** External Application Load Balancer (v2) Route /search HTTP **WWW** © Stephane Maarek <mark>at</mark> IE'”TS Ol ns 

Application Load Balancer (v2) Target Groups 

• EC2 instances (can be managed by an Auto Scaling Group) – HTTP 

- ECS tasks (managed by ECS itself) – HTTP 

- Lambda functions – HTTP request is translated into a JSON event 

- IP Addresses – must be private IPs 

- ALB can route to multiple target groups 

- Health checks are at the target group level 

© Stephane Maarek 

- Application Load Balancer (v2) Query Strings/Parameters Routing **Target Group 1** 

- ?Platform **=Mobile** AWS – EC2 based 

- External 

- Requests 

- **WWW** Application Load Balancer (v2) **Target Group 2** 

- ?Platform **=Desktop** On-premises – Private IP routing 

- n ~~as~~ 

- © Stephane Maarek tol<sup><u><mark>1</mark></u></sup> 

#### Application Load Balancer (v2) Good to Know 

• Fixed hostname (XXX.region.elb.amazonaws.com) 

• The application servers don’t see the IP of the client directly 

• The true IP of the client is inserted in the header X-Forwarded-For • We can also get Port (X-Forwarded-Port) and proto (X-Forwarded-Proto) Load Balancer IP **Client IP** (Private IP) EC2 **12.34.56.78** Instance -@ <mark>.</mark> - <mark><-y</mark> Connection termination © Stephane Maarek I'”TS Ol <mark>E</mark> ns 

#### Network Load Balancer (v2) 



<!-- Start of picture text -->
ag<br><!-- End of picture text -->

- Network load balancers (Layer 4) allow to: 

   - Forward TCP & UDP traffic to your instances 

   - Handle millions of request per seconds 

   - Less latency ~100 ms (vs 400 ms for ALB) 

- NLB has one static IP per AZ, and supports assigning Elastic IP (helpful for whitelisting specific IP) 

- NLB are used for extreme performance, TCP or UDP traffic 

- Not included in the AWS free tier 

© Stephane Maarek 

Network Load Balancer (v2) TCP (Layer 4) Based Traffic TCP + Rules TCP **WWW** External Network Load Balancer (v2) TCP + Rules HTTP **WWW** ag oie © Stephane Maarek 

#### Network Load Balancer – Target Groups 



<!-- Start of picture text -->
• EC2 instances<br>• IP Addresses  – must be private IPs<br>• Application Load Balancer<br>• Health Checks support the  TCP, HTTP and HTTPS Protocols<br>Network Network Network<br>Load Balancer Load Balancer Load Balancer<br>i-1234567890abcdef0 i-1234567890abcdef0 192.168.1.118 10.0.4.21<br>Target Group  Target Group  Target Group<br>(EC2 Instances) (IP Addresses) (Application Load Balancer)<br><!-- End of picture text -->

© Stephane Maarek 

- Gateway Load Balancer • Deploy, scale, and manage a fleet of 3<sup>rd</sup> party Route network virtual appliances in AWS 

- • Example: Firewalls, Intrusion Detection and Users Application Prevention Systems, Deep Packet Inspection **(source) (destination)** Systems, payload manipulation, … traffic traffic 

- i Table a 

- • Operates at Layer 3 (Network Layer) – IP Gateway Packets Load Balancer 

- • Combines the following functions: • Transparent Network Gateway – single entry/exit for all traffic 

- • Load Balancer – distributes traffic to your virtual Target Group 

- appliances 

- • Uses the GENEVE protocol on port 6081 3<sup>rd</sup> Party Security 

- Virtual Appliances 

© Stephane Maarek 



<!-- Start of picture text -->
Gateway Load Balancer – Target Groups<br><!-- End of picture text -->

- EC2 instances 



<!-- Start of picture text -->
• IP Addresses  – must be private IPs<br>Gateway Gateway<br>Load Balancer Load Balancer<br>re 8s<br>i-1234567890abcdef0 i-1234567890abcdef0 192.168.1.118 10.0.4.21<br>Target Group  Target Group<br>(EC2 Instances) (IP Addresses)<br><!-- End of picture text -->

© Stephane Maarek 

Sticky Sessions (Session Affinity) 

- It is possible to implement stickiness so that the same client is always redirected to the same instance behind a load balancer 

- This works for Classic Load Balancer, Application Load Balancer, and Network Load Balancer 

- • For both CLB & ALB, the “cookie” used for stickiness has an expiration date you control 

- • Use case: make sure the user doesn’t lose his session data 







Client 1 Client 2 Client 3 







• Enabling stickiness may bring imbalance to the load over the backend EC2 instances if 6 EC2 Instance EC2 Instance © Stephane Maarek IE'”TS Ol ns 

#### Sticky Sessions – Cookie Names 

- Application-based Cookies • Custom cookie 

      - Generated by the target 

      - Can include any custom attributes required by the application 

      - Cookie name must be specified individually for each target group 

      - Don’t use AWSALB , AWSALBAPP , or AWSALBTG (reserved for use by the ELB) 

   - Application cookie 

      - Generated by the load balancer 

      - Cookie name is AWSALBAPP 

- Duration-based Cookies 

   - Cookie generated by the load balancer 

   - Cookie name is AWSALB for ALB, AWSELB for CLB 

© Stephane Maarek 

#### Cross-Zone Load Balancing 

**<u>With Cross Zone Load Balancing:</u> each load balancer instance distributes evenly across all registered instances in all AZ** 



<!-- Start of picture text -->
50 50<br>10 10 10 10<br>10 10<br>10 10 10 10<br>Availability Zone 1 Availability Zone 2<br><!-- End of picture text -->

**<u>Without Cross Zone Load Balancing:</u>** 



<!-- Start of picture text -->
Requests are distributed in the instances of the<br>node of the Elastic Load Balancer<br>50 50<br>6.25 6.25 6.25 6.25<br>25 25<br>6.25 6.25 6.25 6.25<br>Availability Zone 1 Availability Zone 2<br><!-- End of picture text -->

© Stephane Maarek 

#### Cross-Zone Load Balancing 

- Application Load Balancer 

   - Enabled by default (can be disabled at the Target Group level) 

   - No charges for inter AZ data 

- Network Load Balancer & Gateway Load Balancer • Disabled by default 

   - You pay charges ($) for inter AZ data if enabled 

- Classic Load Balancer 

   - Disabled by default 

   - No charges for inter AZ data if enabled 

© Stephane Maarek 

#### SSL/TLS - Basics 

- An SSL Certificate allows traffic between your clients and your load balancer to be encrypted in transit (in-flight encryption) 

- SSL refers to Secure Sockets Layer, used to encrypt connections 

- TLS refers to Transport Layer Security, which is a newer version 

- Nowadays, TLS certificates are mainly used , but people still refer as SSL 

- Public SSL certificates are issued by Certificate Authorities (CA) 

- Comodo, Symantec, GoDaddy, GlobalSign, Digicert, Letsencrypt, etc… 

- SSL certificates have an expiration date (you set) and must be renewed 

© Stephane Maarek 

ns 

#### Load Balancer - SSL Certificates 

**LOAD BALANCER** HTTPS (encrypted) HTTP Over www Over private VPC EC2 **Users** Instance ~~—~~ • The load balancer uses an X.509 certificate (SSL/TLS server certificate) • You can manage certificates using ACM (AWS Certificate Manager) 

- You can create upload your own certificates alternatively 

- HTTPS listener: 

   - You must specify a default certificate 

   - You can add an optional list of certs to support multiple domains 

   - Clients can use SNI (Server Name Indication) to specify the hostname they reach 

   - Ability to specify a security policy to support older versions of SSL / TLS (legacy clients) 

© Stephane Maarek IE '”TS Ol 

#### SSL – Server Name Indication (SNI) 

- SNI solves the problem of loading multiple SSL certificates onto one web server (to serve multiple websites) 

- It’s a “newer” protocol, and requires the client to indicate the hostname of the target server in the initial SSL handshake 

- The server will then find the correct certificate, or return the default one 

###### Note: 

- Only works for ALB & NLB (newer generation), CloudFront 

- Does not work for CLB (older gen) 



<!-- Start of picture text -->
Target group for<br>www.mycorp.com<br>Ce<br>Target group for<br>Domain1.example.com<br>I would like<br>www.mycorp.com<br>o- @<br>Client ALB<br>SSL Cert:<br>Use the correct Domain1.example.com<br>SSL cert<br>SSL Cert:<br>www.mycorp.com<br>oi.<br><!-- End of picture text -->

…. 

© Stephane Maarek 

#### Elastic Load Balancers – SSL Certificates 

- Classic Load Balancer (v1) 

   - Support only one SSL certificate 

   - Must use multiple CLB for multiple hostname with multiple SSL certificates 

- Application Load Balancer (v2) 

   - Supports multiple listeners with multiple SSL certificates 

   - Uses Server Name Indication (SNI) to make it work 

- Network Load Balancer (v2) 

   - Supports multiple listeners with multiple SSL certificates 

   - Uses Server Name Indication (SNI) to make it work 

© Stephane Maarek 

#### Connection Draining 

|• Feature naming|
|---|



|• Connection Draining – for CLB|
|---|



|• Deregistration Delay – for ALB & NLB|
|---|



- Time to complete “in-flight requests” while the instance is de-registering or unhealthy 

- Stops sending new requests to the EC2 instance which is de-registering 



<!-- Start of picture text -->
B<br><!-- End of picture text -->

waiting for **<u>existing</u>** connections to complete ~~a~~ EC2 Instance **DRAINING** 



<!-- Start of picture text -->
-<br><!-- End of picture text -->

EC2 Instance Users • Between 1 to 3600 seconds (default: 300 ELB seconds) new connections • Can be disabled (set value to 0) ey established to all other instances EC2 Instance • Set to a low value if your requests are short © Stephane Maarek IE'”TS Ol ns 

#### What’s an Auto Scaling Group? 



<!-- Start of picture text -->
Tt<br><!-- End of picture text -->

- In real-life, the load on your websites and application can change 

- In the cloud, you can create and get rid of servers very quickly 

- The goal of an Auto Scaling Group (ASG) is to: 

   - Scale out (add EC2 instances) to match an increased load 

   - Scale in (remove EC2 instances) to match a decreased load 

   - Ensure we have a minimum and a maximum number of EC2 instances running 

   - Automatically register new instances to a load balancer 

   - Re-create an EC2 instance in case a previous one is terminated (ex: if unhealthy) 

- ASG are free (you only pay for the underlying EC2 instances) 

© Stephane Maarek 

#### Auto Scaling Group in AWS 



Auto Scaling Group **EC2 EC2 EC2 EC2 EC2 EC2 EC2 Instance Instance Instance Instance Instance Instance Instance** Minimum Capacity Scale Out as Needed Desired Capacity Maximum Capacity © Stephane Maarek IE'”TS Ol ns 

#### Auto Scaling Group in AWS With Load Balancer 



<!-- Start of picture text -->
Users<br>Elastic Load Balancer<br>ELB can check the health of your EC2 instances!<br>Auto Scaling Group<br>EC2 EC2 EC2 EC2 EC2 EC2 EC2<br>Instance Instance Instance Instance Instance Instance Instance<br>000 000<br><!-- End of picture text -->

ns 

© Stephane Maarek IE '”TS Ol 

#### Auto Scaling Group Attributes 

- A Launch Template (older “Launch Configurations” are deprecated) • AMI + Instance Type 

   - EC2 User Data 

   - EBS Volumes 

   - Security Groups 

   - SSH Key Pair 

   - IAM Roles for your EC2 Instances 

   - Network + Subnets Information 

   - Load Balancer Information 

- Min Size / Max Size / Initial Capacity 

- Scaling Policies 

ASG Launch Template **AMI Instance EBS Volumes Type Security Groups SSH Key Pair IAM Role** … **VPC + Subnets Load Balancer** 

© Stephane Maarek 

Auto Scaling - CloudWatch Alarms & Scaling 

- It is possible to scale an ASG based on CloudWatch alarms 

- An alarm monitors a metric (such as Average CPU , or a custom metric ) 

• <u>Metrics such as Average CPU are computed for the overall ASG instances</u> 

- Based on the alarm: 

   - We can create scale-out policies (increase the number of instances) 

• We can create scale-in policies (decrease the number of instances) Auto Scaling Group trigger Scaling **EC2 EC2 EC2 EC2 EC2 Instance Instance Instance Instance Instance** CloudWatch Alarm © Stephane Maarek <mark>IE</mark> '”TS Ol ns 

#### Auto Scaling Groups – Scaling Policies 

- Dynamic Scaling 

   - Target Tracking Scaling 

      - Simple to set-up 

      - Example: I want the average ASG CPU to stay at around 40% 

   - Simple / Step Scaling 

      - When a CloudWatch alarm is triggered (example CPU > 70%), then add 2 units 

      - When a CloudWatch alarm is triggered (example CPU < 30%), then remove 1 

- Scheduled Scaling 

   - Anticipate a scaling based on known usage patterns 

   - Example: increase the min capacity to 10 at 5 pm on Fridays 

© Stephane Maarek 

#### Auto Scaling Groups – Scaling Policies 

- Predictive scaling: continuously forecast load and schedule scaling ahead 



<!-- Start of picture text -->
Analyze historical load Generate forecast Schedule scaling actions<br>» »<br>—_ Bute<br>4/1 4/15 4/30 4/1 4/15 4/30 4/1 4/15 4/30<br><!-- End of picture text -->

© Stephane Maarek 

#### Good metrics to scale on 

- CPUUtilization : Average CPU utilization across your instances 

- RequestCountPerTarget : to make sure the number of requests per EC2 instances is stable 

- Average Network In / Out (if you’re application is network bound) 

- • Any custom metric (that you push using CloudWatch) 

Users 



Application Load Balancer 



**RequestCountPerTarget** Target Value: 3 









Auto Scaling group 

© Stephane Maarek 

Auto Scaling Groups - Scaling Cooldowns 

- After a scaling activity happens, you are in Scaling Action the cooldown period (default 300 Occurs seconds) 

- • During the cooldown period, the ASG will not launch or terminate additional Default 

- No 

- Launch or Cooldown 

- instances (to allow for metrics to stabilize) Teminate Instance in effect? Yes 

- • Advice: Use a ready-to-use AMI to reduce configuration time in order to be serving request fasters and reduce the cooldown Ignore Action 

- period 

© Stephane Maarek 

### RDS, Aurora & ElastiCache 

© Stephane Maarek 

#### Amazon RDS Overview 



<!-- Start of picture text -->
RK a<br>“ N<br><!-- End of picture text -->

- RDS stands for Relational Database Service 

- It’s a managed DB service for DB use SQL as a query language. 

- It allows you to create databases in the cloud that are managed by AWS 

   - Postgres 

   - MySQL 

   - MariaDB 

   - Oracle 

   - Microsoft SQL Server 

   - IBM DB2 

   - Aurora (AWS Proprietary database) 

© Stephane Maarek 

#### Advantage over using RDS versus deploying DB on EC2 

- RDS is a managed service: 

   - Automated provisioning, OS patching 

   - Continuous backups and restore to specific timestamp (Point in Time Restore)! 

   - Monitoring dashboards 

   - Read replicas for improved read performance 

   - Multi AZ setup for DR (Disaster Recovery) 

   - Maintenance windows for upgrades 

   - Scaling capability (vertical and horizontal) 

   - Storage backed by EBS (gp2 or io1) 

- BUT you can’t SSH into your instances 

© Stephane Maarek 

#### RDS – Storage Auto Scaling 

- Helps you increase storage on your RDS DB instance dynamically 







- When RDS detects you are running out of free database storage, it scales automatically 

- Avoid manually scaling your database storage Application 

- <mark>Lo</mark> 

- • You have to set Maximum Storage Threshold (maximum limit for DB storage) 

- • Automatically modify storage if: Read/Write • Free storage is less than 10% of allocated storage • Low-storage lasts at least 5 minutes • 6 hours have passed since last modification 

- • Useful for applications with unpredictable workloads • Supports all RDS database engines Storage 

- — 

- IE '”TS Ol ns 

© Stephane Maarek IE '”TS Ol 

RDS Read Replicas for read scalability • Up to 15 Read Replicas • Within AZ, Cross AZ or Application Cross Region <mark>ee</mark> • Replication is ASYNC , so reads are eventually consistent reads writes reads reads tf ji i • Replicas can be promoted to their own DB • Applications must update the connection ASYNC ASYNC string to leverage read D—-O-B replication replication replicas **RDS DB RDS DB RDS DB instance read instance read instance replica replica** © Stephane Maarek IE'”TS Ol ns 

RDS Read Replicas – Use Cases 

• You have a production database that is taking on normal load **Production** Reporting Application Application • You want to run a reporting <mark>yD</mark> application to run some analytics • You create a Read Replica to run **reads** reads the new workload there 1B] 1 • The production application is unaffected • Read replicas are used for SELECT (=read) only kind of statements ASYNC (not INSERT, UPDATE, DELETE) replication MfgR **RDS DB RDS DB instance read instance replica** © Stephane Maarek SE’”Oh es 

RDS Read Replicas – Network Cost In AWS there’s a network cost when data goes from one AZ to another For RDS Read Replicas within the same region, you don’t pay that fee Same Region / Different AZ Region/AZ Region/AZ **us-east-1a                                         us-east-1b us-east-1a eu-west-1b** **<u>VS</u>** ASYNC ASYNC 5-5 0-5 Replication Replication **RDS DB RDS DB RDS DB RDS DB** Same Region **instance read** Cross-Region **instance read instance instance Free replica $$$ replica** 

#### RDS Read Replicas – Network Cost 

- In AWS there’s a network cost when data goes from one AZ to another 

- For RDS Read Replicas within the same region, you don’t pay that fee 

© Stephane Maarek 

RDS Multi AZ (Disaster Recovery) 

- SYNC replication 

- • One DNS name – automatic app failover to standby 

- Increase availability 

- Failover in case of loss of AZ, loss of network, instance or storage failure 

- No manual intervention in apps 

- Not used for scaling 

- <u>Note:</u> ~~;~~ The Read Replicas be setup as Multi AZ for Disaster Recovery (DR) 

Application writes reads Ui One DNS name – automatic failover - SYNC 5-H replication **RDS DB RDS Master DB instance standby instance (AZ A) (AZ B)** 

© Stephane Maarek 

RDS – From Single-AZ to Multi-AZ • Zero downtime operation (no **RDS DB Standby DB** need to stop the DB) **instance** • Just click on “modify” for the database SYNC • The following happens internally: w—& Replication • A snapshot is taken • A new DB is restored from the snapshot in a new AZ restore snapshot • Synchronization is established between the two databases a DB snapshot © Stephane Maarek IE'”TS Ol ns 

#### RDS Custom 

- Managed Oracle and Microsoft SQL Server Database with OS and database customization 

- RDS: Automates setup, operation, and scaling of database in AWS 

- • Custom: access to the underlying database and OS so you can • Configure settings • Install patches • Enable native features 

- Access the underlying EC2 Instance using SSH or SSM Session Manager 

- • De-activate Automation Mode to perform your customization, better to take a DB snapshot before 



User 

**apply SSH cstomizations** 



EC2 Instance Automation Mode **disabled** 

- RDS vs. RDS Custom • RDS: entire database and the OS to be managed by AWS • RDS Custom: full admin access to the underlying OS and the database 

© Stephane Maarek 

ns 

#### Amazon Aurora 



- Aurora is a proprietary technology from AWS (not open sourced) 

- Postgres and MySQL are both supported as Aurora DB (that means your drivers will work as if Aurora was a Postgres or MySQL database) 

- Aurora is “AWS cloud optimized” and claims 5x performance improvement over MySQL on RDS, over 3x the performance of Postgres on RDS 

- Aurora storage automatically grows in increments of 10GB, up to 128  TB. 

- Aurora can have up to 15 replicas and the replication process is faster than MySQL (sub 10 ms replica lag) 

- Failover in Aurora is instantaneous. It’s HA (High Availability) native. 

- Aurora costs more than RDS (20% more) – but is more efficient 

© Stephane Maarek IE '”TS Ol 

- Aurora High Availability and Read Scaling • 6 copies of your data across 3 AZ: AZ 1 AZ 2 AZ 3 

- • 4 copies out of 6 needed for writes • 3 copies out of 6 need for reads • Self healing with peer-to-peer replication 06 66 66 

- • Storage is striped across 100s of volumes W R R R R R 

- oor 

- • One Aurora Instance takes writes (master) 090 • Automated failover for master in less than Shared storage Volume Replication + Self Healing + Auto Expanding 

- <u><mark>_la</mark></u> 

- 30 seconds 

- • Master + up to 15 Aurora Read Replicas serve reads 

- • Support for Cross Region Replication 

- © Stephane Maarek 

- — ~~<mark>|</mark>~~ 

Aurora DB Cluster client **Writer Endpoint Reader Endpoint** Pointing to the master Connection Load Balancing ~~<mark>=</mark>~~ Auto Scaling OD -f=6-0-5-5— W R R R R R ¥ tf f Gf fF Shared storage Volume Auto Expanding from 10G to 128 TB > 

© Stephane Maarek > 

#### Features of Aurora 

- Automatic fail-over • Backup and Recovery • Isolation and security • Industry compliance • Push-button scaling 

- Automated Patching with Zero Downtime 

- Advanced Monitoring 

- Routine Maintenance 

- Backtrack: restore data at any point of time without using backups 

© Stephane Maarek 

Aurora Replicas - Auto Scaling Client Many Requests Writer Endpoint Reader Endpoint Endpoint Extended ~~— es~~ CPU CPU Usage Usage Replicas Auto Scaling oo W R R R R ¥ ft a? Ff Shared Storage Volume SS © Stephane Maarek SE ’”- Oh es 

#### Aurora – Custom Endpoints 

- Define a subset of Aurora Instances as a Custom Endpoint 

• Example: Run analytical queries on specific replicas • The Reader Endpoint is generally not used after defining Custom Endpoints Analytical Queries Queries Client Writer Endpoint Reader Endpoint Custom Endpoint ~~oe —e~~ db.r3.large db.r3.large db.r5.2xlarge db.r5.2xlarge W R R R R Shared Storage Volume ; , ) 

W ; , 

© Stephane Maarek 

#### Aurora Serverless 

- Automated database instantiation and autoscaling based on actual usage 

- Good for infrequent, intermittent or unpredictable workloads 

- • No capacity planning needed 

- Pay per second, can be more cost-effective 



<!-- Start of picture text -->
c=)<br><!-- End of picture text -->



<!-- Start of picture text -->
Client<br><!-- End of picture text -->

**Proxy Fleet (managed by Aurora)** 





<!-- Start of picture text -->
Amazon<br>Aurora :<br><!-- End of picture text -->



<!-- Start of picture text -->
Amazon<br>Aurora=<br><!-- End of picture text -->



<!-- Start of picture text -->
Amazon<br>Aurorag<br><!-- End of picture text -->



<!-- Start of picture text -->
Amazon<br>Aurora=<br><!-- End of picture text -->



<!-- Start of picture text -->
Amazon<br>Aurorag<br><!-- End of picture text -->

Shared storage Volume 

© Stephane Maarek 

#### Global Aurora 

- Aurora Cross Region Read Replicas: • Useful for disaster recovery • Simple to put in place 

- Aurora Global Database (recommended): • 1 Primary Region (read / write) 

   - Up to 5 secondary (read-only) regions, replication lag is less than 1 second 

   - • Up to 16 Read Replicas per secondary region • Helps for decreasing latency • Promoting another region (for disaster recovery) has an RTO of < 1 minute 

   - Typical cross-region replication takes less than 1 second 



us-east-1 - PRIMARY region 





Applications Read / Write 

###### replication 



eu-west-1 - SECONDARY region 





Applications Read Only 

© Stephane Maarek 

#### Aurora Machine Learning 

- Enables you to add ML-based predictions to your applications via SQL 

- Simple, optimized, and secure integration between Aurora and AWS ML services 

- • Supported services • Amazon SageMaker (use with any ML model) • Amazon Comprehend (for sentiment analysis) 

- • You don’t need to have ML experience • Use cases: fraud detection, ads targeting, sentiment analysis, product recommendations 

Application **SQL query query results** (Recommended products?) (red shirt, blue …) Amazon Aurora **data predictions** (user’s profile, (red shirt, shopping history, …) blue pants, …) <mark>Bp.</mark> Amazon Amazon SageMaker Comprehend 

© Stephane Maarek 

#### RDS Backups 





- Automated backups: 

   - Daily full backup of the database (during the backup window) 

   - Transaction logs are backed-up by RDS every 5 minutes 

   - => ability to restore to any point in time (from oldest backup to 5 minutes ago) 

   - 1 to 35 days of retention, set 0 to disable automated backups 

- Manual DB Snapshots 

   - Manually triggered by the user 

   - Retention of backup for as long as you want 

• Trick: in a stopped RDS database, you will still pay for storage. If you plan on stopping it for a long time, you should snapshot & restore instead © Stephane Maarek IE '”TS Ol ns 

ns 

ns 

#### Aurora Backups 





- Automated backups 

   - 1 to 35 days (cannot be disabled) 

   - point-in-time recovery in that timeframe 

- Manual DB Snapshots 

   - Manually triggered by the user 

   - Retention of backup for as long as you want 

© Stephane Maarek IE '”TS Ol 

ns 

#### RDS & Aurora Restore options 







- Restoring a RDS / Aurora backup or a snapshot creates a new database 

- Restoring MySQL RDS database from S3 

   - Create a backup of your on-premises database 

   - Store it on Amazon S3 (object storage) 



   - Restore the backup file onto a new RDS instance running MySQL 

- Restoring MySQL Aurora cluster from S3 

   - Create a backup of your on-premises database using Percona XtraBackup 

   - Store the backup file on Amazon S3 

   - Restore the backup file onto a new Aurora cluster running MySQL 



© Stephane Maarek IE '”TS Ol 

#### Aurora Database Cloning 

- Create a new Aurora DB Cluster from an existing one 

- • Faster than snapshot & restore • Uses _copy-on-write_ protocol Amazon Amazon clone 

- Aurora Aurora 

- • Initially, the new DB cluster uses the same data volume as the original DB cluster (fast and efficient – no copying is needed) = = 

- • When updates are made to the new DB cluster data, then additional storage is allocated and data is Production Aurora Staging Aurora copied to be separated 

- Very fast & cost-effective 

- Useful to create a “staging” database from a “production” database without impacting the production database 

© Stephane Maarek 

#### RDS & Aurora Security 

- At-rest encryption: 

   - Database master & replicas encryption using AWS KMS – must be defined as launch time 

   - If the master is not encrypted, the read replicas cannot be encrypted 

   - To encrypt an un-encrypted database, go through a DB snapshot & restore as encrypted 

- In-flight encryption: TLS-ready by default, use the AWS TLS root certificates client-side 

- IAM Authentication: IAM roles to connect to your database (instead of username/pw) 

- Security Groups: Control Network access to your RDS / Aurora DB 

- No SSH available except on RDS Custom 

- Audit Logs can be enabled and sent to CloudWatch Logs for longer retention 

© Stephane Maarek 

Amazon RDS Proxy VPC • Fully managed database proxy for RDS Lambda functions … • Allows apps to pool and share DB connections established with the database Qa @@® ® • Improving database efficiency by reducing the **IAM Authentication** stress on database resources (e.g., CPU, RAM) and minimize open connections (and timeouts) • Serverless, autoscaling, highly available (multi-AZ) • Reduced RDS & Aurora failover time by up 66% Private subnet • Supports RDS (MySQL, PostgreSQL, MariaDB, MS RDS Proxy SQL Server) and Aurora (MySQL, PostgreSQL) • No code changes required for most apps • Enforce IAM Authentication for DB, and securely store credentials in AWS Secrets Manager RDS DB • RDS Proxy is never publicly accessible (must be accessed from VPC) Instance = © Stephane Maarek NA” Re 

#### Amazon ElastiCache Overview 



- The same way RDS is to get managed Relational Databases… 

- ElastiCache is to get managed Redis or Memcached 

- Caches are in-memory databases with really high performance, low latency 

- Helps reduce load off of databases for read intensive workloads 

- Helps make your application stateless 

- AWS takes care of OS maintenance / patching, optimizations, setup, configuration, monitoring, failure recovery and backups 

- <u>Using ElastiCache involves heavy application code changes</u> 

© Stephane Maarek ~~IE~~ '”TS Ol ns 

#### ElastiCache Solution Architecture - DB Cache 

- Applications queries **Amazon ElastiCache** 

- ElastiCache, if not available, get from RDS Cache hit 

- and store in ElastiCache. 

- • Helps relieve load in RDS Cache miss 

- • Cache must have an application Read from DB 

- invalidation strategy to make sure only the most current data is used in Write to cache **Amazon** 

- there. **RDS** 

© Stephane Maarek 

Solution Architecture – User Session Store Write session application **Amazon ElastiCache** Retrieve session application application <u><mark>J</mark></u> ht <mark>ao</mark> 

- ElastiCache Solution Architecture – User Session Store 

- • User logs into any of the Write session 

- application application 

- • The application writes the session data into ElastiCache Retrieve session 

- • The user hits another application 

- instance of our application 

- • The instance retrieves the data and the user is application 

- already logged in 

- © Stephane Maarek 

- SE '”-= <u><mark>J</mark></u> ht <mark>ao</mark> 

#### ElastiCache – Redis vs Memcached 

REDIS 

- Multi AZ with Auto-Failover 

- • Read Replicas to scale reads and have high availability 

- • Data Durability using AOF persistence 

- Backup and restore features 

- Supports Sets and Sorted Sets 

###### MEMCACHED 

- Multi-node for partitioning of data (sharding) 

- No high availability (replication) 

- Non persistent 

- No backup and restore 

- Multi-threaded architecture 



<!-- Start of picture text -->
Replication +<br>en fs) fey<br>sharding<br>tee teeEJ iO<br>© Stephane Maarek<br>IE '”TS Ol ns<br><!-- End of picture text -->

ns 

#### ElastiCache – Cache Security 

- ElastiCache supports IAM Authentication for Redis 

- IAM policies on ElastiCache are only used for AWS API-level security 

- Redis AUTH 

• You can set a “password/token” when you create a Redis cluster • This is an extra level of security for your cache (on top of security groups) • Support SSL in flight encryption 

- Memcached 

   - Supports SASL-based authentication (advanced) 

EC2 Security group **EC2** Client SSL encryption Redis AUTH 

Redis Security group 



© Stephane Maarek IE '”TS Ol 

#### Patterns for ElastiCache 

- Lazy Loading: all the read data is cached, data can become stale in **Amazon** 

- cache **ElastiCache** 

- • Write Through: Adds or update data in the cache when written Cache hit 

- to a DB (no stale data) 

- • Session Store: store temporary session data in a cache (using Cache miss 

- TTL features) application Read from DB 

- • _Quote: There are only two hard things in Computer Science: cache invalidation and naming things_ Write to cache **Amazon RDS** 

- **Lazy Loading illustrated** 

© Stephane Maarek 

#### ElastiCache – Redis Use Case 

- Gaming Leaderboards are computationally complex 

- Redis Sorted sets guarantee both uniqueness and element ordering 



<!-- Start of picture text -->
• Each time a new element added, it’s ranked in real time, then added in<br>correct order<br>:<br>ElastiCache<br>1<br>for Redis<br>2<br>gp |<br>=<br>ElastiCache<br>3<br>for Redis<br>:<br>Clients ElastiCache  Real-time Leaderboard<br>for Redis<br><!-- End of picture text -->

© Stephane Maarek 

### Amazon Route 53 

© Stephane Maarek 

#### What is DNS? 

- Domain Name System which translates the human friendly hostnames into the machine IP addresses 

- www.google.com => 172.217.18.36 

- DNS is the backbone of the Internet 

- DNS uses hierarchical naming structure 

.com example.com www.example.com api.example.com 

© Stephane Maarek 

#### DNS Terminologies 

- Domain Registrar: Amazon Route 53, GoDaddy, … 

- DNS Records: A, AAAA, CNAME, NS, … 

- Zone File: contains DNS records 

- Name Server: resolves DNS queries (Authoritative or Non-Authoritative) 

- Top Level Domain (TLD): .com, .us, .in, .gov, .org, … 

- Second Level Domain (SLD): amazon.com, google.com, … 

###### **URL** 



<!-- Start of picture text -->
http://api.www.example.co<br>Root<br>Protocol TLD<br>m.<br>SLD<br>Sub Domain<br><!-- End of picture text -->

**FQDN (Fully Qualified Domain Name)** 

© Stephane Maarek 



<!-- Start of picture text -->
How DNS Works<br>Web Server<br>(example.com)<br>(IP: 9.10.11.12)<br>Managed by ICANN<br>Root DNS Server<br>example.com?<br>example.com?<br>Managed by IANA<br>9.10.11.12 (Branch of ICANN)<br>TTL<br>example.com NS 5.6.7.8<br>TTL<br>Web Browser<br>TLD DNS Server<br>You want to access  Local DNS Server<br>(.com)<br>example.com<br>Assigned and Managed by<br>your company or assigned by<br>your ISP dynamically Managed by Domain Registrar<br>(e.g., Amazon Registrar, Inc.)<br>SLD DNS Server<br>(example.com)<br>.com NS 1.2.3.4<br>example.com?<br>example.com?<br>example.com IP 9.10.11.12<br><!-- End of picture text -->

© Stephane Maarek 

#### Amazon Route 53 

example.com? • A highly available, scalable, fully managed and _Authoritative_ DNS Amazon Route 53 G ~~Q££~~ 54.22.33.44 • Authoritative = the customer (you) Client can update the DNS records • Route 53 is also a Domain Registrar • Ability to check the health of your AWS Cloud resources • The only AWS service which Public IP **54.22.33.44** provides 100% availability SLA • Why Route 53? 53 is a reference to EC2 Instance the traditional DNS port 

© Stephane Maarek 

#### Route 53 – Records 

- How you want to route traffic for a domain • Each record contains: 

   - Domain/subdomain Name – e.g., example.com 

   - • Record Type – e.g., A or AAAA • Value – e.g., 12.34.56.78 

- Routing Policy – how Route 53 responds to queries 

- • TTL – amount of time the record cached at DNS Resolvers 

- • Route 53 supports the following DNS record types: • (must know) A / AAAA / CNAME / NS 

   - (advanced) CAA / DS / MX / NAPTR / PTR / SOA / TXT / SPF / SRV 

© Stephane Maarek 

#### Route 53 – Record Types 

- A – maps a hostname to IPv4 

- AAAA – maps a hostname to IPv6 

- CNAME – maps a hostname to another hostname 

   - The target is a domain name which must have an A or AAAA record 

   - Can’t create a CNAME record for the top node of a DNS namespace (Zone Apex) 

   - Example: you can’t create for example.com, but you can create for www.example.com 

- NS – Name Servers for the Hosted Zone 

   - Control how traffic is routed for a domain 

© Stephane Maarek 

#### Route 53 – Hosted Zones 



<!-- Start of picture text -->
C3<br><!-- End of picture text -->

   - A container for records that define how to route traffic to a domain and its subdomains 

   - Public Hosted Zones – contains records that specify how to route traffic on the Internet (public domain names) application1.mypublicdomain.com 

- Private Hosted Zones – contain records that specify how you route traffic within one or more VPCs (private domain names) application1.company.internal 

- • You pay $0.50 per month per hosted zone 

- © Stephane Maarek 

- IE'”TS Ol ns 

#### Route 53 – Public vs. Private Hosted Zones 

|**Public Hosted Zone**|
|---|



|**Private Hosted Zone**|
|---|



example.com? VPC 54.22.33.44 Private Hosted Zone Client Public Hosted Zone DB Instance VPC (db.example.internal) **(Private IP)** S3 Bucket Amazon EC2 Instance Application EC2 Instance EC2 Instance CloudFront **(Public IP)** Load Balancer (webapp.example.internal) (api.example.internal) **(Private IP) (Private IP)** © Stephane Maarek Is <mark>afeE</mark> '”TS <mark>4]</mark> Ol <mark>oo</mark> ns 

Route 53 – Records TTL (Time To Live) 

- High TTL – e.g., 24 hr • Less traffic on Route 53 • Possibly outdated records Amazon 

- • Low TTL – e.g., 60 sec. **A** 12.34.56.78 Route 53 

- • More traffic on Route 53 ($$) **(with TTL) TTL** 

- • Records are outdated for less Client 

- time **Will cache the result for** 

- • Easy to change records **The TTL of the record** 

- • Except for Alias records, TTL is mandatory for each DNS record Web Server 

© Stephane Maarek 

#### CNAME vs Alias 

- AWS Resources (Load Balancer, CloudFront...) expose an AWS hostname: • lb1-1234.us-east-2.elb.amazonaws.com and you want myapp.mydomain.com 

- CNAME: 

   - Points a hostname to any other hostname. (app.mydomain.com => blabla.anything.com) 

   - <u>ONLY FOR NON ROOT DOMAIN (aka. something.mydomain.com)</u> 

- Alias: 

   - Points a hostname to an AWS Resource (app.mydomain.com => blabla.amazonaws.com) 

   - <u>Works for ROOT DOMAIN and NON ROOT DOMAIN (aka mydomain.com)</u> 

   - Free of charge 

   - Native health check 

© Stephane Maarek 

Route 53 – Alias Records Amazon Route 53 • Maps a hostname to an AWS resource • An extension to DNS functionality • Automatically recognizes changes in the **Alias Record (Enabled) Record Name Type Value** resource’s IP addresses example.com A MyALB-123456789.useast1.elb.amazonaws.com • Unlike CNAME, it can be used for the top node of a DNS namespace (Zone Apex), e.g.: example.com • Alias Record is always of type A/AAAA for **MyALB-123456789.us-east-1.elb.amazonaws.com** AWS resources (IPv4 / IPv6) **<u>AWS-Managed (IP Addresses might change)</u>** ~~_—~~ @ • You can’t set the TTL Application Load Balancer © Stephane Maarek I'”TS Ol ~~E~~ ns 

Route 53 – Alias Records Targets 

- Elastic Load Balancers 

- CloudFront Distributions 

- API Gateway 



**Elastic Load Balancer** 





**Amazon Amazon CloudFront API Gateway** 

- Elastic Beanstalk environments 



<!-- Start of picture text -->
[ei<br><!-- End of picture text -->





- S3 Websites 

- VPC Interface Endpoints 

**S3 Websites VPC Interface Endpoints** 

**Elastic Beanstalk** 

- Global Accelerator accelerator 





- Route 53 record in the same hosted zone 

**Global Accelerator** 

**Route 53 Record (same Hosted Zone)** 

- You cannot set an ALIAS record for an EC2 DNS name 

© Stephane Maarek IE '”TS Ol 

#### Route 53 – Routing Policies 

|• Define how Route 53 responds to DNS queries|
|---|
|• Don’t get confused by the word_“Routing”_<br>• It’s not the same as Load balancer routing which routes the traffic<br>• DNS does not route any traffic, it only responds to the DNS queries|
|• Route 53 Supports the following Routing Policies<br>• Simple<br>• Weighted<br>• Failover|
|• Latency based<br>• Geolocation|
|• Multi-Value Answer|
|• Geoproximity (using Route 53 Traffic Flow feature)|



© Stephane Maarek 

#### Routing Policies – Simple 

###### **<u>Single Value</u>** 

• Typically, route traffic to a single foo.example.com resource **A** 11.22.33.44 • Can specify multiple values in the Client Amazon same record Route 53 • If multiple values are returned, a random one is chosen by the client **<u>Multiple Value</u>** • When Alias enabled, specify only one AWS resource foo.example.com • Can’t be associated with Health **A** 11.22.33.44 Checks Client **A** 55.66.77.88 Amazon **chooses A** 99.11.22.33 Route 53 **a random value** 

© Stephane Maarek 



<!-- Start of picture text -->
Routing Policies – Weighted<br>• Control the % of the requests that go to each<br>specific resource<br>• Assign each record a relative weight:<br>Weight: 70<br>!"#$%& ()* + ,-".#(#. *".)*/<br>• 𝑡𝑟𝑎𝑓𝑓𝑖𝑐 (%) =<br>012 )( +33 &%" 4"#$%&, ()* +33 *".)*/,<br>• Weights don’t need to sum up to 100<br>“Sein teenage<br>• DNS records must have the same name and type <n ensebewigt<br>= DnB maton ana)<br>• Can be associated with Health Checks + Canteen “gersit geeetn Cnc 20%<br>“angenop<br>• Use cases: load balancing between regions, testing  “Herotenat<br>new application versions… Amazon Weight: 20<br>Route 53<br>• Assign a weight of 0 to a record to stop<br>sending traffic to a resource<br>• If all records have weight of 0, then all records<br>will be returned equally<br>Weight: 10<br>70%<br>10%<br>NOT FOR DISTRIBUTION © Stephane Maarek www.datacumulus.com<br><!-- End of picture text -->

© Stephane Maarek 

#### Routing Policies – Latency-based 

- Redirect to the resource that has the least latency close to us Q 

- • Super helpful when latency for users is a priority 

- • Latency is based on traffic between users and AWS Regions ALB 

- **(us-east-1)** 

- • Germany users may be S \\ 

- directed to the US (if that’s the ALB 

- lowest latency) **(ap-southeast-1)** 

- Can be associated with Health Checks (has a failover capability) 

© Stephane Maarek 

#### Route 53 – Health Checks 

- HTTP Health Checks are only for public resources 

- Health Check => Automated DNS Failover: 1. Health checks that monitor an endpoint (application, server, other AWS resource) 

- 2. Health checks that monitor other health checks (Calculated Health Checks) 

- 3. Health checks that monitor CloudWatch Alarms (full control !!) – e.g., throttles of DynamoDB, alarms on RDS, custom metrics, … (helpful for private resources) 







Health Check 



us-east-1 



ALB 



Amazon Route 53 DNS Record (latency, geoproximity, …) Health Check 

eu-west-1 



ALB 



Auto Scaling group Auto Scaling group 

- Health Checks are integrated with CW metrics 





EC2 Instance EC2 Instance 

© Stephane Maarek 

#### Health Checks – Monitor an Endpoint 







Health Checker Health Checker Health Checker (us-east-1) (us-west-1) (sa-east-1) eu-west-1 **Must allow incoming requests from Route 53 Health Checkers IP address range** ALB 

- About 15 global health checkers will check the endpoint health • Healthy/Unhealthy Threshold – 3 (default) • Interval – 30 sec (can set to 10 sec – higher cost) • Supported protocol: HTTP,  HTTPS and TCP • If  > 18% of health checkers report the endpoint is healthy, Route 53 considers it Healthy . Otherwise, it’s Unhealthy 

- Ability to choose which locations you want Route 53 to use 

- • Health Checks pass only when the endpoint responds with the 2xx and 3xx status codes 

- Health Checks can be setup to pass / fail based on the text in the first 5120 bytes of the response 

- • Configure you router/firewall to allow incoming requests from Route 53 Health Checkers 



Auto Scaling group EC2 Instance 

<u>https://ip-ranges.amazonaws.com/ip-ranges.json</u> 

© Stephane Maarek 

#### Route 53 – Calculated Health Checks 

- Combine the results of multiple Health Checks into a single Health Check 

- You can use OR , AND , or NOT 

- Can monitor up to 256 Child Health Checks 

- Specify how many of the health checks need to pass to make the parent pass 

- Usage: perform maintenance to your website without causing all health checks to fail 

Amazon Route 53 Health Check **(Parent)** Health Check Health Check Health Check **(Child) (Child) (Child)** monitor monitor monitor EC2 Instance EC2 Instance EC2 Instance 

© Stephane Maarek 

#### Health Checks – Private Hosted Zones 

- Route 53 health checkers are outside the VPC 

- They can’t access private endpoints (private VPC or on-premises resource) 

- You can create a CloudWatch Metric and associate a CloudWatch Alarm , then create a Health Check that checks the alarm itself 

B® VPC Private subnet Health Checker (us-east-1) <mark>a</mark> ee: monitor ; monitor mi CloudWatch Alarm 

© Stephane Maarek 

Routing Policies – Failover (Active-Passive) 



<!-- Start of picture text -->
a<br><!-- End of picture text -->

EC2 Instance Health Check **(Primary) (mandatory)** DNS Requests Failover , Client Amazon Route 53 ~~a~~ : EC2 Instance **(Secondary – Disaster Recovery)** IE '”TS Ol ns 

© Stephane Maarek IE '”TS Ol 

#### Routing Policies – Geolocation 

- Different from Latency-based! 

- • This routing is based on user location • Specify location by Continent, Country or by US State (if there’s overlapping, most precise location selected) 

- • Should create a “Default” record (in case there’s no match on location) 

- • Use cases: website localization, restrict content distribution, load balancing, … 

- • Can be associated with Health Checks 



<!-- Start of picture text -->
A  11.22.33.44<br>Q<br>Netherlands<br>Belgium 7 Germany<br>Luxembourg Default<br>A  99.11.22.33<br>my Austria<br>France<br>Switzerland<br>e<br>A  55.66.77.88<br><!-- End of picture text -->

© Stephane Maarek 

#### Routing Policies – Geoproximity 

- Route traffic to your resources based on the geographic location of users and resources 

- Ability to shift more traffic to resources based on the defined bias 

- • To change the size of the geographic region, specify bias values: • To expand (1 to 99) – more traffic to the resource • To shrink (-1 to -99) – less traffic to the resource 

- • Resources can be: 

   - AWS resources (specify AWS region) 

   - • Non-AWS resources (specify Latitude and Longitude) 

- You must use Route 53 Traffic Flow to use this feature 

© Stephane Maarek 

#### Routing Policies – Geoproximity 



<!-- Start of picture text -->
a 8 A A A<br>us-west-1 us-east-1<br>Bias: 0 Bias: 0<br><!-- End of picture text -->

es 

© Stephane Maarek SE 

#### Routing Policies – Geoproximity 



<!-- Start of picture text -->
us-west-1 us-east-1<br>Bias: 0 Bias: 50<br>Higher bias in us-east-1<br>:<br>© Stephane Maarek<br>ta<br><!-- End of picture text -->

#### Routing Policies – IP-based Routing 

- Routing is based on clients’ IP addresses 

- Y ou provide a list of CIDRs for your clients and the corresponding endpoints/locations (user-IP-to-endpoint mappings) 

User B User A **(200.5.4.100) (203.0.113.56)** 









<!-- Start of picture text -->
Route 53<br><!-- End of picture text -->

###### **CIDR Collection** 

- Use cases: Optimize performance, reduce network costs… 

|**Locations**|**CIDR blocks**|
|---|---|
|location-1|203.0.113.0/24|
|location-2|200.5.4.0/24|



- Example: route end users from a particular ISP to a specific endpoint 

###### **Records** 

|**Record Name**|**Value**|**IP-based**|
|---|---|---|
|example.com|1.2.3.4|location-1|
|example.com|5.6.7.8|location-2|



EC2 Instance EC2 Instance **(5.6.7.8) (1.2.3.4)** 

© Stephane Maarek 

#### Routing Policies – Multi-Value 

- Use when routing traffic to multiple resources 

- Route 53 return multiple values/resources 

- Can be associated with Health Checks (return only values for healthy resources) 

- Up to 8 healthy records are returned for each Multi-Value query 

- Multi-Value is not a substitute for having an ELB 



<!-- Start of picture text -->
Name Type Value TTL Set ID Health Check<br>www.example.com A Record 192.0.2.2 60 Web1 A<br>www.example.com A Record 198.51.100.2 60 Web2 B<br>www.example.com A Record 203.0.113.2 60 Web3 Cc<br><!-- End of picture text -->

© Stephane Maarek 

#### Domain Registar vs. DNS Service 

- You buy or register your domain name with a Domain Registrar typically by paying annual charges (e.g., GoDaddy, Amazon Registrar Inc., …) 

- The Domain Registrar usually provides you with a DNS service to manage your DNS records 

- But you can use another DNS service to manage your DNS records 

• Example: purchase the domain from GoDaddy and use Route 53 to manage your DNS records purchase **example.com** manage DNS records (6) GoDaddy» J User Amazon Route 53 

© Stephane Maarek 

###### GoDaddy as Registrar & Route 53 as DNS Service 





<!-- Start of picture text -->
Records<br>We can't display your DNS information because your nameservers aren't<br>managed by us.<br>Nameservers<br>Using custom nameservers<br>Nameserver<br>ns-1083.awsdns-07.0rg<br>ns-932.awsdns-52.net<br>ns-1911.awsdns-46.co.uk<br>ns-481.awsdns-60.com<br><!-- End of picture text -->



Amazon Route 53 

**Public Hosted Zone** stephanetheteacher.com 



<!-- Start of picture text -->
¥ Hosted zone details Edit hosted zone<br>Hosted zone ID Type Name servers<br>ZBOIUICCWPKZUV Public hosted zone 1s-252.awsdns-31.com<br>1s-1468.awsdns-55.079<br>Record count, ne-633.avadne-1S:net<br>a tion —<br>DstedZonetn  created by Routes3 Registrar 22 1s-1800.awsdns-33.co.uk<br><!-- End of picture text -->

© Stephane Maarek 

3<sup>rd</sup> Party Registrar with Amazon Route 53 

- If you buy your domain on a 3<sup>rd</sup> party registrar, you can still use Route 53 as the DNS Service provider 

1. Create a Hosted Zone in Route 53 

2. Update NS Records on 3<sup>rd</sup> party website to use Route 53 Name Servers 

- Domain Registrar != DNS Service 

- But every Domain Registrar usually comes with some DNS features 

© Stephane Maarek 

### Classic Solutions Architecture 

© Stephane Maarek 

#### Section Introduction 

- These solutions architectures are the best part of this course 

- Let’s understand how all the technologies we’ve seen work together 

- This is a section you need to be 100% comfortable with 

- We’ll see the progression of a Solution’s architect mindset through many sample case studies: 

   - WhatIsTheTime.Com 

   - MyClothes.Com 

   - MyWordPress.Com 

   - Instantiating applications quickly 

   - Beanstalk 

© Stephane Maarek 

#### Stateless Web App: WhatIsTheTime.com 

- WhatIsTheTime.com allows people to know what time it is 

- We don’t need a database 

- We want to start small and can accept downtime 

- We want to fully scale vertically and horizontally, no downtime 

- Let’s go through the Solutions Architect journey for this app 

- Let’s see how we can proceed! 

© Stephane Maarek 

Stateless web app: What time is it? Starting simple Elastic IP Address What time is it? 5:30 pm! dnt User Public EC2 © Stephane Maarek IE'”TS Ol ns 

Stateless web app: What time is it? Scaling vertically What time is it? Elastic IP Address ~~Oe~~ 7:30 pm! What time is it? Downtime while upgrading to M5 5:30 pm! ~~<u>></u>~~ fm User What time is it? Public EC2 6:30 pm! © Stephane Maarek ~~<mark>|</mark>~~ 

Stateless web app: What time is it? Scaling horizontally What time is it? 7:30 pm! ~~a~~ {ms Fo What time is it? 5:30 pm! a8 User frafos What time is it? 6:30 pm! GR {ms fo © Stephane Maarek IE'”TS Ol ns 

Stateless web app: What time is it? Scaling horizontally What time is it? DNS Query Public EC2 instance, For api.whatisthetime.com No Elastic IP A Record TTL 1 hour 7:30 pm! a ~~n.~~ tek What time is it? 5:30 pm! B ~~<u>e</u>~~ <u>(6</u> What time is it? 6:30 pm! o ~~n~~ {ns} © Stephane Maarek ~~SE~~ ’”- Oh es 

Stateless web app: What time is it? Scaling horizontally, adding and removing instances What time is it? DNS Query For api.whatisthetime.com INSTANCE IS GONE! A Record B ~~Q.~~ TTL 1 hour 7:30 pm! What time is it? Public EC2 instance, No Elastic IP 5:30 pm! B ~~<u>s</u>~~ <u>(3</u> What time is it? 6:30 pm! o ~~n~~ {ns} © Stephane Maarek ~~SE~~ ’”- Oh es 

Stateless web app: What time is it? Scaling horizontally, with a load balancer What time is it? Availability zone 1 Availability zone 1 Restricted Security groups rules DNS Query ELB + For api.whatisthetime.com Health Checks Alias Record Private EC2 instances ra 8 © Stephane Maarek | 

Stateless web app: What time is it? Scaling horizontally, with an auto-scaling group What time is it? Availability zone 1 Availability zone 1 Auto Scaling group 3 on : i i DNS Query ELB + For api.whatisthetime.com Health Checks Alias Record — ms : Private gO EC2 instances © Stephane Maarek <mark>|</mark> 

Stateless web app: What time is it? Making our app multi-AZ Auto Scaling group What time is it? **Availability zone 1 to 3** Availability zone 1 a8ON Availability zone 2 DNS Query ELB + For api.whatisthetime.com Health Checks Alias Record Se @ + Multi AZ <mark>.</mark> Availability zone 3 # a 

© Stephane Maarek 

Minimum 2 AZ => Let’s reserve capacity Auto Scaling group **Availability zone 1 to 3** Availability zone 1 <mark>8</mark> Availability zone 2 DNS Query ELB + For api.whatisthetime.com Health Checks Alias Record + Multi AZ Minimum capacity = reserved instances = cost savings © Stephane Maarek ee| 

#### In this lecture we’ve discussed… 

- Public vs Private IP and EC2 instances 

- Elastic IP vs Route 53 vs Load Balancers 

- Route 53 TTL, A records and Alias Records 

- Maintaining EC2 instances manually vs Auto Scaling Groups 

- Multi AZ to survive disasters 

- ELB Health Checks 

- Security Group Rules 

- Reservation of capacity for costing savings when possible 

- • We’re considering 5 pillars for a well architected application: costs, performance, reliability, security, operational excellence 

© Stephane Maarek 

#### Stateful Web App: MyClothes.com 

- MyClothes.com allows people to buy clothes online. 

- There’s a shopping cart 

- Our website is having hundreds of users at the same time 

- We need to scale, maintain horizontal scalability and keep our web application as stateless as possible 

- Users should not lose their shopping cart 

- Users should have their details (address, etc) in a database 

- Let’s see how we can proceed! 

© Stephane Maarek 



<!-- Start of picture text -->
Stateful Web App: MyClothes.com<br>Auto Scaling group<br>Availability zone 1<br>Multi AZ<br>Availability zone 2<br>S c<br>Availability zone 3<br>He<br>© Stephane Maarek<br><!-- End of picture text -->



<!-- Start of picture text -->
Stateful Web App: MyClothes.com<br>Introduce Stickiness (Session Affinity)<br>Auto Scaling group<br>Availability zone 1<br>Multi AZ<br>Availability zone 2<br>A<br>ELB Stickiness<br><!-- End of picture text -->



<!-- Start of picture text -->
Availability zone 3<br><!-- End of picture text -->



© Stephane Maarek 



<!-- Start of picture text -->
Stateful Web App: MyClothes.com<br>Introduce User Cookies<br>Auto Scaling group<br>Availability zone 1<br>Multi AZ<br>Send shopping cart  Stateless<br>content in Web Cookies HTTP requests are heavier<br>Availability zone 2<br>Security risk<br>(cookies can be altered)<br>S c Cookies must be validated<br>Cookies must be less than 4KB<br>Availability zone 3<br>N es<br>© Stephane Maarek<br><!-- End of picture text -->

#### Stateful Web App: MyClothes.com Introduce Server Session 



<!-- Start of picture text -->
ElastiCache<br>Auto Scaling group<br>Availability zone 1<br>Multi AZ<br>Send session_id in<br>3 x<br>Web Cookies<br>Availability zone 2 Store / retrieve<br>session data<br>Availability zone 3<br>Amazon DynamoDB<br>(alternative)<br><!-- End of picture text -->

© Stephane Maarek 



<!-- Start of picture text -->
Stateful Web App: MyClothes.com<br>Storing User Data in a database<br>ElastiCache<br>Auto Scaling group<br>Availability zone 1<br>Multi AZ<br>a ea<br>Availability zone 2<br>Store / retrieve user data<br>(address, name, etc)<br>COf Fso<br>Availability zone 3<br>Amazon RDS<br><!-- End of picture text -->

© Stephane Maarek 



<!-- Start of picture text -->
Stateful Web App: MyClothes.com<br>Scaling Reads<br>ElastiCache<br>Auto Scaling group<br>Availability zone 1<br>Multi AZ<br>Availability zone 2 RDS<br>Master<br>8 (writes)<br>Ra 8so «£<br>replication<br>Availability zone 3<br>RDS<br>Read Replicas<br>© Stephane Maarek<br><!-- End of picture text -->



<!-- Start of picture text -->
Stateful Web App: MyClothes.com<br>Scaling Reads (Alternative) – Lazy Loading<br>ElastiCache<br>Auto Scaling group<br>Availability zone 1 cache<br>Multi AZ<br>S a<br>hit<br>Availability zone 2 Read from cache<br>S Bs .<br>Read/write<br>Availability zone 3<br>RDS<br><!-- End of picture text -->

© Stephane Maarek 



<!-- Start of picture text -->
Stateful Web App: MyClothes.com<br>Multi AZ – Survive disasters<br>ElastiCache<br>Auto Scaling group Multi AZ<br>Availability zone 1<br>Multi AZ<br>Availability zone 2<br>A O ff 2 |<br>Availability zone 3<br>RDS<br>Multi AZ<br><!-- End of picture text -->

© Stephane Maarek 



<!-- Start of picture text -->
Stateful Web App: MyClothes.com<br>Security Groups<br>Restrict traffic to ElastiCache<br>Security group from the<br>EC2 security group<br>Auto Scaling group<br>Availability zone 1 ElastiCache<br>Multi AZ<br>Open HTTP / HTTPS<br>to 0.0.0.0/0 o es<br>Availability zone 2<br>RDS<br>SL 8 go |<br>Availability zone 3<br>Restrict traffic to RDS<br>Restrict traffic to EC2<br>Security group from the<br>Security group from the LB<br>EC2 security group<br>S P<br><!-- End of picture text -->

© Stephane Maarek 

|In this lecture we’ve discussed…|
|---|
|3-tier architectures for web applications|
|• ELB sticky sessions|
|• Web clients for storing cookies and making our web app stateless|
|• ElastiCache<br>• For storing sessions (alternative: DynamoDB)<br>• For caching data from RDS<br>• Multi AZ|
|• RDS|
|• For storing user data<br>• Read replicas for scaling reads<br>• Multi AZ for disaster recovery|
|• Tight Security with security groups referencing each other|



© Stephane Maarek 

#### Stateful Web App: MyWordPress.com 

- We are trying to create a fully scalable WordPress website 

- We want that website to access and correctly display picture uploads 

- Our user data, and the blog content should be stored in a MySQL database. 

- Let’s see how we can achieve this! 

© Stephane Maarek 



<!-- Start of picture text -->
Stateful Web App: MyWordPress.com<br>RDS layer<br>Auto Scaling group<br>Availability zone 1<br>Multi AZ<br>Availability zone 2<br>,om 8 :<br>RDS<br>Multi AZ<br>Availability zone 3<br><!-- End of picture text -->

© Stephane Maarek 

|Stateful Web App: MyWordPress.com<br>Scaling with Aurora: Multi AZ & Read Replicas<br>Auto Scaling group|**NOT FOR DISTRIBUTION**|
|---|---|
|© Stephane Maarek<br>**Multi AZ**<br>Availability zone 1<br>Availability zone 2<br>Availability zone 3<br>Aurora MySQL<br>Multi AZ<br>Read Replicas<br>lan"ies<br>Nes|**© Stephane Maarekwww.datacumulus.com**|



Stateful Web App: MyWordPress.com Storing images with EBS **Multi AZ** Availability zone 1 **Amazon EBS Volume** <mark>5m</mark> Send image ~~<mark>@</mark>~~ © Stephane Maarek <mark>|</mark> 

Stateful Web App: MyWordPress.com Storing images with EBS Availability zone 1 **Multi AZ Amazon EBS Volume** Availability zone 2 [i Send image <mark>e</mark> **Amazon EBS Volume** © Stephane Maarek ~~<mark>a</mark>~~ | 

ns 

Stateful Web App: MyWordPress.com Storing images with EFS Availability zone 1 **Multi AZ** ENI Send image Availability zone 2 EFS <mark>(8,</mark> ENI tf: <mark>&</mark> © Stephane Maarek Ia '”TS Ol <mark>E</mark> ns 

In this lecture we’ve discussed… 

• Aurora Database to have easy Multi-AZ and Read-Replicas • Storing data in EBS (single instance application) • Vs Storing data in EFS (distributed application) 

© Stephane Maarek 

#### Instantiating Applications quickly 

- When launching a full stack (EC2, EBS, RDS), it can take time to: 

   - Install applications 

   - Insert initial (or recovery) data 

   - Configure everything 

   - Launch the application 

- We can take advantage of the cloud to speed that up! 

© Stephane Maarek 

#### Instantiating Applications quickly 

- EC2 Instances: 

   - Use a Golden AMI: Install your applications, OS dependencies etc.. beforehand and launch your EC2 instance from the Golden AMI 

   - Bootstrap using User Data: For dynamic configuration, use User Data scripts 

   - • Hybrid: mix Golden AMI and User Data (Elastic Beanstalk) 

- RDS Databases: 

   - Restore from a snapshot: the database will have schemas and data ready! 

- EBS Volumes: 

   - Restore from a snapshot: the disk will already be formatted and have data! 

© Stephane Maarek 



<!-- Start of picture text -->
Typical architecture: Web App 3-tier<br>Route 53<br>ElastiCache<br>Auto Scaling group<br>Availability zone 1<br>Multi AZ<br>Store / retrieve<br>session data<br>Availability zone 2<br>+ Cached data<br>a a -<br>ELB<br>Availability zone 3<br>gf Amazon RDS<br>Read / write data<br>PUBLIC SUBNET PRIVATE SUBNET DATA SUBNET<br>© Stephane Maarek<br>IE '”TS Ol ns<br>NOT FOR DISTRIBUTION © Stephane Maarek www.datacumulus.com<br><!-- End of picture text -->

© Stephane Maarek IE '”TS Ol 

#### Developer problems on AWS 

- Managing infrastructure 

- Deploying Code 

- Configuring all the databases, load balancers, etc 

- Scaling concerns 

- Most web apps have the same architecture (ALB + ASG) 

- All the developers want is for their code to run! 

- Possibly, consistently across different applications and environments 

© Stephane Maarek 

#### Elastic Beanstalk – Overview 



- Elastic Beanstalk is a developer centric view of deploying an application on AWS 

- It uses all the component’s we’ve seen before: EC2, ASG, ELB, RDS, … 

- Managed service 

   - Automatically handles capacity provisioning, load balancing, scaling, application health monitoring, instance configuration, … 

   - Just the application code is the responsibility of the developer 

- We still have full control over the configuration 

• Beanstalk is free but you pay for the underlying instances © Stephane Maarek IE'”TS Ol ns 

#### Elastic Beanstalk – Components 

- Application: collection of Elastic Beanstalk components (environments, versions, configurations, …) 

- Application Version: an iteration of your application code 

- Environment 

   - Collection of AWS resources running an application version (only one application version at a time) 

   - Tiers: Web Server Environment Tier & Worker Environment Tier 

   - You can create multiple environments (dev, test, prod, …) 

###### update version 

Create Upload Launch Manage Application Version Environment Environment 

###### deploy new version 

© Stephane Maarek 

#### Elastic Beanstalk – Supported Platforms 

- Go 

- Java SE 

- Java with Tomcat 

- .NET Core on Linux 

- .NET on Windows Server 

   - Ruby 

   - Packer Builder 

   - Single Container Docker 

   - Multi-container Docker 

   - Preconfigured Docker 

- Node.js 

- PHP 

- Python 

© Stephane Maarek 

#### Web Server Tier vs. Worker Tier 



<!-- Start of picture text -->
Web Environment<br>Worker Environment<br>(myapp.us-east-1.elasticbeanstalk.com)<br>SQS Queue<br>ELB<br>Availability Zone 1 Availability Zone 2 Availability Zone 1 Availability Zone 2<br>SQS message SQS message<br>pull<br>messages<br>Security Group Security Group<br>Auto Scaling group<br>Auto Scaling group<br>EC2 Instance EC2 Instance<br>EC2 Instance EC2 Instance<br>(Worker) (Worker)<br>(Web Server) (Web Server)<br><!-- End of picture text -->

- Scale based on the number of SQS messages 

- • Can push messages to SQS queue from another Web Server Tier 

© Stephane Maarek 

#### Elastic Beanstalk Deployment Modes 



<!-- Start of picture text -->
High Availability with Load Balancer<br>Single Instance<br>Great for dev Great for prod<br>Availability Zone 1<br>Availability Zone 1 ALB Availability Zone 2<br>Elastic IP<br>Auto Scaling Group<br>inal EC2 Instance gf. EC2 Instance EC2 Instance<br>RDS Master RDS Master RDS Standby<br><!-- End of picture text -->

© Stephane Maarek 

### Amazon S3 

© Stephane Maarek 

ns 

#### Section introduction 



<!-- Start of picture text -->
S<br><!-- End of picture text -->

- Amazon S3 is one of the main building blocks of AWS 

- It’s advertised as ”infinitely scaling” storage 

- Many websites use Amazon S3 as a backbone 

- Many AWS services use Amazon S3 as an integration as well 

- We’ll have a step-by-step approach to S3 

© Stephane Maarek IE '”TS Ol 

#### Amazon S3 Use cases 

- Backup and storage 

- Disaster Recovery 

- Archive 

- Hybrid Cloud storage 

- Application hosting 

- Media hosting 

- Data lakes & big data analytics 

- Software delivery 

- Static website 

Nasdaq stores 7 years of data into S3 Glacier 



<!-- Start of picture text -->
Sysco<br><!-- End of picture text -->

Sysco runs analytics on its data and gain business insights 

© Stephane Maarek EES 

#### Amazon S3 - Buckets 

- Amazon S3 allows people to store objects (files) in “buckets” (directories) 

- Buckets must have a globally unique name (across all regions all accounts) 

- Buckets are defined at the region level 

- S3 looks like a global service but buckets are created in a region 

- Naming convention 

   - No uppercase, No underscore 

 No uppercase, No underscore • 3-63 characters long • Not an IP • Must start with lowercase letter or number • Must NOT start with the prefix xn-S3 Bucket<sup>~</sup> • Must NOT end with the suffix -s3alias © Stephane Maarek IE'”TS Ol ns 

> <sup>©</sup> Object S3 Bucket with Objects 

#### Amazon S3 - Objects 

   - Objects (files) have a Key • The key is the FULL path: • s3://my-bucket/ my_file.txt 

- s3://my-bucket/ my_folder1/another_folder/my_file.txt 

- • The key is composed of prefix + object name • s3://my-bucket/ my_folder1/another_folder/my_file.txt 

- • There’s no concept of “directories” within buckets (although the UI will trick you to think otherwise) S3 Bucket 

- • Just keys with very long names that contain slashes (“/”) with Objects 

- © Stephane Maarek 

- IE'”TS Ol ns 

es 

Amazon S3 – Objects (cont.) 



<!-- Start of picture text -->
OC)<br><!-- End of picture text -->

- Object values are the content of the body: 

   - Max. Object Size is 5TB (5000GB) 

   - If uploading more than 5GB, must use “multi-part upload” 

- Metadata (list of text key / value pairs – system or user metadata) • Tags (Unicode key / value pair – up to 10) – useful for security / lifecycle 

- Version ID (if versioning is enabled) 

© Stephane Maarek EES 

#### Amazon S3 – Security 

- User-Based 

   - IAM Policies – which API calls should be allowed for a specific user from IAM 

- Resource-Based 

   - Bucket Policies – bucket wide rules from the S3 console - allows cross account 

   - Object Access Control List (ACL) – finer grain (can be disabled) 

   - Bucket Access Control List (ACL) – less common (can be disabled) 

- Note: an IAM principal can access an S3 object if 

   - The user IAM permissions ALLOW it OR the resource policy ALLOWS it 

   - <u>AND</u> there’s no explicit DENY 

- Encryption: encrypt objects in Amazon S3 using encryption keys 

© Stephane Maarek 

#### S3 Bucket Policies 

- JSON based policies 

   - Resources: buckets and objects 

   - • Effect: Allow / Deny 

   - Actions: Set of API to Allow or Deny 

   - • Principal: The account or user to apply the policy to 

- Use S3 bucket for policy to: • Grant public access to the bucket 

   - Force objects to be encrypted at upload 

   - • Grant access to another account (Cross Account) 



<!-- Start of picture text -->
{<br>"Version": "2012-10-17",<br>"Statement": [<br>{<br>"Sid": "PublicRead",<br>"Effect": "Allow",<br>"Principal": "x",<br>"Action": [<br>"s3:GetObject"<br>],<br>"Resource": [<br>“arn:awsS:S3:::examplebucket/*"<br>]<br>+<br>]<br>+<br><!-- End of picture text -->

© Stephane Maarek 

Example: Public Access - Use Bucket Policy S3 Bucket Policy Allows Public Access Anonymous www website visitor **S3 Bucket** <mark>5</mark> § © Stephane Maarek IE'”TS Ol ns 

Example: User Access to S3 – IAM permissions IAM Policy IAM User **S3 Bucket** ~~<mark>A</mark> 8~~ © Stephane Maarek IE'”TS Ol ns 

ns 

Example: EC2 instance access - Use IAM Roles 

IAM permissions **EC2 Instance Role** EC2 Instance TN 



###### **S3 Bucket** 

© Stephane Maarek IE '”TS Ol 

Advanced: Cross-Account Access – Use Bucket Policy S3 Bucket Policy Allows Cross-Account **IAM User Other AWS account S3 Bucket** ~~<mark>,</mark> §~~ © Stephane Maarek IE'”TS Ol ns 

#### Bucket settings for Block Public Access 



<!-- Start of picture text -->
Block all public access<br>On<br>Block public access to buckets and objects granted through new access control lists (ACLs)<br>On<br>Block public access to buckets and objects granted through any access control lists (ACLs)<br>On<br>Block public access to buckets and objects granted through new public bucket or access point policies<br>On<br>Block public and cross-account access to buckets and objects through any public bucket or access point policies<br>On<br><!-- End of picture text -->

- These settings were created to prevent company data leaks 

- If you know your bucket should never be public, leave these on 

- Can be set at the account level 

© Stephane Maarek 

Amazon S3 – Static Website Hosting 

- S3 can host static websites and have them accessible on the Internet 



<!-- Start of picture text -->
User<br><!-- End of picture text -->

**http://demo-bucket.s3-website-us-west-2.amazonaws.com http://demo-bucket.s3-website.us-west-2.amazonaws.com** 

- The website URL will be (depending on the region) 

   - http:// _bucket-name_ .s3-website- _aws-region_ .amazonaws.com 

   - OR 

- http:// _bucket-name_ .s3-website. _aws-region_ .amazonaws.com 

- • If you get a 403 Forbidden error, make sure the bucket policy allows public reads! 





<!-- Start of picture text -->
us-west-2<br><!-- End of picture text -->



S3 Bucket **(demo-bucket)** 

© Stephane Maarek 

ns 

Amazon S3 - Versioning User Q • You can version your files in Amazon S3 • It is enabled at the bucket level upload • Same key overwrite will change the “version”: 1, 2, 3…. " • It is best practice to version your buckets • Protect against unintended deletes (ability to restore a version) S3 Bucket (my-bucket) SO • Easy roll back to previous version Version 1 Version 2 • Notes: Version 3 • Any file that is not versioned prior to enabling versioning will <mark>8</mark> have version “null” s3://my-bucket/my-file.docx • Suspending versioning does not delete the previous versions '”TS Ol ns 

© Stephane Maarek IE '”TS Ol 

Amazon S3 – Replication (CRR & SRR) is • Must enable Versioning in source and destination buckets • Cross-Region Replication (CRR) S3 Bucket • Same-Region Replication (SRR) **(eu-west-1)** • Buckets can be in different AWS accounts S, • Copying is asynchronous asynchronous • Must give proper IAM permissions to S3 replication • Use cases: • CRR – compliance, lower latency access, replication across S3 Bucket accounts **(us-east-2)** • SRR – log aggregation, live replication between production and test : accounts © Stephane Maarek IE'”TS Ol ns 

#### Amazon S3 – Replication (Notes) 

- After you enable Replication, only new objects are replicated 

- Optionally, you can replicate existing objects using S3 Batch Replication 

   - Replicates existing objects and objects that failed replication 

- For DELETE operations 

   - Can replicate delete markers from source to target (optional setting) 

   - Deletions with a version ID are not replicated (to avoid malicious deletes) 

- There is no “chaining” of replication 

   - If bucket 1 has replication into bucket 2, which has replication into bucket 3 

   - Then objects created in bucket 1 are not replicated to bucket 3 

© Stephane Maarek 

|S3 Storage Classes|
|---|



|•Amazon S3 Standard - General Purpose|
|---|
|•Amazon S3 Standard-Infrequent Access (IA)|
|•Amazon S3 One Zone-Infrequent Access|
|•Amazon S3 Glacier Instant Retrieval|
|•Amazon S3 Glacier Flexible Retrieval|
|•Amazon S3 Glacier Deep Archive|
|•Amazon S3 Intelligent Tiering|
|•Can move between classes manually or using S3 Lifecycle configurations|



© Stephane Maarek 

#### S3 Durability and Availability 

- Durability: 

   - High durability (99.999999999%, 11 9’s) of objects across multiple AZ 

   - • If you store 10,000,000 objects with Amazon S3, you can on average expect to incur a loss of a single object once every 10,000 years 

   - • Same for all storage classes 

- Availability: 

   - Measures how readily available a service is 

   - Varies depending on storage class 

   - Example: S3 standard has 99.99% availability = not available 53 minutes a year 

© Stephane Maarek 

|S3 Standard – General Purpose|
|---|





<!-- Start of picture text -->
is,<br><!-- End of picture text -->

|•99.99% Availability|
|---|
|•Used for frequently accessed data|
|•Low latency and high throughput|
|•Sustain 2 concurrent facility failures|



• Use Cases: Big Data analytics, mobile & gaming applications, content distribution… © Stephane Maarek IE'”TS Ol ns 

|S3 Storage Classes – Infrequent Access|
|---|



- For data that is less frequently accessed, but requires rapid access when needed 

- Lower cost than S3 Standard 

|• Amazon S3 Standard-Infrequent Access (S3 Standard-IA)|
|---|



- 99.9% Availability 

- Use cases: Disaster Recovery, backups 



<!-- Start of picture text -->
&<br><!-- End of picture text -->

- Amazon S3 One Zone-Infrequent Access (S3 One Zone-IA) • High durability (99.999999999%) in a single AZ; data lost when AZ is destroyed • 99.5% Availability : 

- • Use Cases: Storing secondary backup copies of on-premises data, or data you can recreate 

- © Stephane Maarek 

- IE'”TS Ol ns 

#### Amazon S3 Glacier Storage Classes 

- Low-cost object storage meant for archiving / backup 

- Pricing: price for storage + object retrieval cost 

- Amazon S3 Glacier Instant Retrieval 

   - Millisecond retrieval, great for data accessed once a quarter 

   - Minimum storage duration of 90 days 

- Amazon S3 Glacier Flexible Retrieval (formerly Amazon S3 Glacier): • Expedited (1 to 5 minutes), Standard (3 to 5 hours), Bulk (5 to 12 hours) – free • Minimum storage duration of 90 days 

- Amazon S3 Glacier Deep Archive – for long term storage: 

   - Standard (12 hours), Bulk (48 hours) 

   - Minimum storage duration of 180 days 



<!-- Start of picture text -->
te<br><!-- End of picture text -->



<!-- Start of picture text -->
G&<br><!-- End of picture text -->



© Stephane Maarek 

|S3 Intelligent-Tiering|
|---|





<!-- Start of picture text -->
&<br><!-- End of picture text -->

- Small monthly monitoring and auto-tiering fee 

- Moves objects automatically between Access Tiers based on usage 

- There are no retrieval charges in S3 Intelligent-Tiering 

- _Frequent Access tier (automatic):_ default tier 

- _Infrequent Access tier (automatic)_ : objects not accessed for 30 days 

- _Archive Instant Access tier (automatic):_ objects not accessed for 90 days 

• _Archive Access tier (optional):_ configurable from 90 days to 700+ days • _Deep Archive Access tier (optional):_ config. from 180 days to 700+ days © Stephane Maarek IE'”TS Ol ns 

#### S3 Storage Classes Comparison 

||**Standard**|**Intelligent-**<br>**Tiering**|**Standard-IA**|**One Zone-IA**|**Glacier Instant**<br>**Retrieval**|**Glacier Flexible**<br>**Retrieval**|**Glacier Deep**<br>**Archive**|
|---|---|---|---|---|---|---|---|
|Durability|||99.|999999999% == (1|1 9’s)|||
|Availability|99.99%|99.9%|99.9%|99.5%|99.9%|99.99%|99.99%|
|Availability SLA|99.9%|99%|99%|99%|99%|99.9%|99.9%|
|Availability<br>Zones|>= 3|>= 3|>= 3|1|>= 3|>= 3|>= 3|
|Min. Storage<br>Duration Charge|None|None|30 Days|30 Days|90 Days|90 Days|180 Days|
|Min. Billable<br>Object Size|None|None|128 KB|128 KB|128 KB|40 KB|40 KB|
|Retrieval Fee|None|None|Per GB retrieved|Per GB retrieved|Per GB retrieved|Per GB retrieved|Per GB retrieved|



<u>https://aws.amazon.com/s3/storage-classes/</u> 

© Stephane Maarek 

#### S3 Storage Classes – Price Comparison Example: us-east-1 

||**Standard**|**Intelligent-Tiering**|**Standard-IA**|**One Zone-IA**|**Glacier Instant**<br>**Retrieval**|**Glacier Flexible**<br>**Retrieval**|**Glacier Deep**<br>**Archive**|
|---|---|---|---|---|---|---|---|
|Storage Cost<br>(per GB per month)|$0.023|$0.0025 - $0.023|$0.0125|$0.01|$0.004|$0.0036|$0.00099|
|Retrieval Cost|**GET:**$0.0004|**GET:**$0.0004|**GET:**$0.001|**GET:**$0.001|**GET:**$0.01|**GET:**$0.0004<br>**POST:**$0.03|**GET:**$0.0004<br>**POST:**$0.05|
|(per 1000 request)|**POST:**$0.005|**POST:**$0.005|**POST:**$0.01|**POST:**$0.01|**POST:**$0.02|**Expedited:**$10<br>**Standard:**$0.05<br>**Bulk:**free|**Standard:**$0.10<br>**Bulk:**$0.025|
|Retrieval Time||I|nstantaneous|||**Expedited**(1 – 5 mins)<br>**Standard**(3 – 5 hours)<br>Bulk (5 – 12 hours)|**Standard**(12 hours)<br>**Bulk**(48 hours)|
|Monitoring Cost<br>(pet 1000 objects)||$0.0025||||||
||||||https://<br>|aws.amazon.com/s3|/pricing/|



© Stephane Maarek 

### Amazon S3 – Advanced 

© Stephane Maarek 

Amazon S3 – Moving between Storage Classes 

- You can transition objects between storage classes 

- For infrequently accessed object, move them to Standard IA 

- For archive objects that you don’t need fast access to, move them to Glacier or Glacier Deep Archive 

- Moving objects can be automated using a Lifecycle Rules 





Standard Standard IA Intelligent Tiering One-Zone IA Glacier Instant Retrieval Glacier Flexible Retrieval Glacier Deep Archive 

es 

© Stephane Maarek EES 

#### Amazon S3 – Lifecycle Rules 



<!-- Start of picture text -->
O<br><!-- End of picture text -->

- Transition Actions – configure objects to transition to another storage class 

   - Move objects to Standard IA class 60 days after creation 

   - Move to Glacier for archiving after 6 months 

- Expiration actions – configure objects to expire (delete) after some time 

   - Access log files can be set to delete after a 365 days 

   - Can be used to delete old versions of files (if versioning is enabled) 

   - Can be used to delete incomplete Multi-Part uploads 

- Rules can be created for a certain prefix (example: _s3://mybucket/mp3/*)_ 

- Rules can be created for certain objects Tags (example: _Department: Finance_ ) 

© Stephane Maarek IE '”TS Ol ns 

#### Amazon S3 – Lifecycle Rules (Scenario 1) 

- Your application on EC2 creates images thumbnails after profile photos are uploaded to Amazon S3. These thumbnails can be easily recreated, and only need to be kept for 60 days. The source images should be able to be immediately retrieved for these 60 days, and afterwards, the user can wait up to 6 hours. How would you design this? 

- S3 source images can be on Standard , with a lifecycle configuration to transition them to Glacier after 60 days 

- S3 thumbnails can be on One-Zone IA , with a lifecycle configuration to expire them (delete them) after 60 days 

© Stephane Maarek 

#### Amazon S3 – Lifecycle Rules (Scenario 2) 

- A rule in your company states that you should be able to recover your deleted S3 objects immediately for 30 days, although this may happen rarely. After this time, and for up to 365 days, deleted objects should be recoverable within 48 hours. 

- E nable S3 Versioning in order to have object versions, so that “deleted objects” are in fact hidden by a “delete marker” and can be recovered 

- Transition the “noncurrent versions” of the object to Standard IA 

- Transition afterwards the “noncurrent versions” to Glacier Deep Archive 

© Stephane Maarek 

#### Amazon S3 Analytics – Storage Class Analysis 

|•Help you decide when to transition objects to<br>the right storage class||S3 Bucket|
|---|---|---|
|•Recommendations forStandardandStandard<br>IA<br>• Does NOT work for One-Zone IA or Glacier<br>•Report is updated daily||S3 Analytics|
|•24 to 48 hours to start seeing data analysis||**.csv**report|
|•Good first step to put together Lifecycle Rules<br>|**Date**|**StorageClass**<br>**ObjectAge**|
|(or improve them)!|8/22/2022<br>8/25/2022|STANDARD<br>000-014<br>STANDARD<br>030-044|
||9/6/2022|STANDARD<br>120-149|



© Stephane Maarek 

es 

#### S3 – Requester Pays 

## **Standard Bucket** • In general, bucket owners pay for all **<u>Owner Owner Requester</u>** Amazon S3 storage and data transfer $$ Storage Cost $$ Networking Cost costs associated with their bucket download • With Requester Pays buckets , the ~~<mark>eles</mark>~~ requester instead of the bucket owner pays the cost of the request and the **Requester Pays Bucket** data download from the bucket 

- With Requester Pays buckets , the requester instead of the bucket owner pays the cost of the request and the data download from the bucket 

- Helpful when you want to share large datasets with other accounts 

- The requester must be authenticated in AWS (cannot be anonymous) 

**<u>Owner Requester</u>** $$ Storage Cost $$ Networking Cost download 

© Stephane Maarek EES 

#### S3 Event Notifications 

• S3:ObjectCreated, S3:ObjectRemoved, Gf S3:ObjectRestore, S3:Replication… • Object name filtering possible (*.jpg) SNS • <u>Use case: generate thumbnails of images</u> events uploaded to S3 on Se • Can create as many “S3 events” as desired SQS Amazon S3 • S3 event notifications typically deliver events in seconds but can sometimes take a minute ° or longer Lambda Function IE '”TS Ol ns 

© Stephane Maarek IE '”TS Ol 

#### S3 Event Notifications – IAM Permissions 



<!-- Start of picture text -->
{<br>"Version": "2012-10-17", v<br>“Statement”: { iS<br>"Effect": "Allow", x<br>--------2---0--- “Principal: {<br>VY "Action":"Service":"SNS:Publish","s3.amazonaws.com"<br>he<br>"Resource": “arn:aws:sns:us—east-1: 123456789012 :MyTopic™,<br>"Condition": {<br>SNS “AarnLike"s { {<br>“aws:SourceArn": "arn:aws:s3:::MyBucket" "Version": "2012-10-17", v<br>} , "Statement": { ¥<br>} "Effect": "Allow", x<br>} "Action": "SQS:SendMessage",<br>SNS Resource (Access) Policy<br>"Principal": {<br>"Service": "s3.amazonaws.com"<br>events (aN m<br>for) m (Xe) i "Resource": “arn:aws:sqstus-east-1: 123456789012 :MyQueue",<br>Ca "Condition":"ArnLike": {{<br>“aws:SourceArn": “arn:aws:s3:::MyBucket"<br>SQS { }<br>Amazon S3 "Version": "2012-10-17", v }<br>"statement": { v }<br>"Effect": "Allow", x } SQS Resource (Access) Policy<br>"action": "Lambda: InvokeFunction",<br>"Principal": {<br>"Service": "s3.amazonaws.<br>}, com"<br>function:MyFunction,<br>/) eee | "Resource":"Condition": “arn:aws:{  lambda: us—east-1: 123456789012:<br>“ArnLike": {<br>“AWS:SourceArn": “arn:aws:s3:::MyBucket"<br>Lambda Function +<br>+<br>+ } Lambda Resource Policy<br><!-- End of picture text -->

© Stephane Maarek 

S3 Event Notifications with Amazon EventBridge 

events All events rules Over 18 AWS services as destinations ~~6B Amazon S3 Amazon bucket EventBridge 

• Advanced filtering options with JSON rules (metadata, object size, name...) 

- Multiple Destinations – ex Step Functions, Kinesis Streams / Firehose… 

• EventBridge Capabilities – Archive, Replay Events, Reliable delivery © Stephane Maarek IE '”TS Ol ns 

#### S3 – Baseline Performance 

- Amazon S3 automatically scales to high request rates, latency 100-200 ms 

- Your application can achieve at least 3,500 PUT/COPY/POST/DELETE or 5,500 GET/HEAD requests per second per prefix in a bucket. 

- There are no limits to the number of prefixes in a bucket. 

- <u>Example (object path => prefix):</u> 

   - bucket/folder1/sub1/file  => /folder1/sub1/ 

   - bucket/folder1/sub2/file  => /folder1/sub2/ 

   - bucket/1/file                  => /1/ 

   - bucket/2/file                  => /2/ 

- If you spread reads across all four prefixes evenly, you can achieve 22,000 requests per second for GET and HEAD 

© Stephane Maarek 

#### S3 Performance 

      - S3 Transfer Acceleration 

- Multi-Part upload: 

   - recommended for files > 100MB, must use for files > 5GB 

- Increase transfer speed by transferring file to an AWS edge location which will forward the data to the S3 bucket in the target region 

forward the data to the S3 bucket in the • Can help parallelize uploads (speed target region up transfers) • Compatible with multi-part upload Divide Parallel uploads In parts Fast Fast (public www) (private AWS) File in USA **Edge Location S3 Bucket** Amazon S3 USA Australia BIG file Dem ° * @ © Stephane Maarek IE'”TS Ol ns 

#### S3 Performance – S3 Byte-Range Fetches 

- Parallelize GETs by requesting specific byte ranges 

- Better resilience in case of failures 

<u>Can be used to speed up downloads</u> 



<!-- Start of picture text -->
File in S3<br>Part 1 Part 2 … Part N<br>Requests in parallel<br><!-- End of picture text -->

<u>Can be used to retrieve only partial data (for example the head of a file)</u> File in S3 Byte-range request for header (first XX bytes) header 

© Stephane Maarek 

#### S3 Select & Glacier Select 

- Retrieve less data using SQL by performing server-side filtering • Can filter by rows & columns (simple SQL statements) 

- Less network transfer, less CPU cost client-side 



<!-- Start of picture text -->
CSV file<br>“ 19%! YG |<br>40 OG Sores «| | Get CSV with S3 Select<br>Amazon S3 Seece ene nene n een eeen n nnn n ene eee! en i)<br>Up to 400% Faster i ————————— Send filtered dataset<br>$3 Select prvsersecons<br>Amazon S3<br>Amazon S3 Up ia auchcaper<br>Server-side filtering<br><!-- End of picture text -->

<u>https://aws.amazon.com/blogs/aws/s3-glacier-select/</u> 

© Stephane Maarek 

#### S3 Batch Operations 

S3 Inventory • Perform bulk operations on existing S3 objects with a single request, example: • Modify object metadata & properties Objects List Report • Copy objects between S3 buckets • Encrypt un-encrypted objects • Modify ACLs, tags S3 Select • Restore objects from S3 Glacier filter • Invoke Lambda function to perform custom action on each object filtered list • A job consists of a list of objects, the action to operation + perform, and optional parameters parameters S3 Batch • S3 Batch Operations manages retries, tracks progress, sends completion notifications, generate reports … Operations User • You can use S3 Inventory to get object list and use S3 Select to filter your objects Processed Objects … 

© Stephane Maarek 

#### S3 – Storage Lens 



- Understand, analyze, and optimize storage across entire AWS Organization 

- • Discover anomalies, identify cost efficiencies, and apply data protection best practices across entire AWS Organization (30 days usage & activity metrics) 

- Aggregate data for Organization, specific accounts, regions, buckets, or prefixes 

- • Default dashboard or create your own dashboards 

- Can be configured to export metrics daily to an S3 bucket (CSV, Parquet) 



<!-- Start of picture text -->
Organization<br>Summary Insights<br>Accounts<br>Data Protection<br>S —<br>S3 Storage Lens Regions<br>eg Ee © | a<br>Cost Efficiency<br>Buckets<br>S =<br>Configure Aggregate Analyze Optimize<br>(Dashboard)<br>© Stephane Maarek<br>IE '”TS Ol ns<br><!-- End of picture text -->

© Stephane Maarek IE '”TS Ol 

#### Storage Lens – Default Dashboard 



- Visualize summarized insights and trends for both free and advanced metrics 

- Default dashboard shows Multi-Region and Multi-Account data 

- Preconfigured by Amazon S3 

- Can’t be deleted, but can be disabled 



<!-- Start of picture text -->
Amazons8 > Sgttem > sande<br>s3-lens-demo (we aera coniuration |] amore<br>+ ites<br>counts Regions staage dass<br>araslces Poses rales<br>lect acts sec<br>stRegans Sect ore aes<br>oussrsslces PretoesSasleces<br>Selecttlbuckets Select al prefies<br>pees Mi ui<br><!-- End of picture text -->

<u>https://aws.amazon.com/blogs/aws/s3-storage-lens/</u> 



<!-- Start of picture text -->
Onrew | Act | tos | sorpecn | suet | ret<br>Snapshot<br>for Oct 19,2020<br>68.4 TB 836.9k 85.7 MB 3 2 894M<br>see secungeco<br>—=--— ==] oe i<br>a ae bon omnes sodeytend<br>Totalstorage eae a TT<br>Object count 369k ——————<br>ee 3900 game<br>uae 5 o-<br>pes 2 a<br>Alrequests even om TT<br><!-- End of picture text -->

<u>https://aws.amazon.com/blogs/aws/s3-storage-lens/</u> 

© Stephane Maarek 

#### Storage Lens – Metrics 



<!-- Start of picture text -->
oS<br><!-- End of picture text -->

- Summary Metrics 

   - General insights about your S3 storage 

   - • StorageBytes, ObjectCount… 

   - Use cases: identify the fastest-growing (or not used) buckets and prefixes 

- Cost-Optimization Metrics 

   - Provide insights to manage and optimize your storage costs 

   - NonCurrentVersionStorageBytes, IncompleteMultipartUploadStorageBytes… 

• Use cases: identify buckets with incomplete multipart uploaded older than 7 days, Identify which objects could be transitioned to lower-cost storage class © Stephane Maarek IE'”TS Ol ns 

#### Storage Lens – Metrics 



<!-- Start of picture text -->
oS<br><!-- End of picture text -->

- Data-Protection Metrics 

   - Provide insights for data protection features 

   - VersioningEnabledBucketCount, MFADeleteEnabledBucketCount, SSEKMSEnabledBucketCount, CrossRegionReplicationRuleCount… 

   - • Use cases: identify buckets that aren’t following data-protection best practices 

- Access-management Metrics 

   - Provide insights for S3 Object Ownership 

   - ObjectOwnershipBucketOwnerEnforcedBucketCount… 

   - Use cases: identify which Object Ownership settings your buckets use 

- Event Metrics 

   - Provide insights for S3 Event Notifications 

• EventNotificationEnabledBucketCount (identify which buckets have S3 Event Notifications configured) © Stephane Maarek IE'”TS Ol ns 

#### Storage Lens – Metrics 



<!-- Start of picture text -->
oS<br><!-- End of picture text -->

- Performance Metrics 

   - Provide insights for S3 Transfer Acceleration 

   - TransferAccelerationEnabledBucketCount (identify which buckets have S3 Transfer Acceleration enabled) 

- Activity Metrics 

   - Provide insights about how your storage is requested 

   - AllRequests, GetRequests, PutRequests, ListRequests, BytesDownloaded… 

- Detailed Status Code Metrics 

• Provide insights for HTTP status codes • 200OKStatusCount, 403ForbiddenErrorCount, 404NotFoundErrorCount… © Stephane Maarek IE'”TS Ol ns 

#### Storage Lens – Free vs. Paid 



- Free Metrics 

   - Automatically available for all customers 

   - • Contains around 28 usage metrics • Data is available for queries for 14 days 

- Advanced Metrics and Recommendations • Additional paid metrics and features • Advanced Metrics – Activity, Advanced Cost Optimization, Advanced Data Protection, Status Code 

   - CloudWatch Publishing – Access metrics in CloudWatch without additional charges 

   - Prefix Aggregation – Collect metrics at the prefix level 

   - • Data is available for queries for 15 months 



<!-- Start of picture text -->
Metrics selection<br>Choose additonal metrics and functionality.<br>Metrics selection<br>© Free metrics<br>Includes usage metrics aggregated atthe bucket level Data is available for queries for 14 days.<br>Learn more [4<br>© Advanced metrics and recommendations<br>includes options for adltional metris and aggregations and other advanced capabilities. Data is<br>‘analytesavailable  tabfor queries for 15 months. See Storage Lens metrics pricing [Z on the Management &<br>‘Advanced metrics and recommendations features nfo<br>Advanced metrics CloudWatch publishing) Prefix aggregation ia)<br>Choose advanced metrics ‘Access metrics in CloudWatch Generate insights for usage<br>categories to display in the without incurring separate metrics aggregated by top<br>dashboard. CloudWatch metrics publishing prefixes.<br>Advanced metrics are not Cueaes,See Cour ie<br>available at the prefix level. Pricing<br>Prefix-level metrics are not<br>available in CloudWatch.<br>Advanced metrics categories<br>Specify which advanced metrics categories<br>to spay in the dashboard. Learn more [2<br>Activity metrics<br>Generate metrics that show details about<br>aggregated by bucket. how your storage i requested, such as requests, bytes uploaded downloaded, and errors<br>(Detailed status code metrics - new<br><!-- End of picture text -->

© Stephane Maarek 

### Amazon S3 – Security 

© Stephane Maarek 

Amazon S3 – Object Encryption 



- You can encrypt objects in S3 buckets using one of 4 methods 

- Server-Side Encryption (SSE) 

   - Server-Side Encryption with Amazon S3-Managed Keys (SSE-S3) – <u>Enabled by Default</u> 

      - Encrypts S3 objects using keys handled, managed, and owned by AWS 

   - Server-Side Encryption with KMS Keys stored in AWS KMS (SSE-KMS) 

      - Leverage AWS Key Management Service (AWS KMS) to manage encryption keys 

   - Server-Side Encryption with Customer-Provided Keys (SSE-C) 

      - When you want to manage your own encryption keys 

- Client-Side Encryption 

• It’s important to understand which ones are for which situation for the exam © Stephane Maarek IE'”TS Ol ns 

#### Amazon S3 Encryption – SSE-S3 

- Encryption using keys handled, managed, and owned by AWS 

- • Object is encrypted server-side • Encryption type is AES-256 



<!-- Start of picture text -->
• Must set header  "x-amz-server-side-encryption": "AES256"<br>• Enabled by default for new buckets & new objects<br>Amazon S3<br>Object<br>ee<br>oO<br>upload<br>+ Encryption<br>HTTP(S) + Header<br>User<br>S3 Bucket<br>S3 Owned Key<br><!-- End of picture text -->

© Stephane Maarek 

#### Amazon S3 Encryption – SSE-KMS 

- Encryption using keys handled and managed by AWS KMS (Key Management Service) 

- KMS advantages: user control + audit key usage using CloudTrail 

- Object is encrypted server side 

- Must set header "x-amz-server-side-encryption": "aws:kms" 



<!-- Start of picture text -->
Amazon S3<br>Object<br>upload oO _<br>+ Encryption<br>HTTP(S) + Header<br>User<br>S3 Bucket<br>KMS Key<br>AWS KMS<br>bee!<br><!-- End of picture text -->

© Stephane Maarek 

#### SSE-KMS Limitation 

- If you use SSE-KMS, you may be impacted by the KMS limits 

- When you upload, it calls the GenerateDataKey KMS API 

- When you download, it calls the Decrypt KMS API 

- Count towards the KMS quota per second (5500, 10000, 30000 req/s based on region) 

**S3 Bucket** 

**KMS Key** 

Upload / download SSE-KMS ~~i~~ API call 



<!-- Start of picture text -->
ren<br><!-- End of picture text -->

**Users** 

**Users** • You can request a quota increase using the Service Quotas Console © Stephane Maarek IE'”TS Ol ns 

#### Amazon S3 Encryption – SSE-C 

- Server-Side Encryption using keys fully managed by the customer outside of AWS 

- Amazon S3 does NOT store the encryption key you provide 

- HTTPS must be used 

- Encryption key must provided in HTTP headers, for every HTTP request made 



<!-- Start of picture text -->
Amazon S3<br>Object<br>+<br>upload = Oo —<br>+ Encryption<br>HTTPS ONLY<br>User<br>+ Key in Header<br>S3 Bucket<br>Client-Provided Key<br><!-- End of picture text -->

© Stephane Maarek 

#### Amazon S3 Encryption – Client-Side Encryption 



<!-- Start of picture text -->
• Use client libraries such as  Amazon S3 Client-Side Encryption Library<br>• Clients must encrypt data themselves before sending to Amazon S3<br>• Clients must decrypt data themselves when retrieving from Amazon S3<br>• Customer fully manages the keys and encryption cycle<br>Amazon S3<br>File<br>-<br>upload<br>+ Encryption<br>HTTP(S)<br>File<br>S3 Bucket<br>(encrypted)<br>Client Key<br><!-- End of picture text -->

© Stephane Maarek 

Amazon S3 – Encryption in transit (SSL/TLS) 

|•Encryption in flight is also called SSL/TLS|
|---|



|•Amazon S3 exposes two endpoints:|
|---|



|• HTTP Endpoint– non encrypted|
|---|



|• HTTPS Endpoint– encryption in flight|
|---|





|• HTTPS is recommended|
|---|



|• HTTPS is mandatory for SSE-C|
|---|



• Most clients would use the HTTPS endpoint by default © Stephane Maarek IE'”TS Ol ns 

#### Amazon S3 – Force Encryption in Transit aws:SecureTransport 



<!-- Start of picture text -->
"Version": "2012-10-17",<br>"Statement": [<br>aws {<br>~~" Account B<br>User<br>R "Effect": "Deny",<br>ooooi—?r 4 “Action":"Principal":"s3:GetObject","x",<br>S3 Bucket<br>(my-bucket)<br>fs "Resource": “arn:aws:S3:::my—bucket/*",<br>"Bool": {<br>(Z) = "Condition": {<br>Bucket Policy<br>User<br>R + “aws:SecureTransport": "false"<br>http<br>https<br><!-- End of picture text -->

© Stephane Maarek 

###### Amazon S3 – Default Encryption vs. Bucket Policies 

- SSE-S3 encryption is automatically applied to new objects stored in S3 bucket 

- • Optionally, you can “force encryption” using a bucket policy and refuse any API call to PUT an S3 object without encryption headers (SSE-KMS or SSE-C) 



<!-- Start of picture text -->
{<br>"Version": "2012-10-17",<br>"Statement": [<br>{<br>"Effect": "Deny",<br>"Action": "s3:PutObject",<br>"Principal": "x",<br>"Resource": “arn:aws:s3:::my—bucket/*",<br>"Condition": {<br>"StringNotEquals": {<br>"s3:x-amz-server-side-encryption": "aws:kms"<br>+<br>+<br>+<br>]<br>+<br><!-- End of picture text -->



<!-- Start of picture text -->
{<br>"Version": "2012-10-17",<br>"Statement": [<br>{<br>"Effect": "Deny",<br>"Action": "s3:PutObject",<br>"Principal": "x",<br>"Resource": “arn:aws:s3:::my—bucket/x",<br>"Condition": {<br>"Null": {<br>"s3:x-amz—server-side-encryption—customer-algorithm": "true"<br>+<br>+<br>+<br>]<br>+<br><!-- End of picture text -->

###### • <u>Note: Bucket Policies are evaluated before “Default Encryption”</u> 

© Stephane Maarek 

#### What is CORS? 

- Cross-Origin Resource Sharing (CORS) 

- Origin = scheme (protocol) + host (domain) + port 

   - example: <u>https://www.example.com (implied port is 443 for HTTPS, 80 for HTTP)</u> 

- Web Browser based mechanism to allow requests to other origins while visiting the main origin 

- Same origin: <u>http://example.com /app1 & http://example.com /app2</u> 

- Different origins: <u>http://www.example.com</u> & <u>http://other.example.com</u> 

- The requests won’t be fulfilled unless the other origin allows for the requests, using CORS Headers (example: Access-Control-Allow-Origin ) 

© Stephane Maarek 

What is CORS? OPTIONS / **Host: www.other.com Origin: https://www.example.com Preflight Request Access-Control-Allow-Origin: https://www.example.com Access-Control-Allow-Methods: GET, PUT, DELETE** HTTPS Request **Preflight Response** Web Browser Web Server Web Server **(Origin)** GET / **(Cross-Origin) https://www.example.com Host: www.other.com https://www.other.com Origin: https://www.example.com CORS Headers received already by the Origin** The Web Browser can make requests 

© Stephane Maarek 

#### Amazon S3 – CORS 

- If a client makes a cross-origin request on our S3 bucket, we need to enable the correct CORS headers 

- It’s a popular exam question 

- You can allow for a specific origin or for * (all origins) 

GET /index.html **Host: http://my-bucket-html.s3-website.us-west-2.amazonaws.com** S3 Bucket **(my-bucket-html)** 8 (Static Website **Enabled** ) index.html GET /images/coffee.jpg Web Browser **Host: http://my-bucket-assets.s3-website.us-west-2.amazonaws.com Origin: http://my-bucket-html.s3-website.us-west-2.amazonaws.com** S3 Bucket **(my-bucket-assets)** (Static Website **Enabled** ) **Access-Control-Allow-Origin: http://my-bucket-html.s3-website.us-west-2.amazonaws.com** 

© Stephane Maarek 

#### Amazon S3 – MFA Delete 

• MFA (Multi-Factor Authentication) – force users to generate a code on a device (usually a mobile phone or hardware) before doing important operations on S3 

- MFA will be required to: 

   - Permanently delete an object version 

Google Authenticator 

   - Suspend Versioning on the bucket 

- MFA won’t be required to: 

   - Enable Versioning 

   - List deleted versions 

MFA Hardware Device 

- To use MFA Delete, Versioning must be enabled on the bucket 

• Only the bucket owner (root account) can enable/disable MFA Delete © Stephane Maarek IE'”TS Ol ns 

S3 Access Logs • For audit purpose, you may want to log all access to S3 buckets requests a • Any request made to S3, from any account, authorized or denied, will be logged into another S3 bucket • That data can be analyzed using data analysis tools… SS • The target logging bucket must be in the same AWS region **My-bucket** Log all requests • The log format is at: <u>https://docs.aws.amazon.com/AmazonS3/latest/dev/LogFormat.html</u> **Logging Bucket** © Stephane Maarek ~~<mark>es</mark>~~ 

S3 Access Logs: Warning • Do not set your logging bucket to be the monitored bucket • It will create a logging loop, and your bucket will grow exponentially Logging loop PutObject ce **App Bucket & Logging Bucket** Do not try this at home J © Stephane Maarek e ~~e~~ 

URL 

#### Amazon S3 – Pre-Signed URLs 

|• Generate pre-signed URLs using theS3 Console, AWS CLI or SDK<br>• URL Expiration<br>• S3 Console –1 min up to 720 mins (12 hours)<br>• AWS CLI –configure expiration with_--expires-in_parameter in seconds<br>(default 3600 secs, max. 604800 secs ~ 168 hours)|
|---|
|• Users given a pre-signed URL inherit the permissions of the user<br>that generated the URL for GET / PUT<br>URL|



|• Examples:|
|---|
|• Allow only logged-in users to download a premium video from your S3<br>bucket|
|• Allow an ever-changing list of users to download files by generating URLs<br>dynamically|
|• Allow temporarily a user to upload a file to a precise location in your S3<br>bucket|



Owner 



URL 

S3 Bucket **(Private)** 



User 

© Stephane Maarek 

#### S3 Glacier Vault Lock 

- Adopt a WORM (Write Once Read Many) model 



**Object** 

   - Create a Vault Lock Policy 

- Lock the policy for future edits (can no longer be changed or deleted) 

- • Helpful for compliance and data **Vault Lock Policy** retention Object can’t be deleted 

- © Stephane Maarek 

- IE'”TS Ol ns 

#### S3 Object Lock (versioning must be enabled) 

- Adopt a WORM (Write Once Read Many) model 

- Block an object version deletion for a specified amount of time 

- Retention mode - Compliance : 

   - Object versions can't be overwritten or deleted by any user, including the root user 

   - Objects retention modes can't be changed, and retention periods can't be shortened 

- Retention mode - Governance: 

   - Most users can't overwrite or delete an object version or alter its lock settings 

   - Some users have special permissions to change the retention or delete the object 

- Retention Period : protect the object for a fixed period, it can be extended 

- Legal Hold: 

   - protect the object indefinitely, independent from retention period 

   - can be freely placed and removed using the _s3:PutObjectLegalHold_ IAM permission 

© Stephane Maarek 

#### S3 – Access Points 



<!-- Start of picture text -->
tf<br><!-- End of picture text -->



<!-- Start of picture text -->
Policy<br>Grant  R/W  to<br>Users /finance  prefix Finance<br>S3 Bucket<br>(Finance) Access Point Simple Bucket<br>Policy<br>Policy<br>Grant  R/W  to<br>/finance/…<br>Users /sales  prefix Sales<br>(Sales) Access Point<br>Policy /sales/…<br>Grant  R  to<br>entire bucket AO ,<br>Users Analytics<br>(Analytics) Access Point<br><!-- End of picture text -->

- Access Points simplify security management for S3 Buckets 

- Each Access Point has: 

   - its own DNS name (Internet Origin or VPC Origin) 

   - an access point policy (similar to bucket policy) – manage security at scale 

ns 

© Stephane Maarek IE '”TS Ol 

#### S3 – Access Points – VPC Origin 

- We can define the access point to be accessible only from within the VPC 

- You must create a VPC Endpoint to access the Access Point (Gateway or Interface Endpoint) 

- The VPC Endpoint Policy must allow access to the target bucket and Access Point 



<!-- Start of picture text -->
@&<br><!-- End of picture text -->



<!-- Start of picture text -->
VPC<br>Access Point<br>S3 Bucket<br>EC2 Instance VPC Endpoint VPC Origin<br>i: ®) @3) iS,<br>WA Endpoint  iv Access Point  WA Bucket<br>Wa iv Wa<br>x Policy x Policy x Policy<br><!-- End of picture text -->



<!-- Start of picture text -->
{<br>"Version": "2012-10-17",<br>"Statement": [<br>{<br>"Principal": "x",<br>"Action": [<br>"s3:GetObject"<br>1,<br>“Effect": "Allow",<br>“Resource": [<br>“arn:aws:S3:::awsexamplebucket1/*",<br>“arn:aws:s3:us—west-2:123456789012: accesspoint/examp le-vpc-ap/object/*"<br>]<br>}<br>]<br>+<br><!-- End of picture text -->

© Stephane Maarek 

#### S3 Object Lambda 

- Use AWS Lambda Functions to change the object before it is retrieved by the caller application 

- Only one S3 bucket is needed, on top of which we create S3 Access Point and S3 Object Lambda Access Points. 

- Use Cases: 

   - Redacting personally identifiable information for analytics or nonproduction environments. 

   - Converting across data formats, such as converting XML to JSON. 

   - Resizing and watermarking images on the fly using caller-specific details, such as the user who requested the object. 



<!-- Start of picture text -->
AWS Cloud<br>Original<br>S3 Bucket<br>Object<br>E-Commerce<br>Application<br>Supporting<br>S3 Access Point<br>S3 Object Lambda Redacting<br>Access Point Lambda Function<br>Redacted<br>Object<br>Analytics<br>Application<br>S3 Object Lambda Enriching<br>Access Point Lambda Function<br>Enriched<br>Object<br>Marketing<br>Application Customer Loyalty<br>Database<br><!-- End of picture text -->

© Stephane Maarek 

### CloudFront & Global Accelerator 

© Stephane Maarek 

#### Amazon CloudFront 

- Content Delivery Network (CDN) 

- Improves read performance, content is cached at the edge 

- Improves users experience 

- 216 Point of Presence globally (edge locations) 

- DDoS protection (because worldwide), integration with Shield, AWS Web Application Firewall 





<!-- Start of picture text -->
.<br>eo?<br>LO)<br>. |<br><!-- End of picture text -->

Source: <u>https://aws.amazon.com/cloudfront/features/?nc=sn&loc=2</u> 

© Stephane Maarek 

#### CloudFront – Origins 

- S3 bucket 

   - For distributing files and caching them at the edge 

   - Enhanced security with CloudFront Origin Access Control (OAC) 

   - OAC is replacing Origin Access Identity (OAI) 

   - CloudFront can be used as an ingress (to upload files to S3) 

- Custom Origin (HTTP) 

   - Application Load Balancer 

   - EC2 instance 

   - S3 website (must first enable the bucket as a static S3 website) 

   - Any HTTP backend you want 

© Stephane Maarek 

CloudFront at a high level GET /beach.jpg?size=300x300 HTTP/1.1 User-Agent: Mozilla/4.0 (compatible; MSIE5.01; Windows NT) Host: www.example.com Accept-Encoding: gzip, deflate **Origin** Forward Request to your Origin **S3** " [Hy Ss CloudFront Edge Location or Client **HTTP** Local Cache i © Stephane Maarek IE'”TS Ol ns 

CloudFront – S3 as an Origin AWS Cloud Public www **Private AWS** os fa | 88 Edge **Private AWS** Edge Los Angeles Mumbai **Private AWS Private AWS** Origin (S3 bucket) ; aK ay Public www **OAC** Edge Edge São Paulo Melbourne a8 **Origin Access Control + S3 bucket policy** © Stephane Maarek ee 

#### CloudFront vs S3 Cross Region Replication 

• CloudFront: 

   - Global Edge network 

   - • Files are cached for a TTL (maybe a day) • Great for static content that must be available everywhere 

- S3 Cross Region Replication: 

   - Must be setup for each region you want replication to happen 

   - • Files are updated in near real-time 

   - Read only 

   - Great for dynamic content that needs to be available at low-latency in few regions 

© Stephane Maarek 

ns 

Security group EC2 Instances **Can be Private** fe 

#### CloudFront – ALB or EC2 as an origin 

Security group **Allow Public IP of Edge Locations** <u>http://d7uri8nf7uskq.cloudfront.net/tools/list-cloudfront-ips</u> Edge Location EC2 Instances **<u>Must</u>** be Public 





<!-- Start of picture text -->
Security group<br>Application Load Balancer<br>Must be Public<br><!-- End of picture text -->

**Allow Public IP of Edge Locations** Edge Location **Public IPs** **<u>Must</u>** © Stephane Maarek IE '”TS Ol 

**Allow Security Group of Load Balancer** 

#### CloudFront Geo Restriction 

- You can restrict who can access your distribution 

   - Allowlist: Allow your users to access your content only if they're in one of the countries on a list of approved countries. 

   - Blocklist: Prevent your users from accessing your content if they're in one of the countries on a list of banned countries. 

- The “country” is determined using a 3<sup>rd</sup> party Geo-IP database 

- Use case: Copyright Laws to control access to content 

© Stephane Maarek 

#### CloudFront - Pricing 

- CloudFront Edge locations are all around the world 

- The cost of data out per edge location varies 



<!-- Start of picture text -->
Hong Kong,<br>United States, South Africa, . Philippines,<br>Per Month Mexico, & Europe & Israel Kenya, & South America Japan AustraliaZealand & New Singapore, South India<br>Canada Middle East Korea, Taiwan, &<br>Thailand<br>First 10TB $0.085 $0.085 $0.110 $0.110 $0.114 $0.114 $0.140 $0.170<br>Next 40TB $0.080 $0.080 $0.105 $0.105 $0.089 $0.098 $0.135 $0.130<br>Next 100TB $0.060 $0.060 $0.090 $0.090 $0.086, $0.094 $0.120 $0.110<br>Next 350TB $0.040 $0.040 $0.080 $0.080 $0.084 $0.092 $0.100 $0.100<br>Next 524TB $0.030 $0.030 $0.060 $0.060 $0.080 $0.090 $0.080 $0.100<br>Next 4PB $0.025 $0.025 $0.050 $0.050 $0.070 $0.085 $0.070 $0.100<br>Over 5PB $0.020 $0.020 $0.040 $0.040 $0.060 $0.080 $0.060 $0.100<br><!-- End of picture text -->

**lower** 

**higher** 

© Stephane Maarek 

#### CloudFront – Price Classes 

- You can reduce the number of edge locations for cost reduction 

- Three price classes: 

   1. Price Class All: all regions – best performance 

   2. Price Class 200: most regions, but excludes the most expensive regions 3. Price Class 100: only the least expensive regions 



<!-- Start of picture text -->
Hong Kong,<br>Edge Locations Included United Stat S o uthuth AfriAfrica, ; Australia & New __ PhilippiPhilippines,<br>wae Mexico, & Europe & Israel Kenya, & South America Japan Singapore, South India<br>Within . Zealand .<br>Canada Middle East Korea, Taiwan, &<br>Thailand<br>Price Class All Yes Yes Yes Yes Yes Yes Yes Yes<br>Price Class 200 Yes Yes Yes x Yes x Yes Yes<br>Price Class 100 Yes Yes x x x x x x<br><!-- End of picture text -->

© Stephane Maarek 

CloudFront - Price Class Prices Class 100 |_| nad _ <2 Prices Class 200 |_| am NN . Prices Class All mB 4o=KS 1f fo SC Uc ~~ I —° mS Sy il Gee re5h \ FO pA 3 1 yo O Os) \ |\ \:\ “ee e eSe } \WN e y)|] fe V6 e ayA 'e | ‘\ \. e 4 Naw yp HE ] \ . ~ = ee . \ ay,‘ Ohex ! N / ~~ — — F ( / ; @e oStions \ \. (ee le o/ ‘ & ; ; Cape Locations \ \ ee L 4 ; v @ RegionalEdge Caches @ ~ S . , .<sup>.L</sup> 



<!-- Start of picture text -->
Prices Class 100<br>Prices Class 200<br>Prices Class All<br><!-- End of picture text -->

© Stephane Maarek 

#### CloudFront – Cache Invalidations 





- In case you update the back-end origin, CloudFront doesn’t know about it and will only get the refreshed content after the TTL has expired 

- • However, you can force an entire or partial cache refresh (thus bypassing the TTL) by performing a CloudFront Invalidation 

**Invalidate** - /index.html GET /index.html - /images/* CloudFront 



<!-- Start of picture text -->
invalidate<br><!-- End of picture text -->





<!-- Start of picture text -->
Edge Location Edge Location<br>Cache Cache<br>index.html /images/ index.html /images/<br><!-- End of picture text -->

- You can invalidate all files (*) or a special path (/images/*) 



update files 



**S3 Bucket (origin)** 

© Stephane Maarek 

- Global users for our application • You have deployed an application and have global users who want to access it = = 

- directly. America hops Europe 

- • They go over the public 5 “hgie & 

- internet, which can add a lot of latency due to many hops **Public ALB** 

- • We wish to go as fast as O ASeee& Australia India 

- possible through AWS network to minimize latency 

© Stephane Maarek 

#### Unicast IP vs Anycast IP 

- Unicast IP: one server holds one IP address 

- Anycast IP: all servers hold the same IP address and the client is routed to the nearest one 

**Client** = a FI FI 12.34.56.78 98.76.54.32 



<!-- Start of picture text -->
=<br><!-- End of picture text -->

**Client** 



<!-- Start of picture text -->
ao<br><!-- End of picture text -->



<!-- Start of picture text -->
FI<br><!-- End of picture text -->



<!-- Start of picture text -->
FI<br><!-- End of picture text -->

12.34.56.78 12.34.56.78 ns 

© Stephane Maarek IE '”TS Ol 

ns 

#### AWS Global Accelerator 

- Leverage the AWS internal network to route to your application 

- • 2 Anycast IP are created for your application 

- • The Anycast IP send traffic directly to Edge Locations 

- • The Edge locations send the traffic to your application 



Edge location America Europe Private AWS Australia ia: India 

Edge location America Europe Private AWS **Public ALB** Australia ia: India 

© Stephane Maarek IE '”TS Ol 

#### AWS Global Accelerator 

- Works with Elastic IP, EC2 instances, ALB, NLB, public or private 

- Consistent Performance 

   - Intelligent routing to lowest latency and fast regional failover 

   - No issue with client cache (because the IP doesn’t change) 

   - Internal AWS network 

- Health Checks 

   - Global Accelerator performs a health check of your applications 

   - Helps make your application global (failover less than 1 minute for unhealthy) 

   - Great for disaster recovery (thanks to the health checks) 

- Security 

   - only 2 external IP need to be whitelisted 

   - DDoS protection thanks to AWS Shield 

© Stephane Maarek 

#### AWS Global Accelerator vs CloudFront 

- They both use the AWS global network and its edge locations around the world 

- Both services integrate with AWS Shield for DDoS protection. 

- CloudFront 

   - Improves performance for both cacheable content (such as images and videos) 

   - • Dynamic content (such as API acceleration and dynamic site delivery) 

   - Content is served at the edge 

- Global Accelerator 

   - Improves performance for a wide range of applications over TCP or UDP 

   - • Proxying packets at the edge to applications running in one or more AWS Regions. 

   - Good fit for non-HTTP use cases, such as gaming (UDP), IoT (MQTT), or Voice over IP 

   - • Good for HTTP use cases that require static IP addresses 

   - Good for HTTP use cases that required deterministic, fast regional failover 

© Stephane Maarek 

### AWS Storage Extras 

© Stephane Maarek 

#### AWS Snow Family 

- Highly-secure, portable devices to collect and process data at the edge , and migrate data into and out of AWS 

- Data migration: 







Snowcone 

Snowball Edge 

Snowmobile 

- Edge computing: 





Snowcone 

Snowball Edge 

© Stephane Maarek 

Data Migrations with AWS Snow Family 

Challenges: 

||**Ti**|**me to Transf**|**er**|
|---|---|---|---|
||**100 Mbps**|**1Gbps**|**10Gbps**|
|**10 TB**|12 days|30 hours|3 hours|
|**100 TB**|124 days|12 days|30 hours|
|**1 PB**|3 years|124 days|12 days|



- Limited connectivity 

- • Limited bandwidth • High network cost • Shared bandwidth (can’t maximize the line) 

- Connection stability 

AWS Snow Family: offline devices to perform data migrations If it takes more than a week to transfer over the network, use Snowball devices! 

© Stephane Maarek 

#### Diagrams 

• Direct upload to S3: www: 10Gbit/s Qa **client Amazon S3** 

**Amazon S3 bucket** 

- With Snow Family: 

ship **AWS AWS import/ Amazon S3 client Snowball Snowball export bucket** 

© Stephane Maarek IE '”TS Ol 

#### Snowball Edge (for data transfers) 



- Physical data transport solution: move TBs or PBs of data in or out of AWS 

- Alternative to moving data over the network (and paying network fees) 

- Pay per data transfer job 

- Provide block storage and Amazon S3-compatible object storage 

- Snowball Edge Storage Optimized 

   - <u>80 TB of HDD capacity for block volume and S3 compatible object</u> storage 

- Snowball Edge Compute Optimized 

   - <u>42 TB of HDD or 28TB NVMe capacity for block volume and S3 compatible object storage</u> 

- Use cases: large data cloud migrations, DC decommission, disaster recovery 



© Stephane Maarek 

#### AWS Snowcone & Snowcone SSD 



- Small, portable computing, anywhere, rugged & secure, withstands harsh environments 

- Light (4.5 pounds, 2.1 kg) 

- • Device used for edge computing, storage, and data transfer 

- Snowcone – 8 TB of HDD Storage 

- Snowcone SSD – 14 TB of SSD Storage 

- • Use Snowcone where Snowball does not fit (spaceconstrained environment) 



- Must provide your own battery / cables 

- Can be sent back to AWS offline, or connect it to internet and use AWS DataSync to send data 

© Stephane Maarek 

#### AWS Snowmobile 





<!-- Start of picture text -->
- rdsamazo<br>webservi 4<br>ne<br>© ia<br><!-- End of picture text -->

- Transfer exabytes of data (1 EB = 1,000 PB = 1,000,000 TBs) 

- Each Snowmobile has 100 PB of capacity (use multiple in parallel) 

- High security: temperature controlled, GPS, 24/7 video surveillance 

- Better than Snowball if you transfer more than 10 PB 

© Stephane Maarek 

AWS Snow Family for Data Migrations 













||**Snowcone**|**Snowball Edge**|**Snowmobile**|
|---|---|---|---|
||**Snowcone &**|**Snowball Edge**|**Snowmobile**|
||**Snowcone SSD**|**Storage Optimized**||
|Storage Capacity|8 TB HDD<br>14 TB SSD|80 TB usable|< 100 PB|
|Migration Size|Up to 24 TB, online and<br>offline|Up to petabytes,<br>offline|Up to exabytes, offline|
|DataSync agent|Pre-installed|||



© Stephane Maarek 

#### Snow Family – Usage Process 

1. Request Snowball devices from the AWS console for delivery 

2. Install the snowball client / AWS OpsHub on your servers 

3. Connect the snowball to your servers and copy files using the client 4. Ship back the device when you’re done (goes to the right AWS facility) 

5. Data will be loaded into an S3 bucket 

6. Snowball is completely wiped 

© Stephane Maarek 

#### What is Edge Computing? 

- Process data while it’s being created on an edge location 

   - A truck on the road, a ship on the sea, a mining station underground... 







- These locations may have 

   - Limited / no internet access 

   - Limited / no easy access to computing power 

- We setup a Snowball Edge / Snowcone device to do edge computing 

- Use cases of Edge Computing: 

   - Preprocess data 

   - Machine learning at the edge 

   - Transcoding media streams 

- Eventually (if need be) we can ship back the device to AWS (for transferring data for example) 

© Stephane Maarek 

#### Snow Family – Edge Computing 

- Snowcone & Snowcone SSD (smaller) 

   - 2 CPUs, 4 GB of memory, wired or wireless access 

   - USB-C power using a cord or the optional battery 



- Snowball Edge – Compute Optimized • <u>104 vCPUs, 416 GiB of RAM</u> 

   - <u>Optional GPU</u> (useful for video processing or machine learning) 

   - • <u>28</u> ~~$$~~ <u>TB NVMe or 42TB HDD usable storage</u> 

   - Storage Clustering available (up to 16 nodes) 



- Snowball Edge – Storage Optimized • <u>Up to 40 vCPUs, 80 GiB of RAM, 80 TB storage</u> 

- All: Can run EC2 Instances & AWS Lambda functions (using AWS IoT Greengrass) 

- Long-term deployment options: 1 and 3 years discounted pricing 

© Stephane Maarek 

#### AWS OpsHub 

- Historically, to use Snow Family devices, you needed a CLI (Command Line Interface tool) 

- Today, you can use AWS OpsHub (a software you install on your computer / laptop) to manage your Snow Family Device 

   - Unlocking and configuring single or clustered devices 

   - Transferring files 

   - Launching and managing instances running on Snow Family Devices 

   - Monitor device metrics (storage capacity, active instances on your device) 

   - Launch compatible AWS services on your devices (ex: Amazon EC2 instances, AWS DataSync, Network File System (NFS)) 



<!-- Start of picture text -->
AWS OpsHub for Snow Family<br>@ rvsetesonse © srs comptig © vores nt<br>Get stared Get stared (Censors ]<br>ceed ay py mre foment wey one Seer Sow lenen errno te<br>sro con pond be ceoengetenes<br>(2) c=) (3) (3)<br>99% 0.9 0 1<br>Devices (1)<br>a a9<br>Phitipa<br>vans<br><!-- End of picture text -->

<u>https://aws.amazon.com/blogs/aws/aws-snowball-edge-update/</u> 

© Stephane Maarek 

#### Solution Architecture: Snowball into Glacier 

- Snowball cannot import to Glacier directly 

- You must use Amazon S3 first, in combination with an S3 lifecycle policy 





<!-- Start of picture text -->
Snowball<br><!-- End of picture text -->



<!-- Start of picture text -->
import<br><!-- End of picture text -->

S3 lifecycle policy **Amazon S3 Amazon Glacier** 

© Stephane Maarek IE '”TS Ol 

ns 

#### Amazon FSx – Overview 



- Launch 3rd party high-performance file systems on AWS 

- Fully managed service 





FSx for Lustre FSx for Windows File Server 





FSx for NetApp ONTAP FSx for OpenZFS 

© Stephane Maarek 

#### Amazon FSx for Windows (File Server) 



- FSx for Windows is a fully managed Windows file system share drive 

- Supports SMB protocol & Windows NTFS 

- Microsoft Active Directory integration, ACLs, user quotas 

- Can be mounted on Linux EC2 instances 

- Supports Microsoft's Distributed File System (DFS) Namespaces (group files across multiple FS) 

- Scale up to 10s of GB/s, millions of IOPS, 100s PB of data 

- Storage Options: 

   - SSD – latency sensitive workloads (databases, media processing, data analytics, …) 

   - HDD – broad spectrum of workloads (home directory, CMS, …) 

- Can be accessed from your on-premises infrastructure (VPN or Direct Connect) 

- Can be configured to be Multi-AZ (high availability) 

- Data is backed-up daily to S3 

© Stephane Maarek 

#### Amazon FSx for Lustre 



- Lustre is a type of parallel distributed file system, for large-scale computing 

- The name Lustre is derived from “Linux” and “cluster 

- Machine Learning, High Performance Computing (HPC) 

- Video Processing, Financial Modeling, Electronic Design Automation 

- Scales up to 100s GB/s, millions of IOPS, sub-ms latencies 

- Storage Options: 

   - SSD – low-latency, IOPS intensive workloads, small & random file operations 

   - HDD – throughput-intensive workloads, large & sequential file operations 

- Seamless integration with S3 

   - Can “read S3” as a file system (through FSx) 

   - Can write the output of the computations back to S3 (through FSx) 

- Can be used from on-premises servers (VPN or Direct Connect) 

© Stephane Maarek 

#### FSx Lustre - File System Deployment Options 

- Scratch File System 

   - Temporary storage 

   - Data is not replicated (doesn’t persist if file server fails) 

   - High burst (6x faster, 200MBps per TiB) 

   - • Usage: short-term processing, optimize costs 

- Persistent File System 

   - Long-term storage 

   - Data is replicated within same AZ 

   - Replace failed files within minutes 

   - Usage: long-term processing, sensitive data 





<!-- Start of picture text -->
Region<br>Availability Zone 1 Availability Zone 2<br>ENI<br>Compute  Compute<br>instances instances<br>FSx For Lustre S3 bucket<br>(Scratch file system) (optional data repository)<br><!-- End of picture text -->



###### Region 



<!-- Start of picture text -->
Availability Zone 1 Availability Zone 2<br>ENI<br>Compute  Compute<br>instances instances<br>FSx For Lustre S3 bucket<br>(Persistent file system) (optional data repository)<br><!-- End of picture text -->

© Stephane Maarek 

#### Amazon FSx for NetApp ONTAP 



- Managed NetApp ONTAP on AWS 

- • File System compatible with NFS, SMB, iSCSI protocol 

- • Move workloads running on ONTAP or NAS to AWS • Works with: • Linux • Windows • MacOS • VMware Cloud on AWS • Amazon Workspaces & AppStream 2.0 • Amazon EC2, ECS and EKS 

- Storage shrinks or grows automatically 

- • Snapshots, replication, low-cost, compression and data de-duplication 

- Point-in-time instantaneous cloning (helpful for testing new workloads) 

Amazon FSx for NetApp ONTAP FS NFS, SMB, iSCSI 











EC2 ECS EKS VMware Cloud Amazon Amazon On-premises on AWS AppStream 2.0 WorkSpaces Server 

© Stephane Maarek 

#### Amazon FSx for OpenZFS 

- Managed OpenZFS file system on AWS 

- • File System compatible with NFS (v3, v4, v4.1, v4.2) • Move workloads running on ZFS to AWS • Works with: • Linux • Windows • MacOS • VMware Cloud on AWS • Amazon Workspaces & AppStream 2.0 • Amazon EC2, ECS and EKS 

- Up to 1,000,000 IOPS with < 0.5ms latency 

- Snapshots, compression and low-cost 

- Point-in-time instantaneous cloning (helpful for testing new workloads) 



Amazon FSx for OpenZFS NFS (v3, v4, v4.1, v4.2) 





<!-- Start of picture text -->
oe<br><!-- End of picture text -->









EC2 ECS EKS 









VMware Cloud Amazon Amazon On-premises on AWS AppStream 2.0 WorkSpaces Server 

© Stephane Maarek 

#### Hybrid Cloud for Storage 

- AWS is pushing for ”hybrid cloud” 

   - Part of your infrastructure is on the cloud 

   - Part of your infrastructure is on-premises 

- This can be due to 

   - Long cloud migrations 

   - Security requirements 

   - Compliance requirements 

   - IT strategy 

- S3 is a proprietary storage technology (unlike EFS / NFS), so how do you expose the S3 data on-premises? 

- AWS Storage Gateway! 

© Stephane Maarek 

#### AWS Storage Cloud Native Options 



<!-- Start of picture text -->
Block File Object<br>. BEE<br>Amazon EBS EC2 Instance Amazon EFS Amazon FSx Amazon S3 Amazon Glacier<br>Store<br><!-- End of picture text -->

© Stephane Maarek 

#### AWS Storage Gateway 



|•Bridge between on-premises data and cloud data|
|---|



|• Use cases:<br>• disaster recovery<br>• backup & restore<br>|~~fi~~|**ION © Step**<br>&|
|---|---|---|
|• tiered storage<br>• on-premises cache & low-latency files access<br>|Storage Gateway<br>|**hane M**<br>|
|© Stephane Maarek<br>•Types of Storage Gateway:<br>• S3 File Gateway<br>• FSx File Gateway<br>• Volume Gateway<br>• Tape Gateway<br>S<br>’”-Oh|E<br>e|**aarekwww.datacumulus.com**<br><br>s|



ns 

#### Amazon S3 File Gateway 

- Configured S3 buckets are accessible using the NFS and SMB protocol 

- Most recently used data is cached in the file gateway 

- Supports S3 Standard, S3 Standard IA, S3 One Zone A, S3 Intelligent Tiering 

- Transition to S3 Glacier using a Lifecycle Policy 

- Bucket access using IAM roles for each File Gateway 

- SMB Protocol has integration with Active Directory (AD) for user authentication 



<!-- Start of picture text -->
Corporate  AWS Cloud        .<br>Data Center<br>S3 Standard Lifecycle<br>HTTPS<br>S3 Standard-IA policy<br>S3 One Zone-IA<br>NFS or SMB<br>S3 Intelligent-Tiering<br>S3 Glacier<br>Application S3 File<br>Server Gateway<br><!-- End of picture text -->

© Stephane Maarek IE '”TS Ol 

#### Amazon FSx File Gateway 

- Native access to Amazon FSx for Windows File Server 

- Local cache for frequently accessed data 

- Windows native compatibility (SMB, NTFS, Active Directory...) 

- Useful for group file shares and home directories 



<!-- Start of picture text -->
Corporate  AWS Cloud<br>Data Center<br>SMB Clients<br>Amazon FSx<br>Amazon FSx  File systems<br>File Gateway<br>for Windows File Server<br><!-- End of picture text -->



© Stephane Maarek 

#### Volume Gateway 

- Block storage using iSCSI protocol backed by S3 

- Backed by EBS snapshots which can help restore on-premises volumes! 

- Cached volumes: low latency access to most recent data 

- Stored volumes: entire dataset is on premise, scheduled backups to S3 



<!-- Start of picture text -->
Corporate  AWS Cloud<br>Data Center<br>Region<br>iSCSI HTTPS<br>Application Volume Gateway S3 Bucket Amazon EBS<br>Server Snapshots<br><!-- End of picture text -->

© Stephane Maarek 

#### Tape Gateway 

- Some companies have backup processes using physical tapes (!) 

- With Tape Gateway, companies use the same processes but, in the cloud 

- Virtual Tape Library (VTL) backed by Amazon S3 and Glacier 

- Back up data using existing tape-based processes (and iSCSI interface) 

- Works with leading backup software vendors 



<!-- Start of picture text -->
Corporate  AWS Cloud<br>Data Center<br>Region<br>Media<br>iSCSI Changer HTTPS<br>Virtual Tapes Archived Tapes<br>Tape  Tape<br>Backup stored in stored in<br>Drive Gateway<br>Server Amazon S3 Amazon Glacier<br><!-- End of picture text -->

© Stephane Maarek 

Storage Gateway – Hardware appliance 

- Using Storage Gateway means you need on-premises virtualization 

- Otherwise, you can use a Storage Gateway Hardware Appliance 

- You can buy it on amazon.com 

- Works with File Gateway, Volume Gateway, Tape Gateway 

- Has the required CPU, memory, network, SSD cache resources 

- Helpful for daily NFS backups in small data centers 



<!-- Start of picture text -->
Select host platform<br>VMware ESXi<br>Microsoft Hyper-V 2012R2/2016<br>Linux KVM<br>Amazon EC2<br>@ Hardware Appliance | @ Buy on Amazon [ Activate Appliance J<br><!-- End of picture text -->



<!-- Start of picture text -->
= ATALANTA GAUAATUNNUNNUNNNNNN<br>rrgueze : =a — —— w<br>|_| Sn” ASS) weer Aa<br>ia ir ~ DALLEMC ti<br><!-- End of picture text -->

© Stephane Maarek 

#### AWS Storage Gateway 





<!-- Start of picture text -->
On-Premises AWS Cloud<br>NFS/SMB<br>Any S3 Storage Class<br>User/group file shares File Gateway Amazon S3<br>Including Glacier<br>local cache excluding Glacier &<br>Glacier Deep Archive<br>a iSCSI —he | Encryption  in Transit | = 8<br>Internet  or  Direct Connect<br>Application Server Volume Gateway Amazon S3 AWS EBS<br>local cache Storage Gateway<br>Eject from backup application<br>= le ? | ey<br>iSCSI VTL<br>Amazon S3 Tape Archive<br>Backup Application Tape Gateway Tape Library Glacier &<br>local cache Glacier Deep Archive<br>=f | an<br>Gateway Deployment Options<br>Automated Backups<br>VM(VMware, Hyper-V, KVM) or Hardware Appliance<br>Amazon S3<br>Amazon FSx<br>For Windows File Server<br><!-- End of picture text -->

© Stephane Maarek 

#### AWS Transfer Family 



- A fully-managed service for file transfers into and out of Amazon S3 or Amazon EFS using the FTP protocol 

- Supported Protocols 

   - AWS Transfer for FTP (File Transfer Protocol (FTP)) 

   - AWS Transfer for FTPS (File Transfer Protocol over SSL (FTPS)) 

   - AWS Transfer for SFTP (Secure File Transfer Protocol (SFTP)) 

- Managed infrastructure, Scalable, Reliable, Highly Available (multi-AZ) 

- Pay per provisioned endpoint per hour + data transfers in GB 

- Store and manage users’ credentials within the service 

• Integrate with existing authentication systems (Microsoft Active Directory, LDAP, Okta, Amazon Cognito, custom) • Usage: sharing files, public datasets, CRM, ERP, … © Stephane Maarek IE'”TS Ol ns 

AWS Transfer Family MS Active Directory authenticate LDAP … AWS Transfer for SFTP OE Amazon S3 IAM Role AWS Transfer for FTPS 28 — & 4 Users Route 53 (FTP client) (optional) AWS Transfer for FTP (only within VPC) Amazon EFS **AWS Transfer Family** 

#### AWS Transfer Family 

Users Route 53 (FTP client) (optional) 

© Stephane Maarek 

#### AWS DataSync 



- Move large amount of data to and from 

   - On-premises / other cloud to AWS (NFS, SMB, HDFS, S3 API…) – needs agent 

   - AWS to AWS (different storage services) – no agent needed 

- Can synchronize to: 

   - Amazon S3 (any storage classes – including Glacier) 

   - Amazon EFS 

   - Amazon FSx (Windows, Lustre, NetApp, OpenZFS...) 

- Replication tasks can be scheduled hourly, daily, weekly 

• File permissions and metadata are preserved (NFS POSIX, SMB…) • One agent task can use 10 Gbps, can setup a bandwidth limit © Stephane Maarek IE'”TS Ol ns 

AWS DataSync NFS / SMB to AWS (S3, EFS, FSx…) Region On-Premises AWS Storage Resources NFS or SMB TLS S3 Standard S3 IntelligentS3 Standard-IA Tiering 8 8 8. NFS or SMB AWS DataSync AWS S3 One S3 Glacier S3 Glacier Server Agent Zone-IA Deep Archive DataSync - ThSse a. AWS Snowcone (agent pre-installed) AWS EFS Amazon FSx 

© Stephane Maarek 

#### AWS DataSync Transfer between AWS storage services 







<!-- Start of picture text -->
Amazon S3 Amazon S3<br>Amazon EFS Amazon EFS<br>AWS DataSync<br>copy data and metadata<br>between AWS Storage Services<br>Amazon FSx Amazon FSx<br><!-- End of picture text -->

© Stephane Maarek 

#### Storage Comparison 

- S3: Object Storage 

- S3 Glacier: Object Archival 

- EBS volumes: Network storage for one EC2 instance at a time 

- Instance Storage: Physical storage for your EC2 instance (high IOPS) 

- EFS: Network File System for Linux instances, POSIX filesystem 

- FSx for Windows: Network File System for Windows servers 

- FSx for Lustre: High Performance Computing Linux file system 

- FSx for NetApp ONTAP: High OS Compatibility 

- FSx for OpenZFS: Managed ZFS file system 

- Storage Gateway: S3 & FSx File Gateway, Volume Gateway (cache & stored), Tape Gateway 

- Transfer Family: FTP, FTPS, SFTP interface on top of Amazon S3 or Amazon EFS 

- DataSync: Schedule data sync from on-premises to AWS, or AWS to AWS 

- Snowcone / Snowball / Snowmobile: to move large amount of data to the cloud, physically 

- Database: for specific workloads, usually with indexing and querying 

© Stephane Maarek 

### AWS Integration & Messaging SQS, SNS & Kinesis 

© Stephane Maarek 

#### Section Introduction 

- When we start deploying multiple applications, they will inevitably need to communicate with one another 

- There are two patterns of application communication 

**1) Synchronous communications (application to application)** 

- **2) Asynchronous / Event based (application to queue to application)** 



<!-- Start of picture text -->
Buying  Shipping  Buying  Shipping<br>Queue<br>Service Service Service Service<br><!-- End of picture text -->

© Stephane Maarek 

#### Section Introduction 

- Synchronous between applications can be problematic if there are sudden spikes of traffic 

- What if you need to suddenly encode 1000 videos but usually it’s 10? 

- In that case, it’s better to decouple your applications, 

   - using SQS: queue model 

   - using SNS: pub/sub model 

   - using Kinesis: real-time streaming model 

- These services can scale independently from our application! 

© Stephane Maarek 

ns 



<!-- Start of picture text -->
Amazon SQS<br>What’s a queue?<br>Consumer<br>Producer<br>Consumer<br>Send messages<br>Producer Poll messages<br>— Consumer<br>SQS Queue<br>Producer<br>—] —<br>Consumer<br><!-- End of picture text -->

© Stephane Maarek IE '”TS Ol 

#### Amazon SQS – Standard Queue 



<!-- Start of picture text -->
/<br><!-- End of picture text -->

- Oldest offering (over 10 years old) 

- Fully managed service, used to decouple applications 

- Attributes: 

   - Unlimited throughput, unlimited number of messages in queue 

   - Default retention of messages: 4 days, maximum of 14 days 

   - Low latency (<10 ms on publish and receive) 

   - Limitation of 256KB per message sent 

- Can have duplicate messages (at least once delivery, occasionally) 

- Can have out of order messages (best effort ordering) 

© Stephane Maarek 

|SQS – Producing Messages|
|---|



|•Produced to SQS using the SDK (SendMessage API)|
|---|
|•The message ispersistedin SQS until a consumer deletes it|
|•Message retention: default 4 days, up to 14 days|



|•Example: send an order to be processed|
|---|



• Order id Sent to SQS • Customer id • Any attributes you want Message Up to 256 kb 

- SQS standard: unlimited throughput 



© Stephane Maarek es 

ns 

#### SQS – Consuming Messages 

- Consumers (running on EC2 instances, servers, or AWS Lambda)… 

- Poll SQS for messages (receive up to 10 messages at a time) 

• Process the messages (example: insert the message into an RDS database) • Delete the messages using the DeleteMessage API Poll / Receive messages insert Consumer DeleteMessage 

© Stephane Maarek IE '”TS Ol 

#### SQS – Multiple EC2 Instances Consumers 

SQS Queue 



















- Consumers receive and process messages in parallel 

- At least once delivery 

- Best-effort message ordering • Consumers delete messages after processing them 





poll 

- We can scale consumers horizontally to improve throughput of processing ns 

© Stephane Maarek IE '”TS Ol 



<!-- Start of picture text -->
SQS with Auto Scaling Group (ASG)<br>Poll for messages<br>EC2 Instances<br>SQS Queue<br>Auto Scaling Group<br>scale<br>Alarm for breach<br>CloudWatch Metric – Queue Length CloudWatch Alarm<br>ApproximateNumberOfMessages<br>© Stephane Maarek<br>IE '”TS Ol ns<br><!-- End of picture text -->

ns 



<!-- Start of picture text -->
SQS to  decouple  between application tiers<br>Back-end processing<br>Front-end web app<br>application<br>requests SendMessage ReceiveMessages<br>SQS Queue<br>Sh (infinitely scalable)<br>Auto-Scaling<br>Auto-Scaling<br>© Stephane Maarek<br>IE '”TS Ol<br><!-- End of picture text -->

ns 

#### Amazon SQS - Security 

- Encryption: 

   - In-flight encryption using HTTPS API 

   - At-rest encryption using KMS keys 

   - Client-side encryption if the client wants to perform encryption/decryption itself 

- Access Controls: IAM policies to regulate access to the SQS API 

- SQS Access Policies (similar to S3 bucket policies) 

   - Useful for cross-account access to SQS queues 

   - Useful for allowing other services (SNS, S3…) to write to an SQS queue 

© Stephane Maarek 



<!-- Start of picture text -->
SQS – Message Visibility Timeout<br>• After a message is polled by a consumer, it becomes  invisible  to other consumers<br>• By default, the “message visibility timeout” is  30 seconds<br>• That means the message has 30 seconds to be processed<br>• After the message visibility timeout is over, the message is “visible” in SQS<br>ReceiveMessage ReceiveMessage ReceiveMessage ReceiveMessage<br>Request Request Request Request<br>Visibility timeout<br>Not returned Not returned<br>Time<br>Message returned Message returned (again)<br><!-- End of picture text -->

© Stephane Maarek 

SQS – Message Visibility Timeout 

|ReceiveMessage<br>Request|ReceiveMessage<br>Request|ReceiveMessage<br>Request|ReceiveMessa<br>Request|ge|
|---|---|---|---|---|
||Visibility time|out|||
|Message returned|Not returned|Not returned|Message return|**Time**<br>ed (again)|



- If a message is not processed within the visibility timeout, it will be processed twice 

- A consumer could call the ChangeMessageVisibility API to get more time 

• If visibility timeout is high (hours), and consumer crashes, re-processing will take time • If visibility timeout is too low (seconds), we may get duplicates © Stephane Maarek IE'”TS Ol ns 

- Amazon SQS - Long Polling message 

- • When a consumer requests messages from the queue, it can optionally “wait” for messages to arrive if there are none in the queue 

- • This is called Long Polling • LongPolling decreases the number of API calls **SQS Queue** 

- made to SQS while increasing the efficiency and reducing latency of your application 

- • The wait time can be between 1 sec to 20 sec (20 sec preferable) 

- • Long Polling is preferable to Short Polling poll 

- • Long polling can be enabled at the queue level or at the API level using WaitTimeSeconds Consumer 

- © Stephane Maarek 

- e ~~e~~ 

es 

Amazon SQS – FIFO Queue • FIFO = First In First Out (ordering of messages in the queue) Send messages Poll messages Producer Consumer 4 3 2 1 4 3 2 1 <mark>—__</mark> ~~<mark>so</mark> a:~~ • Limited throughput: 300 msg/s without batching, 3000 msg/s with • Exactly-once send capability (by removing duplicates) 

- Messages are processed in order by the consumer 

© Stephane Maarek SE 



<!-- Start of picture text -->
SQS with Auto Scaling Group (ASG)<br>Poll for messages<br>EC2 Instances<br>SQS Queue<br>Auto Scaling Group<br>scale<br>Alarm for breach<br>CloudWatch Metric – Queue Length CloudWatch Alarm<br>ApproximateNumberOfMessages<br>© Stephane Maarek<br>IE '”TS Ol ns<br><!-- End of picture text -->

ns 

If the load is too big, some transactions may be lost 



<!-- Start of picture text -->
Amazon RDS<br>Application<br>Insert<br>transactions<br>requests<br>Amazon Aurora<br>Te<br>Amazon DynamoDB<br>Auto-Scaling<br><!-- End of picture text -->

© Stephane Maarek 

|© Stephane Maarek<br>SQS as a buffer to database writes<br>**SQS Queue**<br>**(infinitely scalable)**<br>Auto-Scaling<br>**Dequeue message**<br>**Enqueue message**<br>requests<br>SendMessage<br>Auto-Scaling<br>ReceiveMessages<br>insert<br>||**NOT FOR DISTRIBUTION © Stephane Maarekwww.datacumulus.com**<br>|
|---|---|





<!-- Start of picture text -->
SQS to  decouple  between application tiers<br>Back-end processing<br>Front-end web app<br>application<br>requests SendMessage ReceiveMessages<br>SQS Queue<br>Sh (infinitely scalable)<br>Auto-Scaling<br>Auto-Scaling<br>© Stephane Maarek<br>IE '”TS Ol<br><!-- End of picture text -->

ns 

#### Amazon SNS 

• What if you want to send one message to many receivers? 



<!-- Start of picture text -->
Direct  Pub / Sub<br>Email<br>Email<br>integration<br>notification<br>notification<br>Fraud<br>Fraud<br>Service<br>Service<br>Buying  Buying<br>Service Service<br>Shipping<br>Shipping<br>Service<br>SNS Topic Service<br>SQS Queue<br>SQS Queue<br><!-- End of picture text -->

© Stephane Maarek 

#### Amazon SNS 



- The “event producer” only sends message to one SNS topic 

- As many “event receivers” (subscriptions) as we want to listen to the SNS topic notifications 

- Each subscriber to the topic will get all the messages (note: new feature to filter messages) 

- • Up to 12,500,000 subscriptions per topic 

- 100,000 topics limit 



<!-- Start of picture text -->
Subscribers<br>publish SQS Lambda Kinesis Data<br>Firehose<br>- a:<br>SNS<br>Emails SMS & HTTP(S)<br>Mobile Notifications Endpoints<br><!-- End of picture text -->

© Stephane Maarek 

SNS integrates with a lot of AWS services 

• Many AWS services can send data directly to SNS for notifications 







CloudWatch Alarms AWS Budgets Lambda BG Auto Scaling Group S3 Bucket DynamoDB (Notifications) (Events) 

… 

… 

publish 



SNS 







… 

CloudFormation AWS DMS RDS Events (State Changes) (New Replic) 

© Stephane Maarek 

Amazon SNS – How to publish 

- Topic Publish (using the SDK) • Create a topic • Create a subscription (or many) • Publish to the topic 

- Direct Publish (for mobile apps SDK) • Create a platform application • Create a platform endpoint • Publish to the platform endpoint 

   - Works with Google GCM, Apple APNS, Amazon ADM… 

© Stephane Maarek 

#### Amazon SNS – Security 

- Encryption: 

   - In-flight encryption using HTTPS API 

   - At-rest encryption using KMS keys 

   - Client-side encryption if the client wants to perform encryption/decryption itself 

- Access Controls: IAM policies to regulate access to the SNS API 

- SNS Access Policies (similar to S3 bucket policies) 

   - Useful for cross-account access to SNS topics 

   - Useful for allowing other services ( S3…) to write to an SNS topic 

© Stephane Maarek 

#### SNS + SQS: Fan Out 

**SQS Queue** Fraud Service C <mark>i</mark> Buying Service Shipping **SNS Topic** Service **SQS Queue** 

• Push once in SNS, receive in all SQS queues that are subscribers 

- Fully decoupled, no data loss 

- SQS allows for: data persistence, delayed processing and retries of work 

- Ability to add more SQS subscribers over time 

• Make sure your SQS queue access policy allows for SNS to write • Cross-Region Delivery: works with SQS Queues in other regions © Stephane Maarek IE'”TS Ol ns 

Application: S3 Events to multiple queues 

- For the same combination of: event type (e.g. object create) and prefix (e.g. images/) you can only have one S3 Event rule 

- If you want to send the same S3 event to many SQS queues, use fan-out 

**SQS Queues** Fan-out events S3 Object created… **SNS Topic** Amazon S3 Lambda Function © Stephane Maarek IE'”TS Ol ns 

#### Application: SNS to Amazon S3 through Kinesis Data Firehose 

• SNS can send to Kinesis and therefore we can have the following solutions architecture: Buying Amazon S3 Service **SNS Topic Kinesis Data Firehose** Any supported KDF <mark>m</mark> a ~~e8~~ Destination © Stephane Maarek IE'”TS Ol ns 

Amazon SNS – FIFO Topic • FIFO = First In First Out (ordering of messages in the topic) Receive messages Send messages Subscribers Producer **SQS FIFO** 4 3 2 1 4 3 2 1 ~~<mark>|</mark> e~~ =) <mark>=| —</mark> • Similar features as SQS FIFO: • Ordering by Message Group ID (all messages in the same group are ordered) • Deduplication using a Deduplication ID or Content Based Deduplication • Can have SQS Standard and FIFO queues as subscribers • Limited throughput (same throughput as SQS FIFO) ’”- Oh es 

es 

© Stephane Maarek SE 

#### SNS FIFO + SQS FIFO: Fan Out 

- In case you need fan out + ordering + deduplication 

**SQS FIFO Queue** Fraud Service bi <mark>)</mark> Buying Service Shipping **SNS FIFO Topic** Service **SQS FIFO Queue** © Stephane Maarek IE'”TS Ol ns 



<!-- Start of picture text -->
SNS – Message Filtering<br>• JSON policy used to filter messages sent to SNS topic’s subscriptions<br>• If a subscription doesn’t have a filter policy, it receives every message<br>Filter Policy SQS Queue<br>State: Placed<br>Y (Placed orders)<br>SQS Queue<br>(Cancelled orders)<br>Filter Policy<br>Buying  New transaction State: Cancelled Email Subscription<br>Service (Cancelled orders)<br>Order:  1036<br>Product:  Pencil SNS Topic Filter Policy<br>State: Declined<br>Qty:  4 SQS Queue<br>State:  Placed<br>(Declined orders)<br>SQS Queue<br>(All)<br>© Stephane Maarek<br>i= e<br>NOT FOR DISTRIBUTION © Stephane Maarek www.datacumulus.com<br><!-- End of picture text -->

#### Kinesis Overview 



<!-- Start of picture text -->
=Ss<br><!-- End of picture text -->

- Makes it easy to collect , process , and analyze streaming data in real-time 

- Ingest real-time data such as: Application logs, Metrics, Website clickstreams, IoT telemetry data… 



<!-- Start of picture text -->
Ss<br><!-- End of picture text -->





<!-- Start of picture text -->
=<br>ce<br><!-- End of picture text -->



<!-- Start of picture text -->
Se<br>7<br><!-- End of picture text -->

- Kinesis Data Streams: capture, process, and store data streams 

- Kinesis Data Firehose: load data streams into AWS data stores 

- Kinesis Data Analytics: analyze data streams with SQL or Apache Flink 

- Kinesis Video Streams: capture, process, and store video streams 

© Stephane Maarek 



<!-- Start of picture text -->
Kinesis Data Streams<br>Applications Apps (KCL, SDK)<br>Record Record<br>Shard 1<br>Partition Key Partition Key<br>Lambda<br>Client Data Blob Shard 2 Sequence no.<br>(up to 1 MB) Data Blob<br>Kinesis Data<br>1 MB/sec  2 MB/sec (shared)<br>SDK, KPL Firehose<br>or 1000 msg/sec Per shard all consumers<br>per shard Shard N<br>OR<br>Kinesis Agent Kinesis Data<br>Stream 2 MB/sec (enhanced)<br>Analytics<br>Per shard per consumer<br>Producers Kinesis Data Streams Consumers<br>Can scale # of shards<br><!-- End of picture text -->

© Stephane Maarek 

#### Kinesis Data Streams 



- Retention between 1 day to 365 days 

- Ability to reprocess (replay) data 

- Once data is inserted in Kinesis, it can’t be deleted (immutability) 

- Data that shares the same partition goes to the same shard (ordering) 

- Producers: AWS SDK, Kinesis Producer Library (KPL), Kinesis Agent 

- Consumers: 

   - Write your own: Kinesis Client Library (KCL), AWS SDK 

   - Managed: AWS Lambda, Kinesis Data Firehose, Kinesis Data Analytics, 

© Stephane Maarek 

#### Kinesis Data Streams – Capacity Modes 

- Provisioned mode: 

   - You choose the number of shards provisioned, scale manually or using API 

   - Each shard gets 1MB/s in (or 1000 records per second) 

   - Each shard gets 2MB/s out (classic or enhanced fan-out consumer) 

   - You pay per shard provisioned per hour 

- On-demand mode: 

   - No need to provision or manage the capacity 

   - Default capacity provisioned (4 MB/s in or 4000 records per second) 

   - Scales automatically based on observed throughput peak during the last 30 days 

   - Pay per stream per hour & data in/out per GB 

© Stephane Maarek 

#### Kinesis Data Streams Security 

- Control access / authorization using IAM policies 

- Encryption in flight using HTTPS endpoints 

- Encryption at rest using KMS 

- You can implement encryption/decryption of data on client side (harder) 

- VPC Endpoints available for Kinesis to access within VPC 

- Monitor API calls using CloudTrail 



<!-- Start of picture text -->
Region<br>VPC<br>Shard 1<br>Private subnet<br>HTTPS HTTPS<br>Shard 2<br>EC2 Instance VPC Endpoint<br>Shard 3<br>Stream<br>Kinesis Data Stream<br>Encryption at rest<br><!-- End of picture text -->

© Stephane Maarek 



<!-- Start of picture text -->
3rd-party Partner Destinations<br>Kinesis Data Firehose<br>Lambda<br>function<br>Datadog<br>Applications<br>a @y) ti ON e wRelic. |<br>Data<br>Kinesis : & e<br>transformation<br>Data Streams AWS Destinations<br>Amazon S3<br>Client Record<br>go a |<br>Up to 1 MB<br>Amazon Redshift<br>Amazon  Batch writes (COPY through S3)<br>SDK<br>CloudWatch<br>Kinesis<br>(Logs & Events)<br>Amazon OpenSearch<br>Data Firehose<br>All or Failed data<br>Kinesis Agent<br>Custom Destinations<br>AWS IoT<br>S3 backup bucket<br>Producers HTTP Endpoint<br>| FI | a | p ITSIRSLSLSSSSEREIIITIIIEEEEEEIIEAGSSCY |<br>© Stephane Maarek NOT FOR DISTRIBUTION © Stephane Maarek www.datacumulus.com<br><!-- End of picture text -->

© Stephane Maarek 

ns 

#### Kinesis Data Firehose 



- Fully Managed Service, no administration, automatic scaling, serverless • AWS: Redshift / Amazon S3 / OpenSearch 

   - 3rd party partner: Splunk / MongoDB / DataDog / NewRelic / … 

   - Custom: send to any HTTP endpoint 

- Pay for data going through Firehose 

- Near Real Time 

   - Buffer interval: 0 seconds (no buffering) to 900 seconds 

   - Buffer size: minimum 1MB 

- Supports many data formats, conversions, transformations, compression 

- Supports custom data transformations using AWS Lambda 

- Can send failed or all data to a backup S3 bucket 

© Stephane Maarek IE '”TS Ol 

#### Kinesis Data Streams vs Firehose 



Kinesis Data Streams 



Kinesis Data Firehose 

- Streaming service for ingest at scale 

- • Write custom code (producer / consumer) 

- Real-time (~200 ms) 

- Manage scaling (shard splitting / merging) 

- Data storage for 1 to 365 days 

   - Load streaming data into S3 / Redshift / OpenSearch / 3<sup>rd</sup> party / custom HTTP 

   - Fully managed 

   - Near real-time 

   - Automatic scaling 

   - No data storage 

   - Doesn’t support replay capability 

- Supports replay capability 

© Stephane Maarek 

es 

#### Ordering data into Kinesis 

- Imagine you have 100 trucks (truck_1, truck_2, … truck_100) on the road sending their GPS positions regularly into AWS. 

- You want to consume the data in order for each truck, so that you can track their movement accurately. 

- How should you send that data into Kinesis? 

- Answer: send using a “Partition Key” value of the “truck_id” 

> 1 **Kinesis Stream with 3 Shards** — 

> 2 Shard 1 Cp( <mark>aes</mark> e <mark>nscme</mark> ms> 

> 3 Shard 2 Shard 3 

4 5 Partition Key is “truck_id” 

- The same key will always go to the same shard 

© Stephane Maarek SE 

#### Ordering data into SQS 

- For SQS standard, there is no ordering. 

- For SQS FIFO, if you don’t use a Group ID, messages are consumed in the order they are sent, with only one consumer 



<!-- Start of picture text -->
Second batch consumed First batch consumed<br>Consumer 1 Receives Consumer 1 Receives<br>Az Al, C5, C4, C3, B4, C2, B3, C1, B2, B1<br>Direction of consumption<br>a<br>€Last consumed First consumed —><br><!-- End of picture text -->



<!-- Start of picture text -->
5Q5 FIFO Queve<br>Auction | Auction | Auction J Auction ff Auction | Auction | Auction | Auction || Auction | Auction ff Auction<br>A2 Al ¢ ca 3 Ba 2 83 a 82 81 a AU PCN eo ace) BocaEa ed<br>Direction of travel<br>><br><lastin —Firstin—><br><!-- End of picture text -->

- You want to scale the number of consumers, but you want messages to be “grouped” when they are related to each other 

- Then you use a Group ID (similar to Partition Key in Kinesis) 



<!-- Start of picture text -->
Message Group A<br>AA11, A10, A9,AB, AZ, A6, AS, Ad, AS, A2, AT<br>117, 810, 89,88, 87,86, 85,84, BS, 82. B1<br>811, 810, 89, B, 67, 86, 85, 64, 83, 82.81 puacienat aval B10, 89, Consumer88, B7, 86,2 B5,Receives:B4, 83,82, 81<br>Message Group B — Slastin — Firstin> Second batch First batch<br><!-- End of picture text -->

<u>https://aws.amazon.com/blogs/compute/solving-complex-ordering-challenges-with-amazon-sqs-fifo-queues/</u> 

© Stephane Maarek 

#### Kinesis vs SQS ordering 

- Let’s assume 100 trucks, 5 kinesis shards, 1 SQS FIFO 

- <u>Kinesis Data Streams:</u> 

   - On average you’ll have 20 trucks per shard 

   - Trucks will have their data ordered within each shard 

   - The maximum amount of consumers in parallel we can have is 5 

   - Can receive up to 5 MB/s of data 

- <u>SQS FIFO</u> 

   - You only have one SQS FIFO queue 

   - You will have 100 Group ID 

   - You can have up to 100 Consumers (due to the 100 Group ID) 

   - You have up to 300 messages per second (or 3000 if using batching) 

© Stephane Maarek 

#### SQS vs SNS vs Kinesis 



###### **SQS:** 

- Consumer “pull data” 

- Data is deleted after being consumed 

- Can have as many workers (consumers) as we want 

- No need to provision throughput 

- Ordering guarantees only on FIFO queues 

- Individual message delay capability 



###### **SNS:** 

- Push data to many subscribers 

- Up to 12,500,000 subscribers 

- Data is not persisted (lost if not delivered) 

- Pub/Sub 

- Up to 100,000 topics 

- No need to provision throughput 

- Integrates with SQS for fanout architecture pattern 

- FIFO capability for SQS FIFO 



###### **Kinesis:** 

- Standard: pull data 

   - 2 MB per shard 

- Enhanced-fan out: push data 

   - 2 MB per shard per consumer 

- Possibility to replay data 

- Meant for real-time big data, analytics and ETL 

- Ordering at the shard level 

- Data expires after X days 

- • Provisioned mode or ondemand capacity mode 

© Stephane Maarek 

#### Amazon MQ 



- SQS, SNS are “cloud-native” services: proprietary protocols from AWS 

- • Traditional applications running from on-premises may use open protocols such as: MQTT, AMQP, STOMP, Openwire, WSS 

- When migrating to the cloud , instead of re-engineering the application to use SQS and SNS, we can use Amazon MQ 

- Amazon MQ is a managed message broker service for 



<!-- Start of picture text -->
8ay<br>ACTIVEMQ<br><!-- End of picture text -->



<!-- Start of picture text -->
aRabbitMO.<br><!-- End of picture text -->

- Amazon MQ doesn’t “scale” as much as SQS / SNS 

- Amazon MQ runs on servers, can run in Multi-AZ with failover 

- Amazon MQ has both queue feature (~SQS) and topic features (~SNS) 

© Stephane Maarek 

#### Amazon MQ – High Availability 



<!-- Start of picture text -->
Region<br>(us-east-1)<br>ACTIVE Availability Zone<br>1 ‘ H<br>1 i | i '<br>hoa (us-east-1a) H<br>tot i 1<br>pou —, ' :<br>Fe) fo} 1 H<br>H o_o I H<br>Amazon MQ Broker ' H<br>1 f<br>Amazon EFS<br>(storage)<br>Client ee toti STANDBY Availability Zone '' iH<br>failover sel ~ebit (us-east-1b) ‘' Hi<br>ee i H<br>1 1 7s. ‘ H<br>it ~~... a<br>ios me O00 '<br>i ‘o_o<br>to '‘ 1H<br>1 1<br>tot Amazon MQ Broker ' i<br>i | 1 '<br>fo tees eee eee eee eee =e H<br><!-- End of picture text -->

© Stephane Maarek 

### Containers on AWS 

© Stephane Maarek 

es 

#### What is Docker? 



<!-- Start of picture text -->
PCy »<br>docker<br><!-- End of picture text -->

- Docker is a software development platform to deploy apps 

- Apps are packaged in containers that can be run on any OS 

- Apps run the same, regardless of where they’re run 

   - Any machine 

   - No compatibility issues 

   - Predictable behavior 

   - Less work 

   - Easier to maintain and deploy 

   - Works with any language, any OS, any technology 

- Use cases: microservices architecture, lift-and-shift apps from onpremises to the AWS cloud, … 

© Stephane Maarek EES 

#### Docker on an OS 



<!-- Start of picture text -->
A<br><!-- End of picture text -->



<!-- Start of picture text -->
Server (e.g., EC2 instance)<br><!-- End of picture text -->



<!-- Start of picture text -->
docker<br><!-- End of picture text -->



<!-- Start of picture text -->
docker<br><!-- End of picture text -->





<!-- Start of picture text -->
nede<br><!-- End of picture text -->



<!-- Start of picture text -->
docker<br><!-- End of picture text -->



<!-- Start of picture text -->
docker<br><!-- End of picture text -->







<!-- Start of picture text -->
docker<br><!-- End of picture text -->



<!-- Start of picture text -->
DS<br><!-- End of picture text -->



<!-- Start of picture text -->
docker<br><!-- End of picture text -->



© Stephane Maarek 

#### Where are Docker images stored? 

- Docker images are stored in Docker Repositories 

- Docker Hub (https://hub.docker.com) 

   - Public repository 

   - Find base images for many technologies or OS (e.g., Ubuntu, MySQL, …) 

- Amazon ECR (Amazon Elastic Container Registry) 

   - Private repository 

   - Public repository ( Amazon ECR Public Gallery <u>https://gallery.ecr.aws)</u> 

© Stephane Maarek 

#### Docker vs. Virtual Machines 

- Docker is ”sort of” a virtualization technology, but not exactly 

- Resources are shared with the host => many containers on one server 



<!-- Start of picture text -->
Apps Apps Apps<br>a<br>Guest OS  Guest OS  Guest OS<br>(VM) (VM) (VM)<br>Hypervisor Docker Daemon<br>Host OS Host OS (EC2 Instance)<br>Infrastructure Infrastructure<br><!-- End of picture text -->

© Stephane Maarek 

#### Getting Started with Docker 



<!-- Start of picture text -->
ann ' docker |<br>\ [Trt<br>Build Run container<br>Dockerfile<br>docker _ @eython<br>image<br>ubuntu:18.04<br>« /app<br>make /app Push Pull<br>python3 /app/app.y<br>nnn Sn<br>Docker Repository<br>Amazon<br>ECR<br><!-- End of picture text -->

© Stephane Maarek 

#### Docker Containers Management on AWS 

- Amazon Elastic Container Service (Amazon ECS) 

   - Amazon’s own container platform 



Amazon ECS 

- Amazon Elastic Kubernetes Service (Amazon EKS) 

   - Amazon’s managed Kubernetes (open source) 



Amazon EKS 

- AWS Fargate 

   - Amazon’s own Serverless container platform 

   - Works with ECS and with EKS 



AWS Fargate 

- Amazon ECR: 

   - Store container images 



Amazon ECR 

ns 

© Stephane Maarek IE '”TS Ol 

Amazon ECS - EC2 Launch Type 

- ECS = Elastic Container Service 

- Launch Docker containers on AWS = Launch ECS Tasks on ECS Clusters 

- EC2 Launch Type : you must provision & maintain the infrastructure (the EC2 instances) 

- Each EC2 Instance must run the ECS Agent to register in the ECS Cluster 

- AWS takes care of starting / stopping containers 



<!-- Start of picture text -->
Amazon ECS / ECS Cluster<br>New  Docker<br>Container<br>EC2 Instance EC2 Instance EC2 Instance<br>E = = |<br>ECS Agent ECS Agent ECS Agent<br><!-- End of picture text -->

© Stephane Maarek 

**New** Docker Container AWS Fargate / ECS Cluster — 

Amazon ECS – Fargate Launch Type 

- Launch Docker containers on AWS • You do not provision the infrastructure (no EC2 instances to manage) 

- It’s all Serverless! 

- You just create task definitions 

- AWS just runs ECS Tasks for you based on the CPU / RAM you need 

- • To scale, just increase the number of tasks. Simple - no more EC2 instances 

© Stephane Maarek 

- Amazon ECS – IAM Roles for ECS EC2 Instance Profile 

- • EC2 Instance Profile (EC2 Launch Type ECS only): EC2 Instance • Used by the ECS agent ECR 

- • Makes API calls to ECS service • Send container logs to CloudWatch Logs ECS Agent CloudWatch • Pull Docker image from ECR Logs • Reference sensitive data in Secrets Manager or ECS Task A Role SSM Parameter Store Task A S3 

- • ECS Task Role: ECS Task B Role 

- • Allows each task to have a specific role • Use different roles for the different ECS Services you run Task B DynamoDB 

- • Task Role is defined in the <u>task definition</u> 

- © Stephane Maarek 

© Stephane Maarek 

#### Amazon ECS – Load Balancer Integrations 

- Application Load Balancer supported and works for most use cases 

- Network Load Balancer recommended only for high throughput / high performance use cases, or to pair it with AWS Private Link 

- Classic Load Balancer supported but not recommended (no advanced features – no Fargate) 



<!-- Start of picture text -->
EC2 Instance<br>ECS Task<br>ECS Task<br>80/443<br>EC2 Instance<br>Users<br>Application<br>ECS Task<br>Load Balancer<br>ECS Task<br>ECS Cluster<br><!-- End of picture text -->

© Stephane Maarek 

#### Amazon ECS – Data Volumes (EFS) 

- Mount EFS file systems onto ECS tasks 

- Works for both EC2 and Fargate launch types 

- • Tasks running in any AZ will share the same data in the EFS file system 

- Fargate + EFS = Serverless 

- Use cases: persistent multi-AZ shared storage for your containers 

- Note: 

   - Amazon S3 cannot be mounted as a file system 



<!-- Start of picture text -->
EC2 Instance Fargate<br>mount mount<br>ECS Cluster<br>Amazon EFS<br>File System<br><!-- End of picture text -->

© Stephane Maarek 

#### ECS Service Auto Scaling 



<!-- Start of picture text -->
4<br>>tt<<br>v<br><!-- End of picture text -->

- Automatically increase/decrease the desired number of ECS tasks 

- Amazon ECS Auto Scaling uses AWS Application Auto Scaling 

   - ECS Service Average CPU Utilization 

   - ECS Service Average Memory Utilization - Scale on RAM 

   - ALB Request Count Per Target – metric coming from the ALB 

- Target Tracking – scale based on target value for a specific CloudWatch metric 

- Step Scaling – scale based on a specified CloudWatch Alarm 

- Scheduled Scaling – scale based on a specified date/time (predictable changes) 

- ECS Service Auto Scaling (task level) `≠` EC2 Auto Scaling (EC2 instance level) 

- Fargate Auto Scaling is much easier to setup (because Serverless ) 

© Stephane Maarek 

EC2 Launch Type – Auto Scaling EC2 Instances 

- Accommodate ECS Service Scaling by adding underlying EC2 Instances 

- Auto Scaling Group Scaling 

   - Scale your ASG based on CPU Utilization 

   - Add EC2 instances over time 

- ECS Cluster Capacity Provider 

   - Used to automatically provision and scale the infrastructure for your ECS Tasks 

   - Capacity Provider paired with an Auto Scaling Group 

   - Add EC2 Instances when you’re missing capacity (CPU, RAM…) 

© Stephane Maarek 

#### ECS Scaling – Service CPU Usage Example 



<!-- Start of picture text -->
CPU<br>Usage<br>Task 1 Task 3<br>(new)<br>a a e<br>Task 2<br>Service A<br>Auto Scaling<br>Auto Scaling Group<br>Scale ECS Capacity Providers<br>CloudWatch Metric Trigger (optional)<br>(ECS Service CPU Usage)<br>CloudWatch Alarm<br>Scale<br><!-- End of picture text -->

© Stephane Maarek 

ns 

#### ECS tasks invoked by Event Bridge 



<!-- Start of picture text -->
Region<br>VPC<br>Upload object<br>AWS Fargate<br>.<br>Client<br>S3 Bucket<br>Task<br>(new)<br>ECS Task Role<br>Event (Access S3 & DynamoDB) Save result<br>| ; : cf<br>Amazon<br>DynamoDB<br>Amazon ECS Cluster<br>Amazon<br>EventBridge<br>Rule: Run ECS Task<br>Get object<br><!-- End of picture text -->

© Stephane Maarek IE '”TS Ol 

#### ECS tasks invoked by Event Bridge Schedule 



<!-- Start of picture text -->
AWS Fargate<br>Task<br>(new) ECS Task Role<br>Every 1 hour Rule: Run ECS Task Access S3 Batch Processing<br>Amazon S3<br>Amazon<br>EventBridge<br>Amazon ECS Cluster<br><!-- End of picture text -->

© Stephane Maarek IE '”TS Ol 

ns 

#### ECS – SQS Queue Example 



<!-- Start of picture text -->
i) i) ' t<br>i) 1 ' t<br>i) i) Task 1 Task 3 ' t<br>Messages Poll for messages<br>lS ito11 ' ' tHt<br>eni) a) H<br>i) ii '' Ht<br>1 i) ! t<br>SQS Queue i)i i)i) '! tt<br>i) i) ' t<br>i) 1 ' t<br>i) i) Task 2 ' t<br>i 1 ' t<br>i) i) ! t<br>i) Service A ' :<br>1 QE<br>ECS Service Auto Scaling<br>ae Vv<br><!-- End of picture text -->

© Stephane Maarek 

#### ECS – Intercept Stopped Tasks using EventBridge 



<!-- Start of picture text -->
1<br>ECS Task 1<br>1<br>' } Dee event trigger email<br>' er 18 MX @<br>! ie u a5<br>exited<br>' i EventBridge SNS Administrator<br>Containers<br>bee! {<br>"source": [<br>“aws.ecs"<br>1,<br>"detail-type": [<br>"ECS Task State Change"<br>1,<br>"detail": {<br>“lastStatus": [<br>"STOPPED"<br>1,<br>“stoppedReason": [<br>“Essential container in task exited"<br>]<br>+<br>+ Event Pattern<br><!-- End of picture text -->

© Stephane Maarek 

#### Amazon ECR 

- ECR = Elastic Container Registry 

- Store and manage Docker images on AWS 

- Private and Public repository ( Amazon ECR Public Gallery <u>https://gallery.ecr.aws)</u> 

- Fully integrated with ECS, backed by Amazon S3 

- Access is controlled through IAM (permission errors => policy) 

- Supports image vulnerability scanning, versioning, image tags, image lifecycle, … 



ECR Repository Docker Docker Image A Image B 







<!-- Start of picture text -->
pull pull<br>IAM Role<br>EC2 Instance<br>ECS Cluster<br><!-- End of picture text -->

© Stephane Maarek 

#### Amazon EKS Overview 





- Amazon EKS = Amazon Elastic Kubernetes Service 

- It is a way to launch managed Kubernetes clusters on AWS 

- Kubernetes is an open-source system for automatic deployment, scaling and management of containerized (usually Docker) application 

- It’s an alternative to ECS, similar goal but different API 

- EKS supports EC2 if you want to deploy worker nodes or Fargate to deploy serverless containers 

- Use case: if your company is already using Kubernetes on-premises or in another cloud, and wants to migrate to AWS using Kubernetes 

- <u>Kubernetes is cloud-agnostic</u> (can be used in any cloud – Azure, GCP…) 

- For multiple regions, deploy one EKS cluster per region 

- Collect logs and metrics using CloudWatch Container Insights 

© Stephane Maarek 

#### Amazon EKS - Diagram 







<!-- Start of picture text -->
AWS Cloud<br>Availability Zone 1 Availability Zone 2 Availability Zone 3<br>VPC<br>Public subnet 1 Public subnet 2 Public subnet 3<br>EKS<br>Public<br>Service LB<br>ELB NGW ELB NGW ELB NGW<br>Private subnet 1 Private subnet 2 Private subnet 3 EKS<br>Private<br>Service LB<br>ELB<br>EKS node EKS node EKS node<br>Auto Scaling Group<br>EKS Pods EKS Pods EKS Pods<br>EKS Worker Nodes<br><!-- End of picture text -->

© Stephane Maarek 

#### Amazon EKS – Node Types 

- Managed Node Groups • Creates and manages Nodes (EC2 instances) for you • Nodes are part of an ASG managed by EKS • Supports On-Demand or Spot Instances 

- • Self-Managed Nodes • Nodes created by you and registered to the EKS cluster and managed by an ASG • You can use prebuilt AMI - Amazon EKS Optimized AMI • Supports On-Demand or Spot Instances 

- AWS Fargate • No maintenance required; no nodes managed 

© Stephane Maarek 

#### Amazon EKS – Data Volumes 

- Need to specify StorageClass manifest on your EKS cluster 

- Leverages a Container Storage Interface (CSI) compliant driver 

- Support for… 

- Amazon EBS 



<!-- Start of picture text -->
em<br><!-- End of picture text -->



<!-- Start of picture text -->
Ka<br><!-- End of picture text -->

- Amazon EFS (works with Fargate) 

- Amazon FSx for Lustre 

- Amazon FSx for NetApp ONTAP 





© Stephane Maarek 

#### AWS App Runner 

- Fully managed service that makes it easy to deploy web applications and APIs at scale 



<!-- Start of picture text -->
ial<br><!-- End of picture text -->

Container Source Image (Docker) Code 

- No infrastructure experience required 

- Start with your source code or container image 

- Automatically builds and deploy the web app 

- Automatic scaling, highly available, load balancer, encryption 

**Configure Settings** vCPU, RAM, Auto Scaling, Health Check 



- VPC access support 

- Connect to database, cache, and message queue services 

- Use cases: web apps, APIs, microservices, rapid production deployments 

**Create & Deploy** 

**Access using URL** 



<!-- Start of picture text -->
O<br>Y/<br><!-- End of picture text -->



© Stephane Maarek NAYS Cl 

### Serverless Overview 

© Stephane Maarek 

#### What’s serverless? 

- Serverless is a new paradigm in which the developers don’t have to manage servers anymore… 

- They just deploy code 

- They just deploy… functions ! 

- Initially... Serverless == FaaS (Function as a Service) 

- Serverless was pioneered by AWS Lambda but now also includes anything that’s managed: “databases, messaging, storage, etc.” 

- Serverless does not mean there are no servers… it means you just don’t manage / provision / see them 

© Stephane Maarek 

#### Serverless in AWS 

- AWS Lambda 

- DynamoDB 

- AWS Cognito 

- AWS API Gateway 

- Amazon S3 

- AWS SNS & SQS 

- AWS Kinesis Data Firehose 

- Aurora Serverless 

- Step Functions 

- Fargate 

**Users** aNen **S3 bucket API Gateway Cognito Lambda DynamoDB** ns 

###### **S3 bucket API Gateway Cognito** 

**DynamoDB** ns 

© Stephane Maarek IE '”TS Ol 

#### Why AWS Lambda 



- Virtual Servers in the Cloud 

- Limited by RAM and CPU 

- Continuously running 

**Amazon EC2** 

- Scaling means intervention to add / remove servers 

- Virtual functions – no servers to manage! 

- Limited by time - short executions 

• Run on-demand **Amazon Lambda** • Scaling is automated ! © Stephane Maarek IE'”TS Ol ns 

#### Benefits of AWS Lambda 

- Easy Pricing: 

   - Pay per request and compute time 

   - Free tier of 1,000,000 AWS Lambda requests and 400,000 GBs of compute time 

- Integrated with the whole AWS suite of services 

- Integrated with many programming languages 

- Easy monitoring through AWS CloudWatch 

- Easy to get more resources per functions (up to 10GB of RAM!) 

- Increasing RAM will also improve CPU and network! 

© Stephane Maarek 

#### AWS Lambda language support 

- Node.js (JavaScript) 

- • Python 

- Java (Java 8 compatible) 

- • C# (.NET Core) 

- Golang 

- C# / Powershell 

- Ruby 

- Custom Runtime API (community supported, example Rust) 

- Lambda Container Image 

   - The container image must implement the Lambda Runtime API 

   - ECS / Fargate is preferred for running arbitrary Docker images 

© Stephane Maarek 

#### AWS Lambda Integrations Main ones 





**Kinesis** 

**API Gateway** 





**CloudWatch Events CloudWatch Logs EventBridge** 



###### **DynamoDB** 



**SNS** 



**S3** 



**SQS** 



###### **CloudFront** 



**Cognito** 

© Stephane Maarek AN '"Wl 

#### Example: Serverless Thumbnail creation 



<!-- Start of picture text -->
Be<br><!-- End of picture text -->

**New image in S3** —: 



<!-- Start of picture text -->
New thumbnail in S3<br>trigger<br>IN<br>Wy K<br>AWS Lambda Function<br>Creates a Thumbnail<br>Metadata in DynamoDB<br>=<br>push<br>push<br><!-- End of picture text -->





<!-- Start of picture text -->
Image name<br>Image size<br>Creation date<br>etc…<br><!-- End of picture text -->

© Stephane Maarek 

#### Example: Serverless CRON Job 





<!-- Start of picture text -->
Trigger<br>Every 1 hour<br><!-- End of picture text -->



###### **CloudWatch Events AWS Lambda Function EventBridge Perform a task** 

© Stephane Maarek 

AWS Lambda Pricing: example 

- You can find overall pricing information here: <u>https://aws.amazon.com/lambda/pricing/</u> 

- • Pay per calls : • First 1,000,000 requests are free • $0.20 per 1 million requests thereafter ($0.0000002 per request) 

- • Pay per duration : (in increment of 1 ms) • 400,000 GB-seconds of compute time per month for FREE • == 400,000 seconds if function is 1GB RAM • == 3,200,000 seconds if function is 128 MB RAM • After that $1.00 for 600,000 GB-seconds 

- • It is usually very cheap to run AWS Lambda so it’s very popular 

© Stephane Maarek 

#### AWS Lambda Limits to Know - per region 

- Execution: 

   - Memory allocation: 128 MB – 10GB (1 MB increments) 

   - Maximum execution time: 900 seconds (15 minutes) 

   - Environment variables (4 KB) 

   - Disk capacity in the “function container” (in /tmp): 512 MB to 10GB 

   - Concurrency executions: 1000 (can be increased) 

- Deployment: 

   - Lambda function deployment size (compressed .zip): 50 MB 

   - Size of uncompressed deployment (code + dependencies): 250 MB 

   - Can use the /tmp directory to load other files at startup 

   - Size of environment variables: 4 KB 

© Stephane Maarek 

#### Lambda SnapStart 

- Improves your Lambda functions performance up to 10x at no extra cost for Java 11 and above 

- • When enabled, function is invoked from a preinitialized state (no function initialization from scratch) 

- When you publish a new version: 

   - Lambda initializes your function 

   - Takes a snapshot of memory and disk state of the initialized function 

   - Snapshot is cached for low-latency access 



<!-- Start of picture text -->
SnapStart SnapStart<br>enabled disabled<br>invoke invoke<br>Lambda Lambda<br>(Java) (Java)<br>function is<br>pre-initialized<br>Init<br>Invoke Invoke<br>Shutdown Shutdown<br><!-- End of picture text -->

**Lambda Invocation Lifecycle Phases** 

© Stephane Maarek 

#### Customization At The Edge 



- Many modern applications execute some form of the logic at the edge 

- Edge Function: 

   - A code that you write and attach to CloudFront distributions 

   - Runs close to your users to minimize latency 

- CloudFront provides two types: CloudFront Functions & Lambda@Edge 

- You don’t have to manage any servers, deployed globally 

- Use case: customize the CDN content 

• Pay only for what you use • Fully serverless © Stephane Maarek IE'”TS Ol ns 

CloudFront Functions & Lambda@Edge Use Cases 



• Website Security and Privacy 

- Dynamic Web Application at the Edge 

- Search Engine Optimization (SEO) 

- Intelligently Route Across Origins and Data Centers 

- Bot Mitigation at the Edge 

- Real-time Image Transformation 

- A/B Testing 

- User Authentication and Authorization 

• User Prioritization • User Tracking and Analytics © Stephane Maarek IE'”TS Ol ns 

CloudFront Functions Client • Lightweight functions written in JavaScript **Viewer Viewer** • For high-scale, latency-sensitive CDN customizations **Request Response** • Sub-ms startup times, millions of requests/second • Used to change Viewer requests and responses: • Viewer Request: after CloudFront receives a request from a CloudFront viewer • Viewer Response: before CloudFront forwards the response Origin Origin to the viewer Request Response • Native feature of CloudFront (manage code entirely within CloudFront) Origin © Stephane Maarek <mark>|</mark> 

Client Lambda@Edge • Lambda functions written in NodeJS or Python • Scales to 1000s of requests/second **Viewer Viewer Request Response** • Used to change CloudFront requests and responses: • Viewer Request – after CloudFront receives a request from a viewer • Origin Request – before CloudFront forwards the request to the origin CloudFront • Origin Response – after CloudFront receives the response from the origin **Origin Origin** • Viewer Response – before CloudFront forwards the response to **Request Response** the viewer • Author your functions in one AWS Region (us-east-1), then CloudFront replicates to its locations Origin © Stephane Maarek <mark>|</mark> 

#### CloudFront Functions vs. Lambda@Edge 

||**CloudFront Functions**|**Lambda@Edge**|
|---|---|---|
|Runtime Support|JavaScript|Node.js, Python|
|# of Requests|**Millions**of requests per second|**Thousands**of requests per second|
|CloudFront Triggers|-<br>Viewer Request/Response|-<br>Viewer Request/Response<br>-<br>Origin Request/Response|
|Max. Execution Time|< 1 ms|5 – 10 seconds|
|Max. Memory|2 MB|128 MB up to 10 GB|
|Total Package Size|10 KB|1 MB – 50 MB|
|Network Access, File System Access|No|Yes|
|Access to the Request Body|No|Yes|
|Pricing|Free tier available, 1/6<sup>th</sup>price of @Edge|No free tier, charged per request & duration|



© Stephane Maarek 

###### CloudFront Functions vs. Lambda@Edge - Use Cases 

###### CloudFront Functions 

###### Lambda@Edge 

- Cache key normalization 

   - Longer execution time (several ms) 

- Transform request attributes (headers, cookies, query strings, URL) to create an optimal Cache Key 

      - Adjustable CPU or memory 

      - Your code depends on a 3rd libraries (e.g., AWS SDK to access other AWS services) 

- Header manipulation 

   - Insert/modify/delete HTTP headers in the request or response 

- URL rewrites or redirects 

   - Network access to use external services for processing 

- Request authentication & authorization services for processing • Create and validate user-generated • File system access or access to the 

- tokens (e.g., JWT) to allow/deny requests body of HTTP requests 

© Stephane Maarek 

ns 

#### Lambda by default 

- By default, your Lambda function is launched outside your own VPC (in an AWS-owned VPC) 

- Therefore, it cannot access resources in your VPC (RDS, ElastiCache, internal ELB…) 

###### **Default Lambda Deployment** 



<!-- Start of picture text -->
AWS Cloud<br>Public<br>ca www<br>works<br>DynamoDB<br>VPC & Private Subnet<br>Not working<br>Private RDS<br><!-- End of picture text -->

© Stephane Maarek IE '”TS Ol 

Lambda in VPC Lambda Function • You must define the VPC ID, the **Private subnet** Subnets and the Security Groups • Lambda will create an ENI (Elastic Lambda Security group Network Interface) in your subnets Elastic Network Interface (ENI) RDS Security group Amazon RDS In VPC ~~<mark>I</mark>~~ (2 © Stephane Maarek N <mark>NN</mark> '”~-OHOM 22 

#### Lambda with RDS Proxy 

- If Lambda functions directly access your database, they may open too many connections under high load 

- RDS Proxy 

   - Improve scalability by pooling and sharing DB connections 

   - Improve availability by reducing by 66% the failover time and preserving connections 

   - Improve security by enforcing IAM authentication and storing credentials in Secrets Manager 

- The Lambda function must be deployed in your VPC, because RDS Proxy is never <u>publicly accessible</u> 





<!-- Start of picture text -->
VPC<br>Lambda functions<br>…<br><!-- End of picture text -->



<!-- Start of picture text -->
Private subnet<br>RDS Proxy<br><!-- End of picture text -->







<!-- Start of picture text -->
RDS DB<br>Instance<br><!-- End of picture text -->

© Stephane Maarek 

#### Invoking Lambda from RDS & Aurora 

- Invoke Lambda functions from within your DB instance 

- • Allows you to process data events from within a database 

- • Supported for RDS for PostgreSQL and Aurora MySQL • Must allow outbound traffic to your Lambda function from within your DB instance (Public, NAT GW, VPC Endpoints) 

- • DB instance must have the required permissions to invoke the Lambda function (Lambda Resource-based Policy & IAM Policy) 



User register **(INSERT)** RDS DB Instance **Permissions** invoke Lambda function send Email Amazon SES 

© Stephane Maarek 

#### RDS Event Notifications 

RDS DB Instance • Notifications that tells information about the DB = instance itself (created, stopped, start, …) • You don’t have any information about the data itself • Subscribe to the following event categories: DB instance, DB snapshot, DB Parameter Group, DB Security Group, RDS Proxy, Custom Engine Version SNS EventBridge • Near real-time events (up to 5 minutes) • Send notifications to SNS or subscribe to events ae using EventBridge … mH @ @® SQS Lambda Lambda Queue function function IE '”TS Ol ns 

© Stephane Maarek IE '”TS Ol 

#### Amazon DynamoDB 



- Fully managed, highly available with replication across multiple AZs 

- NoSQL database - not a relational database - with transaction support 

- Scales to massive workloads, distributed database 

- Millions of requests per seconds, trillions of row, 100s of TB of storage 

- Fast and consistent in performance (single-digit millisecond) 

- Integrated with IAM for security, authorization and administration 

- Low cost and auto-scaling capabilities 

• No maintenance or patching, always available • Standard & Infrequent Access (IA) Table Class © Stephane Maarek IE'”TS Ol ns 

#### DynamoDB - Basics 



<!-- Start of picture text -->
Oc<br>Oc<br>OC<br>oc<br><!-- End of picture text -->

- DynamoDB is made of Tables 

- Each table has a Primary Key (must be decided at creation time) 

- Each table can have an infinite number of items (= rows) 

- Each item has attributes (can be added over time – can be null) 

- Maximum size of an item is 400KB 

- Data types supported are: 

   - Scalar Types – String, Number, Binary, Boolean, Null 

   - Document Types – List, Map 

   - Set Types – String Set, Number Set, Binary Set 

- <u>Therefore, in DynamoDB you can rapidly evolve schemas</u> 

© Stephane Maarek 

#### DynamoDB – Table example 



<!-- Start of picture text -->
Primary Key Attributes<br>Partition Key Sort Key<br>User_ID Game_ID Score Result<br>7791a3d6-… 4421 92 Win<br>873e0634-… 1894 14 Lose<br>873e0634-… 4521 77 Win<br><!-- End of picture text -->

© Stephane Maarek 

#### DynamoDB – Read/Write Capacity Modes 

- Control how you manage your table’s capacity (read/write throughput) 

- Provisioned Mode (default) 

   - You specify the number of reads/writes per second 

   - You need to plan capacity beforehand 

   - Pay for provisioned Read Capacity Units (RCU) & Write Capacity Units (WCU) 

   - Possibility to add auto-scaling mode for RCU & WCU 

- On-Demand Mode 

   - Read/writes automatically scale up/down with your workloads 

   - No capacity planning needed 

   - Pay for what you use, more expensive ($$$) 

   - Great for unpredictable workloads, steep sudden spikes 

© Stephane Maarek 

#### DynamoDB Accelerator (DAX) 

- Fully-managed, highly available, seamless inmemory cache for DynamoDB 

- Help solve read congestion by caching 

- <u>Microseconds latency for cached data</u> 

- • Doesn’t require application logic modification (compatible with existing DynamoDB APIs) 

- 5 minutes TTL for cache (default) 



<!-- Start of picture text -->
£=<br>—<br><!-- End of picture text -->



<!-- Start of picture text -->
Application<br>|<br>DAX Cluster<br>…<br>Nodes<br><!-- End of picture text -->



<!-- Start of picture text -->
Amazon DynamoDB<br>eeeSS = …<br>Tables<br><!-- End of picture text -->

© Stephane Maarek 



<!-- Start of picture text -->
DynamoDB Accelerator (DAX) vs. ElastiCache<br>Amazon<br>ElastiCache<br>Store Aggregation Result<br>=<br>- Individual objects cache<br>Application<br>- Query & Scan cache<br>Amazon<br>DynamoDB<br>DynamoDB Accelerator (DAX)<br><!-- End of picture text -->

© Stephane Maarek 

ns 

#### DynamoDB – Stream Processing 



<!-- Start of picture text -->
oon<br><!-- End of picture text -->

- Ordered stream of item-level modifications (create/update/delete) in a table 

- • Use cases: 

   - React to changes in real-time (welcome email to users) 

   - Real-time usage analytics 

   - Insert into derivative tables 

   - Implement cross-region replication 

   - Invoke AWS Lambda on changes to your DynamoDB table 

###### <u>DynamoDB Streams</u> 

   - 24 hours retention 

   - Limited # of consumers 

- Process using AWS Lambda Triggers, or DynamoDB Stream Kinesis adapter 

- © Stephane Maarek 

- IE '”TS Ol 

###### <u>Kinesis Data Streams (newer)</u> 

- 1 year retention 

- High # of consumers 

- Process using AWS Lambda, Kinesis Data Analytics, Kineis Data Firehose, AWS Glue Streaming ETL… 



<!-- Start of picture text -->
DynamoDB Streams<br>messaging, notifications<br>Processing Layer Amazon SNS<br>DynamoDB<br>KCL Adapter<br>filtering, transforming, …<br>DDB Table<br>Lambda<br>create/update/delete<br>0 £ 20 ® | =<br>Application Table DynamoDB analytics Amazon<br>Streams<br>Redshift<br>archiving<br>Amazon S3<br>= e<br>Kinesis Data Kinesis Data<br>Streams Firehose<br>indexing Amazon<br>OpenSearch<br>© Stephane Maarek<br>aes iol<br><!-- End of picture text -->

#### DynamoDB Global Tables 



<!-- Start of picture text -->
GLOBAL TABLE<br>Table Table<br>US-EAST-1 AP-SOUTHEAST-2<br>| oo two-way oC<br>replication<br>| Oo oc<br>' oo oc<br>| oo oc<br><!-- End of picture text -->

- Make a DynamoDB table accessible with low latency in multiple-regions • Active-Active replication 

- Applications can <u>READ</u> and <u>WRITE</u> to the table in any region 

- Must enable DynamoDB Streams as a pre-requisite 

© Stephane Maarek 

DynamoDB – Time To Live (TTL) 

**Current Time** © Friday, September 10, 2021, 11:56:11 AM **(Epoch timestamp: 1631274971)** Expiration Process scan & **expire** items • Automatically delete items after an expiry timestamp **SessionData (Table)** • Use cases: reduce stored data by keeping only **User_ID Session_ID ExpTime (TTL)** current items, adhere to regulatory 7791a3d6-… 74686572652 1631188571 obligations, web session handling… 873e0634-… 6e6f7468696 1631274971 a80f73a1-… 746f2073656 1631102171 scan & **delete** items Deletion Process © Stephane Maarek S'”=S Ol ~~E~~ TE <mark>ee</mark> 

#### DynamoDB – Backups for disaster recovery 

- Continuous backups using point-in-time recovery (PITR) 

   - Optionally enabled for the last 35 days 

   - Point-in-time recovery to any time within the backup window 

   - The recovery process creates a new table 

- On-demand backups 

   - Full backups for long-term retention, until explicitely deleted 

   - Doesn’t affect performance or latency 

   - Can be configured and managed in AWS Backup (enables cross-region copy) 

   - The recovery process creates a new table 

© Stephane Maarek 

#### DynamoDB – Integration with Amazon S3 

- Export to S3 (must enable PITR) 

   - Works for any point of time in the last 35 days 

   - Doesn’t affect the read capacity of your table 

   - • Perform data analysis on top of DynamoDB 

   - Retain snapshots for auditing 

   - ETL on top of S3 data before importing back into DynamoDB 

export query DynamoDB S3 Athena 

   - Export in DynamoDB JSON or ION format 

- Import from S3 

   - Import CSV, DynamoDB JSON or ION format 

   - • Doesn’t consume any write capacity • Creates a new table 

   - Import errors are logged in CloudWatch Logs 

import S3 DynamoDB **(.csv, .json, .ion)** ns 

© Stephane Maarek IE '”TS Ol 

Example: Building a Serverless API 

REST API PROXY REQUESTS CRUD o o © oO **Client API Gateway Lambda DynamoDB** 

© Stephane Maarek IE '”TS Ol 

ns 

|AWS API Gateway|
|---|





|• AWS Lambda + API Gateway: No infrastructure to manage|
|---|



|• Support for the WebSocket Protocol|
|---|



|• Handle API versioning (v1, v2…)|
|---|



|• Handle different environments (dev, test, prod…)|
|---|



|• Handle security (Authentication and Authorization)|
|---|



|• Create API keys, handle request throttling|
|---|



|• Swagger / Open API import to quickly define APIs|
|---|



|• Transform and validate requests and responses|
|---|



• Generate SDK and API specifications • Cache API responses © Stephane Maarek IE'”TS Ol ns 

#### API Gateway – Integrations High Level 

- Lambda Function 

   - Invoke Lambda function 

   - Easy way to expose REST API backed by AWS Lambda 

- HTTP 

   - Expose HTTP endpoints in the backend 

   - Example: internal HTTP API on premise, Application Load Balancer… 

   - Why? Add rate limiting, caching, user authentications, API keys, etc… 

- AWS Service 

   - Expose any AWS API through the API Gateway 

   - Example: start an AWS Step Function workflow, post a message to SQS 

   - Why? Add authentication, deploy publicly, rate control… 

© Stephane Maarek 

ns 

API Gateway – AWS Service Integration Kinesis Data Streams example store **.json** send records files Og requests API Gateway Kinesis Data Kinesis Data Amazon S3 **Client** 6 & eB Streams Firehose 

© Stephane Maarek IE '”TS Ol 

#### API Gateway - Endpoint Types 

- Edge-Optimized (default): For global clients 

   - Requests are routed through the CloudFront Edge locations (improves latency) 

   - • The API Gateway still lives in only one region 

- Regional: 

   - For clients within the same region 

   - Could manually combine with CloudFront (more control over the caching strategies and the distribution) 

- Private: 

   - Can only be accessed from your VPC using an interface VPC endpoint (ENI) 

   - • Use a resource policy to define access 

© Stephane Maarek 

#### API Gateway – Security 

- User Authentication through 

   - IAM Roles (useful for internal applications) 

   - Cognito (identity for external users – example mobile users) 

   - Custom Authorizer (your own logic) 

- Custom Domain Name HTTPS security through integration with AWS Certificate Manager (ACM) 

   - If using Edge-Optimized endpoint, then the certificate must be in us-east-1 

   - If using Regional endpoint, the certificate must be in the API Gateway region 

   - Must setup CNAME or A-alias record in Route 53 

© Stephane Maarek 

#### AWS Step Functions 



<!-- Start of picture text -->
a<br><!-- End of picture text -->



<!-- Start of picture text -->
Mi In Progress Mi Succeeded Ml Failed ! Cancelled Mi Caught Error<br><!-- End of picture text -->

- Build serverless visual workflow to orchestrate your Lambda functions 



<!-- Start of picture text -->
3<br><!-- End of picture text -->

- Features: sequence, parallel, conditions, timeouts, error handling, … 

- Can integrate with EC2, ECS, On-premises servers, API Gateway, SQS queues, etc… 

- • Possibility of implementing human approval feature 

- Use cases: order fulfillment, data processing, web applications, any workflow 

© Stephane Maarek 

#### Amazon Cognito 



- Give users an identity to interact with our web or mobile application 

- Cognito User Pools: 

   - Sign in functionality for app users 

   - Integrate with API Gateway & Application Load Balancer 

- Cognito Identity Pools (Federated Identity): 

   - Provide AWS credentials to users so they can access AWS resources directly 

   - Integrate with Cognito User Pools as an identity provider 

• Cognito vs IAM: “hundreds of users”, ”mobile users”, “authenticate with SAML” © Stephane Maarek IE'”TS Ol ns 

Cognito User Pools (CUP) – User Features 

- Create a serverless database of user for your web & mobile apps 

- Simple login: Username (or email) / password combination 

- Password reset 

- Email & Phone Number Verification 

- Multi-factor authentication (MFA) 

- Federated Identities: users from Facebook, Google, SAML… 

© Stephane Maarek 



<!-- Start of picture text -->
Cognito User Pools (CUP) - Integrations<br>• CUP integrates with  API Gateway  and  Application Load Balancer<br>Cognito User Pools<br>Authenticate Authenticate<br>Cognito User Pools<br>Retrieve token<br>Evaluate Cognito Token<br>REST API +<br>Pass Token Application Load Balancer<br>+ Listeners & Rules<br>a 2<br>backend Target Group<br>API Gateway<br><!-- End of picture text -->



<!-- Start of picture text -->
Cognito User Pools<br>Authenticate<br>Application Load Balancer<br>+ Listeners & Rules<br>Target Group<br>Backend<br><!-- End of picture text -->

© Stephane Maarek 

#### Cognito Identity Pools (Federated Identities) 

- Get identities for “users” so they obtain temporary AWS credentials 

- Users source can be Cognito User Pools, 3<sup>rd</sup> party logins, etc… 

- Users can then access AWS services directly or through API Gateway 

- The IAM policies applied to the credentials are defined in Cognito 

- They can be customized based on the user_id for fine grained control 

- Default IAM roles for authenticated and guest users 

© Stephane Maarek 



<!-- Start of picture text -->
Cognito Identity Pools – Diagram<br>Login and Get Token<br>Of. — — +. 6H<br>Social Identity Provider<br>Web & Mobile  Exchange token  Cognito Identity Pools<br>&<br>for temporary<br>Applications<br>AWS credentials validate<br>-<br>[a = SAML4S<br>Direct access to AWS<br>a csOpeniD<br>Cognito<br>Ee<br>User Pools<br>GS O Co ]<br>Private S3 Bucket  DynamoDB Table<br><!-- End of picture text -->

© Stephane Maarek 

#### Cognito Identity Pools Row Level Security in DynamoDB 



<!-- Start of picture text -->
{<br>"Version": "2012-10-17",<br>"Statement": [<br>{<br>"Effect": "Allow",<br>"Action": [<br>“dynamodb:GetItem", "dynamodb:BatchGetItem", "“dynamodb: Query",<br>“dynamodb:PutItem", "dynamodb:UpdateItem", "“dynamodb:DeleteItem",<br>“dynamodb: BatchWriteItem"<br>1,<br>"Resource": [<br>“arn:aws : dynamodb: us—west-2: 123456789012: table/MyTable"<br>1,<br>"Condition": {<br>"ForAllWalues:StringEquals": {<br>“@ynamodb: LeadingKeys":<br>]<br>+<br>+<br>+<br>]<br>+<br><!-- End of picture text -->

© Stephane Maarek 

### Serverless Architectures 

© Stephane Maarek 

Mobile application: MyTodoList 

- We want to create a mobile application with the following requirements 

- Expose as REST API with HTTPS 

- Serverless architecture 

- Users should be able to directly interact with their own folder in S3 

- Users should authenticate through a managed serverless service 

- The users can write and read to-dos, but they mostly read them 

- The database should scale, and have some high read throughput 

© Stephane Maarek 



<!-- Start of picture text -->
Mobile app: REST API layer<br>REST HTTPS invoke query<br>i<br>AWS Lambda Amazon DynamoDB<br>Amazon API Gateway<br>Mobile<br>client<br>Verify authentication<br>authenticate<br>Amazon Cognito<br><!-- End of picture text -->

© Stephane Maarek IE '”TS Ol 

ns 

es 

#### Mobile app: giving users access to S3 



<!-- Start of picture text -->
Store/retrieve files<br>Amazon S3<br>Permissions<br>F<br>AWS Lambda Amazon DynamoDB<br>Amazon API Gateway<br>Mobile<br>client<br>authenticate<br>Generate temp<br>credentials<br>Amazon Cognito AWS STS<br><!-- End of picture text -->

© Stephane Maarek SE 



<!-- Start of picture text -->
Mobile app: high read throughput, static data<br>Store/retrieve files<br>Amazon S3<br>Permissions<br>REST HTTPS invoke Query / read<br>i i DN a<br>AWS Lambda<br>Amazon API Gateway DAX DynamoDB<br>Mobile<br>Caching layer<br>client<br>Verify authentication<br>authenticate<br>Generate temp<br>credentials<br>Amazon Cognito AWS STS<br><!-- End of picture text -->

© Stephane Maarek SE 

es 



<!-- Start of picture text -->
Mobile app: caching at the API Gateway<br>Store/retrieve files<br>Amazon S3<br>CACHING OF RESPONSES<br>Permissions<br>REST HTTPS invoke Query / read<br>i (- DN a<br>AWS Lambda<br>Amazon API Gateway DAX DynamoDB<br>Mobile<br>Caching layer<br>client<br>Verify authentication<br>authenticate<br>Generate temp<br>credentials<br>Amazon Cognito AWS STS<br><!-- End of picture text -->

© Stephane Maarek SE 

es 

#### In this lecture 

- Serverless REST API: HTTPS, API Gateway, Lambda, DynamoDB 

- Using Cognito to generate temporary credentials with STS to access S3 bucket with restricted policy. App users can directly access AWS resources this way. Pattern can be applied to DynamoDB, Lambda… 

- • Caching the reads on DynamoDB using DAX 

- Caching the REST requests at the API Gateway level 

- Security for authentication and authorization with Cognito, STS 

© Stephane Maarek 

#### Serverless hosted website: MyBlog.com 

- This website should scale globally 

- Blogs are rarely written, but often read 

- Some of the website is purely static files, the rest is a dynamic REST API 

- Caching must be implement where possible 

- Any new users that subscribes should receive a welcome email 

- Any photo uploaded to the blog should have a thumbnail generated 

© Stephane Maarek 

ns 

#### Serving static content, globally 



<!-- Start of picture text -->
Interaction with<br>edge locations Amazon CloudFront Amazon S3<br>Global distribution<br>=<br>Client<br><!-- End of picture text -->

© Stephane Maarek IE '”TS Ol 

**Bucket policy** Only authorize from CloudFront Distribution Amazon S3 ns 

#### Serving static content, globally, securely 

OAC: Origin Access Control Interaction with edge locations Amazon CloudFront Global distribution = Client 

© Stephane Maarek IE '”TS Ol 

#### Adding a public serverless REST API 



<!-- Start of picture text -->
OAC: Origin Access Control<br>Bucket policy<br>Only authorize from<br>Interaction with<br>CloudFront Distribution<br>edge locations Amazon CloudFront Amazon S3<br>Global distribution<br>REST HTTPS invoke Query / read<br>CJ ( x ag €<br>AWS Lambda<br>Amazon API Gateway DAX DynamoDB<br>Client<br>Caching layer<br><!-- End of picture text -->

es 

© Stephane Maarek SE 

#### Leveraging DynamoDB Global Tables 



<!-- Start of picture text -->
OAC: Origin Access Control<br>Bucket policy<br>Only authorize from<br>Interaction with<br>CloudFront Distribution<br>edge locations Amazon CloudFront Amazon S3<br>Global distribution<br>REST HTTPS invoke Query / read<br>CJ ( x ag €<br>AWS Lambda<br>Amazon API Gateway DAX DynamoDB<br>Client<br>Caching layer Global Tables<br><!-- End of picture text -->

© Stephane Maarek SE 

es 

#### User Welcome email flow 

OAC: Origin Access Control **Bucket policy** Only authorize from Interaction with CloudFront Distribution edge locations Amazon CloudFront Amazon S3 Global distribution REST HTTPS invoke Query / read = ( DN a £ AWS Lambda Amazon API Gateway DAX DynamoDB Client Caching layer A Stream changes IAM Role SDK to send email @ n Invoke lambda E Amazon Simple AWS Lambda DynamoDB Email Service (SES) **Stream** SE ’”- Oh es 

© Stephane Maarek SE 

#### Thumbnail Generation flow 

OAC: Origin Access Control **Bucket policy** Only authorize from Interaction with CloudFront Distribution edge locations Amazon CloudFront Amazon S3 Global distribution REST HTTPS invoke Query / read AWS Lambda Oo Amazon API Gateway f ~~f 8~~ 8 DAX GB DynamoDB Client Caching layer optional Upload photos Transfer acceleration OAC trigger thumbnail SQS EA8 8a Amazon CloudFront Amazon S3 AWS Lambda Amazon S3 Global distribution SNS © Stephane Maarek SE ’'”-= hs 

#### AWS Hosted Website Summary 

- We’ve seen static content being distributed using CloudFront with S3 

- The REST API was serverless, didn’t need Cognito because public 

- We leveraged a Global DynamoDB table to serve the data globally 

- (we could have used Aurora Global Database) 

- We enabled DynamoDB streams to trigger a Lambda function 

- The lambda function had an IAM role which could use SES 

- SES (Simple Email Service) was used to send emails in a serverless way 

- S3 can trigger SQS / SNS / Lambda to notify of events 

© Stephane Maarek 

#### Micro Services architecture 

- We want to switch to a micro service architecture 

- Many services interact with each other directly using a REST API 

- Each architecture for each micro service may vary in form and shape 

- We want a micro-service architecture so we can have a leaner development lifecycle for each service 

© Stephane Maarek 

#### Micro Services Environment 



<!-- Start of picture text -->
service1.example.com<br>DNS Query<br>Amazon Route 53<br>Elastic Load Balancing ECS DynamoDB<br>service2.example.com<br>HTTPS<br>Amazon API Gateway AWS Lambda ElastiCache<br>Users<br>service3.example.com<br>—_<br>Elastic Load Balancing Amazon EC2<br>Amazon RDS<br>Auto Scaling<br><!-- End of picture text -->

© Stephane Maarek 

#### Discussions on Micro Services 

- You are free to design each micro-service the way you want 

- Synchronous patterns: API Gateway, Load Balancers 

- Asynchronous patterns: SQS, Kinesis, SNS, Lambda triggers (S3) 

- Challenges with micro-services: 

   - repeated overhead for creating each new microservice, 

   - issues with optimizing server density/utilization 

   - complexity of running multiple versions of multiple microservices simultaneously 

   - proliferation of client-side code requirements to integrate with many separate services. 

- Some of the challenges are solved by Serverless patterns: 

   - API Gateway, Lambda scale automatically and you pay per usage 

   - You can easily clone API, reproduce environments 

   - Generated client SDK through Swagger integration for the API Gateway 

© Stephane Maarek 

#### Software updates offloading 

- We have an application running on EC2, that distributes software updates once in a while 

- When a new software update is out, we get a lot of request and the content is distributed in mass over the network. It’s very costly 

- We don’t want to change our application, but want to optimize our cost and CPU, how can we do it? 

© Stephane Maarek 

#### Our application current state 





<!-- Start of picture text -->
Auto Scaling group<br>Availability zone 1<br>Availability zone 1 to 3<br>Availability zone 2<br>Amazon Elastic<br>File System<br>Availability zone 3<br>© Stephane Maarek<br><!-- End of picture text -->



<!-- Start of picture text -->
Easy way to fix things!<br>Auto Scaling group<br>Availability zone 1<br>ol<br>Availability zone 1 to 3<br>Availability zone 2<br>BL OU<br>Amazon Elastic<br>Amazon CloudFront File System<br>Availability zone 3<br>c e:<br>NOT FOR DISTRIBUTION © Stephane Maarek www.datacumulus.com<br><!-- End of picture text -->

© Stephane Maarek 

#### Why CloudFront? 

- No changes to architecture 

- Will cache software update files at the edge 

- Software update files are not dynamic, they’re static (never changing) 

- Our EC2 instances aren’t serverless 

- But CloudFront is, and will scale for us 

- Our ASG will not scale as much, and we’ll save tremendously in EC2 

- We’ll also save in availability, network bandwidth cost, etc 

- Easy way to make an existing application more scalable and cheaper! 

© Stephane Maarek 

### Databases in AWS 

© Stephane Maarek 

#### Choosing the Right Database 

- We have a lot of managed databases on AWS to choose from 

- Questions to choose the right database based on your architecture: • Read-heavy, write-heavy, or balanced workload? Throughput needs? Will it change, does it need to scale or fluctuate during the day? 

- • How much data to store and for how long? Will it grow? Average object size? How are they accessed? 

   - Data durability? Source of truth for the data ? 

   - Latency requirements? Concurrent users? 

   - Data model? How will you query the data? Joins? Structured? Semi-Structured? 

   - • Strong schema? More flexibility? Reporting? Search? RDBMS / NoSQL? • License costs? Switch to Cloud Native DB such as Aurora? 

© Stephane Maarek 

#### Database Types 

- RDBMS (= SQL / OLTP): RDS, Aurora – great for joins 



<!-- Start of picture text -->
Ei<br><!-- End of picture text -->

- NoSQL database – no joins, no SQL : DynamoDB (~JSON), ElastiCache (key / value pairs), Neptune (graphs), DocumentDB (for MongoDB), Keyspaces (for Apache Cassandra) 

- Object Store: S3 (for big objects) / Glacier (for backups / archives) 

- • Data Warehouse (= SQL Analytics / BI): Redshift (OLAP), Athena, EMR 

- Search: OpenSearch (JSON) – free text, unstructured searches 

- Graphs: Amazon Neptune – displays relationships between data 

- Ledger : Amazon Quantum Ledger Database 

- Time series : Amazon Timestream 

• Note: some databases are being discussed in the Data & Analytics section © Stephane Maarek IE'”TS Ol ns 

#### Amazon RDS – Summary 

- Managed PostgreSQL / MySQL / Oracle / SQL Server / DB2 / MariaDB / Custom 



<!-- Start of picture text -->
RA<br>Ces<br><!-- End of picture text -->

- Provisioned RDS Instance Size and EBS Volume Type & Size 

- Auto-scaling capability for Storage 

- Support for Read Replicas and Multi AZ 

- Security through IAM, Security Groups, KMS , SSL in transit 

- Automated Backup with Point in time restore feature (up to 35 days) 

- Manual DB Snapshot for longer-term recovery 

- Managed and Scheduled maintenance (with downtime) 

- Support for IAM Authentication, integration with Secrets Manager 

- RDS Custom for access to and customize the underlying instance (Oracle & SQL Server) 

- Use case: Store relational datasets (RDBMS / OLTP), perform SQL queries, transactions 

© Stephane Maarek 

#### Amazon Aurora – Summary 



- Compatible API for PostgreSQL / MySQL, separation of storage and compute 

- Storage: data is stored in 6 replicas, across 3 AZ – highly available, self-healing, auto-scaling 

- Compute: Cluster of DB Instance across multiple AZ, auto-scaling of Read Replicas 

- Cluster: Custom endpoints for writer and reader DB instances 

- Same security / monitoring / maintenance features as RDS 

- Know the backup & restore options for Aurora 

- Aurora Serverless – for unpredictable / intermittent workloads, no capacity planning 

- Aurora Global: up to 16 DB Read Instances in each region, < 1 second storage replication 

- Aurora Machine Learning: perform ML using SageMaker & Comprehend on Aurora 

- Aurora Database Cloning: new cluster from existing one, faster than restoring a snapshot 

• Use case: same as RDS, but with less maintenance / more flexibility / more performance / more features © Stephane Maarek IE'”TS Ol ns 

ns 

#### Amazon ElastiCache – Summary 



- Managed Redis / Memcached (similar offering as RDS, but for caches) 

- In-memory data store, sub-millisecond latency 

- Select an ElastiCache instance type (e.g., cache.m6g.large) 

- Support for Clustering (Redis) and Multi AZ, Read Replicas (sharding) 

- Security through IAM, Security Groups, KMS, Redis Auth 

- Backup / Snapshot / Point in time restore feature 

- Managed and Scheduled maintenance 

- Requires some application code changes to be leveraged 

• Use Case: Key/Value store, Frequent reads, less writes, cache results for DB queries, store session data for websites, cannot use SQL. © Stephane Maarek IE '”TS Ol ns 

#### Amazon DynamoDB – Summary 



- AWS proprietary technology, managed serverless NoSQL database, millisecond latency 

- Capacity modes: provisioned capacity with optional auto-scaling or on-demand capacity 

- Can replace ElastiCache as a key/value store (storing session data for example, using TTL feature) 

- Highly Available, Multi AZ by default, Read and Writes are decoupled, transaction capability 

- DAX cluster for read cache, microsecond read latency 

- Security, authentication and authorization is done through IAM 

- Event Processing: DynamoDB Streams to integrate with AWS Lambda, or Kinesis Data Streams 

- Global Table feature: active-active setup 

- Automated backups up to 35 days with PITR (restore to new table), or on-demand backups 

- Export to S3 without using RCU within the PITR window, import from S3 without using WCU 

- Great to rapidly evolve schemas 

- Use Case: Serverless applications development (small documents 100s KB), distributed serverless cache 

© Stephane Maarek IE '”TS Ol 

ns 

#### Amazon S3 – Summary 

- S3 is a… key / value store for objects 



<!-- Start of picture text -->
S<br><!-- End of picture text -->

- Great for bigger objects, not so great for many small objects 

- Serverless, scales infinitely, max object size is 5 TB, versioning capability 

- Tiers: S3 Standard, S3 Infrequent Access, S3 Intelligent, S3 Glacier + lifecycle policy 

- Features: Versioning, Encryption, Replication, MFA-Delete, Access Logs… 

- Security: IAM, Bucket Policies, ACL, Access Points, Object Lambda, CORS, Object/Vault Lock 

- Encryption: SSE-S3, SSE-KMS, SSE-C, client-side, TLS in transit, default encryption 

- Batch operations on objects using S3 Batch, listing files using S3 Inventory 

- Performance: Multi-part upload, S3 Transfer Acceleration, S3 Select 

• Automation: S3 Event Notifications (SNS, SQS, Lambda, EventBridge) • Use Cases: static files, key value store for big files, website hosting © Stephane Maarek IE'”TS Ol ns 

#### DocumentDB 



<!-- Start of picture text -->
) mongol}<br><!-- End of picture text -->

- Aurora is an “AWS-implementation” of PostgreSQL / MySQL … 

- DocumentDB is the same for MongoDB (which is a NoSQL database) 

- MongoDB is used to store, query, and index JSON data 

- Similar “deployment concepts” as Aurora 

- Fully Managed, highly available with replication across 3 AZ 

- DocumentDB storage automatically grows in increments of 10GB 

- Automatically scales to workloads with millions of requests per seconds 

© Stephane Maarek IE '”TS Ol 

#### Amazon Neptune 

- Fully managed graph database 

- A popular graph dataset would be a social network 

   - Users have friends 

   - Posts have comments 

   - Comments have likes from users 

   - Users share and like posts… 

- Highly available across 3 AZ, with up to 15 read replicas 

- Build and run applications working with highly connected datasets – optimized for these complex and hard queries 





<!-- Start of picture text -->
Be<br>EIbhSegBh.“Se<br><!-- End of picture text -->

- Can store up to billions of relations and query the graph with milliseconds latency 

- Highly available with replications across multiple AZs 

- Great for knowledge graphs (Wikipedia), fraud detection, recommendation engines, social networking 

© Stephane Maarek 

Amazon Keyspaces (for Apache Cassandra) 



- _Apache Cassandra is an open-source NoSQL distributed database_ 

|• A managed Apache Cassandra-compatible database service|
|---|



- Serverless, Scalable, highly available, fully managed by AWS 

- Automatically scale tables up/down based on the application’s traffic 

- Tables are replicated 3 times across multiple AZ 

- Using the Cassandra Query Language (CQL) 

- Single-digit millisecond latency at any scale, 1000s of requests per second 

- Capacity: On-demand mode or provisioned mode with auto-scaling 

• Encryption, backup, Point-In-Time Recovery (PITR) up to 35 days • Use cases: store IoT devices info, time-series data, … © Stephane Maarek IE'”TS Ol ns 

#### Amazon QLDB 



<!-- Start of picture text -->
Se<br><!-- End of picture text -->

- QLDB stands for ”Quantum Ledger Database” 

- A ledger is a book recording financial transactions 

- Fully Managed, Serverless, High available, Replication across 3 AZ 

- Used to review history of all the changes made to your application data over time 

- Immutable system: no entry can be removed or modified, cryptographically verifiable 



<!-- Start of picture text -->
QLDB JOURNAL<br>BLOCK<br>™ ‘ate Bebo} Oto Oat<br>‘SEQUENCE NO.<br>0 | 25 26 27<br>BLOCK HASH<br>DOCUMENT REVISION ENTRIES<br><!-- End of picture text -->

- 2-3x better performance than common ledger blockchain frameworks, manipulate data using SQL 

- • Difference with Amazon Managed Blockchain: no decentralization component , in accordance with financial regulation rules 

<u>https://docs.aws.amazon.com/qldb/latest/developerguide/ledger-structure.html</u> 

© Stephane Maarek 

#### Amazon Timestream 



- Fully managed, fast, scalable, serverless time series database 

- Automatically scales up/down to adjust capacity 

- Store and analyze trillions of events per day 

- 1000s times faster & 1/10<sup>th</sup> the cost of relational databases 

- Scheduled queries, multi-measure records, SQL compatibility 

- Data storage tiering: recent data kept in memory and historical data kept in a cost-optimized storage 

- Built-in time series analytics functions (helps you identify patterns in your data in near real-time) 

/ 

- Encryption in transit and at rest 

- Use cases: IoT apps, operational applications, real-time analytics, … 

© Stephane Maarek 

Amazon Timestream – Architecture AWS IoT Amazon @a QuickSight Lambda Kinesis Data = Amazon Streams SageMaker Prometheus 0 D eS 3 @ telegraf” Amazon Timestream Kinesis Data aa Bo} Streams Any JDBC connection Amazon MSK & Kinesis Data Analytics al For Apache Flink 

© Stephane Maarek 

### Data & Analytics 

© Stephane Maarek 

#### Amazon Athena 

- Serverless query service to analyze data stored in Amazon S3 

- Uses standard SQL language to query the files (built on Presto) 

- • Supports CSV, JSON, ORC, Avro, and Parquet • Pricing: $5.00 per TB of data scanned • Commonly used with Amazon Quicksight for reporting/dashboards 

- Use cases: Business intelligence / analytics / reporting, analyze & query VPC Flow Logs, ELB Logs, CloudTrail trails , etc... 

- <u>Exam Tip:</u> analyze data in S3 using serverless SQL, use Athena 

load data ES| G S3 Bucket Query & Analyze Amazon Athena Reporting & Dashboards Amazon QuickSight 

© Stephane Maarek 

#### Amazon Athena – Performance Improvement 

- Use columnar data for cost-savings (less scan) 

   - Apache Parquet or ORC is recommended 

   - Huge performance improvement 

   - Use Glue to convert your data to Parquet or ORC 

- Compress data for smaller retrievals (bzip2, gzip, lz4, snappy, zlip, zstd…) 

- Partition datasets in S3 for easy querying on virtual columns 

• s3://yourBucket/pathToTable /<PARTITION_COLUMN_NAME>=<VALUE> /<PARTITION_COLUMN_NAME>=<VALUE> /<PARTITION_COLUMN_NAME>=<VALUE> /etc… 

• Example: s3://athena-examples/flight/parquet/year=1991/month=1/day=1/ 

- Use larger files (> 128 MB) to minimize overhead 

© Stephane Maarek 

#### Amazon Athena – Federated Query 

- Allows you to run SQL queries across data stored in relational, non-relational, object, and custom data sources (AWS or on-premises) 

- Uses Data Source Connectors that run on AWS Lambda to run Federated Queries (e.g., CloudWatch Logs, DynamoDB, RDS, …) 

- Store the results back in Amazon S3 

Amazon Athena > S3 Bucket Lambda **(Data Source** ElastiCache 7 @ **Connector)** & DocumentDB HBase in EMR 2 a DynamoDB Database (On-Premises) Redshift a eo fa Aurora SQL Server MySQL 

© Stephane Maarek a 

#### Redshift Overview 

• Redshift is based on PostgreSQL, but it’s not used for OLTP 



- It’s OLAP – online analytical processing (analytics and data warehousing) 

• 10x better performance than other data warehouses, scale to PBs of data 

- Columnar storage of data (instead of row based) & parallel query engine 

- Pay as you go based on the instances provisioned 

- Has a SQL interface for performing the queries 

• BI tools such as Amazon Quicksight or Tableau integrate with it • vs Athena: faster queries / joins / aggregations thanks to indexes © Stephane Maarek IE'”TS Ol ns 

#### Redshift Cluster 



<!-- Start of picture text -->
SELECT COUNT (*), …<br>Query FROM MY_TABLE<br>GROUP BY …<br>JDBC/ODBC<br>Amazon Redshift Cluster<br>Leader Node<br><!-- End of picture text -->

Amazon Redshift Cluster Compute Nodes ~~<mark>=~</mark>~~ 





- Leader node: for query planning, results aggregation 

- Compute node: for performing the queries, send results to leader 

- You provision the node size in advance 

- You can used Reserved Instances for cost savings 

© Stephane Maarek 

#### Redshift – Snapshots & DR 

- <u>Redshift has “Multi-AZ” mode for some</u> ~~<u>clusters</u>~~ 

- Snapshots are point-in-time backups of a cluster, stored internally in S3 

- Snapshots are incremental (only what has changed is saved) 

- You can restore a snapshot into a new cluster 

- Automated: every 8 hours, every 5 GB, or on a schedule. Set retention between 1 to 35 days 

- Manual: snapshot is retained until you delete it 

- You can configure Amazon Redshift to automatically copy snapshots (automated or manual) of a cluster to another AWS Region 



<!-- Start of picture text -->
Region<br>(us-east-1)<br>Take Snapshot Cluster<br>Snapshot<br>Redshift Cluster<br>(Original)<br>Automated<br>/ Manual<br>Copy<br>Region<br>(eu-west-1)<br>Restore Copied<br>Snapshot<br>Redshift Cluster<br>(New)<br><!-- End of picture text -->

© Stephane Maarek 

Loading data into Redshift: <u>Large inserts are MUCH better</u> 

**Amazon Kinesis S3 using COPY command EC2 Instance Data Firehose** JDBC driver Internet Without Enhanced VPC Routing Through VPC With Enhanced VPC Routing Amazon Kinesis Amazon Redshift S3 Bucket Amazon Redshift EC2 Instance Amazon Redshift Data Firehose f Cluster ~~oc8~~ 0Bo (mybucket) Cluster Cluster (through S3 copy) _Better to write Data in batches_ copy customer from 's3://mybucket/mydata’ iam_role 'arn:aws:iam::0123456789012:role/MyRedshiftRole'; © Stephane Maarek IE'”TS Ol ns 

SELECT COUNT (*), … Redshift Spectrum Query FROM S3.EXT_TABLE GROUP BY … JDBC/ODBC • Query data that is already in Amazon Redshift Cluster S3 without loading it Leader Node ~~<mark>——</mark>~~ • Must have a Redshift cluster available to start the query Compute Nodes • The query is then submitted to thousands of Redshift Spectrum nodes Redshift Spectrum 1 2 …. N Amazon S3 © Stephane Maarek e ~~s~~ <u><mark>sa</mark></u> 

ns 

#### Amazon OpenSearch Service 



- _Amazon OpenSearch is successor to Amazon ElasticSearch_ 

- In DynamoDB, queries only exist by primary key or indexes… 

- With OpenSearch, you can search any field, even partially matches 

- It’s common to use OpenSearch as a complement to another database 

- Two modes: managed cluster or serverless cluster 

- Does _not_ natively support SQL (can be enabled via a plugin) 

- Ingestion from Kinesis Data Firehose, AWS IoT, and CloudWatch Logs 

- Security through Cognito & IAM, KMS encryption, TLS 

- Comes with OpenSearch Dashboards (visualization) 

© Stephane Maarek IE '”TS Ol 



<!-- Start of picture text -->
OpenSearch patterns<br>DynamoDB<br>CRUD<br>DynamoDB Table DynamoDB Stream Lambda Function Amazon OpenSearch<br>API to search items<br>API to retrieve items<br>a<br>© Stephane Maarek<br>IE'”TS Ol ns<br>NOT FOR DISTRIBUTION © Stephane Maarek www.datacumulus.com<br><!-- End of picture text -->

#### OpenSearch patterns CloudWatch Logs 

Real time CQ CQ IN Kel CloudWatch Logs Subscription Filter Lambda Function Amazon OpenSearch (managed by AWS) Near Real Time ce cg “a Hel CloudWatch Logs Subscription Filter Kinesis Data Firehose Amazon OpenSearch 

© Stephane Maarek 



<!-- Start of picture text -->
OpenSearch patterns<br>Kinesis Data Streams & Kinesis Data Firehose<br>Kinesis Data<br>Kinesis Data<br>Streams<br>Streams<br>Lambda<br>Function<br>Kinesis Data<br>data Lambda<br>Firehose transformation<br>a8 Function<br>(near real time)<br>(real time)<br>Amazon<br>Amazon<br>OpenSearch<br>OpenSearch<br><!-- End of picture text -->

© Stephane Maarek 

#### Amazon EMR 



- EMR stands for “Elastic MapReduce” 

- EMR helps creating Hadoop clusters (Big Data) to analyze and process vast amount of data 

- The clusters can be made of hundreds of EC2 instances 

- EMR comes bundled with Apache Spark, HBase, Presto, Flink… 

- EMR takes care of all the provisioning and configuration 

- Auto-scaling and integrated with Spot instances 

• Use cases: data processing, machine learning, web indexing, big data… © Stephane Maarek IE'”TS Ol ns 

#### Amazon EMR – Node types & purchasing 

- Master Node: Manage the cluster, coordinate, manage health – long running 

- Core Node: Run tasks and store data – long running 

- Task Node (optional): Just to run tasks – usually Spot 

- Purchasing options: 

   - On-demand: reliable, predictable, won’t be terminated 

   - Reserved (min 1 year): cost savings (EMR will automatically use if available) 

   - Spot Instances: cheaper, can be terminated, less reliable 

- Can have long-running cluster, or transient (temporary) cluster 

© Stephane Maarek 

#### Amazon QuickSight 



- Serverless machine learning-powered business intelligence service to create interactive dashboards 

- Fast, automatically scalable, embeddable, with per-session pricing 

- Use cases: 

   - Business analytics 

   - Building visualizations 

   - Perform ad-hoc analysis 

   - Get business insights using data 

- Integrated with RDS, Aurora, Athena, Redshift, S3… 

- In-memory computation using SPICE engine if data is imported into QuickSight 

- • Enterprise edition: Possibility to setup Column-Level security (CLS) 



<!-- Start of picture text -->
Business Summary Dashboard<br>a - $4,478K 20.34% +t  -19.45% + 159,904 28.09% 6.71%<br>| $36,755K [joe Cee<br>= = Sine oa" WEL neyo. oe<br><!-- End of picture text -->

<u>https://aws.amazon.com/quicksight/</u> 

© Stephane Maarek 

#### QuickSight Integrations 



<!-- Start of picture text -->
Data Sources  (AWS Services)<br>QuickSight On-Premises<br>Databases (JDBC)<br>RDS Aurora Redshift<br>Data Sources  (Imports)<br>Athena S3 OpenSearch<br>Data Sources  (SaaS)<br>ELF & CLF<br>Timestream<br>(Log Format)<br><!-- End of picture text -->

© Stephane Maarek 

#### QuickSight – Dashboard & Analysis 

- Define Users (standard versions) and Groups (enterprise version) 

   - These users & groups only exist within QuickSight, not IAM !! 

- A _dashboard…_ 

   - is a read-only snapshot of an analysis that you can share 

   - preserves the configuration of the analysis (filtering, parameters, controls, sort) 

- You can share the analysis or the dashboard with Users or Groups 

- To share a dashboard, you must first publish it 

- Users who see the dashboard can also see the underlying data 

© Stephane Maarek 

#### AWS Glue 



• Managed extract, transform, and load (ETL) service • Useful to prepare and transform data for analytics • Fully serverless service Glue ETL S3 Bucket iS, : = **Extract Load** i a Amazon RDS Redshift **Transform** Data Warehouse 

ns 

© Stephane Maarek IE '”TS Ol 

AWS Glue – Convert data into Parquet format **Glue ETL Import CSV Parquet Analyze** Amazon Athena Input Output S3 Bucket S3 Bucket Trigger Glue ETL Job Event notifications LL. S3 Put On S3 PUT Lambda Function _(EventBridge works as an alternative)_ 

ns 

© Stephane Maarek IE '”TS Ol 

Glue Data Catalog: catalog of datasets lied **Glue Jobs (ETL)** Amazon Athena Amazon S3 ei Bo Data discovery Writes Metadata AWS Glue Amazon RDS Data Catalog Amazon AWS Glue Redshift Database Database Data Crawler Spectrum Amazon DynamoDB <mark>os</mark> aa. JDBC Tables Tables (Metadata) (Metadata) Amazon EMR © Stephane Maarek SE “ee 

Glue – things to know at a high-level 

- Glue Job Bookmarks: prevent re-processing old data 

- Glue Elastic Views : 

   - Combine and replicate data across multiple data stores using SQL 

   - No custom code, Glue monitors for changes in the source data, serverless 

   - Leverages a “virtual table” (materialized view) 

- Glue DataBrew: clean and normalize data using pre-built transformation 

- Glue Studio: new GUI to create, run and monitor ETL jobs in Glue 

- Glue Streaming ETL (built on Apache Spark Structured Streaming): compatible with Kinesis Data Streaming, Kafka, MSK (managed Kafka) 

© Stephane Maarek 

#### AWS Lake Formation 



- Data lake = central place to have all your data for analytics purposes 

- Fully managed service that makes it easy to setup a data lake in days 

- Discover, cleanse, transform, and ingest data into your Data Lake 

- It automates many complex manual steps (collecting, cleansing, moving, cataloging data, …) and de-duplicate (using ML Transforms) 

- Combine structured and unstructured data in the data lake 

- Out-of-the-box source blueprints: S3, RDS, Relational & NoSQL DB… 

- Fine-grained Access Control for your applications (row and column-level) 

- Built on top of AWS Glue 

© Stephane Maarek IE'”TS Ol ns 



<!-- Start of picture text -->
AWS Lake Formation<br>Data Sources<br>Athena<br>Source Crawlers<br>Amazon S3 ETL and Data Prep.<br>ingest<br>Data Catalog Redshift<br>Security Settings Users<br>RDS<br>Access Control<br>EMR<br>op 5 AWS Lake Formation<br>On-Premises<br>Database (SQL & NoSQL)<br>BB Aurora ;<br>Data Lake<br>(stored in S3)<br>© Stephane Maarek<br>a Ee<br>NOT FOR DISTRIBUTION © Stephane Maarek www.datacumulus.com<br><!-- End of picture text -->



<!-- Start of picture text -->
AWS Lake Formation<br>Centralized Permissions Example<br>Data Sources<br>ingest Access Control<br>Amazon S3<br>Column-level security<br>Athena Users<br>AWS Lake Formation Quicksight<br>RDS Aurora<br>c yi<br>Data Lake<br>(stored in S3)<br><!-- End of picture text -->

© Stephane Maarek 

#### Kinesis Data Analytics for SQL applications 



<!-- Start of picture text -->
SQL<br>Kinesis<br>Statements Data Streams AWS Lambda anywhere<br>| | = z |<br>Kinesis<br>Applications anywhere<br>Data Streams<br>Kinesis Amazon S3<br>ke s<br>Data Firehose<br>Kinesis Amazon Redshift<br>Kinesis<br>Data Analytics (COPY through S3)<br>‘ti :<br>Data Firehose<br>for SQL Applications<br>Other Firehose destinations…<br>Sources Sinks<br>Reference Data in S3<br><!-- End of picture text -->

© Stephane Maarek 

#### Kinesis Data Analytics (SQL application) 



- Real-time analytics on Kinesis Data Streams & Firehose using SQL 

- Add reference data from Amazon S3 to enrich streaming data 

- Fully managed, no servers to provision 

- Automatic scaling 

- Pay for actual consumption rate 

- • Output: 

   - Kinesis Data Streams: create streams out of the real-time analytics queries 

   - • Kinesis Data Firehose: send analytics query results to destinations 

- Use cases: 

   - Time-series analytics 

   - Real-time dashboards 

   - Real-time metrics 

© Stephane Maarek 

#### Kinesis Data Analytics for Apache Flink 

- Use Flink (Java, Scala or SQL) to process and analyze streaming data 



<!-- Start of picture text -->
Kinesis Data<br>Ss<br>Streams (ae) Ss<br>Amazon MSK<br>Kinesis Data Analytics<br>& il Partin,<br>For Apache Flink<br><!-- End of picture text -->

- Run any Apache Flink application on a managed cluster on AWS 

   - provisioning compute resources, parallel computation, automatic scaling 

   - application backups (implemented as checkpoints and snapshots) 

   - Use any Apache Flink programming features 

   - Flink does not read from Firehose (use Kinesis Analytics for SQL instead) 

© Stephane Maarek 

Amazon Managed Streaming for Apache Kafka (Amazon MSK) 



- Alternative to Amazon Kinesis 

- Fully managed Apache Kafka on AWS 

   - Allow you to create, update, delete clusters 

   - MSK creates & manages Kafka brokers nodes & Zookeeper nodes for you 

   - Deploy the MSK cluster in your VPC, multi-AZ (up to 3 for HA) 

   - Automatic recovery from common Apache Kafka failures 

   - Data is stored on EBS volumes for as long as you want 

- MSK Serverless 

   - Run Apache Kafka on MSK without managing the capacity 

   - MSK automatically provisions resources and scales compute & storage 

© Stephane Maarek 



<!-- Start of picture text -->
Apache Kafka at a high level<br>EMR<br>MSK Cluster<br>Kinesis<br>S3<br>Broker 2<br>BO S<br>IoT<br>Producers Write to topic Poll from topic Consumers SageMaker<br>(your code) (your code)<br>Broker 1<br>RDS Kinesis<br>Etc…<br>RDS<br>Broker 3<br>Etc…<br>© Stephane Maarek<br>SE ’”- Oh es<br>replication<br>replication<br>NOT FOR DISTRIBUTION © Stephane Maarek www.datacumulus.com<br><!-- End of picture text -->

© Stephane Maarek SE 

#### Kinesis Data Streams vs. Amazon MSK 



Kinesis Data Streams 



Amazon MSK 

- 1 MB message size limit 

- Data Streams with Shards 

- Shard Splitting & Merging 

- TLS In-flight encryption 

- KMS at-rest encryption 

- 1MB default, configure for higher (ex: 10MB) 

- Kafka Topics with Partitions 

- Can only add partitions to a topic 

- PLAINTEXT or TLS In-flight Encryption 

- KMS at-rest encryption 

© Stephane Maarek 

#### Amazon MSK Consumers 



<!-- Start of picture text -->
Kinesis Data Analytics<br>for Apache Flink<br>=<br>AWS Glue<br>Streaming ETL Jobs<br>v<br>Powered by Apache Spark Streaming<br>Lambda<br>Amazon MSK<br>& IN<br>Applications Running on<br>Amazon EC2 ECS EKS<br><!-- End of picture text -->

© Stephane Maarek 

#### Big Data Ingestion Pipeline 

- We want the ingestion pipeline to be fully serverless 

- We want to collect data in real time 

- We want to transform the data 

- We want to query the transformed data using SQL 

- The reports created using the queries should be in S3 

- We want to load that data into a warehouse and create dashboards 

© Stephane Maarek 

Big Data Ingestion Pipeline Pull data IoT Devices Real-time Reporting Ingestion Every 1 minute Bucket Bucket trigger = BS Oo z Amazon Kinesis Data Amazon Kinesis Data Amazon Simple Storage Amazon Simple Queue AWS Lambda Amazon Athena Amazon Simple Storage Streams Firehose Service (S3) Service Service (S3) (optional) AWS Lambda BS 

Amazon QuickSight Amazon Redshift Serverless 

© Stephane Maarek 

#### Big Data Ingestion Pipeline discussion 

- IoT Core allows you to harvest data from IoT devices 

- Kinesis is great for real-time data collection 

- Firehose helps with data delivery to S3 in near real-time (1 minute) 

- Lambda can help Firehose with data transformations 

- Amazon S3 can trigger notifications to SQS 

- Lambda can subscribe to SQS (we could have connecter S3 to Lambda) 

- Athena is a serverless SQL service and results are stored in S3 

- The reporting bucket contains analyzed data and can be used by reporting tool such as AWS QuickSight, Redshift, etc… 

© Stephane Maarek 

### Machine Learning 

© Stephane Maarek 

#### Amazon Rekognition 



|•Findobjects, people, text, scenesinimages and videosusing ML|
|---|



- Facial analysis and facial search to do user verification, people counting 

|•Create a database of “familiar faces” or compare against celebrities|
|---|



|• Use cases:|
|---|



|• Labeling|
|---|



|• Content Moderation|
|---|



|• Text Detection|
|---|



|• Face Detection and Analysis (gender, age range, emotions…)|
|---|



|• Face Search and Verification|
|---|



• Celebrity Recognition • Pathing (ex: for sports game analysis) © Stephane Maarek IE'”TS Ol ns 

#### Amazon Rekognition – Content Moderation 

- Detect content that is inappropriate, unwanted, or offensive (image and videos) 

- Used in social media, broadcast media, advertising, and e-commerce situations to create a safer user experience 

- Set a Minimum Confidence Threshold for items that will be flagged 

Image 

Amazon Rekognition 





- Confidence Level 

- • Flag sensitive content for manual review in and Threshold hull Amazon Augmented AI (A2I) 

- • Help comply with regulations Optional Manual review in **A2I** 

- © Stephane Maarek 

- IE's 

#### Amazon Transcribe 



- Automatically convert speech to text 

- Uses a deep learning process called automatic speech recognition (ASR) to convert speech to text quickly and accurately 

- Automatically remove Personally Identifiable Information (PII) using Redaction 

- Supports Automatic Language Identification for multi-lingual audio 

- Use cases: 

   - transcribe customer service calls 

   - automate closed captioning and subtitling 

   - generate metadata for media assets to create a fully searchable archive 



_”Hello my name is Stéphane. I hope you’re enjoying the course!_ 

© Stephane Maarek 

#### Amazon Polly 



- Turn text into lifelike speech using deep learning 

- Allowing you to create applications that talk 

_Hi! My name is Stéphane and this is a demo of Amazon Polly_ 





© Stephane Maarek 

#### Amazon Polly – Lexicon & SSML 

- Customize the pronunciation of words with Pronunciation lexicons 

   - Stylized words: St3ph4ne => “Stephane” 

   - Acronyms: AWS => “Amazon Web Services” 

- Upload the lexicons and use them in the SynthesizeSpeech operation 

- Generate speech from plain text or from documents marked up with Speech Synthesis Markup Language (SSML) – enables more customization 

   - emphasizing specific words or phrases 

   - using phonetic pronunciation 

   - including breathing sounds, whispering 

   - using the Newscaster speaking style 

© Stephane Maarek 

#### Amazon Translate 



<!-- Start of picture text -->
| ay<br>aN<br>®[]<br><!-- End of picture text -->

- Natural and accurate language translation 

- Amazon Translate allows you to localize content - such as websites and applications - for international users , and to easily translate large volumes of text efficiently. 



<!-- Start of picture text -->
Source language Target language<br>Hi my name is Stéphane Bonjour, je m'appelle Stéphane.<br><!-- End of picture text -->



<!-- Start of picture text -->
Portuguese (pt) v<br>Oi, meu nomeé Stéphane.<br><!-- End of picture text -->



<!-- Start of picture text -->
Hindi (hi) Vv<br>era ARTaT ehS<br><!-- End of picture text -->

© Stephane Maarek 

#### Amazon Lex & Connect 

- Amazon Lex: (same technology that powers Alexa) 

   - Automatic Speech Recognition (ASR) to convert speech to text 

   - Natural Language Understanding to recognize the intent of text, callers 

   - Helps build chatbots, call center bots 

- Amazon Connect: 

   - Receive calls, create contact flows, cloud-based virtual contact center 

   - Can integrate with other CRM systems or AWS 

   - No upfront payments, 80% cheaper than traditional contact center solutions 



<!-- Start of picture text -->
Phone Call<br>call stream invoke schedule<br>Schedule an<br>Appointment<br>| i b \<br>Connect Lex Lambda<br>CRM<br>Intent recognized<br><!-- End of picture text -->

© Stephane Maarek 

#### Amazon Comprehend 



|• ForNatural Language Processing – NLP|
|---|



|• Fully managed and serverless service|
|---|



|• Uses machine learning to find insights and relationships in text|
|---|



- Language of the text 

|• Extracts key phrases, places, people, brands, or events|
|---|



|• Understands how positive or negative the text is|
|---|



|• Analyzes text using tokenization and parts of speech|
|---|



   - Automatically organizes a collection of text files by topic 

- Sample use cases: 

• analyze customer interactions (emails) to find what leads to a positive or negative experience • Create and groups articles by topics that Comprehend will uncover © Stephane Maarek IE'”TS Ol ns 

#### Amazon Comprehend Medical 



   - Amazon Comprehend Medical detects and returns useful information in unstructured clinical text: 

      - Physician’s notes 

      - Discharge summaries 

      - Test results 

      - Case notes 

- Uses NLP to detect Protected Health Information (PHI) – _DetectPHI_ API 

- • Store your documents in Amazon S3, analyze real-time data with Kinesis Data Firehose, or use Amazon Transcribe to transcribe patient narratives into text that can be analyzed by Amazon Comprehend Medical. 

- © Stephane Maarek 

- IE'”TS Ol ns 

Amazon SageMaker • Fully managed service for developers / data scientists to build ML models • Typically, difficult to do all the processes in one place + provision servers • Machine learning process (simplified): predicting your exam score 670 label build Train and Tune 890 934 ~~<u>B</u>~~ E ML model <u>Historical Data:</u> score # years of experience in IT Apply model # years of experience with AWS Time spent on the course ~~—_~~ @ <u>@</u> … PASS WITH 906 New data Prediction © Stephane Maarek NN” OOe| ~~e~~ es 

#### Amazon Forecast 



<!-- Start of picture text -->
Ei<br><!-- End of picture text -->

- Fully managed service that uses ML to deliver highly accurate forecasts 

- Example: predict the future sales of a raincoat 

- 50% more accurate than looking at the data itself 

- Reduce forecasting time from months to hours 

- Use cases: Product Demand Planning, Financial Planning, Resource Planning, … 

###### <u>Historical Time-series Data:</u> 

Product features Prices upload produce Discounts Website traffic & Fail | Store locations Forecasting Model Future sales Al Amazon S3 f Amazon Forecast … of raincoat: $500,000 

© Stephane Maarek IE '”TS Ol 

#### Amazon Kendra 



- Fully managed document search service powered by Machine Learning 

- Extract answers from within a document (text, pdf, HTML, PowerPoint, MS Word, FAQs…) 

- Natural language search capabilities 

- Learn from user interactions/feedback to promote preferred results (Incremental Learning) 

- Ability to manually fine-tune search results (importance of data, freshness, custom, …) 



<!-- Start of picture text -->
Data Sources<br>Where is the IT support desk?<br>indexing<br>Amazon S3 Amazon RDS Google Drive MS SharePoint<br>1 st  floor<br>Knowledge Index<br>User<br>3 rd  party,  (powered by ML)<br>APNs,<br>MS OneDrive Amazon Kendra<br>Custom<br>i) servicenow. | |<br><!-- End of picture text -->

© Stephane Maarek 

#### Amazon Personalize 



<!-- Start of picture text -->
“N<br><!-- End of picture text -->

- Fully managed ML-service to build apps with real-time personalized recommendations 

- • Example: personalized product recommendations/re-ranking, customized direct marketing • Example: User bought gardening tools, provide recommendations on the next one to buy 

- Same technology used by Amazon.com 

- Integrates into existing websites, applications, SMS, email marketing systems, … 

- Implement in days, not months (you don’t need to build, train, and deploy ML solutions) 

- Use cases: retail stores, media and entertainment… 



<!-- Start of picture text -->
Websites & Apps<br>read data from S3<br>Amazon S3<br>Mobile Apps<br>Customized personalized API<br>real-time data integration<br>Amazon Personalize API<br>SMS<br>Amazon Personalize<br>Emails<br><!-- End of picture text -->

© Stephane Maarek 

#### Amazon Textract 



- Automatically extracts text, handwriting, and data from any scanned documents using AI and ML 



<!-- Start of picture text -->
{<br>DRIVER LICENSE     “Document ID”: “123456789-005”,<br>analyze result     “Name”: “”,<br>    “SEX”: “F”,<br>BS) =<br>= fname<br>    “DOB”: “23.05.1997”,<br>fA awea010:123456789-005 SURNAME pote— | ==|<br>    …<br>AS TOA<br>}<br>Amazon Textract<br><!-- End of picture text -->

- Extract data from forms and tables 

- Read and process any type of document (PDFs, images, …) 

- • Use cases: 

   - Financial Services (e.g., invoices, financial reports) 

   - Healthcare (e.g., medical records, insurance claims) 

   - • Public Sector (e.g., tax forms, ID documents, passports) 

© Stephane Maarek 

#### AWS Machine Learning - Summary 

- Rekognition: face detection, labeling, celebrity recognition 

- • Transcribe: audio to text (ex: subtitles) • Polly: text to audio • Translate: translations 

- Lex: build conversational bots – chatbots 

- Connect: cloud contact center 

- Comprehend: natural language processing 

- SageMaker : machine learning for every developer and data scientist 

- • Forecast: build highly accurate forecasts 

- Kendra: ML-powered search engine 

- Personalize: real-time personalized recommendations 

- Textract: detect text and data in documents 

© Stephane Maarek 

### AWS Monitoring, Audit and Performance CloudWatch, CloudTrail & AWS Config 

© Stephane Maarek 

|Amazon CloudWatch Metrics|
|---|





|•CloudWatch provides metrics for_every_services in AWS|
|---|



|• Metricis a variable to monitor (CPUUtilization, NetworkIn…)|
|---|



- Metrics belong to namespaces 

|• Dimensionis an attribute of a metric (instance id, environment, etc…).|
|---|



- Up to 30 dimensions per metric 

- Metrics have timestamps 

|•Can create CloudWatch dashboards of metrics|
|---|



• Can create CloudWatch Custom Metrics (for the RAM for example) © Stephane Maarek IE'”TS Ol ns 

#### CloudWatch Metric Streams 

- Continually stream CloudWatch metrics to a destination of your choice, with near-real-time delivery and low latency. 

   - Amazon Kinesis Data Firehose (and then its destinations) 

   - • 3<sup>rd</sup> party service provider: Datadog, Dynatrace, New Relic, Splunk, Sumo Logic… 

- Option to filter metrics to only stream a subset of them 



<!-- Start of picture text -->
.<br><!-- End of picture text -->

**CloudWatch Metrics** Stream near-real-time **Kinesis Data Firehose** 

Stream near-real-time 



<!-- Start of picture text -->
t<br><!-- End of picture text -->





<!-- Start of picture text -->
&<br><!-- End of picture text -->





<!-- Start of picture text -->
Kel<br><!-- End of picture text -->

Amazon S3 Amazon Amazon Redshift OpenSearch Athena 

© Stephane Maarek 

#### CloudWatch Logs 



<!-- Start of picture text -->
|<br><!-- End of picture text -->

   - Log groups: arbitrary name, usually representing an application 

   - Log stream: instances within application / log files / containers 

   - Can define log expiration policies (never expire, 1 day to 10 years…) 

   - CloudWatch Logs can send logs to: 

      - Amazon S3 (exports) 

      - Kinesis Data Streams 

      - Kinesis Data Firehose 

      - AWS Lambda 

      - OpenSearch 

- Logs are encrypted by default 

- • Can setup KMS-based encryption with your own keys 

- © Stephane Maarek 

- IE'”TS Ol ns 

|CloudWatch Logs - Sources|
|---|
|•SDK, CloudWatch Logs Agent, CloudWatch Unified Agent|
|•Elastic Beanstalk: collection of logs from application|
|•ECS: collection from containers|
|•AWS Lambda: collection from function logs|
|•VPC Flow Logs: VPC specific logs|
|•API Gateway|
|•CloudTrail based on filter|
|•Route53: Log DNS queries|



© Stephane Maarek 

#### CloudWatch Logs Insights 



<!-- Start of picture text -->
CloudWatch > Logs Insights . =<br>Change the time Discovered Fields in Fields<br>range here. your log groups.<br>o<br>Selectct loglog groups)group(s WriteA your query ¥ 2021-11-09-11-09(06:40:02)(06:40: > 2021-11-09(06:55:17)-11-09 (06:55:  & Queries<br>[eeatitiontonX] here ©<br>1 fields @timestamp, @message Help<br>2 | sort @timestamp desc<br>3 | Limit 20<br>7<br>add to a dashboard.<br>Queries are allowed to run for up to 15 minutes.<br>Tabs for query results, ZN<br>Logs Visualization and visualization options. ‘Add to dashboard ®&<br>10,197 records (2.3 MB) scanned in 3.3s @ 3,091 records/s (714.9 kB/s)<br>400<br>200<br>300100 bi 1. call ML itll | vill dda 1 |<br>06:40 06:41 06:42 06:43 06:44 06:45 06:46 06:47 06:48 06:49 06:50 06:51 06:52 06:53 06:54 06:55<br>* @timestamp @message<br>ae 2021-11-09706:54:17.62.. {"Severity": "INFO", “message”: “This is where the message detail would go", “IP Address": "10.30.86.98", "Timestamp": "2021-11-09T11:<br>m2 2021-11-09T06:54:13.38.. {"Severity": "INFO", "message": "This is where the message detail would go", "IP Address": "192.168.0.43", “Timestamp”: "2021-11-09T11<br><!-- End of picture text -->

<u>https://mng.workshop.aws/operations-2022/detect/cwlogs.html</u> 

© Stephane Maarek 

#### CloudWatch Logs Insights 

- Search and analyze log data stored in CloudWatch Logs 

- Example: find a specific IP inside a log, count occurrences of “ERROR” in your logs… 

- Provides a purpose-built query language 

   - Automatically discovers fields from AWS services and JSON log events 

   - Fetch desired event fields, filter based on conditions, calculate aggregate statistics, sort events, limit number of events… 

   - Can save queries and add them to CloudWatch Dashboards 

- Can query multiple Log Groups in different AWS accounts 

- It’s a query engine, not a real-time engine 



<!-- Start of picture text -->
Sample queries Learn more [4<br>> Lambda<br>>» VPC Flow Logs<br>>» CloudTrail<br>‘vY Common queries<br>v 25 most recently added log events<br>fields @timestamp, @message<br>| sort @timestamp desc<br>| Limit 25<br>Apply<br>‘v Number of exceptions logged every 5<br>minutes<br>filter @message like /Exception/<br>| stats count(*) as exceptionCount by<br>bin(5m)<br>| sort exceptionCount desc<br>Apply<br>¥ List of log events that are not exceptions<br>fields @message<br>| filter @message not like /Exception/<br>Apply<br><!-- End of picture text -->

© Stephane Maarek 

#### CloudWatch Logs – S3 Export 

- Log data can take up to 12 hours to become available for export 





- The API call is CreateExportTask 

CloudWatch Logs 

###### Amazon S3 

- Not near-real time or real-time… use Logs Subscriptions instead 

© Stephane Maarek IE '”TS Ol 

ns 

#### CloudWatch Logs Subscriptions 

- Get a real-time log events from CloudWatch Logs for processing and analysis 

- Send to Kinesis Data Streams, Kinesis Data Firehose, or Lambda 

- Subscription Filter – filter which logs are events delivered to your destination 



<!-- Start of picture text -->
real-time OpenSearch<br>Service<br>Lambda<br>near<br>logs real-time<br>S3<br>=2 CQ Sb &<br>CloudWatch Logs Kinesis Data Firehose<br>Subscription Filter<br>…<br>KDF KDA EC2 Lambda<br>Kinesis Data Streams<br><!-- End of picture text -->

© Stephane Maarek 

CloudWatch Logs Aggregation Multi-Account & Multi Region **ACCOUNT A** && **REGION 1** CloudWatch Logs Subscription Filter **ACCOUNT B** Near **REGION 2** @@ = & Real Time & CloudWatch Logs Subscription Filter Kinesis Data Streams Kinesis Data Firehose Amazon S3 **ACCOUNT B REGION 3** & & CloudWatch Logs Subscription Filter © Stephane Maarek 

© Stephane Maarek 

| 

#### CloudWatch Logs Subscriptions 

- Cross-Account Subscription – send log events to resources in a different AWS account (KDS, KDF) 



<!-- Start of picture text -->
IAM Role<br>{<br>"Statement": [ (Cross-Account)<br>aws aws {<br>= Account –  Sender = Account –  Recipient "Effect": "Allow",<br>(111111111111) (999999999999) "Action": "kinesis:PutRecord",<br>"Resource": “arn:aws:kinesis:us-east-1:<br>999999999999: stream/RecipientStream"<br>= logs CQ logs CQ =TO ,<br>=Q Q Q<br>CloudWatch<br>Subscription Subscription Kinesis Data Streams<br>Logs Filter Destination (RecipientStream) {<br>Destination<br>mA Destination aH "Statement":"Version": "2012-10-17",[<br>x Access Policy H Access Policy<br>H"sid": "",<br>Can be assumed<br>H "Effect": "Allow",<br>IAM Role<br>aire nae + B sosennnnnnseccnnd allow PutRecord "Principal": {<br>waws": "112111111111"<br>,<br>"Action": "logs:PutSubscriptionFilter",<br>destination:"Resource":testDestination""arnzaws: logs: us-east-1:999999999999:OO<br><!-- End of picture text -->

© Stephane Maarek IE 'TS Ol 

- CloudWatch Logs for EC2 • By default, no logs from your EC2 machine will go to CloudWatch 

- • You need to run a CloudWatch agent on EC2 to push the log files you want 

- Make sure IAM permissions are correct 

- The CloudWatch log agent can be setup on-premises too 

CloudWatch Logs 



<!-- Start of picture text -->
CloudWatch  CloudWatch<br>Logs Agent Logs Agent<br>On Premise<br>EC2 Instance Server<br><!-- End of picture text -->

© Stephane Maarek 

#### CloudWatch Logs Agent & Unified Agent 

- For virtual servers (EC2 instances, on-premises servers…) 

- CloudWatch Logs Agent 

   - Old version of the agent 

   - Can only send to CloudWatch Logs 

- CloudWatch Unified Agent 

   - Collect additional system-level metrics such as RAM, processes, etc… 

   - Collect logs to send to CloudWatch Logs 

   - Centralized configuration using SSM Parameter Store 

© Stephane Maarek 

#### CloudWatch Unified Agent – Metrics 

- Collected directly on your Linux server / EC2 instance 

- CPU (active, guest, idle, system, user, steal) 

- Disk metrics (free, used, total), Disk IO (writes, reads, bytes, iops) 

- RAM (free, inactive, used, total, cached) 

- Netstat (number of TCP and UDP connections, net packets, bytes) 

- Processes (total, dead, bloqued, idle, running, sleep) 

- Swap Space (free, used, used %) 

- Reminder: out-of-the box metrics for EC2 – disk, CPU, network (high level) 

© Stephane Maarek 

|CloudWatch Alarms|
|---|



|•Alarms are used to trigger notifications for any metric|
|---|
|•Various options (sampling, %, max, min, etc…)|
|•Alarm States:|
|• OK|
|• INSUFFICIENT_DATA|
|• ALARM|
|•Period:|





<!-- Start of picture text -->
O<br>Ool)<br><!-- End of picture text -->

• Length of time in seconds to evaluate the metric • High resolution custom metrics: 10 sec, 30 sec or multiples of 60 sec © Stephane Maarek IE'”TS Ol ns 

#### CloudWatch Alarm Targets 

- Stop, Terminate, Reboot, or Recover an EC2 Instance 

- Trigger Auto Scaling Action 

- Send notification to SNS (from which you can do pretty much anything) 







Amazon EC2 

EC2 Auto Scaling 

Amazon SNS 

© Stephane Maarek SE 

es 

#### CloudWatch Alarms – Composite Alarms 

- CloudWatch Alarms are on a single metric 

- Composite Alarms are monitoring the states of multiple other alarms 

- AND and OR conditions 

- Helpful to reduce “alarm noise” by creating complex composite alarms 



<!-- Start of picture text -->
Composite Alarm<br>monitor  CPU ALARM<br>CW Alarm -  A trigger<br>EC2 Instance<br>monitor  IOPS ALARM<br>Amazon SNS<br>pf<br>CW Alarm -  B<br><!-- End of picture text -->

© Stephane Maarek 

#### EC2 Instance Recovery 



<!-- Start of picture text -->
• Status Check:<br>• Instance status = check the EC2 VM<br>• System status = check the underlying hardware<br>monitor alert<br>o 8<br>EC2 Instance CloudWatch Alarm SNS Topic<br>StatusCheckFailed_System<br>EC2 Instance Recovery<br><!-- End of picture text -->

• Recovery: Same Private, Public, Elastic IP, metadata, placement group © Stephane Maarek IE '”TS Ol ns 

#### CloudWatch Alarm: good to know 

- Alarms can be created based on CloudWatch Logs Metrics Filters 



<!-- Start of picture text -->
CloudWatch<br>Metric Filter<br>Alert<br>CW Logs CW Alarm<br>Amazon SNS<br><!-- End of picture text -->

- To test alarms and notifications, set the alarm state to Alarm using CLI aws cloudwatch set-alarm-state --alarm-name "myalarm" --state-value ALARM --state-reason "testing purposes" 

© Stephane Maarek 

ns 

Amazon EventBridge (formerly CloudWatch Events) 



• Schedule: Cron jobs (scheduled scripts) **Schedule Every hour Trigger script on Lambda function** oo} — • Event Pattern: Event rules to react to a service doing something 0 Ozma **IAM Root User Sign in Event SNS Topic with Email Notification** 

- Trigger Lambda functions, send SQS/SNS messages… 

© Stephane Maarek IE '”TS Ol 

#### Amazon EventBridge Rules 

Example Destinations 

Example Source EC2 Instance CodeBuild **(ex: Start Instance) (ex: failed build)** Filter events (optional) S3 Event Trusted Advisor **(ex: upload object) (ex: new Finding)** Amazon EventBridge CloudTrail Schedule or Cron a **(any API call) (ex: every 4 hours)** 

JSON { Lambda AWS Batch ECS Task "version": "0", "id": "6a7e8feb-b491", "detail-type": "EC2 Instance State-change Notification", Filter events …. (optional) } SQS SNS Kinesis Data Streams Amazon EventBridge Step CodePipeline CodeBuild Functions SSM EC2 Actions 

© Stephane Maarek 

#### Amazon EventBridge 



<!-- Start of picture text -->
AWS Services AWS SaaS  Custom<br>Partner  Custom<br>Default  Partners Apps<br>Event Bus Event Bus<br>Event Bus<br>' tot uly a Sale [ Se<br>| iH» Sf\- !  zendesk > = ' \___+5<br>DATADOG 5<br>fe] | Fa oR | 4<br><!-- End of picture text -->

- Event buses can be accessed by other AWS accounts using Resource-based Policies 

- You can archive events (all/filter) sent to an event bus (indefinitely or set period) 

- Ability to replay archived events 

© Stephane Maarek 

#### Amazon EventBridge – Schema Registry 

- EventBridge can analyze the events in your bus and infer the schema 

- The Schema Registry allows you to generate code for your application, that will know in advance how data is structured in the event bus 

- Schema can be versioned 



<!-- Start of picture text -->
aws.codepipeline@CodePipelineActionExecuti...<br>Schema details<br>‘Schema name Last modified ‘Schema ARN<br>aws.codepipeline@ Dec 1, 2019, 12:11 .<br>CodePipelineAction AM GMT<br>ExecutionStateChan Schema Number of ‘Schema<br>ge registry versions.—type<br>Description awsevents 1 30openaPt<br>‘Schema for event type<br>CodePipelineActionExecutionStateChange,<br>published by AWS service aws.codepipeline<br>Version 1 Created on Dec 1, 2019, 12:11 AM GMT<br>Download code bindings<br>1<br>5<br>“titLe’s “Coderipel inenctiontracutionstatechange™<br>‘><br><!-- End of picture text -->

© Stephane Maarek 

Amazon EventBridge – Resource-based Policy 

• Manage permissions for a specific Event Bus • Example: allow/deny events from another AWS account or AWS region • Use case: aggregate all events from your AWS Organization in a single AWS account or AWS region 



<!-- Start of picture text -->
{<br>"Version": 9<br>AWS Account AWS Account<br>"Statement": [ aws aws<br>{ (123456789012) (111122223333)<br>"Effect": 9<br>"Action": '<br>PutEvents<br>"Principal": { "AWS": Yo ~~ ly<br>"Resource": <Y Me<br>/ 20:<br>ms Lambda function<br>} EventBridge Bus<br>] (central-event-bus)<br>}<br>Allow  events  from another AWS account<br><!-- End of picture text -->

© Stephane Maarek 

#### CloudWatch Container Insights 

###### ECS Container EKS Container 

- Collect, aggregate, summarize metrics and logs from containers 

- Available for containers on… 

   - Amazon Elastic Container Service (Amazon ECS) 

   - Amazon Elastic Kubernetes Services (Amazon EKS) 

   - Kubernetes platforms on EC2 

   - Fargate (both for ECS and EKS) 

- In Amazon EKS and Kubernetes, CloudWatch Insights is using a containerized version of the CloudWatch Agent to discover containers 



###### Metrics and logs 



**CloudWatch Container Insights** 



© Stephane Maarek 

#### CloudWatch Lambda Insights 

- Monitoring and troubleshooting solution for serverless applications running on AWS Lambda 

- • Collects, aggregates, and summarizes system-level metrics including CPU time, memory, disk, and network 

- Collects, aggregates, and summarizes diagnostic information such as cold starts and Lambda worker shutdowns 

- • Lambda Insights is provided as a Lambda Layer 



<!-- Start of picture text -->
ps0 ‘Performance monitoring mom om i ow com (*]<br>= a Sey<br>ieee fname Dommmans Come<br>cone “wea Simms |)“ Sime |) —<br>Contaner eights _—— —_ .<br>eames tres aor sg) eo age<br>Soom : see a, Se ES peeee<br>Fey — — — ——<br>edad<br>OAs + arencowe Concave Dect Hem — ~<br><!-- End of picture text -->

© Stephane Maarek 

#### CloudWatch Contributor Insights 

- Analyze log data and create time series that display contributor data. 

   - See metrics about the top-N contributors 

   - The total number of unique contributors, and their usage. 



**VPC Flow Logs** 

- This helps you find top talkers and understand who or what is impacting system performance. 

- Works for any AWS-generated logs (VPC, DNS, etc..) 

- • For example, you can find bad hosts, identify the heaviest network users, or find the URLs that generate the most errors. 

**CloudWatch Logs** • For example, you can find bad hosts, identify the " heaviest network users, or find the URLs that generate the most errors. = • You can build your rules from scratch, or you can also use sample rules that AWS has created – leverages **CloudWatch** your CloudWatch Logs **Contributor Insights** • CloudWatch also provides built-in rules that you can use to analyze metrics from other AWS services. Top-10 IP addresses | IE '”TS Ol ns 

© Stephane Maarek IE '”TS Ol 

#### CloudWatch Application Insights 

- Provides automated dashboards that show potential problems with monitored applications, to help isolate ongoing issues 

- Your applications run on Amazon EC2 Instances with select technologies only (Java, .NET, Microsoft IIS Web Server, databases…) 

- And you can use other AWS resources such as Amazon EBS, RDS, ELB, ASG, Lambda, SQS, DynamoDB, S3 bucket, ECS, EKS, SNS, API Gateway… 

- Powered by SageMaker 

- Enhanced visibility into your application health to reduce the time it will take you to troubleshoot and repair your applications 

- Findings and alerts are sent to Amazon EventBridge and SSM OpsCenter 

© Stephane Maarek 

#### CloudWatch Insights and Operational Visibility 

- CloudWatch Container Insights 

   - ECS, EKS, Kubernetes on EC2, Fargate, needs agent for Kubernetes 

   - Metrics and logs 

- CloudWatch Lambda Insights 

   - Detailed metrics to troubleshoot serverless applications 

- CloudWatch Contributors Insights 

   - Find “Top-N” Contributors through CloudWatch Logs 

- CloudWatch Application Insights 

   - Automatic dashboard to troubleshoot your application and related AWS services 

© Stephane Maarek 

#### AWS CloudTrail 



   - Provides governance, compliance and audit for your AWS Account 

   - CloudTrail is enabled by default! 

   - Get an history of events / API calls made within your AWS Account by: 

      - Console 

      - SDK 

      - CLI 

      - AWS Services 

   - Can put logs from CloudTrail into CloudWatch Logs or S3 

- A trail can be applied to All Regions (default) or a single Region. 

- • If a resource is deleted in AWS, investigate CloudTrail first! 

- © Stephane Maarek 

- IE'”TS Ol ns 



<!-- Start of picture text -->
CloudTrail Diagram<br>SDK<br>©<br>CloudWatch Logs<br>CloudTrail Console<br>CLI<br>CJ<br>Console<br>Inspect & Audit<br>S3 Bucket<br>IAM Users &<br>IAM Roles<br><!-- End of picture text -->

es 

© Stephane Maarek SE 

#### CloudTrail Events 



- Management Events: 

   - Operations that are performed on resources in your AWS account 

   - • Examples: 

      - Configuring security (IAM AttachRolePolicy) 

      - Configuring rules for routing data (Amazon EC2 CreateSubnet) 

   - Setting up logging (AWS CloudTrail CreateTrail) 

   - • By default, trails are configured to log management events. 

   - Can separate Read Events (that don’t modify resources) from Write Events (that may modify resources) 

- Data Events: 

   - By default, data events are not logged (because high volume operations) 

   - Amazon S3 object-level activity (ex: GetObject, DeleteObject, PutObject): can separate Read and Write Events 

   - • AWS Lambda function execution activity (the Invoke API) 

- CloudTrail Insights Events: • See next slide J 

© Stephane Maarek 

#### CloudTrail Insights 



   - Enable CloudTrail Insights to detect unusual activity in your account: • inaccurate resource provisioning 

      - hitting service limits 

      - Bursts of AWS IAM actions 

      - Gaps in periodic maintenance activity 

- CloudTrail Insights analyzes normal management events to create a baseline 

- • And then continuously analyzes write events to detect unusual patterns • Anomalies appear in the CloudTrail console • Event is sent to Amazon S3 • An EventBridge event is generated (for automation needs) **CloudTrail Console** 

- Continous analysis generate 

- **Management Events Insights Events S3 Bucket** * BB. 2 —B **CloudTrail Insights EventBridge event** 

© Stephane Maarek 

#### CloudTrail Events Retention 

- Events are stored for 90 days in CloudTrail 

- To keep events beyond this period, log them to S3 and use Athena 



<!-- Start of picture text -->
Management Events ZO:NASWw CloudTrail<br>“ns Athena<br>NASWw log analyze<br>Data Events<br>“ns<br>S3 Bucket<br>NASWw 90 days<br>Insights Events ZO: Long-term retention<br>“ns retention<br><!-- End of picture text -->

© Stephane Maarek 

ns 

Amazon EventBridge – Intercept API Calls 



<!-- Start of picture text -->
User<br>lan<br>DeleteTable  API Call 💥<br>alert<br>Log API call event<br>DynamoDB CloudTrail Amazon SNS<br>EventBridge<br>(any API call)<br><!-- End of picture text -->

© Stephane Maarek IE '”TS Ol 

#### Amazon EventBridge + CloudTrail 



<!-- Start of picture text -->
API Call logs event<br>IAM CloudTrail EventBridge SNS<br>AssumeRole<br>User<br>XY IAM Role A<br>API Call logs event<br>cH ee CO fee CE<br>AuthorizeSecurityGroupIngress<br>EC2 CloudTrail EventBridge SNS<br>edit SG<br>User<br>Security Group<br>Inbound Rules<br>:<br><!-- End of picture text -->

© Stephane Maarek 

#### AWS Config 



- Helps with auditing and recording compliance of your AWS resources • Helps record configurations and changes over time 

- Questions that can be solved by AWS Config: 

   - Is there unrestricted SSH access to my security groups? 

   - Do my buckets have any public access? 

   - How has my ALB configuration changed over time? 

- You can receive alerts (SNS notifications) for any changes 

- AWS Config is a per-region service 

- Can be aggregated across regions and accounts 

- Possibility of storing the configuration data into S3 (analyzed by Athena) 

© Stephane Maarek IE '”TS Ol 

ns 

#### Config Rules 

- Can use AWS managed config rules (over 75) 

- Can make custom config rules (must be defined in AWS Lambda) • Ex: evaluate if each EBS disk is of type gp2 

   - Ex: evaluate if each EC2 instance is t2.micro 

- Rules can be evaluated / triggered: 

   - For each config change 

   - And / or: at regular time intervals 

- AWS Config Rules does not prevent actions from happening (no deny) 

- <u>Pricing:</u> no free tier, $0.003 per configuration item recorded per region, $0.001 per config rule evaluation per region 

© Stephane Maarek 

#### AWS Config Resource 

- View compliance of a resource over time 



<!-- Start of picture text -->
(e) sg-077b425b1649da83e EC2 SecurityGroup © Compliant<br>(e) sg-0831434f1876c0c74 EC2 SecurityGroup A\Noncompliant<br>(e) sg-09f10ed254d464f30 EC2 SecurityGroup © Compliant<br><!-- End of picture text -->

- View configuration of a resource over time 



<!-- Start of picture text -->
= July 3, 2021<br>14:37:44 | © Configuration change 1 field change(s)<br>14:33:26 GF Configuration change 0 field change(s)<br><!-- End of picture text -->

- View CloudTrail API calls of a resource over time 



<!-- Start of picture text -->
= July 3, 2021<br><!-- End of picture text -->

© Stephane Maarek 

#### Config Rules – Remediations 

- Automate remediation of non-compliant resources using SSM Automation Documents 

- Use AWS-Managed Automation Documents or create custom Automation Documents 

- Tip: you can create custom Automation Documents that invokes Lambda function 

- • You can set Remediation Retries if the resource is still non-compliant after autoremediation 

> expired Auto-Remediation Action monitor trigger ( **SSM Document:** AWSConfigRemediationae HE RevokeUnusedIAMUserCredentials) IAM Access Key AWS Config **Retries: 5** (NON_COMPLIANT) deactivate : 

© Stephane Maarek 

Config Rules – Notifications • Use EventBridge to trigger notifications when AWS resources are noncompliant monitor AWS Resources trigger … Security group … NON_COMPLIANT Lambda SNS SQS <mark>oo</mark> s @ <mark>oR,</mark> AWS Config EventBridge • Ability to send configuration changes and compliance state notifications to SNS (all events – use SNS Filtering or filter at client-side) AWS Resources monitor trigger notification Security group … All events <mark>oo)</mark> (configuration changes, ~~@~~ -« Admin SNS compliance state…) AWS Config 

© Stephane Maarek 

CloudWatch vs CloudTrail vs Config 

|• CloudWatch<br>• Performance monitoring (metrics, CPU, network, etc…) & dashboards<br>• Events & Alerting<br>• Log Aggregation & Analysis|
|---|
|• CloudTrail<br>• Record API calls made within your Account by everyone<br>• Can define trails for specific resources|
|• Global Service|
|• Config|
|• Record configuration changes<br>• Evaluate resources against compliance rules|
|• Get timeline of changes and compliance|



© Stephane Maarek 

#### For an Elastic Load Balancer 

- CloudWatch: 

   - Monitoring Incoming connections metric 

   - Visualize error codes as % over time 

   - Make a dashboard to get an idea of your load balancer performance 

- Config: 

   - Track security group rules for the Load Balancer 

   - Track configuration changes for the Load Balancer 

- Ensure an SSL certificate is always assigned to the Load Balancer (compliance) 

- • CloudTrail: 

   - Track who made any changes to the Load Balancer with API calls 

© Stephane Maarek 

### Advanced Identity in AWS 

© Stephane Maarek 

Organizational Units (OU) - Examples 

<u>Business Unit Environmental Lifecycle</u> 

###### <u>Project-Based</u> 



<!-- Start of picture text -->
Sales Prod Project 1<br>Account 1 Account 1 Account 1<br>Project 1<br>Sales OU Prod OU<br>OU<br>Sales Prod Project 1<br>Account 2 Account 2 Account 2<br>Retail Dev Project 2<br>Account 1 Account 1 Account 1<br>Management  Management  Management  Project 2<br>Retail OU Dev OU<br>Account Account Account OU<br>Retail Dev Project 2<br>Account 2 Account 2 Account 2<br>Finance Test Project 3<br>Account 1 Account 1 Account 1<br>Finance  Project 3<br>Test OU<br>OU OU<br>Finance Test Project 3<br>Account 2 Account 2 Account 2<br><!-- End of picture text -->

© Stephane Maarek 

#### AWS Organizations 

- Global service 



- Allows to manage multiple AWS accounts 

- The main account is the management account 

- Other accounts are member accounts 

- Member accounts can only be part of one organization 

- Consolidated Billing across all accounts - single payment method 

- Pricing benefits from aggregated usage (volume discount for EC2, S3…) 

• Shared reserved instances and Savings Plans discounts across accounts • API is available to automate AWS account creation © Stephane Maarek IE'”TS Ol ns 

#### AWS Organizations 



<!-- Start of picture text -->
Root Organizational Unit (OU)<br>Management Account<br>OU (Dev) OU (Prod)<br>OU (HR) OU (Finance)<br>Member Accounts<br><!-- End of picture text -->

© Stephane Maarek 

#### AWS Organizations 

- Advantages 

   - Multi Account vs One Account Multi VPC 

   - Use tagging standards for billing purposes 

   - Enable CloudTrail on all accounts, send logs to central S3 account 

   - Send CloudWatch Logs to central logging account 

   - Establish Cross Account Roles for Admin purposes 

- Security: Service Control Policies (SCP) 

   - IAM policies applied to OU or Accounts to restrict Users and Roles 

   - They do not apply to the management account (full admin power) 

   - Must have an explicit allow (does not allow anything by default – like IAM) 

© Stephane Maarek 

#### SCP Hierarchy 

- **FullAWSAccess** SCP Root OU • Management Account • Can do anything 

- • (no SCP apply) 

- **DenyAccessAthena** SCP Management Account • Account A • Can do anything 

- • EXCEPT access Redshift 

- **DenyRedshift** SCP OU (Prod) (explicit Deny from OU) • Account B 

- **AuthorizedRedshift** SCP Account A • Can do anything • EXCEPT access Redshift (explicit Deny from Prod OU) 

- • EXCEPT access Lambda 

- **DenyAWSLambda** SCP OU (HR) OU (Finance) (explicit Deny from HR OU) 

- • Account C 

- Account B Account C • Can do anything 

- • EXCEPT access Redshift (explicit Deny from Prod OU) 

© Stephane Maarek 

#### SCP Examples Blocklist and Allowlist strategies 



<!-- Start of picture text -->
\<br>"Version": "2012-10-17",<br>"Statement": [<br>{<br>ASE 8 me<br>"Action": "x",<br>"Resource": "x"<br>},<br>{<br>"Sid": "DenyDynamoDB",<br>"Effect": "Deny",<br>"Action": “dynamodb:*",<br>"Resource": "x"<br>}<br>]<br><!-- End of picture text -->



<!-- Start of picture text -->
K<br>= . = , - soc<br>Version": "2012-10-17",<br>"Statement": [<br>" uw, YS ont?<br>Effect": "Allow",<br>"Action": [<br>'ec2:*",<br>' diy 4 } . '<br>oudwatch:+<br>l,<br>"Resource": "x"<br>}<br>]<br><!-- End of picture text -->

More examples: https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_example-scps.html 

© Stephane Maarek 

#### IAM Conditions 

**<u>aws:SourceIp</u>** restrict the client IP **<u>from</u>** which the API calls are being made 

**<u>aws:RequestedRegion</u>** restrict the region the API calls are made **<u>to</u>** 



<!-- Start of picture text -->
{<br>"Version": "2012-10-17",<br>"Statement": [<br>{<br>"Effect": "Deny",<br>"Action": ["ec2:*", "rds:", "dynamodb:*"],<br>"Resource": "x",<br>"Condition": {<br>"StringEquals": {<br>“aws:RequestedRegion": ["eu-central-1", “eu-west-1"]<br>}<br>}<br>}<br>1<br>}<br><!-- End of picture text -->



<!-- Start of picture text -->
{ {<br>"Version": "2012-10-17",<br>"Statement": [<br>{<br>"Effect": "Deny",<br>"Action": "x",<br>"Resource": "x",<br>"Condition": {<br>"NotIpAddress": {<br>} “aws:SourceIp": ["192.0.2.0/24", "203.0.113.0/2¢<br>, ,<br>]<br>}<br>}<br><!-- End of picture text -->

© Stephane Maarek 

#### IAM Conditions 

**<u>ec2:ResourceTag</u>** restrict based on **tags** 



<!-- Start of picture text -->
{<br>"Version": "2012-10-17",<br>"Statement": [<br>{<br>"Effect": "Allow",<br>"Action": ["ec2:startInstances", “ec2:StopInstances"],<br>"Resource": “arn:aws:ec2:us—east—1: 123456789012: instance/*",<br>"Condition": {<br>"StringEquals": {<br>"ec2:ResourceTag/Project": "DataAnalytics",<br>u we neo u<br>aws:PrincipalTag/Department": "Data<br>}<br>}<br>3<br>}<br>}<br><!-- End of picture text -->

**<u>aws:MultiFactorAuthPresent</u>** to force **MFA** 

} + ] + 

© Stephane Maarek 

#### IAM for S3 

- s3:ListBucket permission applies to arn:aws:s3:::test 

- => bucket level permission 

- s3:GetObject, s3:PutObject , s3:DeleteObject applies to arn:awn:s3:::test/* 

- => object level permission 



<!-- Start of picture text -->
{<br>"Version": "2012-10-17",<br>"Statement": [<br>{<br>"Effect": "Allow",<br>"Action": ["s3:ListBucket"],<br>"Resource": "arn:aws:S3:::test"<br>},<br>{<br>"Effect": "Allow",<br>"Action": [<br>"s3:PutObject",<br>"s53:GetObject",<br>"s3:DeleteObject"<br>],<br>+ "Resource": "arn:aws:S3:: stef/*)<br>]<br>+<br><!-- End of picture text -->

© Stephane Maarek 

#### Resource Policies & aws:PrincipalOrgID 

- aws:PrincipalOrgID can be used in any resource policies to restrict access to accounts that are member of an AWS Organization 



<!-- Start of picture text -->
aon e ene e ee, {<br>"Version": "2012-10-17",<br>AWS Organization<br>ooo ' "Statement": [<br>(o-yyyyyyyyyy)<br>! __<br>\ "Effect": "Allow",<br>…<br>t i "Action": ["s3:PutObject", "s3:GetObject"],<br>' ' "Resource": “arn:aws:S3:::2022-financial-data/x",<br>Member Accounts<br>! H x "Condition": {<br>S3 Bucket<br>Lolli e eee eeeeeeae ee een eee e ee! "StringEquals": {<br>(2022-financial-data) “aws:Principal0rgID": ["o-yyyyyyyyyy"]<br>}<br>+<br>}<br>]<br>+<br>User outside Organization<br><!-- End of picture text -->

© Stephane Maarek 

IAM Roles vs Resource Based Policies • Cross account: • attaching a resource-based policy to a resource (example: S3 bucket policy) • OR using a role as a proxy User Role Account A Account B <mark>e</mark> ~~<mark>e</mark>~~ Amazon S3 User S3 Bucket Account A Policy Amazon S3 © Stephane Maarek <mark>IE=</mark> '”TS Ol <mark>=</mark> ens 

#### IAM Roles vs Resource-Based Policies 

- When you assume a role (user, application or service), you give up your original permissions and take the permissions assigned to the role 

- When using a resource-based policy, the principal doesn’t have to give up his permissions 

- <u>Example:</u> User in account A needs to scan a DynamoDB table in Account A and dump it in an S3 bucket in Account B. 

- Supported by: Amazon S3 buckets, SNS topics, SQS queues, etc… 

© Stephane Maarek 

#### Amazon EventBridge – Security 

- When a rule runs, it needs permissions on the target 

- Resource-based policy: Lambda, SNS, SQS, CloudWatch Logs, API Gateway… 



<!-- Start of picture text -->
77s<br><!-- End of picture text -->



EventBridge Lambda with Rule **Resource based Policy e.g. Allow EventBridge** 

- IAM role: Kinesis stream, Systems Manager Run Command, ECS task… 



<!-- Start of picture text -->
IAM Role<br>a .<br>oN<br>EventBridge Kinesis<br>Rule<br><!-- End of picture text -->

© Stephane Maarek 

#### IAM Permission Boundaries 

- IAM Permission Boundaries are supported for users and roles (not groups) 

- Advanced feature to use a managed policy to set the maximum permissions an IAM entity can get. 



<!-- Start of picture text -->
Example:<br><!-- End of picture text -->



<!-- Start of picture text -->
{<br>"Version": "2@12-10-17",<br>"Statement": [<br>{<br>"Effect": "Allow",<br>"Action": [<br>"s3:*",<br>"cloudwatch:*",<br>"ec2:*"<br>1,<br>3 "Resource": "*"<br>J<br>3<br><!-- End of picture text -->

**+** 



<!-- Start of picture text -->
{<br>"Version": "2012-10-17",<br>"Statement": {<br>"Effect": "Allow",<br>"Action": "iam:CreateUser",<br>"Resource": "*"<br>}<br>}<br><!-- End of picture text -->

**=** 

No Permissions 

**IAM Permission Boundary IAM Permissions Through IAM Policy** 

© Stephane Maarek 

#### IAM Permission Boundaries 

- Can be used in combinations of AWS Organizations SCP 



<!-- Start of picture text -->
Organizations Vv Permissions<br>scP boundary<br>SS Effective<br>Lethe permissions<br><!-- End of picture text -->

<u>https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html</u> 

###### <u>Use cases</u> 

- Delegate responsibilities to non administrators within their permission boundaries, for example create new IAM users 

- Allow developers to self-assign policies and manage their own permissions, while making sure they can’t “escalate” their privileges (= make themselves admin) 

- Useful to restrict one specific user (instead of a whole account using Organizations & SCP) 

© Stephane Maarek 

#### IAM Policy Evaluation Logic 



<!-- Start of picture text -->
Decision starts (s the<br>an ee principal's. No Does the \\ No Yes Does the \_No No<br>account a membe? requested Does the principa principal have a teins Final decision:<br>of an organization resource have a have an identity- missions principal a session ‘Allow<br>with an resource-based based policy? ass principal"?<br>applicableSCP?, policy? -<br>Evaluate all<br>applicable Yes Yes<br>policies<br>Is there a session<br>5 Is this a role session?<br>policy?<br>Is No Yes Yes<br>there an Is there Is there Is there Is there<br>explicit an Allow? an Allow? an Allow? an Allow? No<br>Deny?<br>Yes No Yes No No Final decision<br>\s there an Allow? Deny<br>(implicit deny)<br>Final decision: Final decision: Final decision: Final decision:<br>Deny Deny Deny Deny<br>(explicit deny) (implicit deny) (implicit deny) (implicit deny) Yes<br>Final decision:<br>Deny evaluation Organizations SCPs Resource-based policies Identity-based policies IAM permissions Allow Session policies<br>boundaries<br>*A session principal is either a role session or an IAM federated user session,<br><!-- End of picture text -->

<u>https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic.html</u> 

© Stephane Maarek 

#### Example IAM Policy 

- Can you perform sqs:CreateQueue? 

- Can you perform sqs:DeleteQueue? 

- Can you perform ec2:DescribeInstances? 



<!-- Start of picture text -->
i<br>"Version": "2012-10-17",<br>"Statement": [<br>{<br>"Action": "sqs:x*",<br>"Effect": "Deny",<br>"Resource": "x'<br>},<br>{<br>"Action": [<br>],<br>"Effect": "Allow",<br>"Resource": ''<br>}<br>]<br>}<br><!-- End of picture text -->

© Stephane Maarek 

AWS IAM Identity Center (successor to AWS Single Sign-On) 



<!-- Start of picture text -->
ee<br><!-- End of picture text -->

- One login (single sign-on) for all your • AWS accounts in AWS Organizations 

• Business cloud applications (e.g., Salesforce, Box, Microsoft 365, …) • SAML2.0-enabled applications • EC2 Windows Instances 

• Identity providers 

- Built-in identity store in IAM Identity Center 

• 3<sup>rd</sup> party: Active Directory (AD), OneLogin, Okta… 



<!-- Start of picture text -->
ane2'9<br>AAS<br><!-- End of picture text -->

© Stephane Maarek 

#### AWS IAM Identity Center – Login Flow 

###### **AWS IAM Identity Center** 



<!-- Start of picture text -->
Sign in<br>Username<br>Stephane<br>Remember username<br><!-- End of picture text -->



<!-- Start of picture text -->
AWS Account (4)<br>@ ws courses n<br>#783746093452 |<br>AdministratorAccess Management console | Command line or programmatic access<br>@ datacumutus-main 7<br>#387374203361 |<br>@ stéphane MAAREK ¥<br>#160803648315 |<br>@ stephane-ccp .<br>#855174973723 |<br><!-- End of picture text -->





<!-- Start of picture text -->
a) BO Fankturt + Amnsttertcetephane<br>Console Home ww. Reset to default layout [o|<br>Recently visited ine :<br>BB) tise containerServic mee BB count<br>8 BB razon Pty<br>Bi ws [A Wis costbio<br>Bs BD trciterey<br>Bow BB) crosicrabemetes service<br>BR noce BBD ceyranagement service<br><!-- End of picture text -->



© Stephane Maarek 

#### AWS IAM Identity Center 

AWS Cloud **AWS IAM Identity Center** aws ms!re: **AWS Windows** v **SSO** login **Organization EC2 Permission Sets Business Cloud Apps** Browser Interface | box st slack TOT Store / retrieve jeyeye) 1 User identities (ror | BIN Microsoft365 3% Dropbox **Active Directory IAM Identity Center Custom SAML2.0-enabled Apps** Users & groups Built-in Identity Store (On-premises, cloud) 









<!-- Start of picture text -->
‘Active Directory<br><!-- End of picture text -->

© Stephane Maarek 

#### IAM Identity Center 







<!-- Start of picture text -->
AWS Organization<br>IAM Identity Center<br>(in Management account)<br>Management Account<br>Group (Developers)<br>OU (Development) OU (Production)<br>Bob Alice<br>Dev Account A Prod Account A<br>assign<br>Dev Account B Prod Account B<br>Permission Set<br>ReadOnlyAccess<br>Permission Set<br>I FullAccess z assign<br>IE '”TS Ol ns<br>NOT FOR DISTRIBUTION © Stephane Maarek www.datacumulus.com<br><!-- End of picture text -->

© Stephane Maarek IE '”TS Ol 

AWS IAM Identity Center Fine-grained Permissions and Assignments 



<!-- Start of picture text -->
CIE=e<br><!-- End of picture text -->

- Multi-Account Permissions 

   - Manage access across AWS accounts in your AWS Organization 

   - Permission Sets – a collection of one or more IAM Policies assigned to users and groups to define AWS access 

- Application Assignments 

   - SSO access to many SAML 2.0 business applications (Salesforce, Box, Microsoft 365, …) 

   - Provide required URLs, certificates, and metadata 

- Attribute-Based Access Control (ABAC) 

   - Fine-grained permissions based on users’ attributes stored in IAM Identity Center Identity Store 

   - Example: cost center, title, locale, … 

   - Use case: Define permissions once, then modify AWS access by changing the attributes 



<!-- Start of picture text -->
AWS Organization<br>Dev Prod<br>Account Account<br>RDS Aurora RDS Aurora<br>IAM Role IAM Role<br>assume Permission Sets<br>(DB Admins)<br>Permission Sets<br>(DB Admins)<br><!-- End of picture text -->

Database IAM Identity Center Admins 

© Stephane Maarek 

es 

#### What is Microsoft Active Directory (AD)? 

- Found on any Windows Server with AD Domain Services 

- • Database of objects : User Accounts, Computers, Printers, File Shares, Security Groups 

- • Centralized security management, create account, assign permissions 

- Objects are organized in trees 

- A group of trees is a forest 





Domain Controller = John Password 







© Stephane Maarek SE 

AWS Directory Services • AWS Managed Microsoft AD auth trust auth • Create your own AD in AWS, manage users locally, supports MFA Ly • Establish “trust” connections with your onpremises AD **On-prem AD AWS Managed AD** • AD Connector proxy auth • Directory Gateway (proxy) to redirect to onpremises AD, supports MFA F ae • Users are managed on the on-premises AD **On-prem AD AD Connector** • Simple AD • AD-compatible managed directory on AWS • Cannot be joined with on-premises AD . **Simple AD** IE'”TS'”TS Ol ns 

• AD-compatible managed directory on AWS • Cannot be joined with on-premises AD . **Simple AD** © Stephane Maarek IE'”TS'”TS Ol ns 

#### IAM Identity Center – Active Directory Setup 

- Connect to an AWS Managed Microsoft AD (Directory Service) • Integration is out of the box 

IAM Identity connect AWS Managed Center Microsoft AD 

- Connect to a Self-Managed Directory • Create Two-way Trust Relationship using AWS Managed Microsoft AD • Create an AD Connector 

AWS Managed Microsoft AD connect two-way trust relationship IAM Identity Center connect = proxy Lo AD Connector 





© Stephane Maarek 

#### AWS Control Tower 



<!-- Start of picture text -->
2<br>¢ *<br>¢<br>eegie<br>.o<br><!-- End of picture text -->

- Easy way to set up and govern a secure and compliant multi-account <u>AWS environment</u> based on best practices 

- AWS Control Tower uses AWS Organizations to create accounts 

- Benefits: 

   - Automate the set up of your environment in a few clicks 

   - Automate ongoing policy management using guardrails 

   - Detect policy violations and remediate them 

   - Monitor compliance through an interactive dashboard 

© Stephane Maarek 

#### AWS Control Tower – Guardrails 

- Provides ongoing governance for your Control Tower environment (AWS Accounts) 

- • Preventive Guardrail – using SCPs (e.g., Restrict Regions across all your accounts) • Detective Guardrail – using AWS Config (e.g., identify untagged resources) 



<!-- Start of picture text -->
AWS Control Tower<br>Guardrail trigger notify<br>(Detective) (NON_COMPLIANT)<br>AWS Config<br>Admin<br>SNS<br>monitor un-tagged<br>resources invoke<br>Member remediate<br>Accounts (add tags)<br>Lambda<br><!-- End of picture text -->

© Stephane Maarek 

### AWS Security & Encryption KMS, Encryption SDK, SSM Parameter Store 

© Stephane Maarek 

- Why encryption? Encryption in flight (TLS / SSL) • Data is encrypted before sending and decrypted after receiving • TLS certificates help with encryption (HTTPS) • Encryption in flight ensures no MITM (man in the middle attack) can happen 



<!-- Start of picture text -->
Username: admin aGVsbG8gd29 Username: admin<br>Password: supersecret ybGQgZWh… Password: supersecret<br>Client TLS Encryption TLS Decryption<br>HTTPS Website<br>Client Server<br><!-- End of picture text -->

© Stephane Maarek 

#### Why encryption? Server-side encryption at rest 

• Data is encrypted after being received by the server 

- Data is decrypted before being sent 

- It is stored in an encrypted form thanks to a key (usually a data key) • The encryption / decryption keys must be managed somewhere, and the server must have access to it 



<!-- Start of picture text -->
Encryption Decryption<br>HTTP(S) + + HTTP(S)<br>Ba _ 26 .<br>Object Object<br>Data key Data key<br>AWS Service (e.g., S3)<br><!-- End of picture text -->

© Stephane Maarek 

#### Why encryption? Client-side encryption 



<!-- Start of picture text -->
• Data is encrypted by the client and never decrypted by the server<br>• Data will be decrypted by a receiving client<br>• The server should not be able to decrypt the data<br>• Could leverage Envelope Encryption<br>Encryption store<br>+<br>Data key<br>Object<br>(client-side)<br>retrieve<br>Encrypted object<br>+<br>Decryption<br>Data key<br>Object<br>(client-side)<br>Any storage service<br>(FTP, S3, …)<br>Client<br><!-- End of picture text -->

© Stephane Maarek 

AWS KMS (Key Management Service) 



- Anytime you hear “encryption” for an AWS service, it’s most likely KMS 

- AWS manages encryption keys for us 

- Fully integrated with IAM for authorization 

- Easy way to control access to your data 

- Able to audit KMS Key usage using CloudTrail 

- Seamlessly integrated into most AWS services (EBS, S3, RDS, SSM…) 

- Never ever store your secrets in plaintext, especially in your code! 

• KMS Key Encryption also available through API calls (SDK, CLI) • Encrypted secrets can be stored in the code / environment variables © Stephane Maarek IE'”TS Ol ns 

#### KMS Keys Types 

- KMS Keys is the new name of KMS Customer _Master_ Key 

- Symmetric (AES-256 keys) 

   - Single encryption key that is used to Encrypt and Decrypt 

   - AWS services that are integrated with KMS use Symmetric CMKs 

   - You never get access to the KMS Key unencrypted (must call KMS API to use) 

- Asymmetric (RSA & ECC key pairs) 

   - Public (Encrypt) and Private Key (Decrypt) pair 

   - Used for Encrypt/Decrypt, or Sign/Verify operations 

   - The public key is downloadable, but you can’t access the Private Key unencrypted 

   - Use case: encryption outside of AWS by users who can’t call the KMS API 

© Stephane Maarek 

AWS KMS (Key Management Service) 



- Types of KMS Keys: 

   - AWS Owned Keys (free): SSE-S3, SSE-SQS, SSE-DDB (default key) 

   - AWS Managed Key: free (aws/ _service-name_ , example: aws/rds or aws/ebs) 

   - Customer managed keys created in KMS: $1 / month 



<!-- Start of picture text -->
C<br><!-- End of picture text -->

- Customer managed keys imported (must be symmetric key): $1 / month 



<!-- Start of picture text -->
Encryption key management<br>© Owned by Amazon DynamoDB<br><!-- End of picture text -->

- + pay for API call to KMS ($0.03 / 10000 calls) 



<!-- Start of picture text -->
© AWSKey alias: managedaws/dynamodb. key Lea °<br><!-- End of picture text -->

- Automatic Key rotation: 

   - AWS-managed KMS Key: automatic every 1 year 



<!-- Start of picture text -->
and owned and managed by you<br><!-- End of picture text -->

- Customer-managed KMS Key: (must be enabled) automatic every 1 year 

- Imported KMS Key: only manual rotation possible using alias 

© Stephane Maarek 

#### Copying Snapshots across regions 





**Region ap-southeast-2 EBS Volume Encrypted With KMS** KMS Key B So **EBS Snapshot Encrypted With KMS** KMS Key B ee ns 

**Region eu-west-2 EBS Volume Encrypted With KMS** KMS Key A So **EBS Snapshot Encrypted With KMS** KMS Key A Boo 

**KMS ReEncrypt with KMS Key B** 

© Stephane Maarek IE '”TS Ol 

ns 

#### KMS Key Policies 

- Control access to KMS keys, “similar” to S3 bucket policies 



- Difference: you cannot control access without them 

- Default KMS Key Policy: 

   - Created if you don’t provide a specific KMS Key Policy 

   - Complete access to the key to the root user = entire AWS account 

- Custom KMS Key Policy: 

   - Define users, roles that can access the KMS key 

   - Define who can administer the key 

   - Useful for cross-account access of your KMS key 

© Stephane Maarek IE '”TS Ol 

#### Copying Snapshots across accounts 

1. Create a Snapshot, encrypted with your own KMS Key (Customer Managed Key) 

2. Attach a KMS Key Policy to authorize cross-account access 

3. Share the encrypted snapshot 4. (in target) Create a copy of the Snapshot, encrypt it with a CMK in your account 

5. Create a volume from the snapshot 



<!-- Start of picture text -->
{<br>"Sid": "Allow use of the key with destination account",<br>"Effect": "Allow",<br>"Principal": {<br>“AWS": “arn:aws: iam: : TARGET—-ACCOUNT-ID: role/ROLENAME"<br>},<br>"Action": [<br>"kms:Decrypt",<br>“kms:CreateGrant"<br>],<br>"Resource": "x",<br>"Condition": {<br>"StringEquals": {<br>"kms:ViaService": "“ec2.REGION.amazonaws.com",<br>“kms:CallerAccount": '"TARGET-ACCOUNT-ID"<br>+<br>}<br>+<br><!-- End of picture text -->

###### **KMS Key Policy** 

© Stephane Maarek 

#### KMS Multi-Region Keys 



<!-- Start of picture text -->
AWS KMS<br>us-west-2<br>multi-Region  Replica  key<br>arn:aws:kms: us-west-2 :111122223333:<br>key/ mrk- 1234abcd12ab34cd56ef1234567890ab<br>us-east-1 eu-west-1<br>sync<br>multi-Region  Primary  key multi-Region  Replica  key<br>arn:aws:kms: us-east-1 :111122223333: arn:aws:kms: eu-west-1 :111122223333:<br>key/ mrk- 1234abcd12ab34cd56ef1234567890ab key/ mrk- 1234abcd12ab34cd56ef1234567890ab<br>ap-southeast-2<br>multi-Region  Replica  key<br>arn:aws:kms: ap-southeast-2 :111122223333:<br>key/ mrk- 1234abcd12ab34cd56ef1234567890ab<br><!-- End of picture text -->

© Stephane Maarek 

#### KMS Multi-Region Keys 



<!-- Start of picture text -->
es<br><!-- End of picture text -->



<!-- Start of picture text -->
-eEx<br><!-- End of picture text -->

- Identical KMS keys in different AWS Regions that can be used interchangeably 

- Multi-Region keys have the same key ID, key material, automatic rotation… 

- Encrypt in one Region and decrypt in other Regions 

- No need to re-encrypt or making cross-Region API calls 

- KMS Multi-Region are NOT global (Primary + Replicas) 

- Each Multi-Region key is managed independently 

- Use cases: global client-side encryption, encryption on Global DynamoDB, Global Aurora 

© Stephane Maarek 

DynamoDB Global Tables and KMS MultiRegion Keys Client-Side encryption 

- We can encrypt specific attributes client-side in our DynamoDB table using the Amazon DynamoDB Encryption Client 

- Combined with Global Tables, the client-side encrypted data is replicated to other regions 

- If we use a multi-region key, replicated in the same region as the DynamoDB Global table, then clients in these regions can use lowlatency API calls to KMS in their region to decrypt the data client-side 

- Using client-side encryption we can protect specific fields and guarantee only decryption if the client has access to an API key 



<!-- Start of picture text -->
us-east-1<br>KMS<br>1.  Encrypt attribute<br>with primary MRK<br>2.  Put encrypted Attr<br>MRK<br>attribute (SSN)<br>Client App DDB Table<br>3.  Global Table<br>Replication<br>ap-southeast-2<br>4.  Get encrypted Attr<br>attribute (SSN)<br>MRK<br>Client App DDB Table<br>5.  Decrypt attribute<br>with replica MRK<br>KMS<br>replication<br><!-- End of picture text -->

© Stephane Maarek 

#### Global Aurora and KMS Multi-Region Keys Client-Side encryption 

- We can encrypt specific attributes client-side in our Aurora table using the AWS Encryption SDK 

- Combined with Aurora Global Tables, the client-side encrypted data is replicated to other regions 

- If we use a multi-region key, replicated in the same region as the Global Aurora DB, then clients in these regions can use low-latency API calls to KMS in their region to decrypt the data client-side 

- Using client-side encryption we can protect specific fields and guarantee only decryption if the client has access to an API key, we can protect specific fields even from database admins 



<!-- Start of picture text -->
us-east-1<br>KMS<br>1.  Encrypt attribute<br>with primary MRK<br>2.  Put encrypted Col<br>MRK<br>column (SSN)<br>Client App Table<br>3.  Global DB<br>Replication<br>ap-southeast-2<br>4.  Get encrypted Col<br>column (SSN)<br>MRK<br>Client App Table<br>5.  Decrypt attribute<br>with replica MRK<br>KMS<br>replication<br><!-- End of picture text -->

© Stephane Maarek 

es 

#### S3 Replication Encryption Considerations 





- Unencrypted objects and objects encrypted with SSE-S3 are replicated by default 

- Objects encrypted with SSE-C (customer provided key) can be replicated 

- For objects encrypted with SSE-KMS , you need to enable the option 

   - Specify which KMS Key to encrypt the objects within the target bucket 

   - Adapt the KMS Key Policy for the target key 

   - An IAM Role with kms:Decrypt for the source KMS Key and kms:Encrypt for the target KMS Key 

   - You might get KMS throttling errors, in which case you can ask for a Service Quotas increase 

- You can use multi-region AWS KMS Keys, but they are currently treated as independent keys by Amazon S3 (the object will still be decrypted and then encrypted) 

© Stephane Maarek EES 

#### AMI Sharing Process Encrypted via KMS 

1. AMI in Source Account is encrypted with KMS Key from Source Account 2. Must modify the image attribute to add a Launch Permission which corresponds to the specified target AWS account 3. Must share the KMS Keys used to encrypted the snapshot the AMI references with the target account / IAM Role 

4. The IAM Role/User in the target account must have the permissions to DescribeKey, ReEncrypted, CreateGrant, Decrypt 

5. When launching an EC2 instance from the AMI, optionally the target account can specify a new KMS key in its own account to re-encrypt the volumes 

Account - A KMS AMI Key share share Account - B launch AMI EC2 Instance 

© Stephane Maarek 

#### SSM Parameter Store 

- Secure storage for configuration and secrets • Optional Seamless Encryption using KMS • Serverless, scalable, durable, easy SDK • Version tracking of configurations / secrets • Security through IAM • Notifications with Amazon EventBridge • Integration with CloudFormation 

Bi, **Applications** = Plaintext Encrypted configuration configuration i **SSM Parameter Check IAM Store permissions** Decryption Service os **AWS KMS** ns 

Decryption Service **AWS KMS** ns 

© Stephane Maarek IE '”~~=— Ol 

#### SSM Parameter Store Hierarchy 

• /my-department/ 

• my-app/ GetParameters or • dev/ GetParametersByPath API • db-url **Dev Lambda** • db-password **Function** ez [J] • prod/ • db-url **Prod Lambda** • db-password **Function** e== [J 

      - other-app/ 

   - /other-department/ 

- _/aws/reference/secretsmanager/secret_ID_in_Secrets_Manager_ 

- • _/aws/service/ami-amazon-linux-latest/amzn2-ami-hvm-x86_64-gp2 (public)_ 

- © Stephane Maarek 

- IE'”TS Ol ns 

#### Standard and advanced parameter tiers 

||**Standard**|**Advanced**|
|---|---|---|
|Total number of parameters<br>allowed<br>(per AWS account and<br>Region)|10,000|100,000|
|Maximum size of a<br>parameter value|4 KB|8 KB|
|Parameter policies available|No|Yes|
|Cost|No additional charge|Charges apply|
|Storage Pricing|Free|$0.05 per advanced parameter per<br>month|



© Stephane Maarek 

<mark>}} }</mark> } 

Parameters Policies (for advanced parameters) 

- Allow to assign a TTL to a parameter (expiration date) to force updating or deleting sensitive data such as passwords 

- Can assign multiple policies at a time 

###### **Expiration (to delete a parameter)** 

###### **ExpirationNotification (EventBridge)** 

###### **NoChangeNotification (EventBridge)** 



<!-- Start of picture text -->
{<br>"Type" :"Expiration",<br>"Version":"1.0",<br>"Attributes":{<br>"Timestamp" :"2020-12-02T21:34:33.000Z"<br>+<br><!-- End of picture text -->

© Stephane Maarek 

#### AWS Secrets Manager 



- Newer service, meant for storing secrets 

- Capability to force rotation of secrets every X days 

- Automate generation of secrets on rotation (uses Lambda) 

- Integration with Amazon RDS (MySQL, PostgreSQL, Aurora) 

- Secrets are encrypted using KMS 

- Mostly meant for RDS integration 

© Stephane Maarek IE '”TS Ol 

#### AWS Secrets Manager – Multi-Region Secrets 

- Replicate Secrets across multiple AWS Regions 

- Secrets Manager keeps read replicas in sync with the primary Secret 



<!-- Start of picture text -->
• Ability to promote a read replica Secret to a standalone Secret<br>• Use cases: multi-region apps, disaster recovery strategies, multi-region DB…<br>us-east-1 (Primary) us-west-2 (Secondary)<br>Secrets replicate Secrets<br>Manager Manager<br>MySecret-A MySecret-A<br>(primary) (replica)<br><!-- End of picture text -->

© Stephane Maarek 



<!-- Start of picture text -->
AWS Certificate Manager (ACM)<br>• Easily provision, manage, and deploy  TLS Certificates<br>• Provide in-flight encryption for websites (HTTPS)<br>HTTPS<br>• Supports both public and private TLS certificates<br>provision and<br>Application<br>• Free of charge for public TLS certificates maintain TLS certs<br>Load<br>• Automatic TLS certificate renewal<br>Balancer<br>• Integrations with (load TLS certificates on) AWS Certificate Manager<br>B lan<br>• Elastic Load Balancers (CLB, ALB, NLB)<br>HTTP<br>• CloudFront Distributions<br>• APIs on API Gateway )<br>Auto Scaling group<br>• Cannot use ACM with EC2 (can’t be extracted)<br>EC2 Instance EC2 Instance<br>NOT FOR DISTRIBUTION © Stephane Maarek www.datacumulus.com<br><!-- End of picture text -->

© Stephane Maarek 

#### ACM – Requesting Public Certificates 

1. List domain names to be included in the certificate 

   - Fully Qualified Domain Name (FQDN): corp.example.com 

   - Wildcard Domain: *.example.com 

2. Select Validation Method: DNS Validation or Email validation 

   - DNS Validation is preferred for automation purposes 

   - Email validation will send emails to contact addresses in the WHOIS database 

   - DNS Validation will leverage a CNAME record to DNS config (ex: Route 53) 

3. It will take a few hours to get verified 

4. The Public Certificate will be enrolled for automatic renewal 

   - ACM automatically renews ACM-generated certificates 60 days before expiry 

© Stephane Maarek 

#### ACM – Importing Public Certificates 

- Option to generate the certificate outside of ACM and then import it 

- No automatic renewal , must import a new certificate before expiry 

- ACM sends daily expiration events starting 45 days prior to expiration • The # of days can be configured • Events are appearing in EventBridge 

- AWS Config has a managed rule named _acm-certificate-expiration-check_ to check for expiring certificates (configurable number of days) 

ACM 



<!-- Start of picture text -->
ACM Events:<br>Daily Certificate Expiry<br>Lambda<br>Rule check<br>SNS<br>EventBridge<br>Rule events:<br>Non-compliance<br>SQS<br>AWS Config<br><!-- End of picture text -->

© Stephane Maarek 

ACM – Integration with ALB **Application Load Balancer** With HTTP -> HTTPS redirect rule HTTP Auto Scaling group **Redirect to HTTPS HTTPS** EC2 Instance EC2 Instance provision and maintain TLS certs ~~oT~~ oO oO AWS Certificate Manager IE '”TS Ol ns 

© Stephane Maarek IE '”TS Ol 

#### API Gateway - Endpoint Types 

- Edge-Optimized (default): For global clients 

   - Requests are routed through the CloudFront Edge locations (improves latency) 

   - • The API Gateway still lives in only one region 

- Regional: 

   - For clients within the same region 

   - Could manually combine with CloudFront (more control over the caching strategies and the distribution) 

- Private: 

   - Can only be accessed from your VPC using an interface VPC endpoint (ENI) 

   - • Use a resource policy to define access 

© Stephane Maarek 

#### ACM – Integration with API Gateway 

- Create a Custom Domain Name in API Gateway 

- Edge-Optimized (default): For global clients 

   - Requests are routed through the CloudFront Edge locations (improves latency) 

**us-east-1** linked certificate CloudFront ACM 

- The API Gateway still lives in only one region 

- The TLS Certificate must be in the same region as CloudFront, in us-east-1 

- Then setup CNAME or (better) A-Alias record in Route 53 



API Gateway **Edge-Optimized** 

- Regional: 

   - For clients within the same region 

   - The TLS Certificate must be imported on API Gateway, in the same region as the API Stage 

   - Then setup CNAME or (better) A-Alias record in Route 53 

**ap-southeast-2** linked certificate API Gateway ACM **Regional** 

© Stephane Maarek 

#### AWS WAF – Web Application Firewall 



- Protects your web applications from common web exploits (Layer 7) • Layer 7 is HTTP (vs Layer 4 is TCP/UDP) 

- Deploy on 

   - Application Load Balancer 

   - API Gateway 

   - CloudFront 

   - AppSync GraphQL API 

   - Cognito User Pool 

© Stephane Maarek 

#### AWS WAF – Web Application Firewall 



- Define Web ACL (Web Access Control List) Rules: 

   - IP Set: up to 10,000 IP addresses – use multiple Rules for more IPs 

   - • HTTP headers, HTTP body, or URI strings Protects from common attack - SQL injection and Cross-Site Scripting (XSS) 

   - Size constraints, geo-match (block countries) 

   - Rate-based rules (to count occurrences of events) – for DDoS protection 

- Web ACL are Regional except for CloudFront 

- A rule group is a reusable set of rules that you can add to a web ACL 

© Stephane Maarek 

#### WAF – Fixed IP while using WAF with a Load Balancer 

- WAF does not support the Network Load Balancer (Layer 4) 

- We can use Global Accelerator for fixed IP and WAF on the ALB 



<!-- Start of picture text -->
us-east-1<br>Application Load<br>Balancer<br>Users<br>EC2 Instances<br>Global Accelerator<br>attached<br>Fixed IPv4: 1.2.3.4<br>WebACL<br>WebACL must be in the same<br>AWS WAF<br>AWS Region as ALB<br><!-- End of picture text -->

© Stephane Maarek 

AWS Shield: protect from DDoS attack 



- DDoS: Distributed Denial of Service – many requests at the same time 

- AWS Shield Standard: 

   - Free service that is activated for every AWS customer 

   - Provides protection from attacks such as SYN/UDP Floods, Reflection attacks and other layer 3/layer 4 attacks 

- AWS Shield Advanced: 

   - Optional DDoS mitigation service ($3,000 per month per organization) 

   - Protect against more sophisticated attack on Amazon EC2, Elastic Load Balancing (ELB), Amazon CloudFront, AWS Global Accelerator, and Route 53 

   - 24/7 access to AWS DDoS response team (DRP) 

   - Protect against higher fees during usage spikes due to DDoS 

• Shield Advanced automatic application layer DDoS mitigation automatically creates, evaluates and deploys AWS WAF rules to mitigate layer 7 attacks © Stephane Maarek IE'”TS Ol ns 

ns 

AWS Firewall Manager 



- Manage rules in all accounts of an AWS Organization 

- Security policy: common set of security rules 

   - WAF rules (Application Load Balancer, API Gateways, CloudFront) 

   - AWS Shield Advanced (ALB, CLB, NLB, Elastic IP, CloudFront) 

   - Security Groups for EC2, Application Load BAlancer and ENI resources in VPC 

   - AWS Network Firewall (VPC Level) 

   - Amazon Route 53 Resolver DNS Firewall 

   - Policies are created at the region level 

- Rules are applied to new resources as they are created (good for compliance) across all and future accounts in your Organization 

© Stephane Maarek IE '”TS Ol 

#### WAF vs. Firewall Manager vs. Shield 







AWS WAF AWS Firewall Manager 

AWS Shield 

- WAF, Shield and Firewall Manager are used together for comprehensive protection 

- Define your Web ACL rules in WAF 

- For granular protection of your resources, WAF alone is the correct choice 

- If you want to use AWS WAF across accounts, accelerate WAF configuration, automate the protection of new resources, use Firewall Manager with AWS WAF 

- Shield Advanced adds additional features on top of AWS WAF, such as dedicated support from the Shield Response Team (SRT) and advanced reporting. 

- If you’re prone to frequent DDoS attacks, consider purchasing Shield Advanced 

© Stephane Maarek 

AWS Best Practices for DDoS Resiliency Edge Location Mitigation (BP1, BP3) 

- BP1 – CloudFront 

   - Web Application delivery at the edge 

   - Protect from DDoS Common Attacks (SYN floods, UDP reflection…) 

- BP1 – Global Accelerator • Access your application from the edge 

   - Integration with Shield for DDoS protection 

   - Helpful if your backend is not compatible with CloudFront 

- BP3 – Route 53 



<!-- Start of picture text -->
BP2 BPI aE} AWS Cloud<br>> > & eaa — ieCy | Region ROOT smeueeenemeeneeOH<br>Users H ' Availability Zone 1 : Availability Zone 2 |<br>i} AWSWAF Amazon CloudFront| |H BPS B vec |' ip ratte stnet |1 Hi Bi Piva sutra i]72§<br>BP 3 BP4 | i 1 4 BP7 Wt<br>; 7 H ' BP6 esjeer an Bn<br>SJ Ue H<br>H } Ce ——+—4 | Auto Scaling group | i} |<br>‘Amazon Route 53 Amazon API Gateway H H ‘18‘ if t "ivi<br>{ ' ! ElasticLoadBalancing =| || i lt<br>i i i<br>aR BE ' || {Instance __tnstance! | |<br>Users AWS Global Accelerator leek ee eel atancemrmensi- seiaseaeanseri arene caer af<br><!-- End of picture text -->

- Domain Name Resolution at the edge 

- DDoS Protection mechanism 

© Stephane Maarek 

#### AWS Best Practices for DDoS Resiliency Best pratices for DDoS mitigation 

- Infrastructure layer defense (BP1, BP3, BP6) 

   - Protect Amazon EC2 against high traffic 

   - That includes using Global Accelerator, Route 53, CloudFront, Elastic Load Balancing 

- Amazon EC2 with Auto Scaling (BP7) 

   - Helps scale in case of sudden traffic surges including a flash crowd or a DDoS attack 

- Elastic Load Balancing (BP6) 

   - Elastic Load Balancing scales with the traffic increases and will distribute the traffic to many EC2 instances 



<!-- Start of picture text -->
BP2 BPI aE} AWS Cloud<br>> > & eaa — ieCy | Region ROOT smeueeenemeeneeOH<br>Users H ' Availability Zone 1 : Availability Zone 2 |<br>i} AWSWAF Amazon CloudFront| |H BPS B vec |' ip ratte stnet |1 Hi Bi Piva sutra i]72§<br>BP 3 BP4 | i 1 4 BP7 Wt<br>; 7 H ' BP6 esjeer an Bn<br>SJ Ue H<br>H } Ce ——+—4 | Auto Scaling group | i} |<br>‘Amazon Route 53 Amazon API Gateway H H ‘18‘ if t "ivi<br>{ ' ! ElasticLoadBalancing =| || i lt<br>i i i<br>aR BE ' || {Instance __tnstance! | |<br>Users AWS Global Accelerator leek ee eel atancemrmensi- seiaseaeanseri arene caer af<br><!-- End of picture text -->

© Stephane Maarek 

#### AWS Best Practices for DDoS Resiliency Application Layer Defense 

- Detect and filter malicious web requests (BP1, BP2) 

   - CloudFront cache static content and serve it from edge locations, protecting your backend 

   - AWS WAF is used on top of CloudFront and Application Load Balancer to filter and block requests based on request signatures 

   - WAF rate-based rules can automatically block the IPs of bad actors 

   - Use managed rules on WAF to block attacks based on IP reputation, or block anonymous Ips 

   - • CloudFront can block specific geographies 

- Shield Advanced (BP1, BP2, BP6) 



<!-- Start of picture text -->
BP2 BPI aE} AWS Cloud<br>> > & eaa — ieCy | Region ROOT smeueeenemeeneeOH<br>Users H ' Availability Zone 1 : Availability Zone 2 |<br>i} AWSWAF Amazon CloudFront| |H BPS B vec |' ip ratte stnet |1 Hi Bi Piva sutra i]72§<br>BP 3 BP4 | i 1 4 BP7 Wt<br>; 7 H ' BP6 esjeer an Bn<br>SJ Ue H<br>H } Ce ——+—4 | Auto Scaling group | i} |<br>‘Amazon Route 53 Amazon API Gateway H H ‘18‘ if t "ivi<br>{ ' ! ElasticLoadBalancing =| || i lt<br>i i i<br>aR BE ' || {Instance __tnstance! | |<br>Users AWS Global Accelerator leek ee eel atancemrmensi- seiaseaeanseri arene caer af<br><!-- End of picture text -->

- Shield Advanced automatic application layer DDoS mitigation automatically creates, evaluates and deploys AWS WAF rules to mitigate layer 7 attacks 

© Stephane Maarek 

#### AWS Best Practices for DDoS Resiliency Attack surface reduction 

- Obfuscating AWS resources (BP1, BP4, BP6) 

   - Using CloudFront, API Gateway, Elastic Load Balancing to hide your backend resources (Lambda functions, EC2 instances) 

- Security groups and Network ACLs (BP5) 

   - Use security groups and NACLs to filter traffic based on specific IP at the subnet or ENI-level 

   - Elastic IP are protected by AWS Shield Advanced 

- Protecting API endpoints (BP4) 

   - Hide EC2, Lambda, elsewhere 

   - Edge-optimized mode, or CloudFront + regional mode (more control for DDoS) 



<!-- Start of picture text -->
BP2 BPI aE} AWS Cloud<br>> > & eaa — ieCy | Region ROOT smeueeenemeeneeOH<br>Users H ' Availability Zone 1 : Availability Zone 2 |<br>i} AWSWAF Amazon CloudFront| |H BPS B vec |' ip ratte stnet |1 Hi Bi Piva sutra i]72§<br>BP 3 BP4 | i 1 4 BP7 Wt<br>; 7 H ' BP6 esjeer an Bn<br>SJ Ue H<br>H } Ce ——+—4 | Auto Scaling group | i} |<br>‘Amazon Route 53 Amazon API Gateway H H ‘18‘ if t "ivi<br>{ ' ! ElasticLoadBalancing =| || i lt<br>i i i<br>aR BE ' || {Instance __tnstance! | |<br>Users AWS Global Accelerator leek ee eel atancemrmensi- seiaseaeanseri arene caer af<br><!-- End of picture text -->

- WAF + API Gateway: burst limits, headers filtering, use API keys 

© Stephane Maarek 

#### Amazon GuardDuty 



- Intelligent Threat discovery to protect your AWS Account 

- Uses Machine Learning algorithms, anomaly detection, 3<sup>rd</sup> party data 

- One click to enable (30 days trial), no need to install software 

- Input data includes: 

   - CloudTrail Events Logs –  unusual API calls, unauthorized deployments 

      - CloudTrail Management Events – create VPC subnet, create trail, … 

      - CloudTrail S3 Data Events – get object, list objects, delete object, … 

   - VPC Flow Logs – unusual internal traffic, unusual IP address 

   - DNS Logs – compromised EC2 instances sending encoded data within DNS queries 

   - Optional Features – EKS Audit Logs, RDS & Aurora, EBS, Lambda, S3 Data Events… 

- Can setup EventBridge rules to be notified in case of findings 

- EventBridge rules can target AWS Lambda or SNS 

• Can protect against CryptoCurrency attacks (has a dedicated “finding” for it) © Stephane Maarek IE'”TS Ol ns 

Amazon GuardDuty **VPC Flow Logs CloudTrail Logs DNS Logs (AWS DNS) SNS GuardDuty** ae eS **Optional Features** ga **S3 Logs EBS Volumes** £@ **EventBridge Lambda** i **Lambda Network RDS & Aurora Activity Login Activity EKS Audit Logs & Runtime Monitoring** 

© Stephane Maarek 

#### Amazon Inspector 

- Automated Security Assessments 

- For EC2 instances 

   - Leveraging the AWS System Manager (SSM) agent 

   - Analyze against unintended network accessibility 

   - Analyze the running OS against known vulnerabilities 

- For Container Images push to Amazon ECR 

   - Assessment of Container Images as they are pushed 

- For Lambda Functions 



<!-- Start of picture text -->
SSM Agent<br>Lambda<br>Function<br>Amazon<br>Inspector<br>Amazon ECR<br>Container Image<br><!-- End of picture text -->

   - Identifies software vulnerabilities in function code and package dependencies 

   - Assessment of functions as they are deployed 

- Reporting & integration with AWS Security Hub 

- Send findings to Amazon Event Bridge 

assessment run state & findings 





Security Hub EventBridge 

© Stephane Maarek 

What does Amazon Inspector evaluate? 



- Remember: only for EC2 instances, Container Images & Lambda functions 

- Continuous scanning of the infrastructure, only when needed 

- Package vulnerabilities (EC2, ECR & Lambda) – database of CVE 

- Network reachability (EC2) 

• A risk score is associated with all vulnerabilities for prioritization © Stephane Maarek IE'”TS Ol ns 

AWS Macie • Amazon Macie is a fully managed data security and data privacy service that uses machine learning and pattern matching to discover and protect your sensitive data in AWS. • Macie helps identify and alert you to sensitive data, such as personally identifiable information (PII) analyze notify integrations S3 Buckets **Macie** Amazon Bo 8 Discover Sensitive Data (PII) EventBridge © Stephane Maarek SE’”Oh es 

### Amazon VPC 

© Stephane Maarek 



<!-- Start of picture text -->
VPC Components Diagram<br>Amazon<br>DynamoDB<br>VPC Flow Logs<br>Region<br>NACL NACL<br>VPC<br>Internet<br>Corporate<br>www Public Subnet Private Subnet Data Center<br>CloudWatch<br>Security Group<br>Internet Router<br>Gateway<br>NAT Gateway<br>Transit Private EC2 Instance S3<br>Gateway<br>Route Route Server<br>VPN Customer<br>Table Security Group Table Security Group VPC Gateway<br>Endpoint<br>S2S VPN<br>Connection<br>DX<br>VPC Peering Public EC2 Instance Private EC2 Instance<br>Connections VPN<br>Gateway<br>Direct Connect<br>Availability Zone Connection<br><!-- End of picture text -->



<!-- Start of picture text -->
DX Location<br><!-- End of picture text -->

© Stephane Maarek 

#### Understanding CIDR – IPv4 

- Classless Inter-Domain Routing – a method for allocating IP addresses 

- • Used in Security Groups rules and AWS networking in general 



<!-- Start of picture text -->
IP version v Type v Protocol v Port range v Source v Description<br>IPv4 SSH TCP 22 122.149.196.85/32 -<br>IPv4 HTTP TCP 80 0.0.0.0/0 -<br><!-- End of picture text -->

- They help to define an IP address range: • We’ve seen WW.XX.YY.ZZ <u>/32</u> => one IP • We’ve seen 0.0.0.0 <u>/0</u> => all IPs • But we can define:192.168.0.0 <u>/26</u> =>192.168.0.0 – 192.168.0.63 (64 IP addresses) 

© Stephane Maarek 

#### Understanding CIDR – IPv4 

- A CIDR consists of two components 

- • Base IP 

• Represents an IP contained in the range (XX.XX.XX.XX) • Example: 10.0.0.0, 192.168.0.0, … 

• Subnet Mask • Defines how many bits can change in the IP • Example: /0, /24, /32 • Can take two forms: 

- /8 ó 255.0.0.0 

- /16 ó 255.255.0.0 

- /24 ó 255.255.255.0 

- /32 ó 255.255.255.255 

© Stephane Maarek 

#### Understanding CIDR – Subnet Mask 

- The Subnet Mask basically allows part of the underlying IP to get additional next values from the base IP 

> <mark>192</mark> . <mark>168</mark> . <mark>0</mark> . <mark>0</mark> **/32 =>** allows for **1** IP (2<sup>!</sup> ) 192.168.0.0 

> <mark>192</mark> . <mark>168</mark> . <mark>0</mark> . <mark>0</mark> **/31 =>** allows for **2** IP (2<sup>"</sup> ) 192.168.0.0 -> 192.168.0.1 Quick Memo 

> <mark>192</mark> . <mark>168</mark> . <mark>0</mark> . <mark>0</mark> **/30 =>** allows for **4** IP (2<sup>#</sup> ) 192.168.0.0 -> 192.168.0.3 

> <mark>192</mark> . <mark>168</mark> . <mark>0</mark> . <mark>0</mark> **/29 =>** allows for **8** IP (2<sup>$</sup> ) 192.168.0.0 -> 192.168.0.7 <u>Octets</u> . ~~.~~ . 

> <mark>192</mark> . <mark>168</mark> . <mark>0</mark> . <mark>0</mark> **/28 =>** allows for **16** IP (2<sup>%</sup> ) 192.168.0.0 -> 192.168.0.15 1<sup>*+</sup> 2<sup>,-</sup> 3<sup>.-</sup> 4<sup>+/</sup> 

> <mark>192</mark> . <mark>168</mark> . <mark>0</mark> . <mark>0</mark> **/27 =>** allows for **32** IP (2<sup>&</sup> ) 192.168.0.0 -> 192.168.0.31 

> <mark>192</mark> . <mark>168</mark> . <mark>0</mark> . <mark>0</mark> **/26 =>** allows for **64** IP (2<sup>'</sup> ) 192.168.0.0 -> 192.168.0.63 • **/32** – no octet can change 

> <mark>192</mark> . <mark>168</mark> . <mark>0</mark> . <mark>0</mark> **/25 =>** allows for **128** IP (2<sup>(</sup> ) 192.168.0.0 -> 192.168.0.127 • **/24** – last octet can change • 

> <mark>192</mark> . <mark>168</mark> . <mark>0</mark> . <mark>0</mark> **/24 =>** allows for **256** IP (2<sup>)</sup> ) 192.168.0.0 -> 192.168.0.255 **/16** – last 2 octets can change • … **/8** – last 3 octets can change • **/0** – all octets can change 

> <mark>192</mark> . <mark>168</mark> . <mark>0</mark> . <mark>0</mark> **/16 =>** allows for **65,536** IP (2<sup>"'</sup> ) 192.168.0.0 -> 192.168.255.255 … 

> <mark>192</mark> . <mark>168</mark> . <mark>0</mark> . <mark>0</mark> **/0 =>** allows for **All IPs** 0.0.0.0 -> 255.255.255.255 

- **/32** – no octet can change 

- • **/24** – last octet can change 

- **/16** – last 2 octets can change 

- **/8** – last 3 octets can change 

- • **/0** – all octets can change 

© Stephane Maarek 

#### Understanding CIDR – Little Exercise 

|•192.168.0.0/24 = …|?|
|---|---|
|• 192.168.0.0 – 192.1|68.0.255 (256 IPs)|
|•192.168.0.0/16 = …|?|
|• 192.168.0.0 – 192.1|68.255.255 (65,536 IPs)|
|•134.56.78.123/32 =|… ?|
|• Just 134.56.78.123||
|•0.0.0.0/0<br>• All IPs!||



• When in doubt, use this website <u>https://www.ipaddressguide.com/cidr</u> 

© Stephane Maarek 

Public vs. Private IP (IPv4) 

- The Internet Assigned Numbers Authority (IANA) established certain blocks of IPv4 addresses for the use of private (LAN) and public (Internet) addresses 

- Private IP can only allow certain values: 

   - 10.0.0.0 – 10.255.255.255  (10.0.0.0/8) ç in big networks 

   - 172.16.0.0 – 172.31.255.255 (172.16.0.0/12) ç AWS default VPC in that range 

   - 192.168.0.0 – 192.168.255.255 (192.168.0.0/16) ç e.g., home networks 

- All the rest of the IP addresses on the Internet are Public 

© Stephane Maarek 

#### Default VPC Walkthrough 

- All new AWS accounts have a default VPC 

- New EC2 instances are launched into the default VPC if no subnet is specified 

- Default VPC has Internet connectivity and all EC2 instances inside it have public IPv4 addresses 

- We also get a public and a private IPv4 DNS names 

© Stephane Maarek 

|VPC in AWS – IPv4|
|---|





- VPC = Virtual Private Cloud 

- You can have multiple VPCs in an AWS region (max. 5 per region – soft limit) 

- • Max. CIDR per VPC is 5, for each CIDR: 

   - Min. size is /28 (16 IP addresses) 

   - Max. size is /16 (65536 IP addresses) 

- Because VPC is private, only the Private IPv4 ranges are allowed: 

   - 10.0.0.0 – 10.255.255.255 (10.0.0.0/8) 

   - 172.16.0.0 – 172.31.255.255 (172.16.0.0/12) 

   - 192.168.0.0 – 192.168.255.255 (192.168.0.0/16) 

• <u>Your VPC CIDR should NOT overlap with your other networks (e.g., corporate)</u> © Stephane Maarek ~~IE~~ '”TS Ol ns 

#### State of Hands-on 





<!-- Start of picture text -->
Region<br>VPC<br><!-- End of picture text -->

© Stephane Maarek 

#### Adding Subnets 



<!-- Start of picture text -->
eee<br>Region<br>poo | Hl<br>i) H<br>H 1<br>H @ VPC ! |<br>|<br>Public Subnet Private Subnet<br>H1<br>l<br>H 1<br>1<br>|<br>i\<br>'<br>i fi |<br>H l:H1'A ||<br>|<br>HlHi1<br>i i ||<br>i fi' |<br>H 1<br>Hl |<br>|<br>H<br>‘<br>: '<br>1 |<br>H |<br>H t<br>i '<br>Hl fi |<br>|<br>Availability Zone<br>H a “vopoppopiseieiioisiisnipnessesessness opener en enenennenennneneeneeneeneeneennnenceeeennnencened<br>NOT FOR DISTRIBUTION © Stephane Maarek www.datacumulus.com<br><!-- End of picture text -->

© Stephane Maarek 

#### VPC – Subnet (IPv4) 



- AWS reserves 5 IP addresses (first 4 & last 1) in each subnet 

- • These 5 IP addresses are not available for use and can’t be assigned to an EC2 instance 

- Example: if CIDR block 10.0.0.0/24, then reserved IP addresses are: • 10.0.0.0 – Network Address 

   - 10.0.0.1 – reserved by AWS for the VPC router 

   - 10.0.0.2 – reserved by AWS for mapping to Amazon-provided DNS 

   - 10.0.0.3 – reserved by AWS for future use 

   - 10.0.0.255 – Network Broadcast Address. AWS does not support broadcast in a VPC, therefore the address is reserved 

- <u>Exam Tip,</u> if you need 29 IP addresses for EC2 instances: • You can’t choose a subnet of size /27 (32 IP addresses, 32 – 5 = 27 < 29) 

   - You need to choose a subnet of size /26 (64 IP addresses, 64 – 5 = 59 > 29) 

© Stephane Maarek 

#### Internet Gateway (IGW) 



<!-- Start of picture text -->
@<br><!-- End of picture text -->

- Allows resources (e.g., EC2 instances) in a VPC connect to the Internet 

- It scales horizontally and is highly available and redundant 

- Must be created separately from a VPC 

- One VPC can only be attached to one IGW and vice versa 

• Internet Gateways on their own do not allow Internet access… • Route tables must also be edited! © Stephane Maarek IE'”TS Ol ns 

#### Adding Internet Gateway 



<!-- Start of picture text -->
Region<br>VPC<br>Public Subnet Private Subnet<br>Internet<br>Gateway<br>Availability Zone<br><!-- End of picture text -->

© Stephane Maarek 

#### Editing Route Tables 



<!-- Start of picture text -->
Region<br>VPC<br>Internet<br>www Public Subnet Private Subnet<br>Internet Router<br>Gateway<br>Route<br>Table Security Group<br>Public EC2 Instance<br>Availability Zone<br><!-- End of picture text -->

© Stephane Maarek 

#### Bastion Hosts 

- We can use a Bastion Host to SSH into our private EC2 instances 

- The bastion is in the public subnet which is then connected to all other private subnets 

- Bastion Host security group must allow inbound from the internet on port 22 from restricted CIDR, for example the <u>public CIDR</u> of your corporation 

- Security Group of the EC2 Instances must allow the Security Group of the Bastion Host, or the private IP of the Bastion host 



<!-- Start of picture text -->
Users<br>SSH<br>VPC<br>Public Subnet<br>Security Group (BastionHost-SG)<br>EC2 Instance<br>(Bastion Host)<br>SSH<br>Private Subnet<br>Security Group (LinuxInstance-SG)<br><!-- End of picture text -->

© Stephane Maarek 

NAT Instance ( outdated , but still at the exam) 

- NAT = Network Address Translation 

- Allows EC2 instances in private subnets to connect to the Internet 

- Must be launched in a public subnet 

- Must disable EC2 setting: Source / destination Check 

- Must have Elastic IP attached to it 

- Route Tables must be configured to route traffic from private subnets to the NAT Instance 



<!-- Start of picture text -->
Server<br>( IP:  50.60.4.10)<br>Src.:  50.60.4.10<br>Dest.:  12.34.56.78<br>VPC Dest.:  50.60.4.10<br>Src.:  12.34.56.78<br>Public Subnet<br>Security Group (NATInstance-SG)<br>EIP<br>( IP:  12.34.56.78) NAT Instance<br>Dest.:  50.60.4.10<br>Src.:  50.60.4.10<br>Src.:  10.0.0.20<br>Dest.:  10.0.0.20<br>Private Subnet<br>IP:  10.0.0.10 IP:  10.0.0.20<br><!-- End of picture text -->

© Stephane Maarek 



<!-- Start of picture text -->
NAT Instance<br>Region<br>VPC<br>Internet<br>www Public Subnet Private Subnet<br>Security Group Security Group<br>Internet Router<br>Gateway<br>EIP<br>NAT Instance Private EC2 Instance<br>Route Route<br>Table Security Group Table<br>Public EC2 Instance<br>Availability Zone<br><!-- End of picture text -->

© Stephane Maarek 

#### NAT Instance – Comments 

- Pre-configured Amazon Linux AMI is available • Reached the end of standard support on December 31, 2020 

- • Not highly available / resilient setup out of the box • You need to create an ASG in multi-AZ + resilient user-data script 

- Internet traffic bandwidth depends on EC2 instance type 

- You must manage Security Groups & rules: • Inbound: 

      - Allow HTTP / HTTPS traffic coming from Private Subnets 

   - Allow SSH from your home network (access is provided through Internet Gateway) 

   - • Outbound: 

      - Allow HTTP / HTTPS traffic to the Internet 

© Stephane Maarek 

ns 

#### NAT Gateway 



- AWS-managed NAT, higher bandwidth, high availability, no administration 

- Pay per hour for usage and bandwidth 

- NATGW is created in a specific Availability Zone, uses an Elastic IP 

- Can’t be used by EC2 instance in the same subnet (only from other subnets) 

- Requires an IGW (Private Subnet => NATGW => IGW) 

- 5 Gbps of bandwidth with automatic scaling up to 100 Gbps 

- No Security Groups to manage / required 

© Stephane Maarek IE '”TS Ol 



<!-- Start of picture text -->
NAT Gateway<br>Region<br>VPC<br>Internet<br>www Public Subnet Private Subnet<br>\_@-@ Security Group oo<br>Internet Router<br>Gateway<br>NAT Gateway<br>Private EC2 Instance<br>Route Route<br>Table Security Group Table<br>Public EC2 Instance<br>Availability Zone<br><!-- End of picture text -->

© Stephane Maarek 



<!-- Start of picture text -->
NAT Gateway with High Availability<br>OD<br>Internet<br>www<br>• NAT Gateway is resilient within<br>Region<br>a single Availability Zone<br>Internet<br>Gateway<br>a VPC<br>• Must create  multiple NAT<br>Router<br>Public Subnet Public Subnet<br>Gateways  in  multiple AZs  for<br>fault-tolerance<br>rac<br>NAT Gateway NAT Gateway<br>• There is no cross-AZ failover  Private Subnet Private Subnet<br>needed because if an AZ goes<br>Lo<br>down it doesn't need NAT EC2 Instance EC2 Instance<br>AZ - A AZ - B<br><!-- End of picture text -->

© Stephane Maarek 

#### NAT Gateway vs. NAT Instance 

||**NAT Gateway**|**NAT Instance**|
|---|---|---|
|**Availability**|Highly available within AZ (create in another AZ)|Use a script to manage failover between instances|
|**Bandwidth**|Up to 100 Gbps|Depends on EC2 instance type|
|**Maintenance**|Managed by AWS|Managed by you (e.g., software, OS patches, …)|
|**Cost**|Per hour & amount of data transferred|Per hour, EC2 instance type and size, + network $|
|**Public IPv4**|||
|**Private IPv4**|||
|**Security Groups**|||
|**Use as Bastion Host?**|||



More at: https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-comparison.html 

© Stephane Maarek 

#### Security Groups & NACLs 



<!-- Start of picture text -->
Incoming Request Outgoing Request<br>Subnet Subnet<br>NACL Inbound SG Inbound Security Group NACL Outbound SG Outbound Security Group<br>Rules  Rules  Rules  Rules<br>2<br>1<br>1 2<br>NACL Outbound NACL Inbound<br>Rules  (Stateless) Outbound Allowed EC2 Instance Rules  (Stateless) Inbound Allowed EC2 Instance<br>(Stateful) (Stateful)<br>3 3<br>NACL NACL<br><!-- End of picture text -->

© Stephane Maarek 

#### Network Access Control List (NACL) 



- NACL are like a firewall which control traffic from and to subnets 

- One NACL per subnet, new subnets are assigned the Default NACL 

- You define NACL Rules: 

   - Rules have a number (1-32766), higher precedence with a lower number 

   - • First rule match will drive the decision 

   - Example: if you define #100 ALLOW 10.0.0.10/32 and #200 DENY 10.0.0.10/32, the IP address will be allowed because 100 has a higher precedence over 200 

   - The last rule is an asterisk (*) and denies a request in case of no rule match 

   - • AWS recommends adding rules by increment of 100 

- Newly created NACLs will deny everything 

- NACL are a great way of blocking a specific IP address at the subnet level 

© Stephane Maarek 



<!-- Start of picture text -->
NACLs<br>Region<br>NACL NACL<br>VPC<br>Internet<br>www Public Subnet Private Subnet<br>Security Group<br>Internet Router<br>Gateway<br>NAT Gateway<br>Private EC2 Instance<br>Route Route<br>Table Security Group Table<br>Public EC2 Instance<br>Availability Zone<br><!-- End of picture text -->

© Stephane Maarek 

#### Default NACL 

• Accepts everything inbound/outbound with the subnets it’s associated with 

• Do NOT modify the Default NACL, instead create custom NACLs 



###### <u>Default NACL for a VPC that supports IPv4</u> 

###### **Inbound Rules** 

|**Rule #**|**Type**|**Protocol**|**Port Range**|**Source**|**Allow/Deny**|
|---|---|---|---|---|---|
|100|All IPv4 Traffic|All|All|0.0.0.0/0|ALLOW|
|*<br>**bound Ru**|All IPv4 Traffic<br>**les**|All|All|0.0.0.0/0|DENY|
|**Rule #**|**Type**|**Protocol**|**Port Range**|**Destination**|**Allow/Deny**|
|100|All IPv4 Traffic|All|All|0.0.0.0/0|ALLOW|
|*|All IPv4 Traffic|All|All|0.0.0.0/0|DENY|



###### **Outbound Rules** 

© Stephane Maarek 

#### Ephemeral Ports 

- For any two endpoints to establish a connection, they must use ports 

- Clients connect to a defined port , and expect a response on an ephemeral port 

- Different Operating Systems use different port ranges, examples: 

   - IANA & MS Windows 10 è 49152 – 65535 



<!-- Start of picture text -->
• Many Linux Kernels è 32768 – 60999<br>Request<br>Src. IP Src. Port Dest. IP  Dest. Port<br>Payload …<br>11.22.33.44 50105 55.66.77.88 443<br>Dest. IP  Dest. Port  Src. IP Src. Port<br>Client Payload … Web Server<br>11.22.33.44 50105 55.66.77.88 443<br>IP:  11.22.33.44 IP:  55.66.77.88<br>Ephemeral Port:  50105 Response Fixed Port:  443<br><!-- End of picture text -->

© Stephane Maarek 

#### NACL with Ephemeral Ports 



<!-- Start of picture text -->
VPC<br>Web Tier Database Tier<br>Web Subnet (Public) DB Subnet (Private)<br>Allow Outbound TCP Allow Inbound TCP<br>On  port 3306 On  port 3306<br>To  DB Subnet CIDR From  Web Subnet CIDR<br>Client<br>Allow Inbound TCP Allow Outbound TCP DB Instance<br>Ephemeral<br>On  port 1024-65535 On  port 1024-65535 Port 3306<br>Port<br>From  DB Subnet CIDR To  Web Subnet CIDR<br>https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html#nacl-ephemeral-ports<br>DB-NACL<br>Web-NACL<br><!-- End of picture text -->

© Stephane Maarek 

#### Create NACL rules for each target subnets CIDR 



<!-- Start of picture text -->
@ VPC<br>Web Tier Database Tier<br>Web Subnet - A (Public) DB Subnet – A (Private)<br>i: = ee ee= eSmeAmazon<br>DB Instance<br>Web Subnet - B (Public) DB Subnet – B (Private)<br>1 : 1 t RDS<br>i: a I<br>DB Instance<br>DB-NACL<br>Web-NACL<br><!-- End of picture text -->

© Stephane Maarek 

#### Security Group vs. NACLs 

**Security Group NACL** Operates at the instance level Operates at the subnet level Supports allow rules only Supports allow rules and deny rules **Stateful:** return traffic is automatically allowed, **Stateless:** return traffic must be explicitly allowed by regardless of any rules rules (think of ephemeral ports) All rules are evaluated before deciding whether to Rules are evaluated in order (lowest to highest) when allow traffic deciding whether to allow traffic, first match wins Applies to an EC2 instance when specified by Automatically applies to all EC2 instances in the someone subnet that it’s associated with NACL Examples: https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html 

© Stephane Maarek 

#### VPC Peering 

- Privately connect two VPCs using AWS’ network 

- Make them behave as if they were in the same network 

- Must not have overlapping CIDRs 

- VPC Peering connection is NOT transitive (must be established for each VPC that need to communicate with one another) 

- • You must update route tables in <u>each</u> ~~=~~ 

- <u>VPC’s subnets to ensure EC2 instances</u> can communicate with each other 





VPC - A 



VPC Peering **(A – B)** 

VPC Peering VPC - B **(A – C)** © & VPC Peering **(B – C)** ® VPC - C 

© Stephane Maarek ~~a~~ 

VPC Peering – Good to know 

- You can create VPC Peering connection between VPCs in different AWS accounts/regions 

- You can reference a security group in a peered VPC (works cross accounts – same region) 



<!-- Start of picture text -->
Type Vv Protocol ¥v Portrange V Source Vv<br>HTTP. TCP 80 sg-04991f9af3473b939 / default<br>HTTP TcP 80 HR  / s5-027a01F7865d4be76<br><!-- End of picture text -->

###### Account ID 

© Stephane Maarek 



<!-- Start of picture text -->
VPC Peering<br>Region<br>NACL NACL<br>VPC<br>Internet<br>www Public Subnet Private Subnet<br>Security Group<br>\__-@~-@y Internet Router '<br>Gateway<br>NAT Gateway<br>Private EC2 Instance<br>Route Route<br>Table Security Group Table<br>VPC Peering Public EC2 Instance<br>Connections<br>Availability Zone<br><!-- End of picture text -->

© Stephane Maarek 



<!-- Start of picture text -->
VPC Endpoints<br>Amazon<br>DynamoDB<br>Region<br>NACL NACL<br>VPC<br>Internet<br>www Public Subnet Private Subnet<br>CloudWatch<br>Security Group<br>Internet Router<br>Gateway<br>NAT Gateway<br>Private EC2 Instance S3<br>Route Route<br>Table Security Group Table VPC<br>Endpoint<br>VPC Peering Public EC2 Instance<br>Connections<br>Availability Zone<br><!-- End of picture text -->

© Stephane Maarek 

#### VPC Endpoints (AWS PrivateLink) 

- Every AWS service is publicly exposed (public URL) 

- VPC Endpoints (powered by AWS PrivateLink) allows you to connect to AWS services using a private network instead of using the public Internet 

- They’re redundant and scale horizontally 

- They remove the need of IGW, NATGW, … to access AWS Services 

- In case of issues: 

   - Check DNS Setting Resolution in your VPC 

   - Check Route Tables 



<!-- Start of picture text -->
Amazon SNS<br>www<br>Region<br>Internet<br>Gateway<br>VPC<br>Public Subnet<br>NAT<br>EC2 Instance<br>Gateway<br>Private Subnet<br>Option 1<br>EC2 Instance<br>Option 2<br>| &<br>VPC Endpoint<br>Amazon SNS<br><!-- End of picture text -->

© Stephane Maarek 

#### Types of Endpoints 

- <u>Interface Endpoints (powered by PrivateLink)</u> 

   - Provisions an ENI (private IP address) as an entry point (must attach a Security Group) 

   - Supports most AWS services 

   - $ per hour + $ per GB of data processed 

- <u>Gateway Endpoints as a</u> 

- • Provisions a gateway and must be used <u>target in a route table (does not use security groups)</u> 

   - Supports both S3 and DynamoDB 

   - Free 



<!-- Start of picture text -->
Region<br>VPC<br>Private Subnet<br>VPC Endpoint<br>(Interface)<br>EC2 Instance<br>ENI (PrivateLink)<br>Amazon SNS<br>Region<br>VPC<br>Private Subnet<br>VPC Endpoint<br>EC2 Instance<br>(Gateway)<br>Amazon<br>Amazon S3 OR<br>DynamoDB<br><!-- End of picture text -->

© Stephane Maarek 

#### Gateway or Interface Endpoint for S3? 

- Gateway is most likely going to be preferred all the time at the exam 

- Cost: free for Gateway, $ for interface endpoint 

- Interface Endpoint is preferred access is required from onpremises (Site to Site VPN or Direct Connect), a different VPC or a different region 



<!-- Start of picture text -->
Users<br>ES<br>AWS Cloud<br>S2S VPN Direct Connect<br>Region<br>VPC<br>Interface<br>In-VPC<br>Endpoint<br>Apps<br>Gateway<br>Endpoint<br>PrivateLink Amazon S3<br><!-- End of picture text -->

© Stephane Maarek 

#### Lambda in VPC accessing DynamoDB 

- DynamoDB is a public service from AWS 

- Option 1: Access from the public internet 

   - Because Lambda is in a VPC, it needs a NAT Gateway in a public subnet and an internet gateway 

- Option 2 (better & free): Access from the private VPC network 

   - Deploy a VPC Gateway endpoint for DynamoDB 





<!-- Start of picture text -->
AWS Cloud<br>Public subnet<br>DynamoDB<br>NAT IGW<br>Private subnet<br>VPC Gateway Endpoint<br>For DynamoDB<br><!-- End of picture text -->

- Change the Route Tables 

© Stephane Maarek 

#### VPC Flow Logs 



• Capture information about IP traffic going into your interfaces: 

   - VPC Flow Logs 

   - Subnet Flow Logs 

   - Elastic Network Interface (ENI) Flow Logs 

- Helps to monitor & troubleshoot connectivity issues 

- Flow logs data can go to S3, CloudWatch Logs, and Kinesis Data Firehose 

• Captures network information from AWS managed interfaces too: ELB, RDS, ElastiCache, Redshift, WorkSpaces, NATGW, Transit Gateway… © Stephane Maarek IE'”TS Ol ns 



<!-- Start of picture text -->
VPC Flow Logs<br>VPC Flow Logs<br>Region<br>NACL NACL<br>VPC<br>Internet<br>www Public Subnet Private Subnet<br>CloudWatch<br>Security Group<br>Internet Router<br>Gateway<br>NAT Gateway<br>Amazon<br>Private EC2 Instance S3<br>DynamoDB<br>Route Route<br>Table Security Group Table VPC<br>Endpoint<br>VPC Peering Public EC2 Instance<br>Connections<br>Availability Zone<br><!-- End of picture text -->

© Stephane Maarek 

#### VPC Flow Logs Syntax 

**version interface-id dstaddr dstport packets start action** 2 123456789010 eni-1235b8ca123456789 172.31.16.139 172.31.16.21 20641 22 6 20 4249 1418530010 1418530070 ACCEPT OK 2 123456789010 eni-1235b8ca123456789 172.31.9.69 172.31.9.12 49761 3389 6 20 4249 1418530010 1418530070 REJECT OK **account-id srcaddr srcport protocol bytes end log-status** 

- srcaddr & dstaddr – help identify problematic IP 

- • srcport & dstport – help identity problematic ports • Action – success or failure of the request due to Security Group / NACL • Can be used for analytics on usage patterns, or malicious behavior • Query VPC flow logs using Athena on S3 or CloudWatch Logs Insights • Flow Logs examples: <u>https://docs.aws.amazon.com/vpc/latest/userguide/flow-logsrecords-examples.html</u> 

© Stephane Maarek 

###### VPC Flow Logs – Troubleshoot SG & NACL issues 

###### <u>Look at the</u> **“ACTION”** <u>field</u> 

###### Incoming Requests Outgoing Requests 



<!-- Start of picture text -->
• Inbound REJECT => NACL or SG<br>• Inbound ACCEPT, Outbound REJECT =><br>NACL<br>Subnet<br>NACL Inbound SG Inbound<br>Security Group<br>Rules  Rules<br>NACL Outbound<br>Outbound Allowed<br>Rules  (Stateless) EC2 Instance<br>(Stateful)<br>NACL<br><!-- End of picture text -->



<!-- Start of picture text -->
• Outbound REJECT => NACL or SG<br>• Outbound ACCEPT, Inbound REJECT =><br>NACL<br>Subnet<br>NACL Outbound SG Outbound<br>Security Group<br>Rules  Rules<br>NACL Inbound<br>Inbound Allowed<br>Rules  (Stateless) (Stateful) EC2 Instance<br>NACL<br><!-- End of picture text -->

© Stephane Maarek 

VPC Flow Logs – Architectures Top-10 IP addresses @ 2»&— **CloudWatch VPC Flow Logs CloudWatch Logs Contributor Insights Metric Filter** Alert SSH, RDP… @ »” pi* B **VPC Flow Logs CloudWatch Logs CW Alarm Amazon SNS** ® s B @ **Amazon Amazon VPC Flow Logs S3 Bucket Athena QuickSight** SE ’”- Oh es 

© Stephane Maarek SE 



<!-- Start of picture text -->
AWS Site-to-Site VPN<br>VPC Flow Logs<br>Region<br>NACL NACL<br>VPC<br>Internet<br>Corporate<br>www Public Subnet Private Subnet Data Center<br>CloudWatch<br>Security Group<br>Internet Router<br>Gateway<br>Amazon NAT Gateway<br>DynamoDB Private EC2 Instance S3<br>Route Route Server<br>Customer<br>Table Security Group Table Security Group VPC Gateway<br>Endpoints<br>S2S VPN<br>Connection<br>VPC Peering Public EC2 Instance Private EC2 Instance<br>Connections VPN<br>Gateway<br>Availability Zone<br><!-- End of picture text -->

© Stephane Maarek 

#### AWS Site-to-Site VPN 



- Virtual Private Gateway (VGW) 

   - VPN concentrator on the AWS side of the VPN connection 

   - VGW is created and attached to the VPC from which you want to create the Site-to-Site VPN connection 

   - Possibility to customize the ASN (Autonomous System Number) 

- Customer Gateway (CGW) 

   - Software application or physical device on customer side of the VPN connection 

   - • <u>https://docs.aws.amazon.com/vpn/latest/s2svpn/your-cgw.html#DevicesTested</u> 

© Stephane Maarek IE '”TS Ol 

ns 

#### Site-to-Site VPN Connections 



<!-- Start of picture text -->
Route Table<br>Site-to-Site VPN Connections<br>(Route Propagation enabled)<br>VPC<br>Private Subnet<br>Security Group<br>• Customer Gateway Device (On-premises)<br>• What IP address to use?<br>• Public Internet-routable IP address for your Customer<br>Gateway device<br>Virtual Private<br>• If it’s behind a NAT device that’s enabled for NAT<br>Gateway<br>traversal (NAT-T), use the public IP address of the NAT<br>device<br>• Important step: enable  Route Propagation  for  OR Customer<br>Gateway<br>the Virtual Private Gateway in the route table<br>that is associated with your subnets (Public IP)<br>NAT Device<br>• If you need to ping your EC2 instances from  (Public IP)<br>Corporate Data Center<br>on-premises, make sure you add the ICMP<br>protocol on the inbound of your security<br>Customer<br>groups<br>Gateway<br>(Private IP)<br>Server<br><!-- End of picture text -->

© Stephane Maarek 

#### AWS VPN CloudHub 

- Provide secure communication between multiple sites, if you have multiple VPN connections 

- Low-cost hub-and-spoke model for primary or secondary network connectivity between different locations (VPN only) 

- It’s a VPN connection so it goes over the public Internet 

- To set it up, connect multiple VPN connections on the same VGW, setup dynamic routing and configure route tables 



<!-- Start of picture text -->
VPC Customer Network<br>Availability Zone<br>Customer<br>Private Subnet 1<br>Gateway<br>Customer Network<br>EC2 Instances<br>Availability Zone Virtual Customer<br>Gateway<br>Private<br>Private Subnet 2<br>Gateway<br>(VGW)<br>Customer Network<br>EC2 Instances<br>Customer<br>Gateway<br>NOT FOR DISTRIBUTION © Stephane Maarek www.datacumulus.com<br><!-- End of picture text -->

© Stephane Maarek 

#### Direct Connect (DX) 



- Provides a dedicated <u>private</u> connection from a remote network to your VPC 

- Dedicated connection must be setup between your DC and AWS Direct Connect locations 

- You need to setup a Virtual Private Gateway on your VPC 

- Access public resources (S3) and private (EC2) on same connection 

- Use Cases: 

   - Increase bandwidth throughput - working with large data sets – lower cost 

   - More consistent network experience - applications using real-time data feeds 

   - Hybrid Environments (on prem + cloud) 

- Supports both IPv4 and IPv6 

© Stephane Maarek IE '”TS Ol 

ns 



<!-- Start of picture text -->
Direct Connect Diagram<br>Region<br>(us-east-1)<br>VPC Corporate<br>data center<br>Private Subnet<br>VLAN 1<br>VLAN 2<br>Virtual Private Gateway AWS Direct Customer or Customer<br>Connect Endpoint partner router router/firewall<br>EC2 Instances<br>Customer or<br>AWS Cage partner cage<br>AWS Direct Connect Location Customer Network<br>Amazon Glacier Amazon S3<br>as Private virtual interface<br>Public virtual interface<br><!-- End of picture text -->

© Stephane Maarek 

#### Direct Connect Gateway 

- If you want to setup a Direct Connect to one or more VPC in many different regions (same account), you must use a Direct Connect Gateway 



<!-- Start of picture text -->
Region Region<br>(us-east-1) (us-west-1)<br>VPC VPC<br>Customer network<br>10.0.0.0/16 172.16.0.0/16<br>Private virtual<br>Private virtual<br>interface<br>interface<br>Private virtual AWS Direct<br>interface Connect<br>connection<br>Direct Connect Gateway<br><!-- End of picture text -->

© Stephane Maarek 

#### Direct Connect – Connection Types 

- Dedicated Connections: 1Gbps,10 Gbps and 100 Gbps capacity 

   - Physical ethernet port dedicated to a customer 

   - Request made to AWS first, then completed by AWS Direct Connect Partners 

- Hosted Connections: 50Mbps, 500 Mbps, to 10 Gbps 

   - Connection requests are made via AWS Direct Connect Partners 

   - Capacity can be added or removed on demand 

   - 1, 2, 5, 10 Gbps available at select AWS Direct Connect Partners 

- Lead times are often longer than 1 month to establish a new connection 

© Stephane Maarek 

#### Direct Connect – Encryption 



<!-- Start of picture text -->
Region<br>but is<br>• Data in transit is not encrypted (us-east-1)<br>VPC<br>private<br>Availability Zone<br>Corporate<br>(us-east-1a)<br>data center<br>• AWS Direct Connect + VPN  Private Subnet 1<br>provides an IPsec-encrypted private  Client Client<br>connection<br>EC2 Instances<br>Availability Zone<br>(us-east-1b) AWS Direct VPN  Customer<br>• Good for an extra level of security,  Connect Endpoint Connection router/firewall<br>but slightly more complex to put in  Private Subnet 2<br>AWS Direct<br>place<br>Connect Location Customer Network<br>EC2 Instances<br><!-- End of picture text -->

© Stephane Maarek 

#### Direct Connect - Resiliency 





<!-- Start of picture text -->
High Resiliency for Critical Workloads Maximum Resiliency for Critical Workloads<br>Corporate Corporate<br>data center data center<br>Region Region<br>AWS Direct<br>Connect Location - 1 AWS Direct<br>Connect Location - 1<br>Corporate<br>Corporate<br>data center<br>data center<br>AWS Direct<br>Connect Location - 2<br>AWS Direct<br>Connect Location - 2<br><!-- End of picture text -->

One connection at multiple locations 

Maximum resilience is achieved by separate connections terminating on separate devices in more than one location. 

© Stephane Maarek 

#### Site-to-Site VPN connection as a backup 

- In case Direct Connect fails, you can set up a backup Direct Connect connection (expensive), or a Site-to-Site VPN connection 



<!-- Start of picture text -->
AWS Cloud<br>Direct Connect<br>Primary Connection<br>VPC<br>Site-to-Site VPN<br>Corporate DC<br>Backup Connection<br><!-- End of picture text -->

© Stephane Maarek 



<!-- Start of picture text -->
Network topologies can become complicated<br>VPC Peering<br>VPN Connection Connection<br>Bi ®<br>Customer Gateway Amazon VPC Amazon VPC<br>VPC Peering<br>Connection<br>VPN Connection<br>VPC Peering VPC Peering<br>@ Connection Q © Connection<br>Direct Connect<br>Gateway<br>i 3S<br>VPN Connection VPC Peering<br>Amazon VPC Connection Amazon VPC<br><!-- End of picture text -->

© Stephane Maarek 

#### Transit Gateway 

- For having transitive peering between thousands of VPC and on-premises, hub-and-spoke (star) connection 

- Regional resource, can work cross-region 

- Share cross-account using Resource Access Manager (RAM) 

- You can peer Transit Gateways across regions 

- Route Tables: limit which VPC can talk with other VPC 

- Works with Direct Connect Gateway, VPN connections 

- Supports IP Multicast (not supported by any other AWS service) 





AWS Direct Connect Gateway 





Amazon VPC Amazon VPC **Transit Gateway** Amazon VPC Amazon VPC inal VPN Connection Customer Gateway ns® 

© Stephane Maarek IE '”~=S hl 

#### Transit Gateway: Site-to-Site VPN ECMP 

- ECMP = Equal-cost multi-path routing 



<!-- Start of picture text -->
routing VPC<br>• Routing strategy to allow to<br>Corporate data center<br>172.16.0.0/16<br>forward a packet over multiple  VPC<br>VPN attachment<br>best path<br>• Use case: create multiple Site- VPC<br>to-Site VPN connections  to<br>AWS Transit Gateway<br>increase the bandwidth of<br>VPC<br>your connection to AWS<br>VPC attachment<br>VPC attachment<br>VPC attachment<br>VPC attachment<br><!-- End of picture text -->

© Stephane Maarek 

#### Transit Gateway: throughput with ECMP 



VPN to transit gateway VPN to virtual private gateway 



<!-- Start of picture text -->
VPC VPC<br>1x = 1x 1x = 1x VPC<br>VPC<br>VPC<br>1x = 1.25 Gbps 1x = 2.5 Gbps (ECMP) – 2 tunnels used<br>=<br>2x iia} 5.0 Gbps (ECMP)<br>=<br>3x 7.5 Gbps (ECMP)<br>VPN connection<br>(2 tunnels)<br>+$$ per GB of TGW<br>processed data<br><!-- End of picture text -->

© Stephane Maarek 

#### Transit Gateway – Share Direct Connect between multiple accounts 



<!-- Start of picture text -->
AWS Cloud<br>Corporate<br>Region data center<br>Account 1<br>Clients Clients<br>VPC<br>Transit VIF VLAN<br>Transit Direct ——e— AWS Direct Customer  ®<br>Gateway Connect Connect endpoint router/firewall<br>Account 2<br>Gateway<br>VPC<br>AWS Direct Servers<br>Connect Location<br>You can use AWS Resource Access Manager to share Transit<br>Gateway with other accounts.<br><!-- End of picture text -->

© Stephane Maarek 

#### VPC – Traffic Mirroring 

- Allows you to capture and inspect network traffic in your VPC 

- Route the traffic to security appliances that you manage 

- Capture the traffic 

   - From (Source) – ENIs 

   - To (Targets) – an ENI or a Network Load Balancer 

- Capture all packets or capture the packets of your interest (optionally, truncate packets) 

- • Source and Target can be in the same VPC or different VPCs (VPC Peering) 

- Use cases: content inspection, threat monitoring, troubleshooting, … 

Source B 

Source A Source B fi ~~a~~ 

Inbound & Inbound & Outbound traffic Outbound traffic 



**Traffic Mirroring** (filter traffic, optional) 

Network Load Balancer Auto Scaling group 







EC2 instances with Security Appliances <mark>as</mark> 

© Stephane Maarek I 

#### What is IPv6? 

- IPv4 designed to provide 4.3 Billion addresses (they’ll be exhausted soon) 

- IPv6 is the successor of IPv4 

- IPv6 is designed to provide 3.4 × 10<sup>,-</sup> unique IP addresses 

- Every IPv6 address in AWS is public and Internet-routable (no private range) 

- Format è x.x.x.x.x.x.x.x ( <u>x</u> is hexadecimal, range can be from 0000 to ffff) 

- Examples: 

   - 2001:db8:3333:4444:5555:6666:7777:8888 

   - 2001:db8:3333:4444:cccc:dddd:eeee:ffff 

   - :: è all 8 segments are zero 

   - 2001:db8:: è the last 6 segments are zero 

   - ::1234:5678 è the first 6 segments are zero 

   - 2001:db8::1234:5678 è the middle 4 segments are zero 

© Stephane Maarek 

#### IPv6 in VPC 

Internet OD • <u>IPv4 cannot be disabled for your VPC and subnets</u> • You can enable IPv6 (they’re public IP addresses) Internet to operate in dual-stack mode VPC Gateway IPv4 & IPv6 • Your EC2 instances will get at least a private internal IPv4 and a public IPv6 ; • They can communicate using either IPv4 or IPv6 EC2 Instance to the internet through an Internet Gateway ( **Private IP:** 10.0.0.5) ( **IPv6:** _2001:db8::ff00:42:8329)_ © Stephane Maarek IE'”TS Ol ns 

ns 

#### IPv6 Troubleshooting 

User 

- <u>IPv4 cannot be disabled for your VPC and subnets</u> 



<!-- Start of picture text -->
A<br><!-- End of picture text -->

create 

- So, if you cannot launch an EC2 instance in your subnet 

VPC • It’s not because it cannot acquire an IPv6 (IPv4: 192.168.0.0/24) (IPv4: 10.0.0.0/24) (the space is very large) (IPv6: 2001:db8:1234:5678::/56) • It’s because there are no available IPv4 in … your subnet 192.168.0.10 192.168.0.15 <u>Solution:</u> create a new IPv4 CIDR in your subnet 10.0.0.35 

- <u>Solution:</u> create a new IPv4 CIDR in your subnet 

© Stephane Maarek IE '”TS Ol 

#### Egress-only Internet Gateway 



<!-- Start of picture text -->
@)<br><!-- End of picture text -->

• <u>Used for IPv6 only</u> • (similar to a NAT Gateway but for IPv6) (similar to a NAT Gateway but for IPv6) • Allows instances in your VPC outbound  Allows instances in your VPC outbound connections over IPv6 while preventing the internet to initiate an IPv6 connection to your instances 

Internet • (similar to a NAT Gateway but for IPv6) (similar to a NAT Gateway but for IPv6) can’t initiate initiate connections connections from from both sides Internet • Allows instances in your VPC outbound  Allows instances in your VPC outbound connections over IPv6 while preventing VPC the internet to initiate an IPv6 connection Internet Egress-only Gateway Internet Gateway to your instances **Public Subnet** Private Subnet • You must update the Route Tables **IPv6:** 2001:db8::b1c2 **IPv6:** 2001:db8::e1c3 © Stephane Maarek I'”~”~=— Ol <mark>E</mark> as 

#### IPv6 Routing 



<!-- Start of picture text -->
Route Table<br>(Public Subnet)<br>Region<br>Destination Target<br>10.0.0.0/16 local<br>VPC 2001:db8:1234:1a00::/56 local<br>( IPv4:  10.0.0.0/16) NAT Gateway<br>0.0.0.0/0 igw-id<br>( IPv6:  2001:db8:1234:1a00::/56) (IPv4)<br>Public Subnet ::/0 igw-id<br>( IPv4:  10.0.0.0/24) EIP:  198.51.100.1<br>( IPv6:  2001:db8:1234:1a00::/64)<br>Internet<br>Private IPv4:  10.0.0.5<br>EIP:  198.51.100.1 Gateway Internet<br>IPv6:  2001:db8:1234:1a00::123 Web server (IPv4 & IPv6)<br>Private Subnet<br>Route Table<br>( IPv4:  10.0.1.0/24)<br>( IPv6:  2001:db8:1234:1a02::/64) Egress-only (Private Subnet)<br>Private IPv4:  10.0.1.5 Internet Gateway Destination Target<br>IPv6:  2001:db8:1234:1a02::456 (IPv6)<br>10.0.0.0/16 local<br>Server<br>2001:db8:1234:1a00::/56 local<br>0.0.0.0/0 nat-gateway-id<br>::/0 eigw-id<br><!-- End of picture text -->

© Stephane Maarek 

#### VPC Section Summary (1/3) 

- CIDR – IP Range 

- VPC – Virtual Private Cloud => we define a list of IPv4 & IPv6 CIDR 

- Subnets – tied to an AZ, we define a CIDR 

- Internet Gateway – at the VPC level, provide IPv4 & IPv6 Internet Access 

- Route Tables – must be edited to add routes from subnets to the IGW, VPC Peering Connections, VPC Endpoints, … 

- Bastion Host – public EC2 instance to SSH into, that has SSH connectivity to EC2 instances in private subnets 

- NAT Instances – gives Internet access to EC2 instances in private subnets. Old, must be setup in a public subnet, disable Source / Destination check flag 

- NAT Gateway – managed by AWS, provides scalable Internet access to private EC2 instances, when the target is an IPv4 address 

© Stephane Maarek 

#### VPC Section Summary (2/3) 

- NACL – stateless, subnet rules for inbound and outbound, don’t forget Ephemeral Ports 

- Security Groups – stateful, operate at the EC2 instance level 

- VPC Peering – connect two VPCs with non overlapping CIDR, non-transitive 

- VPC Endpoints – provide private access to AWS Services (S3, DynamoDB, CloudFormation, SSM) within a VPC 

- VPC Flow Logs – can be setup at the VPC / Subnet / ENI Level, for ACCEPT and REJECT traffic, helps identifying attacks, analyze using Athena or CloudWatch Logs Insights 

- Site-to-Site VPN – setup a Customer Gateway on DC, a Virtual Private Gateway on VPC, and site-to-site VPN over public Internet 

- AWS VPN CloudHub – hub-and-spoke VPN model to connect your sites 

© Stephane Maarek 

#### VPC Section Summary (3/3) 

- Direct Connect – setup a Virtual Private Gateway on VPC, and establish a direct private connection to an AWS Direct Connect Location 

- Direct Connect Gateway – setup a Direct Connect to many VPCs in different AWS regions 

- AWS PrivateLink / VPC Endpoint Services: 

   - Connect services privately from your service VPC to customers VPC 

   - Doesn’t need VPC Peering, public Internet, NAT Gateway, Route Tables 

   - Must be used with Network Load Balancer & ENI 

- ClassicLink – connect EC2-Classic EC2 instances privately to your VPC 

- Transit Gateway – transitive peering connections for VPC, VPN & DX 

- Traffic Mirroring – copy network traffic from ENIs for further analysis 

- Egress-only Internet Gateway – like a NAT Gateway, but for IPv6 targets 

© Stephane Maarek 

#### Networking Costs in AWS per GB - Simplified 



<!-- Start of picture text -->
Region Region<br>• Use Private IP<br>Availability Zone Availability Zone Availability Zone<br>instead of Public<br>IP for good<br>savings and<br>Free  if using  better network<br>private IP<br>9 Free  for traffic in<br>$0.01  if  $0.02 performance<br>Using private IP Inter-region<br>• Use same AZ for<br>maximum savings<br>(at the cost of<br>og $0.02  if using je<br>Public IP / Elastic IP high availability)<br>© Stephane Maarek<br>EES es<br>NOT FOR DISTRIBUTION © Stephane Maarek www.datacumulus.com<br><!-- End of picture text -->

© Stephane Maarek EES 

#### Minimizing egress traffic network cost 

- <u>Egress traffic: outbound</u> traffic (from AWS to outside) 

- <u>Ingress traffic: inbound</u> traffic - from outside to AWS (typically free) 

- Try to keep as much internet traffic within AWS to minimize costs 

- Direct Connect location that are co-located in the same AWS Region result in lower cost for egress network 

**Egress cost is high** 



<!-- Start of picture text -->
AWS Cloud Corporate data center<br>DB Query<br>Query Results<br>100 MB<br>50 KB<br>Database Application<br><!-- End of picture text -->

**Egress cost is minimized** 



<!-- Start of picture text -->
AWS Cloud Corporate data center<br>Query Results<br>DB Query<br>50 KB<br>100 MB<br>Database Application<br><!-- End of picture text -->



© Stephane Maarek 

S3 Data Transfer Pricing – Analysis for USA S3 ingress: free internet S3 to Internet: $0.09 per GB S3 Transfer Acceleration: $0.09 • Faster transfer times (50 to 500% better) - • Additional cost on top of Data Transfer Transfer acceleration +$0.04 Pricing: +$0.04 to $0.08 per GB S3 to CloudFront: $0.00 per GB Edge location CloudFront to Internet: $0.085 per GB (slightly cheaper than S3) $0.00 • Caching capability (lower latency) • Reduce costs associated with S3 Requests Replication $0.02 $0.085 Pricing (7x cheaper with CloudFront) S3 Cross Region Replication: $0.02 per GB <>PeAD CloudFront '”TS Ol ns 

- S3 ingress: free internet 

- • S3 to Internet: $0.09 per GB • S3 Transfer Acceleration: $0.09 

- - 

- S3 to CloudFront: $0.00 per GB 

- CloudFront to Internet: $0.085 per GB (slightly cheaper than S3) $0.00 

- S3 Cross Region Replication: $0.02 per GB 

ns 

© Stephane Maarek IE '”TS Ol 

#### Pricing: NAT Gateway vs Gateway VPC Endpoint 



<!-- Start of picture text -->
Subnet 1 route table<br>Destination Target<br>10.0.0.0/16 Local<br>0.0.0.0/0 igw-id<br><!-- End of picture text -->



<!-- Start of picture text -->
Subnet 2 route table<br>Destination Target<br>10.0.0.0/16 Local<br>pl-id for  vpce-id<br>Amazon S3<br><!-- End of picture text -->



<!-- Start of picture text -->
Region<br>(us-east-1)<br>VPC $0.045 NAT Gateway / hour<br>(10.0.0.0/16) $0.045 NAT Gateway data processed / GB<br>$0.09 Data transfer out to S3 (cross-region)<br>Private subnet 1 Public subnet<br>$0.00 Data transfer out to S3 (same-region)<br>(10.0.0.0/24)<br>Internet<br>EC2 Instance NAT Gateway<br>Internet<br>Gateway<br>Private subnet 2<br>(10.0.1.0/24)<br>No cost for using Gateway Endpoint.<br>$0.01 Data transfer in/out (same-<br>EC2 Instance VPC Endpoint S3 Bucket region)<br><!-- End of picture text -->

© Stephane Maarek 

#### Network Protection on AWS 

- To protect network on AWS, we’ve seen • Network Access Control Lists (NACLs) • Amazon VPC security groups • AWS WAF (protect against malicious requests) • AWS Shield & AWS Shield Advanced • AWS Firewall Manager (to manage them across accounts) 

- But what if we want to protect in a sophisticated way our entire VPC? 

© Stephane Maarek 

#### AWS Network Firewall 

- internet 

- • Protect your entire Amazon VPC OD **AWS Network Firewall** 

- | 

- • From Layer 3 to Layer 7 protection • Any direction, you can inspect • VPC to VPC traffic VPC Direct Connect 

- • Outbound to internet • Inbound from internet Private subnet • To / from Direct Connect & Site-to-Site VPN | Corporate DC 

- • Internally, the AWS Network Firewall uses VPN connection the AWS Gateway Load Balancer <mark>_|</mark> ° 

- • Rules can be centrally managed crossaccount by AWS Firewall Manager to apply to many VPCs Peered VPC 

© Stephane Maarek 

#### Network Firewall – Fine Grained Controls 



- Supports 1000s of rules 

   - IP & port - example: 10,000s of IPs filtering 

   - Protocol – example: block the SMB protocol for outbound communications 

   - Stateful domain list rule groups: only allow outbound traffic to *.mycorp.com or third-party software repo 

   - General pattern matching using regex 

- Traffic filtering: Allow, drop, or alert for the traffic that matches the rules 

• Active flow inspection to protect against network threats with intrusionprevention capabilities (like Gateway Load Balancer, but all managed by AWS) • Send logs of rule matches to Amazon S3, CloudWatch Logs, Kinesis Data Firehose © Stephane Maarek IE'”TS Ol ns 

### Disaster Recovery & Migrations 

© Stephane Maarek 

#### Disaster Recovery Overview 

- Any event that has a negative impact on a company’s business continuity or finances is a disaster 

- Disaster recovery (DR) is about preparing for and recovering from a disaster 

- What kind of disaster recovery? 

   - On-premise => On-premise: traditional DR, and very expensive 

   - On-premise => AWS Cloud: hybrid recovery 

   - AWS Cloud Region A => AWS Cloud Region B 

- Need to define two terms: 

   - RPO: Recovery Point Objective 

   - RTO: Recovery Time Objective 

© Stephane Maarek 



<!-- Start of picture text -->
RPO and RTO<br>Data loss Downtime<br>RPO RTO<br>Disaster<br><!-- End of picture text -->

© Stephane Maarek 

- Disaster Recovery Strategies • Backup and Restore • Pilot Light • Warm Standby • Hot Site / Multi Site Approach 

###### **Faster RTO** 



© Stephane Maarek 



<!-- Start of picture text -->
Backup and Restore (High RPO)<br>Corporate data  AWS Cloud AWS Cloud<br>center us LE<br>Amazon EC2<br>AWS Storage Gateway Amazon S3<br>OF oo<br>AWS Snowball<br>Glacier<br>AMI<br>AWS Cloud<br>Scheduled regular<br>EBS<br>snapshots<br>Redshift<br>o<br>Amazon RDS<br>Snapshot<br>RDS<br>lifecycle<br><!-- End of picture text -->

© Stephane Maarek 

#### Disaster Recovery – Pilot Light 

- A small version of the app is always running in the cloud 

- Useful for the critical core (pilot light) 

- Very similar to Backup and Restore 

- Faster than Backup and Restore as critical systems are already up 





<!-- Start of picture text -->
AWS Cloud<br>Corporate data<br>Route 53<br>center<br>EC2 (not running)<br>5 Data Replication<br>RDS (running)<br><!-- End of picture text -->

© Stephane Maarek 

#### Warm Standby 

- Full system is up and running, but at minimum size 

- Upon disaster, we can scale to production load 



<!-- Start of picture text -->
Corporate data  AWS Cloud<br>center<br>Route 53<br>Reverse<br> proxy<br>ELB<br>App<br>Server<br>EC2 Auto Scaling failover<br>(minimum)<br>Master Data Replication<br>DB<br>RDS Slave (running)<br><!-- End of picture text -->

© Stephane Maarek IE '”TS Ol 

ns 

ns 

#### Multi Site / Hot Site Approach 

- Very low RTO (minutes or seconds) – very expensive • Full Production Scale is running AWS and On Premise 



<!-- Start of picture text -->
Corporate data  AWS Cloud<br>active active<br>center<br>Route 53<br>Reverse<br> proxy<br>ELB<br>F :<br>App<br>Server<br>EC2 Auto Scaling failover<br>(production)<br>Master Data Replication<br>DB<br>RDS Slave (running)<br><!-- End of picture text -->

© Stephane Maarek IE '”TS Ol 

#### All AWS Multi Region 



<!-- Start of picture text -->
aws= AWS Cloud active active aws= AWS Cloud<br>Route 53<br>ELB ELB<br>EC2 Auto Scaling EC2 Auto Scaling failover<br>(production)<br>(production)<br>Data Replication<br>gi oo<br>Aurora Global (slave)<br>Aurora Global (master)<br><!-- End of picture text -->

© Stephane Maarek 

|Disaster Recovery Tips|
|---|
|•<br>Backup<br>•<br>EBS Snapshots, RDS automated backups / Snapshots, etc…<br>•<br>Regular pushes to S3 / S3 IA / Glacier, Lifecycle Policy, Cross Region Replication<br>•<br>From On-Premise: Snowball or Storage Gateway<br>•<br>High Availability<br>•<br>Use Route53 to migrate DNS over from Region to Region<br>•<br>RDS Multi-AZ, ElastiCache Multi-AZ, EFS, S3<br>•<br>Site to Site VPN as a recovery from Direct Connect<br>•<br>Replication<br>•<br>RDS Replication (Cross Region), AWS Aurora + Global Databases<br>•<br>Database replication from on-premises to RDS<br>•<br>Storage Gateway|
|•<br>Automation<br>•<br>CloudFormation / Elastic Beanstalk to re-create a whole new environment<br>•<br>Recover / Reboot EC2 instances with CloudWatch if alarms fail<br>•<br>AWS Lambda functions for customized automations|
|•<br>Chaos<br>•<br>Netflix has a “simian-army” randomly terminating EC2|



© Stephane Maarek 

DMS – Database Migration Service 

- Quickly and securely migrate databases to AWS, resilient, self healing 

- • The source database remains available during the migration 



<!-- Start of picture text -->
D<br><!-- End of picture text -->



- Supports: 

   - Homogeneous migrations: ex Oracle to Oracle 

• Heterogeneous migrations: ex Microsoft SQL Server to Aurora 



<!-- Start of picture text -->
-<br><!-- End of picture text -->

- Continuous Data Replication using CDC 

- You must create an EC2 instance to perform the replication tasks 



Source DB 

EC2 instance Running DMS 

Target DB 

© Stephane Maarek IE '”TS Ol 

#### DMS Sources and Targets 

###### <u>SOURCES:</u> 

###### <u>TARGETS:</u> 

- On-Premises and EC2 instances databases: _Oracle, MS SQL Server, MySQL, MariaDB, PostgreSQL, MongoDB, SAP, DB2_ 

- Azure: _Azure SQL Database_ • Amazon RDS: all including Aurora 

- Amazon S3 

- DocumentDB 

- On-Premises and EC2 instances databases: Oracle, MS SQL Server, MySQL, MariaDB, PostgreSQL, SAP 

- • Amazon RDS 

- Redshift, DynamoDB, S3 

- • OpenSearch Service • Kinesis Data Streams • Apache Kafka • DocumentDB & Amazon Neptune • Redis & Babelfish 

© Stephane Maarek 

#### AWS Schema Conversion Tool (SCT) 

- Convert your Database’s Schema from one engine to another 

- Example OLTP: (SQL Server or Oracle) to MySQL, PostgreSQL, Aurora 

- Example OLAP: (Teradata or Oracle) to Amazon Redshift 

- Prefer compute-intensive instances to optimize data conversions 





**Source DB DMS + SCT** 



**Target DB (different engine)** 

• You do not need to use SCT if you are migrating the same DB engine • Ex: On-Premise PostgreSQL => RDS PostgreSQL • The DB engine is still PostgreSQL (RDS is the platform) © Stephane Maarek IE'”TS Ol ns 

|DMS - Continuous Replication<br>Corporate data center<br>VPC<br>Region<br>Public Subnet<br>Data migration<br>e<br>5<br>f<br>|Private Subnet<br>l<br>p<br>|**NOT FOR DISTRIBUTION © Stephane**<br>|
|---|---|---|
|Oracle DB<br>(source)<br>AWS DMS<br>Replication<br>Instance<br>Full load +<br>CDC<br>Schema conversion<br><br><br>|Amazon RDS<br>for MySQL DB<br>(target)<br><br>|**Maarekwww.**|
|© Stephane Maarek<br>Server with<br>AWS SCT installed<br>||**datacumulus.com**|



#### AWS DMS – Multi-AZ Deployment 

- When Multi-AZ Enabled, DMS AWS Region 

- provisions and maintains a synchronously stand replica in a Availability Zone - A Availability Zone - B 

- different AZ 

- • Advantages: synchronousreplication • Provides Data Redundancy DMS Replication DMS Replication 

- • Eliminates I/O freezes Instance Instance 

- • Minimizes latency spikes **(Standby Replica)** 

© Stephane Maarek 

#### RDS & Aurora MySQL Migrations 







- RDS MySQL to Aurora MySQL • Option 1: DB Snapshots from RDS MySQL restored as MySQL Aurora DB 

   - Option 2: Create an Aurora Read Replica from your RDS MySQL, and when the replication lag is 0, promote it as its own DB cluster (can take time and cost $) 





Read Replica 

- External MySQL to Aurora MySQL 

Percona • Option 1: XtraBackup import • Use Percona XtraBackup to create a file backup in Amazon S3 • Create an Aurora MySQL DB from Amazon S3 • Option 2: • Create an Aurora MySQL DB • Use the mysqldump utility to migrate MySQL into Aurora mysqldump (slower than S3 method) • Use DMS if both databases are up and running © Stephane Maarek IE'”TS Ol ns 

#### RDS & Aurora PostgreSQL Migrations 

- RDS PostgreSQL to Aurora PostgreSQL • Option 1: DB Snapshots from RDS PostgreSQL restored as PostgreSQL Aurora DB 

   - Option 2: Create an Aurora Read Replica from your RDS PostgreSQL, and when the replication lag is 0, promote it as its own DB cluster (can take time and cost $) 



<!-- Start of picture text -->
PostgreSQL<br>"g<br><!-- End of picture text -->



<!-- Start of picture text -->
"Eg<br><!-- End of picture text -->



<!-- Start of picture text -->
Amazon<br>FeAurora<br><!-- End of picture text -->



<!-- Start of picture text -->
O<br>5 5<br><!-- End of picture text -->



<!-- Start of picture text -->
|gA<br><!-- End of picture text -->

Read Replica 

- External PostgreSQL to Aurora PostgreSQL • Create a backup and put it in Amazon S3 • Import it using the aws_s3 Aurora extension 



<!-- Start of picture text -->
PostgreSQL<br><!-- End of picture text -->

backup import 



<!-- Start of picture text -->
Amazon<br>Aurorag<br><!-- End of picture text -->

- Use DMS if both databases are up and running 

© Stephane Maarek 

#### On-Premise strategy with AWS 

|• Ability to download Amazon Linux 2 AMI as a VM (.iso format)<br>• VMWare, KVM, VirtualBox (Oracle VM), Microsoft Hyper-V|
|---|
|• VM Import / Export<br>• Migrate existing applications into EC2<br>• Create a DR repository strategy for your on-premises VMs<br>• Can export back the VMs from EC2 to on-premises|
|• AWS Application Discovery Service<br>• Gather information about your on-premises servers to plan a migration<br>• Server utilization and dependency mappings<br>• Track with AWS Migration Hub|
|• AWS Database Migration Service (DMS)<br>• replicate On-premise => AWS , AWS => AWS, AWS => On-premise<br>• Works with various database technologies (Oracle, MySQL, DynamoDB, etc..)|
|• AWS Server Migration Service (SMS)<br>• Incremental replication of on-premises live servers to AWS|



© Stephane Maarek 

|AWS Backup|
|---|





|• Fully managed service|
|---|



|• Centrally manage and automate backups across AWS services|
|---|



|• No need to create custom scripts and manual processes|
|---|



|• Supported services:|
|---|



|• Amazon EC2 / Amazon EBS|
|---|



|• Amazon S3|
|---|



|• Amazon RDS (all DBs engines) / Amazon Aurora / Amazon DynamoDB|
|---|



|• Amazon DocumentDB / Amazon Neptune|
|---|



|• Amazon EFS / Amazon FSx (Lustre & Windows File Server)|
|---|



|• AWS Storage Gateway (Volume Gateway)|
|---|



|• Supports cross-region backups|
|---|



|• Supports cross-account backups|
|---|



© Stephane Maarek IE'”TS Ol ns 

#### AWS Backup 



- Supports PITR for supported services 

- On-Demand and Scheduled backups 

- Tag-based backup policies 

- You create backup policies known as Backup Plans 

   - Backup frequency (every 12 hours, daily, weekly, monthly, cron expression) 

   - Backup window 

• Transition to Cold Storage (Never, Days, Weeks, Months, Years) • Retention Period (Always, Days, Weeks, Months, Years) © Stephane Maarek IE'”TS Ol ns 

#### AWS Backup 

Assign AWS Resources oy EC2 EBS S3 Create Backup Plan RDS DynamoDB DocumentDB (frequency, retention policy) AWS Backup . eB EFS Aurora Neptune FSx Storage Gateway 

Automatically backed up to 



Amazon S3 

© Stephane Maarek 

#### AWS Backup Vault Lock 

- Enforce a WORM (Write Once Read Many) state for all the backups that you store in your AWS Backup Vault 



**backup** 

- Additional layer of defense to protect your backups against: 

   - Inadvertent or malicious delete operations 

   - Updates that shorten or alter retention periods 

**Backup Vault Lock Policy** Backups can’t be deleted • Even the root user cannot delete backups when enabled © Stephane Maarek IE'”TS Ol ns 

#### AWS Application Discovery Service 



- Plan migration projects by gathering information about on-premises data centers 

- • Server utilization data and dependency mapping are important for migrations 

- Agentless Discovery (AWS Agentless Discovery Connector) • VM inventory, configuration, and performance history such as CPU, memory, and disk usage 

- Agent-based Discovery (AWS Application Discovery Agent) 

   - System configuration, system performance, running processes, and details of the network connections between systems 

- Resulting data can be viewed within AWS Migration Hub 

© Stephane Maarek IE '”TS Ol 

AWS Application Migration Service (MGN) 

- _The “AWS evolution” of CloudEndure Migration, replacing AWS Server Migration Service (SMS)_ 

- Lift-and-shift (rehost) solution which simplify migrating applications to AWS 

- Converts your physical, virtual, and cloud-based servers to run natively on AWS 

- Supports wide range of platforms, Operating Systems, and databases 

- Minimal downtime, reduced costs 



<!-- Start of picture text -->
Corporate Data Center / Any cloud AWS Cloud<br>Application Migration Service<br>OS<br>Staging Production<br>continuous replication<br>Apps<br>cutover<br>DB + e Oe =<br>AWS Replication<br>Agent<br>Disks Low-cost EC2 instances Target EC2 instances<br>& EBS volumes & EBS volumes<br><!-- End of picture text -->

© Stephane Maarek 

#### VMware Cloud on AWS 

- Some customers use VMware Cloud to manage their on-premises Data Center 



<!-- Start of picture text -->
CM»<br><!-- End of picture text -->

- They want to extend the Data Center capacity to AWS, but keep using the VMware Cloud software 

- …Enter VMware Cloud on AWS 

- Use cases 

   - Migrate your VMware vSphere-based workloads to AWS 

   - Run your production workloads across VMware vSphere-based private, public, and hybrid cloud environments 

   - • Have a disaster recover strategy 



<!-- Start of picture text -->
Customer Data Center AWS Cloud<br>AWS Services<br>Amazon Amazon Direct<br>EC2 S3 Connect<br>VMware Cloud<br>On-Premises vCenter on AWS vSphere<br>Amazon Amazon Amazon<br>vSphere-based FSx RDS Redshift<br>environment<br><!-- End of picture text -->

© Stephane Maarek 

#### Transferring large amount of data into AWS 

- <u>Example:</u> transfer 200 TB of data in the cloud. We have a 100 Mbps internet <u>connection.</u> 

- Over the internet / Site-to-Site VPN: 

   - Immediate to setup 

   - Will take 200(TB)*1000(GB)*1000(MB)*8(Mb)/100 Mbps = 16,000,000s = 185d 

- Over direct connect 1Gbps: 

   - Long for the one-time setup (over a month) 

   - Will take 200(TB)*1000(GB)*8(Gb)/1 Gbps = 1,600,000s = 18.5d 

- Over Snowball: 

   - Will take 2 to 3 snowballs in parallel 

   - Takes about 1 week for the end-to-end transfer 

   - Can be combined with DMS 

- For on-going replication / transfers: Site-to-Site VPN or DX with DMS or DataSync 

© Stephane Maarek 

### More Solutions Architecture 

© Stephane Maarek 

#### Lambda, SNS & SQS 



<!-- Start of picture text -->
Try, retry<br>retries<br>(poll)<br>SQS asynchronous<br>DLQ SQS + Lambda<br>SNS<br>DLQ<br>Try, retry<br>blocking<br>SQS<br>SQS FIFO<br>SNS + Lambda sn<br>DLQ<br>SQS FIFO + Lambda<br>|!<br><!-- End of picture text -->

© Stephane Maarek 

#### Fan Out Pattern: deliver to multiple SQS 



<!-- Start of picture text -->
SQS SQS<br>1 Ge<br>OO O7Leo<br>PUT #1<br>Ne Se<br>SDK  SDK<br>SNS<br>PUT #2 Ge PUT subscribe ‘SS<br>GF >3 Gi a oh)9Me)<br>PUT #3<br>G@ ‘SS<br>O7L PO Oe RO<br>Ne Ne<br>Option 1 Option 2 – Fan Out<br><!-- End of picture text -->

© Stephane Maarek 

#### S3 Event Notifications 

• S3:ObjectCreated, S3:ObjectRemoved, Gf S3:ObjectRestore, S3:Replication… • Object name filtering possible (*.jpg) SNS • <u>Use case: generate thumbnails of images</u> events uploaded to S3 on Se • Can create as many “S3 events” as desired SQS Amazon S3 • S3 event notifications typically deliver events in seconds but can sometimes take a minute ° or longer Lambda Function IE '”TS Ol ns 

© Stephane Maarek IE '”TS Ol 

S3 Event Notifications with Amazon EventBridge 

events All events rules Over 18 AWS services as destinations ~~6B Amazon S3 Amazon bucket EventBridge 

• Advanced filtering options with JSON rules (metadata, object size, name...) 

- Multiple Destinations – ex Step Functions, Kinesis Streams / Firehose… 

• EventBridge Capabilities – Archive, Replay Events, Reliable delivery © Stephane Maarek IE '”TS Ol ns 

ns 

Amazon EventBridge – Intercept API Calls 



<!-- Start of picture text -->
User<br>lan<br>DeleteTable  API Call 💥<br>alert<br>Log API call event<br>DynamoDB CloudTrail Amazon SNS<br>EventBridge<br>(any API call)<br><!-- End of picture text -->

© Stephane Maarek IE '”TS Ol 

ns 

API Gateway – AWS Service Integration Kinesis Data Streams example store **.json** send records files Og requests API Gateway Kinesis Data Kinesis Data Amazon S3 **Client** 6 & eB Streams Firehose 

© Stephane Maarek IE '”TS Ol 



<!-- Start of picture text -->
Caching Strategies<br>Redis<br>Memcached<br>DAX<br>CloudFront API Gateway App logic<br>Client<br>EC2 / Lambda<br>Database<br>SomanRDSg<br>S3<br>CloudFront (edge)<br>Caching, TTL, Network, Computation, Cost, Latency<br>—=*=—~—axK—><*Zz*z~7_[_&K—&_=_—~—E—>_Zx_Z_==—i ><br>© Stephane Maarek<br>><br>NOT FOR DISTRIBUTION © Stephane Maarek www.datacumulus.com<br><!-- End of picture text -->

© Stephane Maarek > 

Blocking an IP address VPC Security group NACL **Client** EC2 Instance Public IP + Optional Firewall Software in EC2 = ~~<mark>f</mark>~~ <mark>o |</mark> © Stephane Maarek IE'”TS Ol ns 

Blocking an IP address – with an ALB VPC ALB Security group EC2 Security group NACL **Client** EC2 Instance **Application Load Balancer** Private IP **Connection Termination** ~~<mark>+L</mark>~~ <mark>?)</mark> © Stephane Maarek IE'”TS Ol ns 

Blocking an IP address – with an NLB VPC NLB Security group EC2 Security group NACL **Client Network Load Balancer** EC2 Instance Private IP B ~~<mark>e</mark>~~ <mark>@ lO)</mark> © Stephane Maarek IE '”TS Ol ns 

ns 



<!-- Start of picture text -->
Blocking an IP address – ALB + WAF<br>VPC<br>ALB Security group EC2 Security group<br>NACL<br>ALB<br>Client<br>EC2 Instance<br>Private IP<br>ail dloo<br>WAF<br>IP address filtering<br>© Stephane Maarek NOT FOR DISTRIBUTION © Stephane Maarek www.datacumulus.com<br><!-- End of picture text -->

# Blocking an IP address – ALB, CloudFront WAF VPC ALB Security group EC2 Security group CloudFront Public IPs **Client CloudFront Public ALB** EC2 Instance Private IP **Geo Restriction** NACL NACL not helpful r) **WAF IP address filtering** © Stephane Maarek <mark>o</mark> ~~<mark>a</mark>~~ <mark>t</mark> 

High Performance Computing (HPC) 

- The cloud is the perfect place to perform HPC 

- You can create a very high number of resources in no time 

- You can speed up time to results by adding more resources 

- You can pay only for the systems you have used 

- Perform genomics, computational chemistry, financial risk modeling, weather prediction, machine learning, deep learning, autonomous driving 

- Which services help perform HPC? 

© Stephane Maarek 

#### Data Management & Transfer 

- AWS Direct Connect: • Move GB/s of data to the cloud, over a private secure network 

- • Snowball & Snowmobile • Move PB of data to the cloud 

- AWS DataSync • Move large amount of data between on-premises and S3, EFS, FSx for Windows 

© Stephane Maarek 

#### Compute and Networking 

- EC2 Instances: • CPU optimized, GPU optimized 

   - Spot Instances / Spot Fleets for cost savings + Auto Scaling 



<!-- Start of picture text -->
• EC2 Placement Groups:  Cluster  for good network performance<br>EC2 EC2 EC2<br>Placement group<br>Cluster<br>Same Rack<br>Same AZ Low latency<br>10Gbps network<br>EC2 EC2 EC2<br><!-- End of picture text -->

© Stephane Maarek 

#### Compute and Networking 

- EC2 Enhanced Networking (SR-IOV) 

   - Higher bandwidth, higher PPS (packet per second), lower latency 

   - Option 1: Elastic Network Adapter (ENA) up to 100 Gbps 

   - Option 2: Intel 82599 VF up to 10 Gbps – LEGACY 

- Elastic Fabric Adapter (EFA) 

   - Improved ENA for HPC , only works for Linux 

   - Great for inter-node communications, tightly coupled workloads 

   - Leverages Message Passing Interface (MPI) standard 

   - Bypasses the underlying Linux OS to provide low-latency, reliable transport 

© Stephane Maarek 

#### Storage 

- Instance-attached storage: 

   - EBS: scale up to 256,000 IOPS with io2 Block Express 

   - Instance Store: scale to millions of IOPS, linked to EC2 instance, low latency 

- Network storage: 

   - Amazon S3: large blob, not a file system 

   - Amazon EFS: scale IOPS based on total size, or use provisioned IOPS 

   - • Amazon FSx for Lustre: 

      - HPC optimized distributed file system, millions of IOPS 

      - Backed by S3 

© Stephane Maarek 

#### Automation and Orchestration 

- AWS Batch 

   - AWS Batch supports multi-node parallel jobs, which enables you to run single jobs that span multiple EC2 instances. 

   - Easily schedule jobs and launch EC2 instances accordingly 

- AWS ParallelCluster 

   - Open-source cluster management tool to deploy HPC on AWS 

   - • Configure with text files 

   - Automate creation of VPC, Subnet, cluster type and instance types 

   - • Ability to enable EFA on the cluster (improves network performance) 

© Stephane Maarek 

Creating a highly available EC2 instance monitor Attachment CloudWatch Event What time is it? Public EC2 (or Alarm based on metric) 5:30 pm! Elastic IP Address Start the instance Attach the Elastic IP A ——-+_ <mark>—</mark> Standby EC2 instance © Stephane Maarek 

Creating a highly available EC2 instance With an Auto Scaling Group **<u>ASG Settings</u>** Auto Scaling group 1 min Availability Zone 1 1 max 1 desired >= 2 AZ What time is it? EC2 user data to attach Public EC2 The Elastic IP on 5:30 pm! Elastic IP Address Availability Zone 2 OE EC2 instance role to Allow API calls to attach The Elastic IP <u>EC2 User Data</u> ~~‘~~ Attachment Based on Tag Replacement EC2 instance 

ns 

© Stephane Maarek NS” 

Creating a highly available EC2 instance With ASG + EBS Auto Scaling group Availability Zone 1 EBS Snapshot On ASG _Terminate_ lifecycle hook What time is it? **EBS Volume** Public EC2 5:30 pm! Elastic IP Address Availability Zone 2 **EBS Snapshot + tags** <u>EC2 User Data</u> o ~~n~~ | Attachment ~~B~~ Based on Tag e EBS Volume created + attached **EBS** On ASG _Launch_ lifecycle hook Replacement EC2 instance © Stephane Maarek 

### Other Services 

Overview of Services that might come up in a few questions 

© Stephane Maarek 

#### What is CloudFormation 



|•CloudFormation is a declarative way of outlining your AWS<br>Infrastructure, for any resources (most of them are supported).|
|---|



|•For example, within a CloudFormation template, you say:|
|---|



|• I want a security group|
|---|



|• I want two EC2 instances using this security group|
|---|



|• I want an S3 bucket|
|---|



|• I want a load balancer (ELB) in front of these machines|
|---|



• Then CloudFormation creates those for you, in the right order , with the exact configuration that you specify © Stephane Maarek IE'”TS Ol ns 

#### Benefits of AWS CloudFormation (1/2) 

- Infrastructure as code 

   - No resources are manually created, which is excellent for control 

   - • Changes to the infrastructure are reviewed through code 

- Cost 

   - Each resources within the stack is tagged with an identifier so you can easily see how much a stack costs you 

   - You can estimate the costs of your resources using the CloudFormation template 

   - • Savings strategy: In Dev, you could automation deletion of templates at 5 PM and recreated at 8 AM, safely 

© Stephane Maarek 

#### Benefits of AWS CloudFormation (2/2) 

- Productivity 

   - Ability to destroy and re-create an infrastructure on the cloud on the fly 

   - Automated generation of Diagram for your templates! 

   - Declarative programming (no need to figure out ordering and orchestration) 

- Don’t re-invent the wheel 

   - Leverage existing templates on the web! 

   - Leverage the documentation 

- Supports (almost) all AWS resources: 

   - Everything we’ll see in this course is supported 

   - You can use “custom resources” for resources that are not supported 

© Stephane Maarek 

#### CloudFormation Stack Designer 

- Example: WordPress CloudFormation Stack 

- We can see all the resources • We can see the relations between the components 



<!-- Start of picture text -->
e oe, -@-@—e,<br>e om eé<br>| We<br>ALBTarget... Applicati... e DBinstance @<br>TargetGroup @ LoadBalancer @ Binstance @<br>@ @ ‘@-0,0-e”<br>@ @o——, e—_><br>© t © t & i<br>@ WebServer...securityGroup @ @DBEC2Secu...securityGroup @ @LaunLaun c hconfi.hCon. .. @|<br>‘eo—e \e— eo ‘o—@<br>,® e<br>td e td<br>@WebServer...Autoscating... @ ALBListen...Listener<br>‘ee @<br><!-- End of picture text -->

© Stephane Maarek 

#### CloudFormation – Service Role 

- IAM role that allows CloudFormation to create/update/delete stack resources on your behalf 

- Give ability to users to create/update/delete the stack resources even if they don’t have permissions to work with the resources in the stack 

- Use cases: 

   - You want to achieve the least privilege principle 

   - • But you don’t want to give the user all the required permissions to create the stack resources 

- User must have iam:PassRole permissions 

Permissions - cloudformation:* User - **iam:PassRole** Template 



Service Role 

- s3:*Bucket CloudFormation 





S3 bucket Stack 

© Stephane Maarek 

##### Amazon Simple Email Service (Amazon SES) 



- Fully managed service to send emails securely, globally and at scale 

- Allows inbound/outbound emails 

- Reputation dashboard, performance insights, anti-spam feedback 

- Provides statistics such as email deliveries, bounces, feedback loop results, email open 

- Supports DomainKeys Identified Mail (DKIM) and Sender Policy Framework (SPF) 

- Flexible IP deployment: shared, dedicated, and customer-owned IPs 



Users 

**bulk emails** 



###### Amazon SES 

- Send emails using your application using AWS Console, APIs, or SMTP 

**APIs** 

or **SMTP** 

- Use cases: transactional, marketing and bulk email communications 



Application 

© Stephane Maarek 

#### Amazon Pinpoint 

- Scalable 2-way (outbound/inbound) marketing communications service 

- Supports email, SMS, push, voice, and in-app messaging 

- • Ability to segment and personalize messages with the right content to customers 

- Possibility to receive replies 

- Scales to billions of messages per day 

- Use cases: run campaigns by sending marketing, bulk, transactional SMS messages 

- Versus Amazon SNS or Amazon SES • In SNS & SES you managed each message's audience, content, and delivery schedule 

   - In Amazon Pinpoint, you create message templates, delivery schedules, highly-targeted segments, and full campaigns 



Customers 

Amazon **SMS** a Pinpoint stream events (e.g., **TEXT_SUCCESS** , **TEXT_DELIVERED** , …) Spe Kinesis Data CloudWatch es Firehose Logs 

SNS Kinesis Data CloudWatch es Firehose Logs 

© Stephane Maarek SE 

Systems Manager – SSM Session Manager • Allows you to start a secure shell on your EC2 and EC2 Instance on-premises servers i **(SSM Agent)** _Execute_ • No SSH access, bastion hosts, or SSH keys _commands_ needed Session • No port 22 needed (better security) Manager IAM • Supports Linux, macOS, and Windows Permissions • Send session log data to S3 or CloudWatch Logs : User IE '”TS Ol ns 

© Stephane Maarek IE '”TS Ol 

Systems Manager – Run Command • Execute a document (= script) or just run a command 3 • Run command across multiple instances (using resource groups) Amazon SNS EventBridge • No need for SSH trigger • Command Output can be shown in the AWS Console, sent to S3 bucket or CloudWatch Logs Amazon S3 output # • Send notifications to SNS about command Run Command status (In progress, Success, Failed, …) 7 CloudWatch • Integrated with IAM & CloudTrail Logs • Can be invoked using EventBridge thy EC2 Instances EC2 Instances **(with SSM Agent) (with SSM Agent)** '”TS Ol ns 

EC2 Instances EC2 Instances **(with SSM Agent) (with SSM Agent)** ns 

© Stephane Maarek IE '”TS Ol 



<!-- Start of picture text -->
We<br><!-- End of picture text -->

#### Systems Manager – Patch Manager 

- Automates the process of patching managed instances 







- OS updates, applications updates, security updates 

**AWS Console AWS SDK Maintenance Windows** 

- Supports EC2 instances and on-premises servers 

run **AWS-RunBatchBaseline** 

- Supports Linux, macOS, and Windows • Patch on-demand or on a schedule using Maintenance Windows 



**Run Command** 



- Scan instances and generate patch compliance report (missing patches) 



<!-- Start of picture text -->
a<br><!-- End of picture text -->



<!-- Start of picture text -->
a<br><!-- End of picture text -->

EC2 Instances EC2 Instances **(with SSM Agent) (with SSM Agent)** 

© Stephane Maarek 

Systems Manager – Maintenance Windows • Defines a schedule for when to perform actions on your instances • Example: OS patching, updating drivers, installing software, … • Maintenance Window contains • Schedule • Duration • Set of registered instances • Set of registered tasks EC2 Instances trigger every 24 hour update **(with SSM Agent)** Maintenance Windows Run Command ®@. 8 | EC2 Instances **(with SSM Agent)** © Stephane Maarek IE'”TS Ol ns 

#### Systems Manager - Automation 

- Simplifies common maintenance and deployment tasks of EC2 instances and other AWS resources 

- • Examples: restart instances, create an AMI, EBS snapshot 











**AWS Console AWS SDK Maintenance Amazon AWS Config Windows EventBridge Remediation** • Examples: restart instances, create an AMI, EBS snapshot execute automation • Automation Runbook – SSM Documents to **(AWS-RestartEC2Instance)** define actions preformed on your EC2 instances or AWS resources (pre-defined or custom) Runbooks SSM Automation • Can be triggered using: (automation documents) • Manually using AWS Console, AWS CLI or SDK execute • Amazon EventBridge • On a schedule using Maintenance Windows AWS Resources • By AWS Config for rules remediations **…** EC2 Instances **EBS AMI RDS** 

© Stephane Maarek 

#### Cost Explorer 



- Visualize, understand, and manage your AWS costs and usage over time 

- Create custom reports that analyze cost and usage data. 

- Analyze your data at a high level: total costs and usage across all accounts 

- Or Monthly, hourly, resource level granularity 

- Choose an optimal Savings Plan (to lower prices on your bill) 

- Forecast usage up to 12 months based on previous usage 

© Stephane Maarek IE '”TS Ol 

ns 

#### Cost Explorer – Monthly Cost by AWS Service 



<!-- Start of picture text -->
& Monthly costs by service FILTERS. CLEAR ALL<br>Last 6 Months + Monthly » lia, Stack v Service Include only +<br>oe<br>Group by: Service Linked Account Region Usage Type Tag~ APIOperation Availability Zone More ~<br>Linked Account<br>Costs ($ in thousands)<br>14 Region<br>12 Instance Type<br>10 Usage Type<br>08 Usage Type Group<br>06 Tag<br>04 API Operation<br>02<br>Charge Type<br>00 Oct 2018 Nov 2018 Dec 2018 Jan 2019 Feb 2019 Mar 2019 More filters<br>MM 2.micro c4.2xlarge mS.large [—llim4large cd large lj Others ADVANCED OPTIONS e<br>Download CSV Show costs as ©<br>Instance Type Oct 1, 2018 Nov 1, 2018 Dec 1, 2018 Jan 1, 2019 IncludeUnblended costs related costs to<br>Total cost ($) 4,312.71 1,328.54 1,125.99 1,129.65, © Show only untagged resources<br>t2.micro ($) 486.75 475.89 405.63, 409.27<br>c4.2xlarge (8) 296.11 286.56 296.11 296.11<br><!-- End of picture text -->

© Stephane Maarek 

#### Cost Explorer– Hourly & Resource Level 



<!-- Start of picture text -->
aws Services » ResourceGroups v LX Admin/rosachae-Isengard@ 5... ~ Global ~ Support ~<br>@§ AWS Cost Management > Cost Explorer: Cost& Usage %, Settings Ov<br>a o FEE Ferons~ | ONaw reper<br>u Oct 25, 2019 - Oct 27, 2019 y Houryy @ lia Stack v « FILTERS CLEAR ALL<br>s Group by: Service Linked Account Region Instance Type Usage Type Tag More + Service<br>-_ Costs ($) Linked Account<br>= Region<br>Ss 200 Instance Type<br>150 Usage Type<br>Usage Type Group<br>100<br>Resource @<br>50 Tag<br>API Operation<br>° Oct-25" Oct-26" Oct-27" More filters ~<br>mio Hii-o i-o8 Mili-oc Hi Others 4 ADVANCED OPTIONS e<br>‘Show costs as @<br><!-- End of picture text -->

© Stephane Maarek 

#### Cost Explorer – Savings Plan Alternative to Reserved Instances 



<!-- Start of picture text -->
Recommendation options<br>Savings Plans type Savings Plans term Payment option Based on the past<br>© compute O tear © At uptront O Teays<br>© Ece instance © sear (© Pata upront © s0days,<br>(© io uptront © 60 days,<br>Recommendation: Purchase a Compute Savings Plan at a commitment of $2.40/hour<br>‘You could save an estimated $1,173 monthly by purchasing the recommended Compute Savings Plan.<br>this‘accountBased commitment, onoryour pastvariablewe 60usageproject dayspatters,thatof usage,you tiscouldwerecommendation recommend save an average purchasingmaximizes of $1.61/houra Savingsyour savings- representing Plan wihby leavinga commitmenta 40%an average savingsof $2.40/hourcompared$0.04hourtofr On-Demand.of a On-Demand 3-year term.To With<br>spend,<br>Before recommended purchase Aer recommended purchase based on your past 60 days of use)<br>Monthly On-Demand spend @ Estimated monthly spend © Estimated monthly savings ©<br>$2,955 ($4.05/hour) $1,782 ($2.44/hour) $1,173 ($1.61/hour)<br>{azedonyour On Demand spend verte ‘eurrecommendea S240houSainge Pans 40% many savings ovr On Demand<br>ast 0 cays commitmentsDemand spendan average S0O¢noucofOn-—_ $2955-81782=,172<br>“Ts recommendation examines our usage ove be pas 60 das incudng you exstng Saungs Pans andECZ Reserve stances) and caeales what our<br>‘AScost sullewould haveyour been lorhaueen prchaseatne comment recommendedamounts and SasngsrecommendsPlans ieSee appicabecommitment rasamount fr SasngsMat rougePlans heegreatsTo generatestates issaHngs. acommencaton,Lean mae<br>Recommended Compute Savings Plans Downloaa esv<br>x _ = Recommended Estimated hourly savings<br>Ter Payment opti at A<br>@ year ‘Atuptont s2.4omour $161 (60%)<br><!-- End of picture text -->

© Stephane Maarek 

#### Cost Explorer – Forecast Usage 



<!-- Start of picture text -->
Group by: None | Service Linked Account Region Instance Type Usage Type Tag» APIOperation Availability Zone More<br>Costs ($ in thousands)<br>25 :<br>sul 2019 H<br>Il Costs mean estimate $1,368 57 :<br>2.0 20% Confidence: $1,216.50-$1,520.64 :<br>Ml Usage mean estimate: 11,167.05 Hrs :<br>80% Confidence: 10,349.27 Hrs - 11,984.84 Hrs :<br>15 T<br>10 :<br>00. im [| UJ LI :: |<br>Usage (Hrs in thousands)<br>20 : -<br>BO sh Se ad en eee ee ee<br>Jan 2019 Feb 2019 Mar 2019 Apr 2019 May 2019 Jun 2019 Jul2019" Aug 2019" == Sep 2019" Oct 2019<br>MiCosts [_]Forecast —— 80% Confidence<br>[Usage [Forecast — 80% Confidence<br><!-- End of picture text -->

© Stephane Maarek 

#### AWS Batch 



- Fully managed batch processing at any scale 

- Efficiently run 100,000s of computing batch jobs on AWS 

- A “batch” job is a job with a start and an end (opposed to continuous) 

- Batch will dynamically launch EC2 instances or Spot Instances 

- AWS Batch provisions the right amount of compute / memory 

- You submit or schedule batch jobs and AWS Batch does the rest! 

• Batch jobs are defined as Docker images and run on ECS • Helpful for cost optimizations and focusing less on the infrastructure © Stephane Maarek IE'”TS Ol ns 

#### AWS Batch – Simplified Example 



<!-- Start of picture text -->
AWS Batch<br>EC2 Instance<br>Insert<br>ECS<br>Amazon S3<br>processed object<br>Trigger<br>Spot Instance<br>Amazon S3<br><!-- End of picture text -->

© Stephane Maarek 

#### Batch vs Lambda 

- Lambda: 

   - Time limit 

   - Limited runtimes 



   - Limited temporary disk space 

   - Serverless 

- Batch: 

   - No time limit 

   - Any runtime as long as it’s packaged as a Docker image 

• Rely on EBS / instance store for disk space • Relies on EC2 (can be managed by AWS) © Stephane Maarek IE'”TS Ol ns 

#### Amazon AppFlow 



- Fully managed integration service that enables you to securely transfer data between Software-as-a-Service (SaaS) applications and AWS 

- <u>Sources:</u> Salesforce , SAP, Zendesk, Slack, and ServiceNow 

- <u>Destinations:</u> AWS services like Amazon S3, Amazon Redshift or nonAWS such as SnowFlake and Salesforce 

- <u>Frequency: on a schedule, in response to events, or on demand</u> 

- <u>Data transformation capabilities like filtering and validation</u> 

- <u>Encrypted over the public internet or privately over AWS PrivateLink</u> 

- Don’t spend time writing the integrations and leverage APIs immediately 

© Stephane Maarek IE '”TS Ol 

ns 



AWS Amplify - web and mobile applications 

- A set of tools and services that helps you develop and deploy scalable full stack web and mobile applications 

- Authentication, Storage, API (REST, GraphQL), CI/CD, PubSub, Analytics, AI/ML Predictions, Monitoring, … 

- Connect your source code from GitHub, AWS CodeCommit, Bitbucket, GitLab, or upload directly 



<!-- Start of picture text -->
connect frontend to backend configure backend<br>using using<br>Amplify Frontend Libraries Amplify CLI<br>0 o :<br>Amazon S3 Amazon Cognito AWS  API<br>im * build using  Amplify Console  : AppSync Gateway … |<br>& deploy<br>3 Vv & Flutter: le | 3<br>Amazon Amazon Lex Lambda DynamoDB<br>| NEXT. … Oronac … : | | | SageMaker és |<br>Frontend Amplify Amazon  Amplify backend<br>Console CloudFront<br><!-- End of picture text -->

© Stephane Maarek 

### White Papers & Architectures Well Architected Framework, Disaster Recovery, etc… 

© Stephane Maarek 

|Section Overview|
|---|
|•Well Architected Framework Whitepaper|
|•Well Architected Tool|
|•AWS Trusted Advisor|
|•Reference architectures resources (for real-world)|
|•Disaster Recovery on AWS Whitepaper|



© Stephane Maarek 

Well Architected Framework General Guiding Principles 

• <u>https://aws.amazon.com/architecture/well-architected</u> 

- Stop guessing your capacity needs 

- Test systems at production scale • Automate to make architectural experimentation easier • Allow for evolutionary architectures 

- Design based on changing requirements 

- • Drive architectures using data • Improve through game days 

   - Simulate applications for flash sale days 

© Stephane Maarek 

Well Architected Framework 6 Pillars 

- 1) Operational Excellence • 2) Security • 3) Reliability • 4) Performance Efficiency • 5) Cost Optimization • 6) Sustainability 

• <u>They are not something to balance, or trade-offs, they’re a synergy</u> 

© Stephane Maarek 

#### AWS Well-Architected Tool 



- Free tool to review your architectures against the 6 pillars Well-Architected Framework and adopt architectural best practices 

- How does it work? 

   - Select your workload and answer questions 

   - Review your answers against the 6 pillars 

   - Obtain advice: get videos and documentations, generate a report, see the results in a dashboard 

- Let’s have a look: <u>https://console.aws.amazon.com/wellarchitected</u> 



<!-- Start of picture text -->
WellArchitected<br>Tool > Workioads<br>Workloads Generate reper ww detail it He Define workload<br>Q. Seorchby workload nome <1> @<br>Name Overall status Highrisks Medium risks Improvement status Last updated<br>Internal Employee Portal Answered 18 2 None: Now 24,2018 5:40 PM UTC-8<br>Mobile app - Android © Answered 9 1 None. Nov 24, 2018 3:45 PM UTC-8<br>Mobile app -i05, © Answered 0 1 None Now 24,2018 549 PM UTC-8<br>Retail Website- EU © Unanswered 0 ° None Nov 24, 2018352 PMUTC-S<br>Retail Website-North America @ Unanswered 0 ° None Nov 24, 2018 319 PM UTC-8<br><!-- End of picture text -->

<u>https://aws.amazon.com/blogs/aws/new-aws-well-architected-tool-review-workloads-against-best-practices/</u> 

© Stephane Maarek 

#### Trusted Advisor 

- No need to install anything – high level AWS account assessment 

- Analyze your AWS accounts and provides recommendation on 6 categories: 

   - Cost optimization 

   - Performance 

   - Security 

   - Fault tolerance 

   - Service limits 

   - Operational Excellence 

- <u>Business</u> & Enterprise Support plan 

   - Full Set of Checks 

   - Programmatic Access using AWS Support API 





<!-- Start of picture text -->
Checks<br>> © Amazon EBS Public Snapshots<br>Checks the permission settings for your Amazon Elastic<br>O EBS snapshots are marked as public.<br>> © > Amazon RDS Public Snapshots<br>Checks the permission settings for your Amazon Relatiot<br>public.<br>O RDS snapshots are marked as public.<br>> @© IAMUse<br>This check is intended to discourage the use of root acca<br>At least one IAM user has been created for this account.<br><!-- End of picture text -->

© Stephane Maarek 

#### More Architecture Examples 

- We’ve explored the most important architectural patterns: 

   - Classic: EC2, ELB, RDS, ElastiCache, etc… 

   - Serverless: S3, Lambda, DynamoDB, CloudFront, API Gateway, etc… 

- If you want to see more AWS architectures: 

- <u>https://aws.amazon.com/architecture/</u> 

- <u>https://aws.amazon.com/solutions/</u> 

© Stephane Maarek 

### Exam Review & Tips 

© Stephane Maarek 

#### State of learning checkpoint 

- Let’s look how far we’ve gone on our learning journey 

- <u>https://aws.amazon.com/certification/certified-solutions-architectassociate/</u> 

© Stephane Maarek 

#### Practice makes perfect 

- If you’re new to AWS, take a bit of AWS practice thanks to this course before rushing to the exam 

- The exam recommends you to have one or more years of hands-on experience on AWS 

- Practice makes perfect! 

- If you feel overwhelmed by the amount of knowledge you just learned, just go through it one more time 

© Stephane Maarek 

#### Proceed by elimination 

- Most questions are going to be scenario based 

- For all the questions, rule out answers that you know for sure are wrong 

- For the remaining answers, understand which one makes the most sense 

- There are very few trick questions 

- Don’t over-think it 

- If a solution seems feasible but highly complicated, it’s probably wrong 

© Stephane Maarek 

#### Skim the AWS Whitepapers 

- You can read about some AWS White Papers here: 

   - Architecting for the Cloud: AWS Best Practices 

   - AWS Well-Architected Framework 

   - AWS Disaster Recovery (https://aws.amazon.com/disaster-recovery/) 

- Overall we’ve explored all the most important concepts in the course • It’s never bad to have a look at the whitepapers you think are interesting! 

© Stephane Maarek 

#### Read each service’s FAQ 

- FAQ = Frequently asked questions • Example: <u>https://aws.amazon.com/vpc/faqs/</u> 

- FAQ cover a lot of the questions asked at the exam • They help confirm your understanding of a service 

© Stephane Maarek 

#### Get into the AWS Community 

|•Help out and discuss with other people in the course Q&A<br>•Review questions asked by other people in the Q&A<br>•Do the practice test in this section|
|---|
|•Read forums online<br>•Read online blogs|
|•Attend local meetups and discuss with other AWS engineers|
|•Watch re-invent videos on Youtube (AWS Conference)|



© Stephane Maarek 

#### How will the exam work? 

- You’ll have to register online at https://www.aws.training/ 

- Fee for the exam is 150 USD 

- Provide one identity documents (ID, Passport, details are in emails sent to you…) 

- No notes are allowed, no pen is allowed, no speaking 

- 65 questions will be asked in 130 minutes 

- Use the “Flag” feature to mark questions you want to re-visit 

- At the end you can optionally review all the questions / answers 

- To pass you need a score of a least 720 out of 1000 

- You will know within 5 days if you passed / failed the exams (most of the time less) 

- You will know the overall score a few days later (email notification) 

- You will not know which answers were right / wrong 

- If you fail, you can retake the exam again 14 days later 

© Stephane Maarek 

#### AWS Certification Paths – Architecture 

###### **Architecture Solutions Architect** 

Design, develop, and manage cloud infrastructure and assets, work with DevOps to migrate applications to the cloud 



<!-- Start of picture text -->
aws@<br>certified<br>Cloud<br>Practitioner<br>FOUNDATIONAL<br><!-- End of picture text -->



<!-- Start of picture text -->
aws@<br>certified<br>Solutions<br>Architect<br>ASSOCIATE<br><!-- End of picture text -->



<!-- Start of picture text -->
aws@<br>certified<br>Solutions<br>Architect<br>PROFESSIONAL<br><!-- End of picture text -->



<!-- Start of picture text -->
aws@<br>certified<br>.<br>security<br>SPECIALTY<br><!-- End of picture text -->

**Dive Deep** 

###### **Architecture Application Architect** 

Design significant aspects of application architecture including user interface, middleware, and infrastructure, and ensure enterprise-wide scalable, reliable, and manageable systems 



<!-- Start of picture text -->
aws@<br>certified<br>Cloud<br>Practitioner<br>FOUNDATIONAL<br><!-- End of picture text -->



<!-- Start of picture text -->
aws@<br>certified<br>Solutions<br>Architect<br>ASSOCIATE<br><!-- End of picture text -->



<!-- Start of picture text -->
aws@<br>certified<br>eeecloper<br>ASSOCIATE<br><!-- End of picture text -->



<!-- Start of picture text -->
aws@<br>certified<br>DevOps<br>Engineer<br>PROFESSIONAL<br><!-- End of picture text -->



<!-- Start of picture text -->
aws@<br>certified<br>Solutions<br>Architect<br>PROFESSIONAL<br><!-- End of picture text -->

**Dive Deep** 

<u>https://d1.awsstatic.com/training-andcertification/docs/AWS_certification_paths.pdf</u> 

© Stephane Maarek 

#### AWS Certification Paths – Operations 

###### **Operations Systems Administrator** 

Install, upgrade, and maintain computer components and software, and integrate automation processes 



<!-- Start of picture text -->
aws@<br>certified<br>Cloud<br>Practitioner<br>FOUNDATIONAL<br><!-- End of picture text -->



<!-- Start of picture text -->
aws@<br>certified<br>SysOps<br>Administrator<br>ASSOCIATE<br><!-- End of picture text -->



<!-- Start of picture text -->
aws@<br>certified<br>DevOps<br>Engineer<br>PROFESSIONAL<br><!-- End of picture text -->

**Dive Deep** 

**Operations Cloud Engineer** Implement and operate an organization’s networked computing infrastructure and Implement security systems to maintain data safety 



<!-- Start of picture text -->
aws@<br>certified<br>PractitionerCloud<br>FOUNDATIONAL<br><!-- End of picture text -->



<!-- Start of picture text -->
aws@<br>certified<br>AdministratorSysOps<br>ASSOCIATE<br><!-- End of picture text -->



<!-- Start of picture text -->
aws@<br>certified<br>SecurityA<br>SPECIALTY<br><!-- End of picture text -->



<!-- Start of picture text -->
aws@<br>certified<br>ptDevOpsicar<br>PROFESSIONAL<br><!-- End of picture text -->



<!-- Start of picture text -->
aws@<br>certified<br>oeAdvanced<br>SPECIALTY<br><!-- End of picture text -->

**Dive Deep** 

© Stephane Maarek 

#### AWS Certification Paths – DevOps 

**DevOps Test Engineer** Embed testing and quality best practices for software development from design to release, throughout the product life cycle **DevOps Cloud DevOps Engineer** Design, deployment, and operations of large-scale global hybrid cloud computing environment, advocating for end-to-end automated CI/CD DevOps pipelines 



<!-- Start of picture text -->
aws@<br>certified<br>Cloud<br>Practitioner<br>FOUNDATIONAL<br><!-- End of picture text -->



<!-- Start of picture text -->
aws@<br>certified<br>Cloud<br>Practitioner<br>FOUNDATIONAL<br><!-- End of picture text -->



<!-- Start of picture text -->
aws@<br>certified<br>Developer<br>ASSOCIATE<br><!-- End of picture text -->



<!-- Start of picture text -->
aws@<br>certified<br>Peveloper<br>ASSOCIATE<br><!-- End of picture text -->



<!-- Start of picture text -->
aws@<br>certified<br>DevOps<br>Engineer<br>PROFESSIONAL<br><!-- End of picture text -->



<!-- Start of picture text -->
aws@<br>certified<br>SysOps<br>Administrator<br>ASSOCIATE<br><!-- End of picture text -->



<!-- Start of picture text -->
aws@<br>certified<br>DevOps<br>Engineer<br>PROFESSIONAL<br><!-- End of picture text -->

**Optional** 

**Dive Deep** 

**DevOps DevSecOps Engineer** 

Accelerate enterprise cloud adoption while enabling rapid and stable delivery of capabilities using CI/CD principles, methodologies, and technologies 



<!-- Start of picture text -->
aws@<br>certified<br>PractitionerCloud<br>FOUNDATIONAL<br><!-- End of picture text -->



<!-- Start of picture text -->
awse@<br>certified<br>RurninistratorSysOps<br>ASSOCIATE<br><!-- End of picture text -->



<!-- Start of picture text -->
aws@<br>certified<br>EngineerDevOps<br>PROFESSIONAL<br><!-- End of picture text -->



<!-- Start of picture text -->
aws@<br>certified<br>Securityy<br>SPECIALTY<br><!-- End of picture text -->

© Stephane Maarek 

#### AWS Certification Paths – Security 

###### **Security Cloud Security Engineer** 

Design computer security architecture and develop detailed cyber security designs. Develop, execute, and track performance of security measures to protect information 



<!-- Start of picture text -->
awse<br>certified<br>Cloud<br>Practitioner<br>FOUNDATIONAL<br><!-- End of picture text -->



<!-- Start of picture text -->
aws@<br>certified<br>SysOps<br>Administrator<br>ASSOCIATE<br><!-- End of picture text -->



<!-- Start of picture text -->
awse<br>certified<br>s it<br>ecurity<br>SPECIALTY<br><!-- End of picture text -->



<!-- Start of picture text -->
aws@<br>certified<br>DevOps<br>Engineer<br>PROFESSIONAL<br><!-- End of picture text -->



<!-- Start of picture text -->
awse<br>certified<br>Advanced<br>Networking<br>SPECIALTY<br><!-- End of picture text -->

**Dive Deep** 

###### **Security Cloud Security Architect** 

Design and implement enterprise cloud solutions applying governance to identify, communicate, and minimize business and technical risks 



<!-- Start of picture text -->
aws@<br>certified<br>Cloud<br>Practitioner<br>FOUNDATIONAL<br><!-- End of picture text -->



<!-- Start of picture text -->
aws@<br>certified<br>Solutions<br>Architect<br>ASSOCIATE<br><!-- End of picture text -->



<!-- Start of picture text -->
awse<br>certified<br>‘<br>pecurity,<br>SPECIALTY<br><!-- End of picture text -->



<!-- Start of picture text -->
aws@<br>certified<br>Solutions<br>Architect<br>PROFESSIONAL<br><!-- End of picture text -->

**Dive Deep** 

© Stephane Maarek 

#### AWS Certification Paths – Data Analytics & Development 

###### **Data Analytics Cloud Data Engineer** 

Automate collection and processing of structured/semi-structured data and monitor data pipeline performance 



<!-- Start of picture text -->
aws@<br>certified<br>Cloud<br>Practitioner<br>FOUNDATIONAL<br><!-- End of picture text -->



<!-- Start of picture text -->
aws@<br>certified<br>Solutions<br>Architect<br>ASSOCIATE<br><!-- End of picture text -->



<!-- Start of picture text -->
aws@<br>certified<br>Data<br>Analytics<br>SPECIALTY<br><!-- End of picture text -->



<!-- Start of picture text -->
aws@<br>certified<br>.<br>Security<br>SPECIALTY<br><!-- End of picture text -->

**Dive Deep** 

###### **Development Software Development Engineer** 

Develop, construct, and maintain software across platforms and devices 



<!-- Start of picture text -->
awse@<br>certified<br>Cloud<br>Practitioner<br>FOUNDATIONAL<br><!-- End of picture text -->



<!-- Start of picture text -->
aws@<br>certified<br>Developer<br>ASSOCIATE<br><!-- End of picture text -->



<!-- Start of picture text -->
aws@<br>certified<br>DevOps<br>Engineer<br>PROFESSIONAL<br><!-- End of picture text -->

© Stephane Maarek 

#### AWS Certification Paths – Networking & AI/ML 

###### **Networking Network Engineer** 

Design and implement computer and information networks, such as local area networks (LAN), wide area networks (WAN), intranets, extranets, etc. 



<!-- Start of picture text -->
aws@<br>certified<br>Cloud<br>Practitioner<br>FOUNDATIONAL<br><!-- End of picture text -->



<!-- Start of picture text -->
aws@<br>certified<br>Solutions<br>Architect<br>ASSOCIATE<br><!-- End of picture text -->



<!-- Start of picture text -->
aws@<br>certified<br>Advanced<br>Networking<br>SPECIALTY<br><!-- End of picture text -->



<!-- Start of picture text -->
aws@<br>certified<br>s it<br>ecurity<br>SPECIALTY<br><!-- End of picture text -->

**Dive Deep** 

###### **AI/ML Machine Learning Engineer** 

Research, build, and design artificial intelligence (AI) systems to automate predictive models, and design machine learning systems, models, and schemes 



<!-- Start of picture text -->
aws@<br>certified<br>Cloud<br>Practitioner<br>FOUNDATIONAL<br><!-- End of picture text -->



<!-- Start of picture text -->
aws@<br>certified<br>Solutions<br>Architect<br>ASSOCIATE<br><!-- End of picture text -->



<!-- Start of picture text -->
aws@<br>certifiedul<br>SysOps<br>Administrator<br>ASSOCIATE<br><!-- End of picture text -->



<!-- Start of picture text -->
aws@<br>certified<br>Machine<br>Learning<br>SPECIALTY<br><!-- End of picture text -->

© Stephane Maarek 

Congratulations! 

© Stephane Maarek 

#### Congratulations! 

- Congrats on finishing the course! 

- I hope you will pass the exam without a hitch J 

- If you haven’t done so yet, I’d love a review from you! 

- If you passed, I’ll be more than happy to know I’ve helped 

   - Post it in the Q&A to help & motivate other students. Share your tips! 

   - Post it on LinkedIn and tag me! 

- Overall, I hope you learned how to use AWS and that you will be a tremendously good AWS Solutions Architect 

© Stephane Maarek 

