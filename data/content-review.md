# Editorial review report

Reviewed: 2026-10-29. Original screenshot selections were disregarded.

- Uploaded screenshots: **727**
- Combined question/source records: **606**
- Study-ready, with option-level explanations: **534**
- Reviewed exclusions: **72**
- Awaiting review: **0**

All sources are preserved in `source-manifest.json`; merged capture IDs are recorded in `source-aliases.json`.
Substantive wording corrections are labeled in the app and documented with the question. These are independent study explanations, not an AWS answer key.

## Study-ready pool by domain

- secure: 176
- resilient: 156
- performance: 130
- cost: 72

## Reviewed exclusions

These are closed editorial dispositions, not an automatic/background work queue. The source issue and relevant reading are listed below.

### #002 — Audit & observability

CloudTrail Lake is the intended historical answer, but it closed to new customers on May 31, 2026. Existing customers can continue using it. The question does not establish customer eligibility. Trails, S3 and Athena are a current alternative, but that complete option is absent.

- Source: `public/questions/Screenshot 2026-10-08 190300.png`
- [CloudTrail Lake: querying and availability changes](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-lake.html)

### #003 — Hybrid architectures

The wording reverses the direction of Outposts: Outposts brings AWS infrastructure on premises; it does not extend an arbitrary existing database into an AWS Region. No option specifies the required secure hybrid database connection.

- Source: `public/questions/Screenshot 2026-10-08 191148.png`
- [VPC: route tables and local routing](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Route_Tables.html)

### #006 — Block storage

The scenario omits required IOPS and throughput. gp3 with st1 can satisfy some database workloads, while higher requirements may need provisioned-IOPS SSD. Several choices can be valid without the missing performance targets.

- Source: `public/questions/Screenshot 2026-10-08 192152.png`
- [EBS volume types: IOPS and throughput](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-volume-types.html)

### #009 — Database encryption

None of these configurations establishes the stated direct CloudHSM-backed TDE integration for a standard RDS instance. RDS-managed encryption and TDE support vary by engine; do not infer a valid integration simply because Oracle and CloudHSM appear together.

- Source: `public/questions/Screenshot 2026-10-08 193203.png`
- [AWS KMS: key policies](https://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html)
- [RDS: Multi-AZ deployments](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.MultiAZ.html)

### #015 — Database selection

This question does not distinguish fast storage of recommendation results from generating recommendations over relationships. ElastiCache can serve low-latency values, while Neptune supports graph-based recommendations. The missing data model prevents a unique answer.

- Source: `public/questions/Screenshot 2026-10-08 194507.png`
- [Amazon Neptune: purpose-built graph database](https://docs.aws.amazon.com/neptune/latest/userguide/intro.html)

### #018 — Data analytics

Comprehend asynchronous jobs use S3 for input and output. The proposed answer that writes directly to Redshift omits a necessary output/ingestion step, so none of the choices completely describes the integration.

- Source: `public/questions/Screenshot 2026-10-09 030917.png`
- [Comprehend FAQs: customer content and data privacy](https://aws.amazon.com/comprehend/faqs/)
- [S3 storage classes and access patterns](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html)

### #019 — AI service selection

Lex is the conversational interface, while Personalize generates recommendations. One service alone does not satisfy both conversational assistance and personalized financial recommendations as worded.

- Source: `public/questions/Screenshot 2026-10-09 030940.png`
- [Lex V2: conversational intent and fulfillment](https://docs.aws.amazon.com/lexv2/latest/dg/what-is.html)
- [Personalize: managed recommendation models](https://docs.aws.amazon.com/personalize/latest/dg/what-is-personalize.html)

### #022 — Data analytics

Redshift Spectrum is the correct query concept, but Spectrum's S3 access does not use a cluster's enhanced VPC routing/S3 endpoint in the manner asserted. The options conflate the query service and network path, so the seemingly intended answer is not scored.

- Source: `public/questions/Screenshot 2026-10-09 031046.png`
- [Redshift Spectrum considerations and network routing](https://docs.aws.amazon.com/redshift/latest/dg/c-spectrum-considerations.html)
- [VPC: gateway endpoints for S3](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-s3.html)

### #025 — Object storage classes

Glacier retrieval pricing, bulk retrieval availability, latency and request patterns differ by class. The options refer to an unspecified free retrieval quota and treat Deep Archive bulk retrieval as automatically cheapest. A retrieval SLA and actual costs are needed.

- Source: `public/questions/Screenshot 2026-10-09 031231.png`
- [S3 storage classes and access patterns](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html)

### #031 — Cross-account access

SCPs limit principals in member accounts, not external principals merely because they access a member account's bucket. The wording omits how the restriction is implemented, and the bucket-policy option unnecessarily grants write access to an auditor. A unique least-privilege answer is not established.

- Source: `public/questions/Screenshot 2026-10-09 031609.png`
- [Organizations: service control policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html)
- [IAM: roles and temporary credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html)

### #035 — Network availability

A zonal NAT gateway per AZ can improve outbound egress availability, but RDS patching is AWS-managed and database connections within a VPC do not traverse a NAT gateway. Healthy RDS connection loss is not explained by the stated premise.

- Source: `public/questions/Screenshot 2026-10-09 031750.png`
- [VPC: NAT gateway availability and routing](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html)
- [RDS: Multi-AZ deployments](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.MultiAZ.html)

### #040 — Object storage limits

The old 5-TB object-limit premise is outdated. Current S3 documentation lists a maximum object size of 48.8 TiB with multipart upload. A 12-TB object is not inherently invalid on that old limit alone; Snowball/device/tool limits must be assessed separately.

- Source: `public/questions/Screenshot 2026-10-09 031920.png`
- [Current S3 multipart upload limits](https://docs.aws.amazon.com/AmazonS3/latest/userguide/qfacts.html)

### #043 — Hybrid containers

EKS Anywhere can run on bare metal, but its control plane and nodes are customer-managed. The question explicitly asks for AWS-managed on-premises Kubernetes, so its intended EKS Anywhere answer contradicts that requirement.

- Source: `public/questions/Screenshot 2026-10-09 032022.png`
- [EKS Anywhere: on-premises Kubernetes](https://anywhere.eks.amazonaws.com/docs/overview/)

### #048 — Data transfer

The options mix file locking, changes during transfer and verification-stage changes, whose behavior depends on the source protocol and task configuration. The source does not establish two unambiguous skipping causes; consult task error details rather than infer from the selected marks.

- Source: `public/questions/Screenshot 2026-10-09 032150.png`
- [DataSync: supported locations and transfers](https://docs.aws.amazon.com/datasync/latest/userguide/what-is-datasync.html)

### #053 — Network access controls

NACL evaluation differs between workload subnets and transit-gateway attachment subnets, including direction-specific exceptions. The wording does not clearly identify the subnet/direction being evaluated, so the generic destination-IP answer may be misleading.

- Source: `public/questions/Screenshot 2026-10-09 032331.png`
- [VPC: route tables and local routing](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Route_Tables.html)

### #064 — Audit & observability

Both a missing CloudTrail S3 bucket-policy permission and an inadequate KMS key policy can prevent log delivery. The problem provides no error or policy evidence to choose uniquely between B and C.

- Source: `public/questions/Screenshot 2026-10-09 032832.png`
- [AWS KMS: key policies](https://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html)
- [CloudTrail Lake: querying and availability changes](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-lake.html)

### #066 — Content delivery

AWS-origin-to-CloudFront transfer is generally free; being in the 'same Region as CloudFront' is not meaningful because CloudFront is global. Cache hit ratio and origin request/processing costs should be analyzed, but the choices do not state a sound unique optimization.

- Source: `public/questions/Screenshot 2026-10-09 032913.png`
- [CloudFront: private content with signed URLs and cookies](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html)

### #067 — Database selection

Timestream for LiveAnalytics matches the historical serverless time-series description, but it is no longer open to new customers. Timestream for InfluxDB is a distinct offering and not interchangeable with that claim. Eligibility is missing.

- Source: `public/questions/Screenshot 2026-10-09 032936.png`
- [Timestream for LiveAnalytics: service overview and availability](https://docs.aws.amazon.com/timestream/latest/developerguide/what-is-timestream.html)

### #071 — Block storage

Both a conflicting root-device attachment and duplicate filesystem labels can cause boot/mount problems. Without the attachment mapping, fstab/UUID configuration or logs, the stated symptom is not enough to pick one unique cause.

- Source: `public/questions/Screenshot 2026-10-09 033100.png`
- [EBS volume types: IOPS and throughput](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-volume-types.html)

### #080 — Infrastructure automation

To block replacement/deletion during stack updates, a stack policy is the relevant control, but it is absent. DeletionPolicy Retain preserves a resource when removed or on stack deletion; it does not prevent all update replacement/deletion. The source conflates these controls.

- Source: `public/questions/Screenshot 2026-10-09 034756.png`
- [CloudFormation: cfn-init metadata processing](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/cfn-init.html)

### #122 — Network troubleshooting

Security-group ingress and NACL filtering are plausible causes, but the route option describes an underspecified modified local route. Current local routes can be replaced/overridden for supported routing designs. The question does not provide enough actual route/rule configuration for its exact two-choice claim.

- Source: `public/questions/Screenshot 2026-10-09 041957.png`
- [VPC: route tables and local routing](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Route_Tables.html)

### #126 — VPN authentication

Client VPN requires a server certificate in ACM and suitable client-certificate trust configuration. When server and client certificates share the same CA, separately importing every client certificate is not generally required. The unspecified import error cannot be resolved uniquely by the asserted step.

- Source: `public/questions/Screenshot 2026-10-09 042158.png`
- [AWS Client VPN: secure remote user access](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/what-is.html)

### #142 — Database migration

DynamoDB requires redesign around partition/sort keys and access patterns; preserving arbitrary relational table structures through SCT is not a general supported conversion guarantee. The options omit a defensible mapping and direct DMS DynamoDB-target workflow.

- Source: `public/questions/Screenshot 2026-10-09 043825.png`
- [DMS: data migration and change replication](https://docs.aws.amazon.com/dms/latest/userguide/Welcome.html)
- [DynamoDB: core components and access patterns](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.CoreComponents.html)

### #143 — Hybrid recovery

DataSync plus File Gateway does not automatically turn a failed database into a writable database backed directly by S3 with no code or recovery changes. File-level access and database replication/failover are different guarantees.

- Source: `public/questions/Screenshot 2026-10-09 043858.png`
- [DataSync: supported locations and transfers](https://docs.aws.amazon.com/datasync/latest/userguide/what-is-datasync.html)
- [Storage Gateway: cached versus stored volumes](https://docs.aws.amazon.com/storagegateway/latest/vgw/WhatIsStorageGateway.html)

### #157 — Object protection

Versioning and least-privilege deletion are sound controls, but both MFA Delete and appropriate Object Lock governance retention can protect versions. The question supplies four potentially relevant controls while demanding exactly three and does not specify retention/operational constraints.

- Source: `public/questions/Screenshot 2026-10-09 114942.png`
- Source: `public/questions/Screenshot 2026-10-09 131508.png`
- [S3 storage classes and access patterns](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html)
- [IAM: roles and temporary credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html)

### #173 — Browser object access

An S3 CORS rule uses AllowedMethods (GET), AllowedOrigins and optionally AllowedHeaders/ExposeHeaders. The options incorrectly present Access-Control-Request-Method as the bucket configuration field and conflate request headers with rule format.

- Source: `public/questions/Screenshot 2026-10-09 115624.png`
- [S3 storage classes and access patterns](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html)

### #174 — Resource policies

An allow-only bucket policy does not override other identity-based allows, while deny exceptions need carefully scoped Principal/condition handling. Several deny choices can work or misbehave depending on full policy details, permissions boundaries and role sessions; no complete policy is supplied.

- Source: `public/questions/Screenshot 2026-10-09 115649.png`
- [IAM: roles and temporary credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html)

### #175 — Database observability

The options do not identify whether the team needs CloudWatch metrics, database system views or console query-monitoring views. All require different data sources, so 'build custom queries' plus a console name is insufficiently specified.

- Source: `public/questions/Screenshot 2026-10-09 115722.png`
- [Redshift: purchasing reserved nodes](https://docs.aws.amazon.com/redshift/latest/mgmt/purchase-reserved-node-instance.html)
- [CloudWatch: collect host metrics with the unified agent](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Install-CloudWatch-Agent.html)

### #179 — Private ingress

Global Accelerator supplies static anycast IPs, but its public internet ingress does not meet 'avoid the public internet for device ingress'. Route 53 private endpoints do not repair that requirement either. The options do not provide a complete private-ingress design.

- Source: `public/questions/Screenshot 2026-10-09 115954.png`
- [Global Accelerator: endpoints and network performance](https://docs.aws.amazon.com/global-accelerator/latest/dg/what-is-global-accelerator.html)

### #182 — Object storage performance

Parallel multipart uploads and a metadata index can help, but Transfer Acceleration benefits depend on geography and are not automatically useful for EC2-to-S3 processing within one Region. The source bundles conditional techniques into one mandatory answer without the relevant network details.

- Source: `public/questions/Screenshot 2026-10-09 120358.png`
- [S3 storage classes and access patterns](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html)

### #183 — Immutable data

Neither DynamoDB Streams nor an ordinary mutable database guarantees an immutable transaction ledger. The options omit an explicit append-only/tamper-evident design, so no unique service choice satisfies the requirement as stated.

- Source: `public/questions/Screenshot 2026-10-09 120428.png`
- [S3 Object Lock: retention and legal holds](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock.html)
- [DynamoDB Streams and Lambda](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Streams.Lambda.html)

### #209 — Shared storage

The access protocol, sharing scope and meaning of global low latency are unspecified. EFS is regional shared NFS; S3 is globally reachable object storage; neither automatically guarantees low-latency shared filesystem semantics worldwide.

- Source: `public/questions/Screenshot 2026-10-09 122830.png`
- [EFS: lifecycle management](https://docs.aws.amazon.com/efs/latest/ug/lifecycle-management-efs.html)
- [S3 storage classes and access patterns](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html)

### #210 — Network access controls

Restrict database ingress to the application security group/port is the relevant control, but option A refers only to ports within a security group without specifying the source. Ports alone do not exclude external principals. The exact least-privilege rule is missing.

- Source: `public/questions/Screenshot 2026-10-09 122850.png`
- [VPC: route tables and local routing](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Route_Tables.html)

### #221 — Workflow orchestration

Separate queues/state machines do not automatically prioritize Polly's own asynchronous tasks, and Lambda reserved concurrency does not guarantee Polly scheduling priority or lower off-peak per-request pricing. The compound answer overpromises these properties.

- Source: `public/questions/Screenshot 2026-10-09 124120.png`
- [Step Functions: visual workflow orchestration](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html)

### #225 — Compute scaling

Target tracking and AZ rebalancing can both help, but the source's per-AZ limits and 'without additional scaling costs' guarantee are not well-defined. Rebalancing, warm-up, allocation rules and application routing need concrete configuration.

- Source: `public/questions/Screenshot 2026-10-09 124240.png`
- [EC2 Auto Scaling: health checks and replacement](https://docs.aws.amazon.com/autoscaling/ec2/userguide/health-checks-overview.html)

### #273 — Object ownership

The question relies on legacy cross-account object ownership/ACL assumptions and asks for exactly two choices despite incomplete object-owner permissions. Modern bucket-owner-enforced ownership disables ACLs. A private S3 origin with CloudFront/OAC is a more controlled public-delivery design.

- Source: `public/questions/Screenshot 2026-10-09 133145.png`
- [S3 storage classes and access patterns](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html)
- [CloudFront: private content with signed URLs and cookies](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html)

### #290 — Messaging & integration

SNS-to-SQS plus per-queue DLQs is a good design, but EventBridge-to-SQS plus those DLQs can also meet these requirements. The exact TWO formulation leaves an additional valid routing alternative.

- Source: `public/questions/Screenshot 2026-10-09 135311.png`
- [SNS: fanout to SQS queues](https://docs.aws.amazon.com/sns/latest/dg/sns-sqs-as-subscriber.html)
- [SQS: queue types and delivery semantics](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.html)

### #292 — Source attachment

This upload shows DNS dashboard records rather than an exam question. It is preserved as a source attachment and excluded from the study pool.

- Source: `public/questions/Screenshot 2026-10-09 145219.png`
- [Route 53: alias records and DNS record types](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/ResourceRecordTypes.html)

### #299 — Block storage performance

The instance EBS bandwidth ceiling is the stated bottleneck. A larger suitable instance can raise it, but switching to provisioned-IOPS volumes alone cannot exceed that same instance ceiling. Without an additional volume IOPS constraint, the source does not justify its required TWO answers.

- Source: `public/questions/Screenshot 2026-10-09 152657.png`
- [EBS volume types: IOPS and throughput](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-volume-types.html)

### #308 — Database change events

Aurora MySQL's Lambda integration can invoke Lambda from database logic, but merely publishing unrelated messages to SQS does not capture Aurora row changes. Option C omits the change-to-queue producer, so exactly TWO complete solutions are not supplied.

- Source: `public/questions/Screenshot 2026-10-09 152926.png`
- [DynamoDB Streams and Lambda](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Streams.Lambda.html)
- [Lambda: execution role permissions](https://docs.aws.amazon.com/lambda/latest/dg/lambda-intro-execution-role.html)

### #316 — Container compute

EKS on Fargate satisfies no worker-node management and per-pod isolation, but the stated EBS CSI requirement is unsupported: Fargate pods cannot mount EBS volumes. Fargate also has specific Pod Identity/agent restrictions. No choice satisfies every listed requirement.

- Source: `public/questions/Screenshot 2026-10-09 153149.png`
- [EKS Fargate capabilities and restrictions](https://docs.aws.amazon.com/eks/latest/userguide/fargate.html)

### #333 — Block storage performance

st1 is optimized for sequential throughput, but sustained 500 MiB/s requires a sufficiently large baseline (12.5 TiB under current documentation). A smaller gp3 volume can provision that throughput separately from capacity. Without required capacity, credits, instance bandwidth and prices, the source cannot establish the cheapest option.

- Source: `public/questions/Screenshot 2026-10-09 153658.png`
- [EBS HDD volume sizes, baselines and burst credits](https://docs.aws.amazon.com/ebs/latest/userguide/hdd-vols.html)
- [EBS volume types: IOPS and throughput](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-volume-types.html)

### #334 — Object storage classes

S3 buckets can mix per-object classes, but both Glacier Instant Retrieval and One Zone-IA can serve infrequent objects in milliseconds. Required retrieval frequency, recoverability and AZ-loss tolerance are missing, so the question does not uniquely choose A versus C.

- Source: `public/questions/Screenshot 2026-10-09 153713.png`
- [S3 storage classes and access patterns](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html)

### #344 — AI service selection

The question only asks to 'enhance customer service'. Polly, Lex, Kendra and Textract can all support legitimate customer-service workflows, and it gives no workload constraints that select exactly TWO.

- Source: `public/questions/Screenshot 2026-10-09 154034.png`
- [Lex V2: conversational intent and fulfillment](https://docs.aws.amazon.com/lexv2/latest/dg/what-is.html)
- [Polly: lexicons, styles and Brand Voice](https://aws.amazon.com/polly/features/)
- [Textract: text, forms and handwriting extraction](https://docs.aws.amazon.com/textract/latest/dg/what-is.html)

### #347 — Event notifications

A Lambda can construct a usable download/presigned link and send it through SES. A native S3-to-SNS email notification instead contains an event record and does not generate the requested usable download link for external recipients. Only one complete option is supplied despite Select TWO.

- Source: `public/questions/Screenshot 2026-10-09 154139.png`
- [S3: event notifications](https://docs.aws.amazon.com/AmazonS3/latest/userguide/EventNotifications.html)
- [S3: uploading objects using presigned URLs](https://docs.aws.amazon.com/AmazonS3/latest/userguide/PresignedUrlUploadObject.html)

### #360 — Bulk migration

The historical offline-transfer answer is Snowball devices, but new-customer Snowball access ended in November 2025 and Snowmobile is retired. The question omits eligibility, required completion time and current transfer alternatives, so its fastest/cheapest claim is not a current general recommendation.

- Source: `public/questions/Screenshot 2026-10-16 112028.png`
- [DataSync: supported locations and transfers](https://docs.aws.amazon.com/datasync/latest/userguide/what-is-datasync.html)

### #387 — IP address planning

Adding a larger IPv4 subnet can work only if free VPC address space exists; IPv6-only subnets require supported instance/workload configurations. The source does not establish these prerequisites and incorrectly describes associating a new VPC, so it cannot uniquely choose the proposed migration path.

- Source: `public/questions/Screenshot 2026-10-16 122645.png`
- [VPC: subnet address sizes and reserved addresses](https://docs.aws.amazon.com/vpc/latest/userguide/subnet-sizing.html)

### #393 — Network inspection

The offered 'minimum' topology misstates ALB public-subnet requirements and calls FQDNs a source identity for incoming requests. Network Firewall domain inspection applies to supported HTTP Host/TLS SNI flows, not authenticated source FQDN identity; NAT and a direct ALB integration do not solve this. A precise inspectable traffic direction/topology is required.

- Source: `public/questions/Screenshot 2026-10-16 123405.png`
- [VPC: route tables and local routing](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Route_Tables.html)
- [WAF: use-case-specific managed rule groups](https://docs.aws.amazon.com/waf/latest/developerguide/aws-managed-rule-groups-use-case.html)

### #394 — Unreadable source

The original PNG is a tiny horizontal strip with no readable question or answer content. This is a source attachment, not a recoverable exam question; no answer is inferred.

- Source: `public/questions/Screenshot 2026-10-16 123654.png`
- [AWS Well-Architected: disaster recovery strategies](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/plan-for-disaster-recovery-dr.html)

### #415 — Compute hibernation

Hibernation can preserve application memory, but A (migrate to an enabled instance) and C (enable on an existing supported stopped instance) depend on current eligibility/root-volume configuration. The source gives neither instance/AMI eligibility nor a consistent single choice, and hibernation also bills stored RAM in EBS.

- Source: `public/questions/Screenshot 2026-10-17 083209.png`
- Source: `public/questions/Screenshot 2026-10-18 114509.png`
- [EC2 hibernation prerequisites and behavior](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Hibernate.html)

### #416 — Object events

Tracking new objects, ordinary delete markers and permanent version deletes requires the appropriate ObjectCreated and both relevant ObjectRemoved events (or ObjectRemoved:*). Options B and C each omit one deletion case; the MQ options are not the stated SQS queue. No offered option covers all required events.

- Source: `public/questions/Screenshot 2026-10-17 083231.png`
- Source: `public/questions/Screenshot 2026-10-18 114611.png`
- [S3: event notifications](https://docs.aws.amazon.com/AmazonS3/latest/userguide/EventNotifications.html)

### #447 — Object transformation

S3 Object Lambda is closed to new customers from November 7, 2025. The question does not establish an eligible existing customer and conflates obtaining a transformed response with avoiding the Lambda function reading the source object. Its bucket/key answer is historical, not a complete current solution.

- Source: `public/questions/Screenshot 2026-10-17 084438.png`
- Source: `public/questions/Screenshot 2026-10-18 121856.png`
- Source: `public/questions/Screenshot 2026-10-24 122130.png`
- [S3 Object Lambda availability and operation](https://docs.aws.amazon.com/AmazonS3/latest/userguide/transforming-objects.html)
- [Athena: serverless SQL queries over S3](https://docs.aws.amazon.com/athena/latest/ug/what-is.html)

### #448 — Serverless storage

Both ECS Fargate (with its default larger ephemeral allocation) and a container-image Lambda configured with 5 GB of /tmp can satisfy at least 5 GB of serverless temporary storage. Runtime, execution duration and exact-versus-minimum sizing are not specified, so B and D are both viable.

- Source: `public/questions/Screenshot 2026-10-17 084503.png`
- Source: `public/questions/Screenshot 2026-10-18 121911.png`
- [Lambda ephemeral storage configuration](https://docs.aws.amazon.com/lambda/latest/dg/configuration-ephemeral-storage.html)
- [Fargate: serverless compute for containers](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/AWS_Fargate.html)

### #459 — Database scaling

Only C explicitly configures DAX and provisioned auto scaling. A falsely assumes console-style auto-scaling defaults for a CLI-created table; B adds unrequired cross-Region replication/cost and does not fix missing capacity configuration. The source does not establish TWO required cost-effective choices.

- Source: `public/questions/Screenshot 2026-10-17 084956.png`
- Source: `public/questions/Screenshot 2026-10-18 122320.png`
- [DynamoDB: reactive provisioned-capacity auto scaling](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/AutoScaling.html)

### #463 — VPC function troubleshooting

Current Lambda uses shared Hyperplane ENIs, not one ENI per invocation. IP exhaustion and ENI quota errors have distinct failure codes; EC2ThrottledException points to throttled EC2 operations rather than proving either duplicate IP-exhaustion option. Exact error/context is needed for two justified causes.

- Source: `public/questions/Screenshot 2026-10-17 085154.png`
- Source: `public/questions/Screenshot 2026-10-18 122444.png`
- [Lambda: execution role permissions](https://docs.aws.amazon.com/lambda/latest/dg/lambda-intro-execution-role.html)

### #466 — Non-question attachment

The upload is a search result for a university society website, not an AWS exam question. It contains no answer options and is retained only as a source attachment.

- Source: `public/questions/Screenshot 2026-10-17 133749.png`
- Source: `public/questions/Screenshot 2026-10-17 140036.png`
- Source: `public/questions/Screenshot 2026-10-17 142043.png`
- [AWS Well-Architected: disaster recovery strategies](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/plan-for-disaster-recovery-dr.html)

### #469 — Unreadable source

The upload is a Google Drive file-open error page, not readable question content. No question or answer options can be recovered from this image.

- Source: `public/questions/Screenshot 2026-10-17 145918.png`
- [AWS Well-Architected: disaster recovery strategies](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/plan-for-disaster-recovery-dr.html)

### #557 — Sensitive data remediation

Macie in C is the appropriate PII discovery service, but it does not automatically delete detected objects. Every offered choice omits the required removal/quarantine workflow and approval/retention behavior. A complete design needs findings-driven remediation as well as access policies.

- Source: `public/questions/Screenshot 2026-10-22 133749.png`
- Source: `public/questions/Screenshot 2026-10-22 135222.png`
- [Macie: discovering sensitive S3 data](https://docs.aws.amazon.com/macie/latest/user/what-is-macie.html)

### #576 — IAM policy scope

The original PNG shows one entire IAM policy option only; the remaining candidate policies are not in the upload. The visible policy correctly scopes GetItem/PutItem/UpdateItem/DeleteItem to one table ARN, but inventing three unseen alternatives would not reconstruct the source question.

- Source: `public/questions/Screenshot 2026-10-22 140340.png`
- [IAM: roles and temporary credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html)
- [DynamoDB: core components and access patterns](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.CoreComponents.html)

### #594 — Big data authorization

The source requires Apache Ranger integration without selecting an EMR release, but native Ranger integration is unsupported starting with EMR 7.4. Simultaneous Lake Formation authorization also has mode/release restrictions. The steady-core/Spot-task cost pattern alone cannot satisfy this unspecified current feature combination.

- Source: `public/questions/Screenshot 2026-10-23 125924.png`
- [EMR Apache Ranger integration and release restrictions](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-ranger.html)
- [Lake Formation permissions and data access](https://docs.aws.amazon.com/lake-formation/latest/dg/access-control-overview.html)

### #596 — Bulk migration

Snowball is the historical offline-transfer answer, but it is not available to new customers after the November 2025 availability change. The source gives no existing-customer eligibility or target deadline; Transfer Acceleration cannot repair a slow local uplink. A current eligible transfer plan cannot be selected unconditionally.

- Source: `public/questions/Screenshot 2026-10-23 130124.png`
- [DataSync: supported locations and transfers](https://docs.aws.amazon.com/datasync/latest/userguide/what-is-datasync.html)
- [S3 Transfer Acceleration](https://docs.aws.amazon.com/AmazonS3/latest/userguide/transfer-acceleration.html)

### #607 — Container data authorization

Every option confuses ECS task execution role with the application task role, and several invent a standard RDS data VPC endpoint or allow public S3 access. The correct pattern needs a task role plus private RDS SG restrictions and scoped S3 authorization; no listed choice fully provides it.

- Source: `public/questions/Screenshot 2026-10-23 133017.png`
- Source: `public/questions/Screenshot 2026-10-24 121401.png`
- Source: `public/questions/Screenshot 2026-10-24 121416.png`
- [ECS task IAM role versus execution role](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-iam-roles.html)
- [VPC: gateway endpoints for S3](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-s3.html)

### #608 — Windows file migration

DataSync can preserve supported SMB permissions using an appropriately deployed agent and identity mapping, but the other proposed paths via ordinary S3 copies discard the required Windows security metadata. Snowcone/Snowmobile options are obsolete/inaccurate and the prompt requires TWO complete solutions. Only one plausible path is offered.

- Source: `public/questions/Screenshot 2026-10-23 133252.png`
- Source: `public/questions/Screenshot 2026-10-24 113705.png`
- Source: `public/questions/Screenshot 2026-10-24 113710.png`
- Source: `public/questions/Screenshot 2026-10-24 113721.png`
- Source: `public/questions/Screenshot 2026-10-24 113730.png`
- [DataSync: supported locations and transfers](https://docs.aws.amazon.com/datasync/latest/userguide/what-is-datasync.html)
- [FSx for Windows: Active Directory and SMB](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/what-is.html)

### #612 — Platform templates

AWS Proton ended support on October 7, 2026; its console/resources are no longer accessible after that date. Components are the historical intended feature, but none of the offered services supplies that same current Proton workflow. Existing deployed infrastructure remains; use the service migration guidance.

- Source: `public/questions/Screenshot 2026-10-23 133934.png`
- [AWS Proton service availability](https://docs.aws.amazon.com/proton/latest/userguide/Welcome.html)
- [CloudFormation: templates, stacks and change sets](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html)

### #623 — Bulk export

Snowball export is the historical offline answer, but new-customer access ended in November 2025 and eligibility is not specified. Direct Connect lead time and local bandwidth are also missing, while CloudFront is not a Global Accelerator standard endpoint. A current fastest/cheapest answer cannot be selected unconditionally.

- Source: `public/questions/Screenshot 2026-10-23 134737.png`
- [DataSync: supported locations and transfers](https://docs.aws.amazon.com/datasync/latest/userguide/what-is-datasync.html)
- [S3 Transfer Acceleration](https://docs.aws.amazon.com/AmazonS3/latest/userguide/transfer-acceleration.html)

### #630 — Migration assessment

Application Discovery Service/Migration Hub have current new-customer availability transitions, and the source uses a legacy discovery connector without specifying eligibility. The historical inventory-plus-Migration-Hub answer needs an available supported discovery/migration assessment path for the actual customer.

- Source: `public/questions/Screenshot 2026-10-23 135343.png`
- [Application Migration Service: server rehosting](https://docs.aws.amazon.com/mgn/latest/ug/what-is-application-migration-service.html)

### #646 — Legacy gateway deployment

The intended interface is S3 File Gateway for NFS, but the choice couples it to a legacy hardware appliance SKU and the alternative to a VM despite an absolute no-virtualization constraint. Current appliance eligibility/availability and where the gateway may run are not established; the image cannot justify a new physical-appliance purchase.

- Source: `public/questions/Screenshot 2026-10-24 110615.png`
- Source: `public/questions/Screenshot 2026-10-24 110603.png`
- Source: `public/questions/Screenshot 2026-10-24 110652.png`
- [Storage Gateway: cached versus stored volumes](https://docs.aws.amazon.com/storagegateway/latest/vgw/WhatIsStorageGateway.html)

### #661 — Authentication latency

A 504/login slowdown needs origin and authentication-path diagnosis. Longer static caching, multi-Region deployment, edge token validation and origin failover can address different symptoms, but failover is method-limited and does not automatically fail over POST login operations. No workload/auth details establish exactly TWO guaranteed cost-effective fixes.

- Source: `public/questions/Screenshot 2026-10-24 112859.png`
- Source: `public/questions/Screenshot 2026-10-24 112908.png`
- [Lambda@Edge: CloudFront event triggers](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/lambda-cloudfront-trigger-events.html)
- [CloudFront: private content with signed URLs and cookies](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html)

### #672 — Platform templates

AWS Proton ended support on October 7, 2026; its console/resources are no longer accessible after that date. Components are the historical intended feature, but none of the offered services supplies that same current Proton workflow. Existing deployed infrastructure remains; use the service migration guidance.

- Source: `public/questions/Screenshot 2026-10-24 113511.png`
- [AWS Proton service availability](https://docs.aws.amazon.com/proton/latest/userguide/Welcome.html)
- [CloudFormation: templates, stacks and change sets](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html)

### #682 — Shared filesystems

Visual inspection confirms that the source repeats ElastiCache for B and D and never offers EFS. S3 is object storage and higher EBS IOPS does not create a scalable multi-AZ POSIX shared filesystem. The intended EFS answer is absent; this is an actual defective question, not a transcription gap.

- Source: `public/questions/Screenshot 2026-10-24 113927.png`
- Source: `public/questions/Screenshot 2026-10-24 113951.png`
- [EFS: lifecycle management](https://docs.aws.amazon.com/efs/latest/ug/lifecycle-management-efs.html)

### #712 — Incomplete IAM policy

The original screenshot ends mid-policy and does not include the remainder, final question or answer choices. A visible explicit deny generally overrides an allow, but the complete action/resource/condition scope cannot be reconstructed from this crop.

- Source: `public/questions/Screenshot 2026-10-24 121950.png`
- [IAM: roles and temporary credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html)

### #727 — Bulk migration

The historical offline-transfer answer is Snowball devices, but new-customer Snowball access ended in November 2025 and Snowmobile is retired. The question omits eligibility, required completion time and current transfer alternatives, so its fastest/cheapest claim is not a current general recommendation.

- Source: `public/questions/Screenshot 2026-10-24 123421.png`
- [DataSync: supported locations and transfers](https://docs.aws.amazon.com/datasync/latest/userguide/what-is-datasync.html)
