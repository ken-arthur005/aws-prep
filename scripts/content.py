"""Editorial answer reviews. Indexes refer to data/extracted.json, never screenshot marks.

Each reviewed record has a rationale for every option and primary AWS reading.
Unresolved/obsolete source questions are intentionally not silently corrected.
"""
REVIEWS = {}
HOLDS = {}
FIXES = {}
MERGES = {38: [37]}

DOCS = {
    "cfnfull": ("CloudFormation: templates, stacks and change sets", "https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html"),
    "cfnoutputs": ("CloudFormation: template Outputs", "https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/outputs-section-structure.html"),
    "cfnDrift": ("CloudFormation drift detection: considerations", "https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.html"),
    "crr": ("S3 replication and Batch Replication", "https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication.html"),
    "trailvalidation": ("CloudTrail: log file integrity validation", "https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-log-file-validation-intro.html"),
    "hooks": ("EC2 Auto Scaling: lifecycle hooks", "https://docs.aws.amazon.com/autoscaling/ec2/userguide/lifecycle-hooks.html"),
    "tracking": ("EC2 Auto Scaling: target tracking", "https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scaling-target-tracking.html"),
    "spot": ("EC2 Auto Scaling: mixed instances and purchase options", "https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-mixed-instances-groups.html"),
    "peering": ("VPC peering: private connectivity and limits", "https://docs.aws.amazon.com/vpc/latest/peering/what-is-vpc-peering.html"),
    "transferaccel": ("S3 Transfer Acceleration", "https://docs.aws.amazon.com/AmazonS3/latest/userguide/transfer-acceleration.html"),
    "sessionmanager": ("Systems Manager Session Manager", "https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager.html"),
    "emr": ("Amazon EMR: managed big data processing", "https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-what-is-emr.html"),
    "consistency": ("S3: strong read-after-write consistency", "https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html#ConsistencyModel"),
    "versioning": ("S3: versioning and delete markers", "https://docs.aws.amazon.com/AmazonS3/latest/userguide/Versioning.html"),
    "objectlock": ("S3 Object Lock: retention and legal holds", "https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock.html"),
    "cferror": ("CloudFront: custom error responses", "https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/GeneratingCustomErrorResponses.html"),
    "cfinvalidate": ("CloudFront: invalidating cached files", "https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Invalidation.html"),
    "glue": ("Glue crawlers and the Data Catalog", "https://docs.aws.amazon.com/glue/latest/dg/add-crawler.html"),
    "standby": ("EC2 Auto Scaling: temporarily remove instances with Standby", "https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-enter-exit-standby.html"),
    "clientvpn": ("AWS Client VPN: secure remote user access", "https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/what-is.html"),
    "placement": ("EC2: placement groups", "https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups.html"),
    "steps": ("Step Functions: visual workflow orchestration", "https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html"),
    "ecsnetwork": ("ECS: awsvpc task networking", "https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-networking-awsvpc.html"),
    "metadata": ("EC2: accessing instance metadata with IMDSv2", "https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-instance-metadata-service.html"),
    "fargate": ("Fargate: serverless compute for containers", "https://docs.aws.amazon.com/AmazonECS/latest/developerguide/AWS_Fargate.html"),
    "athena": ("Athena: serverless SQL queries over S3", "https://docs.aws.amazon.com/athena/latest/ug/what-is.html"),
    "quicksight": ("QuickSight: supported data sources", "https://docs.aws.amazon.com/quicksight/latest/user/supported-data-sources.html"),
    "fsxwindows": ("FSx for Windows: Active Directory and SMB", "https://docs.aws.amazon.com/fsx/latest/WindowsGuide/what-is.html"),
    "kinesis": ("Kinesis Data Streams: stream consumers and retention", "https://docs.aws.amazon.com/streams/latest/dev/key-concepts.html"),
    "dms": ("DMS: data migration and change replication", "https://docs.aws.amazon.com/dms/latest/userguide/Welcome.html"),
    "datasync": ("DataSync: supported locations and transfers", "https://docs.aws.amazon.com/datasync/latest/userguide/what-is-datasync.html"),
    "waf": ("WAF: use-case-specific managed rule groups", "https://docs.aws.amazon.com/waf/latest/developerguide/aws-managed-rule-groups-use-case.html"),
    "ad": ("Directory Service: choosing a directory option", "https://docs.aws.amazon.com/directoryservice/latest/admin-guide/what_is.html"),
    "redshift": ("Redshift: purchasing reserved nodes", "https://docs.aws.amazon.com/redshift/latest/mgmt/purchase-reserved-node-instance.html"),
    "orgbilling": ("Organizations: consolidated billing", "https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html"),
    "orgmove": ("Organizations: leaving an organization", "https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts_leave-as-member.html"),
    "privatelink": ("PrivateLink: endpoint services", "https://docs.aws.amazon.com/vpc/latest/privatelink/endpoint-service-overview.html"),
    "rdsencrypt": ("RDS: encrypting existing database resources", "https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.Encryption.html"),
    "publicip": ("EC2: public IPv4 addresses and stop/start behavior", "https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-instance-addressing.html"),
    "efa": ("EC2: Elastic Fabric Adapter for HPC", "https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/efa.html"),
    "scheduled": ("EC2 Auto Scaling: scheduled scaling", "https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-scheduled-scaling.html"),
    "s3events": ("S3: event notifications", "https://docs.aws.amazon.com/AmazonS3/latest/userguide/EventNotifications.html"),
    "pit": ("RDS: automated backups and point-in-time recovery", "https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithAutomatedBackups.html"),
    "cognito": ("Cognito: user pools and identity pools", "https://docs.aws.amazon.com/cognito/latest/developerguide/what-is-amazon-cognito.html"),
    "gateway": ("Storage Gateway: cached versus stored volumes", "https://docs.aws.amazon.com/storagegateway/latest/vgw/WhatIsStorageGateway.html"),
    "presign": ("S3: uploading objects using presigned URLs", "https://docs.aws.amazon.com/AmazonS3/latest/userguide/PresignedUrlUploadObject.html"),
    "dynamostream": ("DynamoDB Streams and Lambda", "https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Streams.Lambda.html"),
    "globaltable": ("DynamoDB global tables", "https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GlobalTables.html"),
    "beanstalk": ("Elastic Beanstalk: application environments", "https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/Welcome.html"),
    "vpn": ("AWS Site-to-Site VPN: encrypted hybrid connectivity", "https://docs.aws.amazon.com/vpn/latest/s2svpn/VPC_VPN.html"),
    "ram": ("RAM: sharing supported AWS resources", "https://docs.aws.amazon.com/ram/latest/userguide/what-is.html"),
    "license": ("License Manager: license usage management", "https://docs.aws.amazon.com/license-manager/latest/userguide/license-manager.html"),
    "dns": ("Route 53: alias records and DNS record types", "https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/ResourceRecordTypes.html"),
    "routing": ("Route 53: choosing a routing policy", "https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html"),
    "s3": ("S3 storage classes and access patterns", "https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html"),
    "s3limits": ("Current S3 multipart upload limits", "https://docs.aws.amazon.com/AmazonS3/latest/userguide/qfacts.html"),
    "lifecycle": ("S3 Lifecycle: abort incomplete multipart uploads", "https://docs.aws.amazon.com/AmazonS3/latest/userguide/mpu-abort-incomplete-mpu-lifecycle-config.html"),
    "kms": ("AWS KMS: asymmetric and symmetric keys", "https://docs.aws.amazon.com/kms/latest/developerguide/symmetric-asymmetric.html"),
    "kmspolicy": ("AWS KMS: key policies", "https://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html"),
    "endpoint": ("AWS KMS: private connections through VPC endpoints", "https://docs.aws.amazon.com/kms/latest/developerguide/kms-vpc-endpoint.html"),
    "iam": ("IAM: roles and temporary credentials", "https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html"),
    "scp": ("Organizations: service control policies", "https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html"),
    "efs": ("EFS: lifecycle management", "https://docs.aws.amazon.com/efs/latest/ug/lifecycle-management-efs.html"),
    "lustre": ("FSx for Lustre: deployment options", "https://docs.aws.amazon.com/fsx/latest/LustreGuide/using-fsx-lustre.html"),
    "ebs": ("EBS volume types: IOPS and throughput", "https://docs.aws.amazon.com/ebs/latest/userguide/ebs-volume-types.html"),
    "archive": ("EBS Snapshots Archive", "https://docs.aws.amazon.com/ebs/latest/userguide/snapshot-archive.html"),
    "aurora": ("Aurora: cluster, reader, instance and custom endpoints", "https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Overview.Endpoints.html"),
    "auroraha": ("Aurora high availability and storage recovery", "https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Concepts.AuroraHighAvailability.html"),
    "serverless": ("Aurora Serverless v2: automatic capacity scaling", "https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-serverless-v2.html"),
    "rds": ("RDS: Multi-AZ deployments", "https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.MultiAZ.html"),
    "snapshot": ("RDS: sharing a DB snapshot", "https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ShareSnapshot.html"),
    "neptune": ("Amazon Neptune: purpose-built graph database", "https://docs.aws.amazon.com/neptune/latest/userguide/intro.html"),
    "documentdb": ("Amazon DocumentDB: how it works", "https://docs.aws.amazon.com/documentdb/latest/developerguide/how-it-works.html"),
    "dynamo": ("DynamoDB: core components and access patterns", "https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.CoreComponents.html"),
    "ecs": ("ECS Anywhere: external instances and agents", "https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-anywhere.html"),
    "eks": ("EKS Anywhere: on-premises Kubernetes", "https://anywhere.eks.amazonaws.com/docs/overview/"),
    "cloudwatch": ("CloudWatch: collect host metrics with the unified agent", "https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Install-CloudWatch-Agent.html"),
    "xray": ("AWS X-Ray: distributed tracing", "https://docs.aws.amazon.com/xray/latest/devguide/aws-xray.html"),
    "cloudtrail": ("CloudTrail Lake: querying and availability changes", "https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-lake.html"),
    "ssm": ("Systems Manager: Run Command", "https://docs.aws.amazon.com/systems-manager/latest/userguide/run-command.html"),
    "parameter": ("Systems Manager Parameter Store: SecureString parameters", "https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-parameter-store.html"),
    "mgn": ("Application Migration Service: server rehosting", "https://docs.aws.amazon.com/mgn/latest/ug/what-is-application-migration-service.html"),
    "macie": ("Macie: discovering sensitive S3 data", "https://docs.aws.amazon.com/macie/latest/user/what-is-macie.html"),
    "inspector": ("Inspector: automated vulnerability management", "https://docs.aws.amazon.com/inspector/latest/user/what-is-inspector.html"),
    "vpc": ("VPC: route tables and local routing", "https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Route_Tables.html"),
    "s3endpoint": ("VPC: gateway endpoints for S3", "https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-s3.html"),
    "flow": ("VPC Flow Logs: VPC, subnet and network-interface scopes", "https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html"),
    "nat": ("VPC: NAT gateway availability and routing", "https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html"),
    "cloudfront": ("CloudFront: private content with signed URLs and cookies", "https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html"),
    "acm": ("CloudFront: HTTPS certificate requirements", "https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cnames-and-https-requirements.html"),
    "alb": ("Application Load Balancer: listener rule conditions", "https://docs.aws.amazon.com/elasticloadbalancing/latest/application/rule-condition-types.html"),
    "ga": ("Global Accelerator: endpoints and network performance", "https://docs.aws.amazon.com/global-accelerator/latest/dg/what-is-global-accelerator.html"),
    "as": ("EC2 Auto Scaling: health checks and replacement", "https://docs.aws.amazon.com/autoscaling/ec2/userguide/health-checks-overview.html"),
    "savings": ("Savings Plans: Compute Savings Plans", "https://docs.aws.amazon.com/savingsplans/latest/userguide/what-is-savings-plans.html"),
    "apigw": ("API Gateway: execution and access logging", "https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-logging.html"),
    "privateapi": ("API Gateway: private integrations", "https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-private-integration.html"),
    "appsync": ("AppSync: managed GraphQL APIs", "https://docs.aws.amazon.com/appsync/latest/devguide/what-is-appsync.html"),
    "video": ("Kinesis Video Streams: video ingestion and storage", "https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/what-is-kinesis-video.html"),
    "dr": ("AWS Well-Architected: disaster recovery strategies", "https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/plan-for-disaster-recovery-dr.html"),
    "cfn": ("CloudFormation: cfn-init metadata processing", "https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/cfn-init.html"),
    "requester": ("S3: Requester Pays buckets", "https://docs.aws.amazon.com/AmazonS3/latest/userguide/RequesterPaysBuckets.html"),
    "sse": ("S3: server-side encryption options", "https://docs.aws.amazon.com/AmazonS3/latest/userguide/serv-side-encryption.html"),
    "clientside": ("S3: client-side encryption", "https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingClientSideEncryption.html"),
    "lambda": ("Lambda: execution role permissions", "https://docs.aws.amazon.com/lambda/latest/dg/lambda-intro-execution-role.html"),
    "sqs": ("SQS: queue types and delivery semantics", "https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.html"),
    "sns": ("SNS: fanout to SQS queues", "https://docs.aws.amazon.com/sns/latest/dg/sns-sqs-as-subscriber.html"),
    "secrets": ("Secrets Manager: automatic rotation", "https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotating-secrets.html"),
}


def r(index, answer, domain, topic, takeaway, explanations, docs, note=""):
    REVIEWS[index] = {"correct": [ord(a) - 65 for a in answer], "domain": domain, "topic": topic, "takeaway": takeaway, "explanations": explanations, "docs": docs.split(), "note": note}


def h(index, note, domain="performance", topic="Architecture tradeoffs", docs="", takeaway=""):
    HOLDS[index] = {"note": note, "domain": domain, "topic": topic, "docs": docs.split(), "takeaway": takeaway}


r(0,"C","performance","DNS & routing","A CNAME cannot live at the zone apex. A Route 53 alias can point the apex to an ALB; a CNAME is valid for www.",[
"The apex record is a CNAME, which DNS does not permit. An alias for www does not repair the invalid apex.",
"Both records are CNAMEs, so the root-domain record remains invalid even though a CNAME for www is allowed.",
"The alias supports the root domain and tracks the ALB endpoint. The www CNAME can point to that endpoint or the root name.",
"Ordinary A/AAAA records require IP addresses; an ALB has changing addresses and should be targeted with aliases or a valid subdomain CNAME."],"dns")
h(1,"CloudTrail Lake is the intended historical answer, but it closed to new customers on May 31, 2026. Existing customers can continue using it. The question does not establish customer eligibility. Trails, S3 and Athena are a current alternative, but that complete option is absent.","secure","Audit & observability","cloudtrail")
h(2,"The wording reverses the direction of Outposts: Outposts brings AWS infrastructure on premises; it does not extend an arbitrary existing database into an AWS Region. No option specifies the required secure hybrid database connection.","resilient","Hybrid architectures","vpc")
r(3,"C","performance","Database scaling","Aurora Serverless v2 automatically adjusts database compute capacity within configured limits for variable workloads.",[
"Aurora alone does not specify serverless compute; a provisioned Aurora cluster does not automatically resize its writer to match every change in demand.",
"A provisioned RDS MySQL instance can scale storage, but it does not provide the automatic serverless compute behavior requested.",
"Aurora Serverless automatically adjusts compute capacity, reducing the need to manually choose and resize provisioned instances.",
"Provisioned RDS PostgreSQL requires instance sizing and does not imply automatic serverless compute scaling."],"serverless")
r(4,"B","secure","Fleet management","SSM Run Command executes commands across managed instances without opening inbound SSH. Instances still need the agent, IAM permissions and service connectivity.",[
"Config records configurations and evaluates rules. It is not a command-distribution engine for installing packages on a fleet.",
"An appropriate instance role enables SSM-managed operation, and Run Command can target and patch the fleet in parallel without inbound port 22.",
"Session Manager supports interactive access without inbound SSH, but individually patching 100 hosts is unnecessarily manual; calling it browser-based SSH is also imprecise.",
"Sharing SSH credentials violates the stated access restriction and increases credential exposure. It also fails the parallel fleet-management requirement."],"ssm")
h(5,"The scenario omits required IOPS and throughput. gp3 with st1 can satisfy some database workloads, while higher requirements may need provisioned-IOPS SSD. Several choices can be valid without the missing performance targets.","cost","Block storage","ebs")
r(6,"A","secure","Encryption & key management","Digital signatures use an asymmetric signing key: protect the private key and let recipients verify with the public key. Grant kms:Sign only to the sender.",[
"An asymmetric SIGN_VERIFY KMS key signs with the private key and verifies with its public key. The key policy can restrict signing to the sending application.",
"CloudHSM is a hardware security service, not a KMS key type. It can support custom cryptography but adds management the question does not require.",
"A symmetric encryption key encrypts and decrypts with the same secret; it is not an asymmetric digital-signature key.",
"Customer managed describes ownership and policy control, not the cryptographic key type. A customer-managed key could be symmetric or asymmetric."],"kms kmspolicy")
h(7,"The intended cryptographic type is a symmetric 256-bit KMS key, but key type and key ownership are different dimensions. An AWS-managed key is not one application-wide key that the application can arbitrarily reuse across S3, Lambda and DynamoDB. The question conflates these requirements.","secure","Encryption & key management","kms")
h(8,"None of these configurations establishes the stated direct CloudHSM-backed TDE integration for a standard RDS instance. RDS-managed encryption and TDE support vary by engine; do not infer a valid integration simply because Oracle and CloudHSM appear together.","secure","Database encryption","kmspolicy rds")
r(9,"D","resilient","Infrastructure automation","cfn-init reads AWS::CloudFormation::Init metadata and installs packages, writes files and starts services during instance configuration.",[
"cfn-hup detects changes to resource metadata and triggers hooks; it is not the initial package-installation processor.",
"cfn-signal reports success or failure to a wait condition or creation policy. It does not install software from Init metadata.",
"cfn-get-metadata retrieves metadata, but does not itself apply the installation and configuration instructions.",
"cfn-init both reads the Init metadata and performs its declared package, file and service configuration."],"cfn")
FIXES[11] = {"option": {3: "Use AWS Application Migration Service (AWS MGN) to automate the migration process, ensuring minimal downtime."}}
r(10,"D","secure","Private service access","Use a KMS interface VPC endpoint and a key-policy condition on aws:SourceVpce when access must come through a specific endpoint.",[
"An internet-facing proxy does not satisfy the private AWS network path and adds an unnecessary instance to operate.",
"A NAT gateway reaches public service endpoints. NACLs filter IP traffic, not permission to use individual KMS keys.",
"aws:SourceVpc scopes the originating VPC, not one specific endpoint. It is broader than the endpoint-level restriction offered in D.",
"The interface endpoint supplies private connectivity, and aws:SourceVpce can restrict KMS key use to the specified endpoint, combined with least-privilege identity/key permissions."],"endpoint kmspolicy",note="A VPC endpoint condition is not a substitute for authorizing the intended principals and KMS operations. Avoid policies that inadvertently block AWS service integrations.")
r(11,"D","resilient","Migration","MGN rehosts complete servers using continuous replication and a controlled cutover; database migration and file transfer are narrower tasks.",[
"DataSync moves files and objects. It does not rehost an entire server application and operating system.",
"DMS migrates supported database data and can replicate changes, but it does not migrate the entire CRM application server.",
"Application Discovery gathers inventory and dependencies for planning; discovery is not the server replication and cutover mechanism.",
"MGN replicates server disks and supports test launches and cutover to EC2 with a short final interruption."],"mgn")
r(12,"C","secure","Sensitive data discovery","Macie discovers sensitive data in S3. Distinguish data classification from threat detection and host vulnerability scanning.",[
"GuardDuty looks for malicious or suspicious activity. S3 threat detection is not scanning object contents for PII classification.",
"Detective supports investigation of security activity and relationships; it is not the sensitive-data discovery service for S3 objects.",
"Macie uses managed and custom data identifiers to inspect S3 objects and produce sensitive-data findings for investigation and compliance.",
"Inspector identifies software vulnerabilities and exposure in supported workloads; it does not perform Macie's S3 object-content PII scanning."],"macie inspector")
r(13,"B","cost","Object storage classes","For durable, long-retained data with rare access and no fast-retrieval requirement, Deep Archive minimizes storage cost; budget for restore delays and retrieval charges.",[
"S3 Standard and cross-Region replication provide availability and regional copies but retain a higher storage cost than archive tiers.",
"Lifecycle transitions to Deep Archive suit rarely retrieved, decade-long data retention when asynchronous restoration is acceptable.",
"EBS is attached block storage. Maintaining volumes and snapshots is not the lowest-overhead object archive for petabytes of research data.",
"FSx for Lustre is a high-performance processing filesystem. Its purpose is not low-cost long-term archival storage."],"s3",note="Retention for compliance may additionally require S3 Object Lock and an appropriate retention policy; a storage class alone does not enforce immutability.")
h(14,"This question does not distinguish fast storage of recommendation results from generating recommendations over relationships. ElastiCache can serve low-latency values, while Neptune supports graph-based recommendations. The missing data model prevents a unique answer.","performance","Database selection","neptune")
h(15,"Generic Rekognition labels do not guarantee identification of the required animal species. Custom Labels can use transfer learning, but it still requires labeled examples and training. The species accuracy requirements and meaning of 'without training from scratch' are unclear.","performance","AI service selection")
h(16,"Amazon Polly Brand Voice is historical/specialized material. Availability and customer access must be established before recommending it as a general deployment choice. It is low-priority material for a four-day SAA revision plan.","performance","AI service selection")
h(17,"Comprehend asynchronous jobs use S3 for input and output. The proposed answer that writes directly to Redshift omits a necessary output/ingestion step, so none of the choices completely describes the integration.","performance","Data analytics")
h(18,"Lex is the conversational interface, while Personalize generates recommendations. One service alone does not satisfy both conversational assistance and personalized financial recommendations as worded.","performance","AI service selection")
r(19,"A","secure","TLS & certificates","CloudFront viewer certificates in ACM must be in us-east-1, regardless of the origin's Region. Imported certificates require renewal/reimport management.",[
"Import the viewer certificate into ACM in us-east-1 and attach it to CloudFront. Its expiration can be monitored; imported certificates are not automatically renewed by ACM.",
"The EC2 origin's Region does not determine the Region of the CloudFront viewer certificate. ACM certificates for CloudFront must be in us-east-1.",
"IAM server certificates are a separate legacy storage mechanism, not a service named IAM Certificate Manager in a Region. ACM in us-east-1 is the intended managed integration.",
"IAM Certificate Manager is not the stated regional service, and the origin's Region is not the ACM viewer-certificate requirement."],"acm")
r(20,"C","performance","Database scaling","Separate Aurora read traffic from writes: the reader endpoint distributes read connections across Aurora Replicas, while the cluster endpoint targets the writer.",[
"A custom endpoint can target a chosen subset of instances, but no special subset is required. The built-in reader endpoint is the simpler fit.",
"The cluster endpoint targets the primary writer, so sending the same read workload there preserves the overload.",
"The reader endpoint connection-balances read-only traffic across available replicas, offloading the primary. The application must direct writes to the writer endpoint.",
"An instance endpoint targets one specific instance and does not distribute reads across the five replicas."],"aurora")
h(21,"Redshift Spectrum is the correct query concept, but Spectrum's S3 access does not use a cluster's enhanced VPC routing/S3 endpoint in the manner asserted. The options conflate the query service and network path, so the seemingly intended answer is not scored.","performance","Data analytics")
r(22,"A","secure","Encryption & key management","SSE-C lets S3 perform encryption while the client supplies the encryption key on each request; S3 does not retain that key for later requests.",[
"SSE-C matches server-side cryptography with customer-held key material. Supply the key over HTTPS on upload and retrieval and protect it yourself.",
"SSE-S3 uses S3-managed keys. The customer does not retain and provide the secret key as required.",
"SSE-KMS relies on keys managed in KMS, even when the customer controls the key policy. It is not the customer-supplied-key model described here.",
"Client-side encryption would require the client or an encryption library to encrypt/decrypt data before and after S3 operations, contrary to the requested server-side handling."],"sse",note="SSE-C availability/default-blocking controls can vary for new buckets and security configurations. Verify bucket settings before deploying it; do not lose the key.")
r(23,"D","performance","Data analytics","Athena provides serverless SQL over S3; QuickSight provides visualization. This avoids building and operating a cluster or a custom dashboard.",[
"Spectrum can query S3, but Managed Service for Apache Flink is a stream-processing service, not the dashboard visualization layer.",
"Redshift and a custom dashboard add provisioning/design work when serverless S3 querying and managed visualization meet the requirements.",
"EMR supports large-scale data processing but adds cluster/job complexity that is unnecessary for this straightforward SQL-and-dashboard use case.",
"Athena queries the S3 data in place, and QuickSight can visualize the results with a managed dashboard."],"athena quicksight")
h(24,"Glacier retrieval pricing, bulk retrieval availability, latency and request patterns differ by class. The options refer to an unspecified free retrieval quota and treat Deep Archive bulk retrieval as automatically cheapest. A retrieval SLA and actual costs are needed.","cost","Object storage classes","s3")
r(25,"D","resilient","Serverless APIs","AppSync supplies a managed GraphQL layer and real-time subscriptions over multiple data sources.",[
"Data Firehose delivers streaming data into supported destinations. It does not expose a general GraphQL query and mutation API.",
"Neptune is a graph database, not a managed GraphQL aggregation API across arbitrary databases and microservices.",
"API Gateway supports REST, HTTP and WebSocket APIs; AppSync is the purpose-built managed GraphQL solution with subscriptions.",
"AppSync connects GraphQL resolvers to multiple sources and supports real-time updates without managing API servers."],"appsync")
r(26,"B","performance","High-performance file storage","Lustre Scratch is optimized for temporary processing where files can be recreated; persistent deployments are for durable, longer-lived workloads.",[
"Persistent Lustre provides durable storage and higher availability, but those additional guarantees are not needed for temporary, reproducible processing.",
"Scratch Lustre supplies high aggregate parallel throughput and burst capability for short-lived processing without paying for the persistent deployment model.",
"EFS is shared elastic NFS, but it is not the specialized Lustre parallel filesystem targeted at the stated HPC performance pattern.",
"FSx for Windows serves SMB and Windows filesystem semantics, rather than the POSIX-oriented Lustre HPC requirement."],"lustre")
r(28,"D","resilient","VPC routing","Associating a secondary VPC CIDR automatically creates local routes so resources inside that CIDR can route within the VPC.",[
"A peering target routes to another VPC. The new CIDR belongs to this VPC, not a peer.",
"A virtual private gateway target is for VPN/hybrid routing, not a locally associated VPC CIDR.",
"Direct Connect is a hybrid connectivity service and does not replace the VPC local route for a secondary CIDR.",
"The route table gains a route for 30.0.0.0/20 with target local, just as it has a local route for the primary CIDR."],"vpc")
r(29,"C","cost","Object storage classes","Glacier Instant Retrieval is designed for long-lived archive data accessed roughly quarterly but still requiring millisecond retrieval.",[
"Glacier Flexible Retrieval requires a restore operation and is not immediately available with millisecond access.",
"Deep Archive trades the lowest storage cost for long restore times, so it violates the immediate-access requirement.",
"Glacier Instant Retrieval provides millisecond access to rarely accessed archives, matching the quarterly pattern and long retention.",
"Standard-IA also provides millisecond access, but Glacier Instant Retrieval is designed for still rarer access and can reduce storage cost for this pattern."],"s3",note="Compare total storage plus retrieval costs for the actual dataset. Retention enforcement is separate from choosing a storage class.")
h(30,"SCPs limit principals in member accounts, not external principals merely because they access a member account's bucket. The wording omits how the restriction is implemented, and the bucket-policy option unnecessarily grants write access to an auditor. A unique least-privilege answer is not established.","secure","Cross-account access","scp iam")
r(31,"C","cost","Shared file storage","EFS supplies managed elastic NFS, and lifecycle management can move cold files into lower-cost access classes.",[
"S3 is object storage and does not natively expose the required NFS v4.1 shared filesystem interface.",
"S3 Glacier classes are object archives, not a directly mounted elastic NFS filesystem.",
"EFS grows and shrinks with stored files, supports NFS v4.1 and lifecycle policies, and avoids managing filesystem servers.",
"Lustre is optimized for high-performance parallel processing rather than this infrequent-access NFS workload."],"efs")
r(32,"C","secure","Network observability","Choose the narrowest useful Flow Log scope: a subnet log captures all affected ENIs without logging the other 99 subnets.",[
"VPC-wide logging includes the other 99 subnets, increasing log volume beyond the affected application scope.",
"Individual ENI logs are granular, but configuring 50 logs separately creates unnecessary operational work and is brittle when instances change.",
"A subnet Flow Log captures network-flow metadata for the affected subnet's interfaces, balancing coverage with low configuration effort and volume.",
"Subnet-scoped Flow Logs are a supported and appropriate troubleshooting tool, so 'none' is not correct."],"flow")
r(33,"AD","secure","Secrets & operations","Application Manager helps investigate application resources; Parameter Store SecureString suits centrally managed secrets when automatic rotation is unnecessary.",[
"Application Manager groups application resources and operational context to help investigate and resolve issues more quickly.",
"AppSync manages GraphQL APIs; it is not an application failure-investigation console.",
"Secrets Manager is a valid secret store, but its rotation-focused capabilities and pricing are unnecessary here compared with appropriately configured standard SecureString parameters.",
"Parameter Store SecureString uses KMS protection and IAM access control. The application retrieves values rather than hard-coding them; rotation is managed separately.",
"A private S3 bucket plus VPN adds an ad hoc secret-delivery system instead of the purpose-built parameter store and fine-grained parameter access."],"parameter",note="Standard Parameter Store parameters have different cost/quota characteristics from advanced parameters. Grant only the needed ssm:GetParameter and kms:Decrypt permissions.")
h(34,"A zonal NAT gateway per AZ can improve outbound egress availability, but RDS patching is AWS-managed and database connections within a VPC do not traverse a NAT gateway. Healthy RDS connection loss is not explained by the stated premise.","resilient","Network availability","nat rds")
r(35,"D","performance","Database selection","Graph workloads are about traversing relationships, not just storing JSON or key-value records. Neptune is the purpose-built graph database.",[
"DocumentDB stores and queries documents. It is not the purpose-built graph traversal engine for billions of connected relationships.",
"DynamoDB scales key-value/document access, but arbitrary graph traversal would require application-side modeling and multiple lookups.",
"Aurora is relational; repeated joins over deep, highly connected relationships are not the specialized graph model described.",
"Neptune supports property-graph/RDF relationship queries and is designed for highly connected data such as social and recommendation graphs."],"neptune")
r(36,"A","performance","Database selection","DocumentDB is the managed MongoDB-compatible choice among these options, but compatibility must be tested rather than assumed perfect.",[
"DocumentDB provides MongoDB-compatible APIs and managed operations, making it the closest fit for this migration among the listed services.",
"DynamoDB has a different data model and API; a MongoDB application would need substantial access-layer changes.",
"Keyspaces is Cassandra-compatible, not MongoDB-compatible.",
"Neptune is a graph database and does not provide the MongoDB document API."],"documentdb",note="The source says no code changes, which cannot be guaranteed for arbitrary MongoDB features. Check supported APIs, indexes and behavioral differences during migration assessment.")
FIXES[38] = {"prompt": "A multi-account environment uses AWS Organizations. All accounts in OU-development must be restricted from creating regional resources outside eu-west-1. A policy denies actions when aws:RequestedRegion is not eu-west-1. Where should this policy be applied?", "option": {1: "Add the policy as a Service Control Policy (SCP) and attach it to OU-development."}}
r(38,"B","secure","Multi-account governance","Attach an SCP to the target OU to set a permission ceiling for all its member accounts. SCPs never grant permissions.",[
"A boundary on one developer role does not enforce the restriction across all roles and accounts in the OU.",
"An OU-level SCP is inherited by accounts in that OU and can deny regional operations outside the permitted Region.",
"An SCP on the organization root would apply more broadly than the requested development OU.",
"An identity policy on one role is not an organization-wide guardrail and can leave other principals unrestricted."],"scp",note="Production region-deny policies need explicit handling of global services. aws:RequestedRegion describes the requested service endpoint, not every possible cross-Region effect.")
h(39,"The old 5-TB object-limit premise is outdated. Current S3 documentation lists a maximum object size of 48.8 TiB with multipart upload. A 12-TB object is not inherently invalid on that old limit alone; Snowball/device/tool limits must be assessed separately.","performance","Object storage limits","s3limits")
r(40,"A","secure","Data ownership","Using an AWS AI service does not transfer ownership of customer content to AWS; data-use and retention terms are separate questions.",[
"The customer retains ownership of their content. Service-specific processing, retention and opt-out terms should still be reviewed.",
"AWS does not acquire ownership of customer content simply because its service processes the data.",
"Processing in Comprehend does not automatically transfer ownership to a third-party company.",
"The use of an AWS service does not create joint ownership of the customer's content."],"macie",note="Ownership is distinct from permitted processing, retention, privacy and AI service-improvement terms. Consult the applicable AWS agreement and service data-protection documentation.")
r(41,"A","resilient","Hybrid containers","ECS Anywhere uses the SSM agent for registration/credentials, the ECS agent for task orchestration, and a container runtime such as Docker.",[
"These are the required Linux components for the described ECS Anywhere setup: Systems Manager agent, ECS container agent and Docker.",
"SSM and Docker alone do not include the ECS container agent that coordinates container tasks with the ECS control plane.",
"The ECS agent and Docker omit the SSM agent required by the ECS Anywhere registration and credential mechanism.",
"CloudWatch's monitoring agent does not replace the required Systems Manager agent."],"ecs")
h(42,"EKS Anywhere can run on bare metal, but its control plane and nodes are customer-managed. The question explicitly asks for AWS-managed on-premises Kubernetes, so its intended EKS Anywhere answer contradicts that requirement.","resilient","Hybrid containers","eks")
r(43,"B","resilient","Hybrid containers","ECS Anywhere extends the ECS control plane to customer-managed external servers, with the necessary agents and runtime installed.",[
"EKS is Kubernetes; adding an SSM agent does not turn it into the described ECS external-instance management model.",
"ECS Anywhere registers on-premises servers with ECS and uses the SSM/ECS agents for control and credentials, enabling a consistent ECS management surface.",
"ECR stores container images. A registry and Docker do not supply centralized container scheduling across environments.",
"EKS Distro is a Kubernetes distribution; it is not the managed ECS control-plane integration described."],"ecs")
r(44,"B","performance","Distributed tracing","Use distributed traces to follow one request through services and find latency bottlenecks. Metrics and audit logs answer different questions.",[
"CloudWatch provides metrics and logs, and can present trace-related data, but the specific distributed-tracing service among the choices is X-Ray.",
"X-Ray traces requests across instrumented services and helps identify slow downstream calls, errors and service-to-service bottlenecks.",
"EventBridge routes events; it is not a tracing system for following synchronous request latency.",
"CloudTrail audits AWS API activity; it does not provide end-to-end application request traces."],"xray cloudwatch")
h(45,"EKS Anywhere is intended for consistent Kubernetes operations outside AWS, but it is customer-managed. The question's short wording does not distinguish management of AWS-hosted EKS from consistent self-managed Kubernetes installations.","resilient","Hybrid containers","eks")
h(46,"The SQL examples omit an actual database user name and contain OCR damage in the plugin identifier. IAM database authentication uses a database user identified with AWSAuthenticationPlugin AS 'RDS', plus IAM permissions; malformed commands should not be memorized.","secure","Database authentication","iam")
h(47,"The options mix file locking, changes during transfer and verification-stage changes, whose behavior depends on the source protocol and task configuration. The source does not establish two unambiguous skipping causes; consult task error details rather than infer from the selected marks.","resilient","Data transfer")
r(48,"B","performance","Streaming ingestion","Use Kinesis Video Streams for timestamped video ingestion and retention. Data Streams is a general record stream, not the specialized video service.",[
"IoT Core manages device messaging and connectivity; it is not the managed durable video-stream ingestion and playback service requested.",
"Kinesis Video Streams ingests and stores video from cameras and makes it available for real-time or batch analysis by integrated consumers.",
"Kinesis Data Streams processes general data records and does not supply the specialized video ingestion, indexing and playback features.",
"Elastic Transcoder is a legacy media-transcoding service, not live camera video ingestion and analysis."],"video")
r(49,"A","cost","Compute pricing","Compute Savings Plans exchange a consistent dollars-per-hour commitment for discounts across eligible EC2, Fargate and Lambda usage.",[
"A Compute Savings Plan fits the spend-based commitment and can cover eligible EC2, Fargate and Lambda usage with flexibility across compute configurations.",
"EC2 Reserved Instances apply to matching EC2 usage, not the unified cross-service hourly-spend commitment for Fargate and Lambda.",
"Dedicated Hosts provide dedicated physical servers and license/control benefits, not the requested multi-service savings model.",
"Spot provides interruptible spare capacity without the stated spend commitment and is not a universal discount mechanism for all three services."],"savings")
r(50,"B","resilient","API observability","For REST API payload-level diagnostics, enable execution logging with data tracing. Access logs summarize request context rather than full bodies.",[
"Access logging records configured request/context fields, but does not itself log full request and response payloads.",
"REST API execution logging with data tracing can capture request/response details and payloads for troubleshooting.",
"CloudTrail records supported AWS API control activity; it is not the API Gateway application payload execution log.",
"CloudTrail execution logging is not the API Gateway payload logging feature."],"apigw",note="Payload logging can expose sensitive data. Enable data tracing deliberately, restrict log access and retention, and prefer scoped diagnostics over indiscriminate production logging.")
r(51,"C","secure","Private content delivery","Signed cookies authorize access to restricted CloudFront content without changing the original URL, and can cover multiple files.",[
"CloudFront signed URLs put the signature and policy information into the URL, conflicting with the unchanged-URL requirement.",
"S3 presigned URLs are temporary signed object URLs and change how the requester accesses the object; they do not provide CloudFront cookie authorization.",
"CloudFront signed cookies let the browser request the existing URLs while conveying time-limited authorization through cookies.",
"S3 does not offer the CloudFront signed-cookie private-content feature."],"cloudfront")
h(52,"NACL evaluation differs between workload subnets and transit-gateway attachment subnets, including direction-specific exceptions. The wording does not clearly identify the subnet/direction being evaluated, so the generic destination-IP answer may be misleading.","secure","Network access controls","vpc")
r(53,"A","secure","Database backups","Share an unencrypted manual RDS snapshot privately with specific account IDs. An authorized recipient can restore directly without first copying it.",[
"Private snapshot sharing restricts the eligible AWS accounts, and an unencrypted shared manual snapshot can be restored directly.",
"Public visibility exposes the snapshot to all AWS accounts, not just the specifically authorized recipients.",
"A recipient may copy a shared snapshot, but copying an unencrypted snapshot is not required before direct restore and adds unnecessary steps.",
"Making the snapshot public violates the access restriction; adding a copy does not repair that exposure."],"snapshot",note="Encrypted snapshots have additional KMS and sharing restrictions; these are not interchangeable with the unencrypted case.")
r(54,"B","resilient","Database availability","Aurora's distributed storage repairs failed storage segments, while replicas in different AZs provide compute failover. These are complementary protections.",[
"Cross-Region replicas are not needed to handle a disk failure inside the cluster; the answer also attributes disk repair to crash recovery rather than storage repair.",
"Aurora storage automatically repairs lost segments from replicated data. Multi-AZ Aurora Replicas additionally provide a ready compute failover target.",
"A survivable page cache reduces warm-up after some restarts; it is not the durable storage repair mechanism, and cross-Region deployment is unnecessary here.",
"Multi-AZ replicas help availability, but crash recovery is not the storage-level self-repair mechanism specifically addressing a failed disk."],"auroraha",note="Replicas themselves do not create the cluster's storage redundancy; Aurora's shared cluster volume already replicates storage across AZs.")
h(55,"A 20-minute RTO/RPO does not uniquely select pilot light versus warm standby. Both depend on replication, automation, scaling and tested recovery time; limited budget alone does not establish feasibility.","resilient","Disaster recovery","dr")
r(56,"D","resilient","DNS failover","Route 53 failover routing and health checks automate DNS responses for a primary/secondary topology. DNS caching still affects switchover time.",[
"Weighted routing distributes proportions of traffic; manual failover is not the required automatic health-based primary/secondary failover.",
"Manually editing records during a disaster adds operator delay and does not meet automatic failover.",
"A private hosted zone with manual record changes does not provide automatic health-based public application failover.",
"Failover routing can answer with the healthy primary or secondary according to configured health checks and target health evaluation."],"routing")
r(57,"C","performance","DNS & routing","Geolocation routing selects records by the user's geographic location. Geoproximity uses resource/user location and an optional bias; latency routing optimizes latency.",[
"Weighted routing splits traffic by assigned weights and does not ensure a country-specific site.",
"Geoproximity distributes based on distances and adjustable bias, not an exact country/continent-based content selection rule.",
"Geolocation routing matches the geographic location of DNS queries to configured records, suitable for country-specific versions of a site.",
"Multivalue routing returns multiple healthy records; it is not the policy for selecting a localized country site."],"routing",note="Configure an appropriate default record for locations that are not explicitly mapped. DNS query location can be influenced by the resolver and EDNS client subnet.")
r(58,"B","cost","Object storage billing","Requester Pays shifts eligible S3 request and download-transfer charges to authenticated requesters; the bucket owner continues paying storage.",[
"Moving to EFS does not implement S3 Requester Pays and changes the data-access interface unnecessarily.",
"Requester Pays matches the requested split: the bucket owner pays storage, while eligible request and transfer charges go to authenticated requesters.",
"Transfer Acceleration improves upload/download paths and can incur additional charges. It does not implement the requested billing ownership.",
"DataSync is a data-transfer tool; configuring a task does not activate S3 request billing to arbitrary external downloaders."],"requester",note="Requester Pays is not anonymous public access: requesters must authenticate and acknowledge the charges. Review supported access patterns and billing exceptions.")
r(59,"B","performance","Streaming ingestion","Kinesis Video Streams is built for durable camera-video ingestion with encryption; analytics runs in consumers or integrated services.",[
"Data Streams carries general streaming records, without the video-specific media storage and playback APIs.",
"Video Streams handles camera-video ingestion, durable retention and encrypted storage, enabling downstream real-time analytics.",
"Data Firehose buffers and delivers general streaming records to destinations; it is not the specialized camera video ingestion service.",
"QuickSight is a business-intelligence visualization service and does not ingest live camera feeds as a video streaming service."],"video")
r(60,"B","secure","Encryption & key management","Client-side encryption happens before upload. KMS can protect the data-encryption key while an encryption client handles the object encryption.",[
"SSE-S3 encrypts after S3 receives the object, so plaintext reaches the service endpoint and the client-side requirement is not met.",
"An appropriate client-side encryption library can encrypt before upload and use a customer-managed KMS key to protect data keys.",
"Object Lock enforces retention/immutability; it does not encrypt the content on the client.",
"Hard-coding the key in application code defeats secure key management and does not satisfy the AWS-managed key-storage requirement."],"clientside kms")
r(61,"B","secure","Vulnerability management","Inspector continuously assesses supported workloads for software vulnerabilities and unintended network exposure; GuardDuty detects threats instead.",[
"GuardDuty detects suspicious activity and threats; it is not the primary continuous CVE and package-vulnerability assessment tool.",
"Inspector performs automated vulnerability assessment and network-exposure analysis for supported EC2 workloads, producing findings for remediation workflows.",
"Detective helps investigate security events rather than scan installed software for missing security fixes.",
"Artifact provides compliance reports and agreements, not runtime vulnerability scanning."],"inspector")
r(62,"B","cost","Load balancing","One ALB can route HTTP requests to different target groups using host/path conditions, reducing unnecessary load balancer duplication.",[
"An NLB routes transport-layer traffic and cannot directly replace the ALBs' HTTP host/path routing behavior.",
"ALB listener rules can direct different hostnames or URL paths to the appropriate ECS service target groups on one ALB.",
"Log retention may affect cost, but disabling access logs does not address paying for 50 separate ALBs.",
"Replacing workloads with Lambda is a separate application migration and does not preserve the existing functionality without changes."],"alb")
h(63,"Both a missing CloudTrail S3 bucket-policy permission and an inadequate KMS key policy can prevent log delivery. The problem provides no error or policy evidence to choose uniquely between B and C.","secure","Audit & observability","kmspolicy cloudtrail")
r(64,"B","performance","High-performance file storage","FSx for Lustre supplies a parallel filesystem for HPC datasets and high aggregate throughput.",[
"FSx for NetApp ONTAP provides enterprise multiprotocol data management; Lustre is the specialized parallel HPC fit among the choices.",
"FSx for Lustre is purpose-built for parallel HPC and analytics file workloads needing high throughput and low latency.",
"FSx for Windows supplies managed SMB/Windows file sharing rather than the specialized parallel HPC filesystem.",
"FSx for OpenZFS provides managed ZFS file storage, but Lustre is the explicitly optimized parallel HPC option here."],"lustre")
h(65,"AWS-origin-to-CloudFront transfer is generally free; being in the 'same Region as CloudFront' is not meaningful because CloudFront is global. Cache hit ratio and origin request/processing costs should be analyzed, but the choices do not state a sound unique optimization.","cost","Content delivery","cloudfront")
h(66,"Timestream for LiveAnalytics matches the historical serverless time-series description, but it is no longer open to new customers. Timestream for InfluxDB is a distinct offering and not interchangeable with that claim. Eligibility is missing.","performance","Database selection")
r(67,"B","resilient","Database availability","DocumentDB separates compute from a distributed storage layer with six copies across three AZs, rather than storing durability in one instance.",[
"A single EBS volume would not provide the stated distributed multi-AZ storage architecture.",
"DocumentDB divides storage into segments replicated six ways across three AZs, providing redundancy independent of one database instance.",
"The primary instance is not the only durable copy; storage is a distributed cluster volume rather than just asynchronous instance-local copying.",
"DocumentDB does not store its cluster data inside customer DynamoDB tables or use global tables as its storage layer."],"documentdb")
r(68,"C","secure","Cross-account encryption","Sharing an encrypted AMI also requires authorizing the destination principal to use its customer-managed KMS key. AMI launch permission is not enough.",[
"AMIs are regional; an inaccessible regional AMI would fail differently. The given KMS decryption errors point to key authorization.",
"Supported EC2 instances can use encrypted EBS volumes; changing to an arbitrary instance type is not the indicated permission fix.",
"The source KMS key policy and destination identity permissions must allow the required operations, including decrypt/grant use for the encrypted backing snapshots.",
"Fast snapshot restore improves initialization performance and does not authorize KMS decryption."],"kmspolicy iam")
r(69,"D","resilient","Compute availability","A multi-AZ Auto Scaling group with desired capacity one can replace a failed instance, but it does not provide uninterrupted service during replacement.",[
"Latency routing is not the simplest automatic replacement mechanism for one private instance and does not repair the failed compute.",
"An Elastic IP is public and manual reassignment does not meet the private, automated recovery goal.",
"An ENI belongs to one AZ and cannot be moved to a standby instance in a different AZ.",
"An Auto Scaling group spanning multiple AZs can maintain desired capacity one and replace an unhealthy instance without a load balancer."],"as",note="This is the best cost-conscious replacement option listed, not zero-downtime high availability. The application must tolerate replacement and recover state appropriately.")
h(70,"Both a conflicting root-device attachment and duplicate filesystem labels can cause boot/mount problems. Without the attachment mapping, fstab/UUID configuration or logs, the stated symptom is not enough to pick one unique cause.","resilient","Block storage","ebs")
r(71,"A","performance","Database selection","DocumentDB fits document-oriented JSON data and flexible schemas among these choices; validate performance and MongoDB compatibility during migration.",[
"DocumentDB is a managed document database with MongoDB compatibility, matching the JSON document data model.",
"Neptune models graph relationships, not a general JSON document-store rehosting target.",
"Timestream is intended for time-series data, which is not the described content-management document model.",
"Keyspaces is Cassandra-compatible wide-column storage rather than a MongoDB-compatible JSON document database."],"documentdb",note="The source's millions-of-requests claim is not a capacity guarantee for an arbitrary cluster. Benchmark the actual access patterns and indexes.")
r(72,"B","resilient","Host observability","Default EC2 metrics do not include guest OS memory and filesystem usage. The unified CloudWatch agent collects host-level metrics and logs on EC2 and on-premises servers.",[
"Config tracks resource configuration and compliance, not continuous guest memory/disk metrics and arbitrary host logs.",
"The unified CloudWatch agent can collect selected memory, filesystem and other OS metrics plus logs from both EC2 and supported on-premises servers.",
"Session Manager provides remote sessions; it is not the ongoing host metric/log collector.",
"Basic EC2 monitoring supplies infrastructure metrics but not guest memory and disk-space usage without an agent or custom publishing."],"cloudwatch")
r(73,"B","secure","Private service access","An S3 gateway endpoint inserts routes to the S3 prefix list and avoids NAT/Internet Gateway traversal for supported same-Region access.",[
"S3 is an AWS service, not a customer VPC that can be joined through VPC peering.",
"A gateway endpoint routes S3 traffic privately using the service prefix list and an endpoint policy, without NAT or an internet gateway.",
"A NAT gateway is explicitly disallowed and is unnecessary for private S3 access through a gateway endpoint.",
"A public IP plus a security group does not provide the requested private endpoint path and still needs public routing."],"s3endpoint")
r(74,"C","secure","Workload IAM roles","Attach least-privilege SQS permissions to the Lambda execution role. An event source mapping uses those permissions to poll the queue.",[
"SQS queue policies are resource-based policies, not inline identity policies attached to a queue. They may be needed for cross-account access but do not replace the execution-role requirement.",
"A Lambda resource policy controls who can invoke the function; it does not grant the function permission to read SQS messages.",
"The execution role supplies temporary credentials and the needed SQS receive/delete/get-attributes permissions, scoped to the queue.",
"An SCP is a maximum-permission guardrail and never grants a function the SQS permissions it needs."],"lambda sqs")
r(75,"B","resilient","Shared file storage","Use EFS for concurrently mounted, elastic Linux NFS storage across AZs. EBS volumes are AZ-scoped block devices.",[
"EBS is block storage bound to an AZ; its limited Multi-Attach capability is not a general elastic multi-AZ shared filesystem.",
"Regional EFS provides managed NFS with elastic storage and concurrent access from Linux instances across AZs.",
"FSx for Windows is an SMB/Windows-oriented service and not the natural Linux NFS solution requested.",
"S3 is object storage; Transfer Acceleration does not turn it into a mounted POSIX shared filesystem."],"efs")
h(76,"The correct architectural idea is API Gateway private integration through a VPC Link to an appropriate private load balancer/backend. The option says only 'a VPC endpoint', which is not the same thing and is incomplete for this EC2 backend isolation requirement.","secure","Private APIs","privateapi")
r(77,"A","cost","Backup storage tiers","EBS Snapshots Archive is the managed low-cost tier for infrequently restored long-term snapshots; restoration takes time and minimum storage charges apply.",[
"Archive is the native EBS snapshot tier for rarely restored, long-retained backups, avoiding a custom export-and-restore workflow.",
"EBS managed snapshots are not exposed as objects that Lambda can simply move directly into a customer Glacier bucket.",
"Third-party export introduces operational effort and a different restoration workflow when a native managed archive tier exists.",
"The standard snapshot tier supports faster restoration but has higher storage cost for cold long-term backups."],"archive",note="Archived snapshots are full snapshots, with a minimum retention charge and a restore delay. Check the economics of each snapshot before archiving.")
r(78,"B","performance","Global network performance","Global Accelerator improves TCP/UDP routing to regional endpoints; the ALB still performs TLS termination. It does not act as an HTTP cache.",[
"Multiple ALBs do not by themselves supply global traffic steering, health-based routing or a complete multi-Region application deployment.",
"Global Accelerator routes users through the AWS global network to healthy ALB endpoints. The ALB can terminate TLS with its certificate.",
"S3 Transfer Acceleration optimizes S3 object transfers, not generic dynamic requests to an ALB.",
"Putting an NLB in front of an ALB may provide other capabilities, but it is not the global edge acceleration mechanism."],"ga alb")
h(79,"To block replacement/deletion during stack updates, a stack policy is the relevant control, but it is absent. DeletionPolicy Retain preserves a resource when removed or on stack deletion; it does not prevent all update replacement/deletion. The source conflates these controls.","resilient","Infrastructure automation","cfn")
r(80,"B","cost","Object storage lifecycle","Incomplete multipart parts are billed until completed or aborted. A lifecycle AbortIncompleteMultipartUpload rule cleans them up without a scheduled server.",[
"A cron job can call multipart APIs but introduces an instance, scheduling and maintenance that a native lifecycle rule avoids.",
"An S3 Lifecycle abort rule automatically removes incomplete upload parts after the configured number of days from initiation, reducing wasted storage.",
"Default encryption protects stored data and does not cause automatic cleanup of abandoned multipart parts.",
"S3 does not automatically discard every incomplete upload after ninety days; the parts remain until completed or aborted."],"lifecycle",note="The lifecycle threshold is days since upload initiation, not a sliding idle timer since the last uploaded part. That distinction matters in real implementations.")

r(82,"D","performance","Compute scaling","When the demand spike is predictable, scheduled scaling can provision capacity before it starts instead of reacting after performance degrades.",[
"A CPU-triggered policy reacts after demand rises; it does not guarantee that instances are ready at 09:00.",
"A second group does not by itself anticipate the spike and complicates capacity management.",
"A shorter cooldown may affect some scaling behavior but cannot eliminate instance warm-up or predict the start of a demand spike.",
"A scheduled action raises desired capacity before the known spike and reduces it afterward, matching readiness and cost requirements."],"scheduled")
r(83,"B","secure","Workload IAM roles","Use a Lambda execution role with the exact DynamoDB actions and table ARN required, rather than embedding long-term credentials.",[
"Hard-coded access keys create a long-lived secret and dynamodb:* is broader than necessary.",
"The Lambda execution role supplies automatically managed temporary credentials. A scoped policy can authorize the required writes to the intended table.",
"Lambda does not give application code default root-user credentials, and using root permissions would violate least privilege.",
"An IAM console username/password is not an AWS SDK credential mechanism and would expose personal credentials."],"lambda iam")
r(84,"C","cost","Object storage lifecycle","Deep Archive objects must be restored before copying into an immediately accessible class. A restore is temporary; a copy makes the class change persistent.",[
"An archived object is not immediately readable for a copy; first restore it and wait for the restore to complete.",
"S3 storage-class objects are managed through S3, not the separate Glacier vault console.",
"Restore through S3, wait for completion, then copy into Intelligent-Tiering while the restored copy is accessible. Remove unnecessary archived versions only when retention allows.",
"Changing an upload/default setting does not automatically rewrite existing Deep Archive objects into another class."],"s3",note="A same-key copy in a versioned bucket creates a new version. Retention/Object Lock and minimum archive-duration charges still apply to old versions.")
r(85,"B","performance","Shared file storage","FSx for Windows File Server provides managed SMB shares with Microsoft Active Directory integration.",[
"Lustre is a parallel HPC filesystem, not the Windows SMB/AD service requested.",
"FSx for Windows supports SMB file sharing and AD-based identity and access control for joined Windows clients.",
"EFS provides NFS for Linux-oriented workloads rather than native Windows SMB and AD file-sharing semantics.",
"S3 is object storage; AD Connector does not turn a bucket into a Windows SMB server."],"fsxwindows")
r(86,"B","cost","Compute pricing","For a stable commitment to a particular EC2 instance family and Region, EC2 Instance Savings Plans trade flexibility for a deeper discount than Compute Savings Plans.",[
"Compute Savings Plans offer broader flexibility, but typically a smaller maximum discount than the more constrained EC2 Instance Savings Plans.",
"EC2 Instance Savings Plans fit a three-year, steady EC2 family/Region commitment while retaining size, OS and tenancy flexibility within that commitment.",
"Spot can be interrupted and does not meet the requirement to keep a non-interruptible workload continuously running.",
"On-Demand avoids commitment but forgoes the commitment-based discounts available for steady usage."],"savings",note="Compare actual Region, family, payment terms and utilization before purchasing. A Savings Plan is a billing discount, not a capacity reservation.")
r(87,"C","cost","Object storage architecture","Store durable input/output artifacts outside ephemeral workers. S3 scales object storage independently of the processing fleet.",[
"Worker-attached EBS requires volume sizing and lifecycle management; periodic snapshots are not equivalent to immediate shared durable object storage for each upload.",
"Cold archive storage adds restore latency and retrieval operations that do not fit frequent interactive download access.",
"S3 stores audio and transcript objects durably, scales without preallocating disk, and decouples file retention from EC2 worker lifetimes.",
"Instance store is ephemeral and can be lost with instance termination or hardware failure, so it cannot be the durable retained copy."],"s3 ebs")
r(88,"C","secure","Network access controls","Security groups control instance-level ingress. Permit TCP 22 only from the administrator's trusted source address when SSH is required.",[
"The default NACL already allows the traffic, so adding another NACL allow does not open an instance security group.",
"NACL outbound permission is already present and does not authorize the inbound SSH connection at the instance security group.",
"An inbound security-group rule for SSH from the administrator's IP permits the requested connection, assuming routing, public addressing and host SSH are configured.",
"The SSH session is initiated inbound. Security groups are stateful, so return traffic for an allowed inbound session is automatically permitted."],"vpc",note="Also verify the key pair, SSH service, public address and internet route. For production management, Systems Manager can avoid opening inbound SSH.")
r(89,"D","resilient","Database migration","For supported source and target engines, DMS full load plus change data capture can keep a target current until a short migration cutover.",[
"An offline device transfer does not itself continuously replicate ongoing database changes during the migration window.",
"DataSync moves files/objects; it does not provide database-aware change-data capture for a running database.",
"RDS is relational, so it is not an automatic migration target for an unspecified NoSQL database, and backup/restore alone does not keep changes synchronized.",
"DMS supports full load plus ongoing replication for supported endpoint combinations, reducing final cutover downtime."],"dms",note="The source omits the NoSQL engine and network bandwidth. DMS compatibility, CDC support and the one-week transfer target must be validated for the actual endpoints.")
r(90,"A","performance","Streaming ingestion","Kinesis Data Streams retains events for independent consumers; an SQS queue distributes each message to competing consumers rather than replaying the whole stream to each application.",[
"Data Streams ingests ordered per-shard records, retains them, and supports independent consumers for dashboards, alerts and model pipelines.",
"Data Pipeline is a legacy workflow-orchestration service, not the live multi-consumer stream buffer.",
"Elastic Transcoder handles media transcoding, not GPS event ingestion.",
"SQS is useful for work queues, but consumers of one queue compete for messages. It does not give every independent application its own replayable stream."],"kinesis sqs")
r(91,"A","secure","Directory federation","Use AD Connector to proxy an existing directory, or Managed Microsoft AD with appropriate trusts, instead of operating domain controllers on EC2.",[
"Directory Service provides managed integration choices so AWS workloads can use existing corporate AD credentials without self-patching EC2 domain controllers.",
"Self-hosted controllers on EC2 introduce the management and patching overhead the question asks to avoid.",
"Requiring a different identity source does not preserve the existing corporate credential workflow and is unnecessary for the stated integration.",
"Separate, unintegrated directories duplicate identity management rather than preserving one corporate sign-in experience."],"ad")
r(92,"C","cost","Database pricing","Use a Redshift reserved-node commitment for predictably utilized provisioned capacity; pause/resume is only useful when there is genuine idle time.",[
"The cluster is continuously used, so shutting it down during idle windows does not fit the workload as described.",
"Automated backups improve recoverability but do not supply a discount on continuously running compute.",
"A three-year reserved-node offering discounts matching provisioned Redshift compute for the stated steady commitment.",
"Serverless can be efficient for variable demand, but it does not automatically beat a reserved commitment for an already continuously utilized provisioned workload."],"redshift")
r(93,"B","resilient","Data transfer","DataSync agents and scheduled tasks automate incremental file transfers between supported on-premises and AWS locations.",[
"Shipping devices is suited to offline bulk transfer, not frequent scheduled incremental synchronization in either direction.",
"A DataSync agent accesses the supported on-premises protocol and scheduled tasks copy changed data to/from supported S3, EFS or FSx locations.",
"DMS is for supported database migrations and replication, not generic Windows file synchronization.",
"Transfer Acceleration changes S3 network paths; it does not supply an incremental filesystem-sync engine or a native mounted drive."],"datasync")
r(94,"B","secure","Web application security","Use WAF's AWS-managed PHP rule group for PHP-specific request signatures rather than treating DDoS protection as application exploit filtering.",[
"Shield focuses on DDoS protection; a PHP managed rule group is a WAF feature, not a Shield PHP rule setting.",
"The AWS-managed PHP rule group in a WAF web ACL provides maintained PHP-specific request protections with minimal custom rule management.",
"Marketplace rules may help, but a suitable AWS-managed PHP group already meets the stated use case without requiring a separate third-party subscription.",
"Custom groups and action overrides require rule design and tuning; they do not automatically supply the maintained PHP exploit signatures."],"waf",note="Managed rules require testing and tuning to the application. They supplement patching and secure coding rather than replacing them.")
r(95,"A","performance","Data analytics","Athena handles serverless ad hoc SQL on S3; QuickSight supplies interactive business dashboards.",[
"Athena queries S3 files with SQL, and QuickSight provides the visualization layer without operating a warehouse or query server.",
"Glue can catalog and transform data, but Glue plus Athena does not include the requested interactive dashboard service.",
"Glue handles data integration, not the ad hoc SQL query engine requested; Athena is the missing component.",
"Kinesis Data Streams ingests live events rather than providing SQL queries over existing S3 JSON files."],"athena quicksight")
r(96,"C","secure","Multi-account governance","An explicit deny inherited from a parent SCP cannot be overridden by a child OU allow or an identity policy.",[
"A child allow cannot override the parent's explicit deny; SCP inheritance still constrains the member-account principal.",
"FullAWSAccess is an allow ceiling, not an override for explicit denies elsewhere in the applicable policy hierarchy.",
"The deny on Project_OU is inherited by Dev_OU accounts and prevents the operation even when child and IAM policies allow it.",
"The root FullAWSAccess policy is not a deny; it is the parent's explicit deny that blocks the action."],"scp")
r(97,"D","secure","Multi-account governance","An AWS account can belong to one organization at a time. Make it standalone, then invite it into the destination organization.",[
"There is no cross-organization drag-and-drop account migration workflow.",
"Moving an account between OUs within one organization is different from transferring it to another organization.",
"Deleting the entire source organization is unnecessary for moving a member account and disrupts other members and governance.",
"Remove/leave the source organization, satisfy standalone-account requirements, then accept an invitation from the target organization."],"orgmove",note="Review billing, IAM access, organization policies, delegated administration and service integrations before a real account move.")
r(98,"B","secure","API authorization","IAM policies distinguish management API permissions from execute-api invocation permissions. Authentication tokens do not by themselves define authorization.",[
"STS issues temporary credentials, but the permissions still come from IAM policies; credentials alone do not define each role's allowed actions.",
"Identity policies authorize management actions and can authorize IAM-based invocation, while supported API resource policies constrain who can access the API.",
"Config evaluates resource configurations and compliance; it is not the real-time authorization engine for API operations.",
"Distributing long-term access keys and enforcing privileges only in application code creates unnecessary credential risk and bypasses the intended IAM authorization design."],"iam apigw")
r(99,"D","resilient","DNS & routing","A Route 53 alias targets the ALB resource, not a fixed list of its changing IP addresses.",[
"Replacing the alias with fixed IP addresses loses its automatic tracking of the load balancer endpoint.",
"An alias does not require manually updating a list of ALB IP addresses as subnets change.",
"The alias references the ALB's DNS name and hosted-zone target, not individual IP addresses that must be refreshed.",
"Route 53 follows the ALB target as its addresses change, so the alias record does not need an update."],"dns")
r(100,"BE","resilient","Monitoring & alerting","CloudWatch alarms detect metric thresholds; SNS delivers the notifications to confirmed email subscribers.",[
"SES is an email-sending service, but it does not itself monitor RDS metrics or provide the simplest native alarm-to-email integration.",
"CloudWatch collects the database metrics and evaluates alarms against the configured CPU/memory thresholds.",
"SQS is a message queue, not an email notification destination for the operations team.",
"Route 53 manages DNS and health-based routing, not RDS CPU/memory threshold evaluation.",
"An SNS topic connected to the CloudWatch alarm can fan out notifications to confirmed email subscriptions."],"cloudwatch sns",note="Use the relevant RDS metrics such as CPUUtilization and FreeableMemory. Metric choice and threshold direction must match the symptom.")
r(101,"AB","performance","Database read scaling","Read replicas offload read queries; a cache serves reusable results without querying the database. Both reduce pressure on the writer.",[
"RDS read replicas provide independent read capacity when the application directs suitable read queries to replica endpoints.",
"ElastiCache can serve reusable query results or objects and reduce repeated reads on the primary database.",
"CloudFront can cache HTTP responses according to application semantics, but does not directly cache arbitrary database queries simply by being placed in front of RDS.",
"Migrating a relational schema and application to DynamoDB is a substantial redesign, not the requested straightforward read-load improvement.",
"A larger writer can add capacity but does not reduce its read load or create the independent read capacity requested."],"rds aurora",note="Read replicas can lag and cached data can become stale. Keep consistency requirements and cache invalidation in the design.")
r(102,"D","resilient","Event-driven integration","Use S3 ObjectRemoved event notifications to publish to SNS; confirm the email subscription and permit S3 to publish to the topic.",[
"CloudTrail delivery notifications indicate log-file delivery, not a direct per-object deletion email workflow without additional event processing.",
"Server access logging produces logs for analysis but does not directly trigger an email notification for each removal event.",
"Config does not provide the simplest per-object removal event path; adding custom Lambda logic is unnecessary for S3-to-SNS notifications.",
"S3 supports ObjectRemoved notifications to SNS, providing a native event-to-email subscription path with the required topic policy."],"s3events sns")
r(103,"D","cost","Multi-account billing","Consolidated billing combines usage for one payer and eligible volume discounts. Organization-wide governance policies require all features.",[
"SCP governance requires Organizations all features; consolidated billing alone does not enable it.",
"Tag-policy governance is an all-features capability, not the primary consolidated-billing benefit.",
"Preventing changes through organization-wide controls is governance beyond the billing-only feature set.",
"Combining eligible account usage supports unified payment and volume-pricing benefits while accounts remain distinct."],"orgbilling")
h(104,"The scenario does not establish that inbound SSH is allowed by the security group or that the configured auto-assigned public IP was actually attached. A blocking NACL is possible, but not uniquely proven. The public IP and TCP return path need verification.","secure","Network troubleshooting","vpc")
r(105,"B","secure","Private service access","PrivateLink exposes a specific service through consumer interface endpoints without full network-to-network connectivity or public internet access.",[
"Internet gateways and public access explicitly violate the private AWS-network path requirement.",
"An endpoint service backed by the appropriate NLB lets consumers create interface endpoints for private service access across VPCs.",
"S3/DynamoDB gateway endpoints reach those AWS services only; they cannot target an arbitrary internal web application.",
"A full mesh of VPN connections adds routing and tunnel management; PrivateLink is the purpose-built service-sharing pattern here."],"privatelink")
h(106,"RAM can share Dedicated Hosts and supported Capacity Reservations. An EC2 Reserved Instance is a billing product, not generic shareable 'Reserved Instance capacity' via RAM. The question conflates these resources.","cost","Resource sharing","ram")
r(107,"C","cost","License management","License Manager tracks and can enforce rules for supported license configurations across resources/accounts; Config and Audit Manager serve different purposes.",[
"Trusted Advisor offers recommendations; it is not the central BYOL license inventory and consumption-control service.",
"Config tracks resource configuration and compliance history, not a complete software-license consumption management workflow.",
"License Manager provides centralized license configuration, discovery and tracking, with supported enforcement/reporting across accounts.",
"Audit Manager collects evidence for audits but is not the primary license consumption and enforcement service."],"license")
r(108,"B","secure","Database encryption","Existing unencrypted RDS storage cannot simply be toggled to encrypted. Copy a snapshot with encryption and restore a new instance.",[
"In-place encryption cannot be enabled, but you do not need to manually recreate and reload the database from scratch; an encrypted snapshot copy provides a supported path.",
"Create a manual snapshot, copy it with the chosen KMS key, and restore a new encrypted instance from that encrypted copy.",
"For this conversion, first make an encrypted snapshot copy. Restoring the unencrypted snapshot without that step does not enable the required encryption.",
"Stopping and restarting does not expose a supported in-place encryption toggle for an existing unencrypted instance."],"rdsencrypt snapshot",note="Plan final synchronization, endpoint changes and cutover downtime. Protect the KMS key because encrypted backups and replicas depend on it.")
r(109,"D","resilient","IP addressing","An auto-assigned public IPv4 address is released on instance stop and normally replaced on start. A reboot is different from stop/start.",[
"Route 53 hosted zones are not restarted when instances stop. DNS records remain until changed.",
"An Elastic IP can provide stable addressing, but its absence is not the direct lifecycle event explaining the changed auto-assigned addresses.",
"An ordinary reboot does not normally replace the public address; the described operation is a stop/start, not a requirement to manually reattach an address after reboot.",
"Stop releases the auto-assigned public IPv4 addresses, and start assigns new ones, leaving fixed DNS records pointing at the old addresses."],"publicip dns")
r(110,"A","secure","Audit & observability","Centralize application/OS log files with CloudWatch Logs for retention and analysis; CloudTrail records supported AWS API activity instead.",[
"CloudWatch Logs receives host/application logs through an agent or application integration and supports retention, queries and alerting workflows.",
"CloudTrail does not automatically collect arbitrary files from EC2 guest operating systems or application logs.",
"AWS Health shows relevant service/account health events, not centralized storage for the application's log files.",
"Trusted Advisor provides recommendations rather than ingesting and searching the runtime logs."],"cloudwatch",note="Log collection enables investigation; threat detection still requires appropriate queries, rules or security integrations. Configure retention and permissions deliberately.")
r(111,"B","performance","HPC networking","EFA adds OS-bypass capabilities for tightly coupled HPC/ML internode communication on supported instances and software stacks.",[
"ENA enhanced networking improves standard IP networking, but EFA specifically targets tightly coupled distributed HPC/ML communication.",
"EFA supports low-latency, high-throughput inter-instance communication with an OS-bypass interface for supported HPC/ML libraries.",
"An ENI or larger MTU alone does not supply EFA's specialized communication capabilities or guarantee the required performance.",
"EFS supplies shared files, not an internode low-latency communication fabric."],"efa")
r(112,"A","performance","Streaming ingestion","Independent analytics teams need retained records and independent read positions. That is a streaming log pattern, not one shared work queue.",[
"Kinesis Data Streams retains records and lets separate consumers process/reprocess the sensor stream at their own positions.",
"EMR can process data but is not by itself the durable live ingestion buffer for independent consumers.",
"Consumers of the same SQS queue compete for messages; they do not each receive a complete independently replayable stream.",
"SNS fans out notifications but a basic topic is not the general retained ordered data stream requested. Fanout/archival features and integrations are different designs."],"kinesis sqs sns")
h(113,"The CPU threshold is missing in the screenshot, and CloudWatch alarm period/evaluation limits matter for a 24-hour window. A native EC2 stop alarm is the right concept, but the source lacks enough configuration detail for the exact condition.","cost","Compute optimization","cloudwatch")
r(114,"B","secure","Private subnet egress","A public NAT gateway gives private instances outbound IPv4 internet access without accepting unsolicited inbound internet connections to those instances.",[
"Moving instances and adding direct internet routing changes the private placement; it is not the requested private-subnet egress solution.",
"Place the public NAT gateway in a public subnet with an internet route, then route private-subnet outbound traffic to it. Instances need no public IPv4 addresses.",
"A bastion is for controlled administration, not automatically a NAT/proxy for all downloads, and introduces host management.",
"Routing through on-premises infrastructure can be built, but adds dependency and routing complexity compared with the native NAT gateway option."],"nat",note="Choose an availability-aware NAT design. NAT does not replace security groups, endpoint controls or restrictions on egress destinations.")
r(115,"C","performance","Queue-driven scaling","Queue backlog reflects pending work. For target tracking, backlog per running worker/task is generally more useful than an unnormalized total.",[
"The total S3 object count includes already processed images and does not directly measure waiting jobs.",
"Memory usage may remain stable even while queued work grows; it is not the direct workload-backlog signal.",
"Visible SQS messages measure work waiting to be processed and can drive scaling. With consistent processing time, normalize by task count for backlog-per-task target tracking.",
"The running-task count measures capacity, not the amount of pending work that should trigger more capacity."],"sqs as",note="Use ApproximateNumberOfMessagesVisible with an appropriate per-task backlog target and maximum acceptable queue latency. Consider startup time and scale-in protection.")
r(116,"B","secure","Private data transfer","DataSync private endpoints plus private hybrid connectivity can transfer supported on-premises data without routing the data path over the public internet.",[
"A NAT gateway provides a path to public endpoints and does not satisfy the private hybrid transfer requirement.",
"A DataSync agent using the private VPC endpoint over Direct Connect supplies managed transfer through a private network path to supported storage locations.",
"Offline devices require shipping/handling and do not supply the requested scalable online migration path; device eligibility/availability also needs review.",
"Lambda does not directly mount arbitrary on-premises NFS shares as a general replacement for DataSync; the proposal omits supported connectivity and transfer management."],"datasync privatelink",note="Direct Connect is private connectivity, not automatic encryption. DataSync uses encryption in transit; validate every required endpoint and data/control path.")
r(117,"BC","secure","Network segmentation","Keep the database private and authorize its port only from the application/web security group. Private placement and least-privilege ingress work together.",[
"Putting the database in the public tier fails the requested network segmentation even if a security-group rule limits some access.",
"A private subnet and no public address prevent direct internet reachability of the database instance.",
"Referencing the web-tier security group on the database port permits only the intended application tier without relying on broad public CIDRs.",
"A public IP and a database-port rule open to 0.0.0.0/0 directly violate the database isolation requirement."],"vpc")
r(118,"D","secure","Private content delivery","CloudFront signed cookies are convenient for authorizing a subscriber to a set of restricted files rather than signing every file URL individually.",[
"The S3 origin should remain protected, but a bucket policy alone does not authenticate individual CloudFront premium viewers.",
"HTTPS encrypts transport; it does not establish that a viewer is entitled to premium content.",
"Signed URLs can restrict individual files, but cookies are the better fit when a subscriber needs access to many files under a common policy.",
"Signed cookies convey the authenticated application's time-limited authorization for premium content across the allowed paths."],"cloudfront",note="The application authenticates and authorizes the subscriber before issuing signed cookies. Protect the S3 origin so users cannot bypass CloudFront.")
FIXES[119] = {"select": 2}
r(119,"BC","resilient","Change-driven processing","DynamoDB Streams captures item-level changes, and a Lambda event source mapping invokes processing code for those records.",[
"Write-capacity metrics are aggregated signals and do not identify each changed item's contents or reliably trigger one action per transaction.",
"Streams records creates/updates/deletes according to the configured stream view, providing the item-change feed.",
"Lambda can consume the stream and perform downstream actions without polling the base table for changes.",
"Scheduled table polling adds latency and custom change-detection logic, instead of using the native item-change stream."],"dynamostream",note="Stream event processing can retry and deliver records more than once; implement idempotent downstream side effects.")
r(120,"AC","resilient","Database backups","RDS combines automated daily snapshots and transaction-log backups for point-in-time recovery within the configured retention window.",[
"RDS takes a daily storage snapshot during the backup window and generally uploads transaction logs about every five minutes for supported engines.",
"The stated twelve-hour snapshot and hourly-log schedule does not describe the normal RDS automated-backup mechanism.",
"Point-in-time restore reconstructs state from the snapshot and subsequent transaction logs up to an available restore time.",
"Logs are backed up outside the snapshot window as well; discarding them afterward would prevent continuous point-in-time recovery.",
"Enabling RDS automated backups with nonzero retention manages the necessary log backups; a separate manual log-backup setup is not required for this standard behavior."],"pit",note="Restore creates a new database instance. Check LatestRestorableTime and plan connectivity/cutover; retention does not promise a zero-delay recovery point.")
h(121,"Security-group ingress and NACL filtering are plausible causes, but the route option describes an underspecified modified local route. Current local routes can be replaced/overridden for supported routing designs. The question does not provide enough actual route/rule configuration for its exact two-choice claim.","secure","Network troubleshooting","vpc")
r(122,"AB","performance","Streaming ingestion","Use Kinesis Data Streams for parallel ingestion/consumption and Firehose for managed delivery of records into storage/analytics destinations.",[
"A correctly sized stream and parallel consumers support the incoming telemetry rate and near-real-time processing. Provision capacity based on bytes and record counts.",
"Firehose provides managed delivery to supported destinations such as S3 and Redshift, fitting the storage/analytics part of the pipeline.",
"SQS plus EC2 can form a work-processing design but is not the preferred pair for the retained, scalable streaming analytics and delivery pattern described.",
"SimpleDB is not a purpose-built high-throughput streaming ingestion and aggregation service."],"kinesis",note="At 10,000 sensors × 20 KB every 5 seconds the raw rate is about 40 MB/s before overhead. Size shard/consumer capacity and account for partition-key distribution.")
r(123,"D","secure","Customer identity","An identity provider authenticates a user. A Cognito identity pool exchanges an accepted identity token for temporary AWS role credentials.",[
"Identity pools and external identity providers have different responsibilities; they are not the same authentication service.",
"A user does not need a second independent social sign-in after a Cognito user-pool sign-in. Federation can connect the flow.",
"The identity provider authenticates users; S3 authorizes AWS requests using the resulting AWS credentials and permissions.",
"The identity pool accepts supported provider tokens and supplies temporary credentials for the mapped IAM role to access permitted AWS resources."],"cognito iam")
r(124,"B","resilient","Network availability","For zonal NAT gateways, route each AZ's private subnets through a local gateway to avoid one-AZ dependency and cross-AZ egress transfer.",[
"One zonal NAT gateway creates a shared-AZ dependency and can incur cross-AZ transfer for workloads in the other AZs.",
"A NAT gateway in each AZ, with local private-subnet routes, preserves zonal independence and avoids routing egress across AZs.",
"NAT gateways are route targets, not application targets placed behind an NLB for automatic NAT failover.",
"A different Region and VPC peering do not provide the supported local NAT gateway routing design."],"nat",note="This describes the zonal NAT options in the source. AWS also offers evolving regional NAT features; evaluate current availability and pricing rather than assuming one deployment model is universal.")
h(125,"Client VPN requires a server certificate in ACM and suitable client-certificate trust configuration. When server and client certificates share the same CA, separately importing every client certificate is not generally required. The unspecified import error cannot be resolved uniquely by the asserted step.","secure","VPN authentication","vpn")
h(126,"Managed Grafana's supported plugin management evolves, and the options combine several capabilities with an absolute plugin-installation claim. This needs current workspace-version and plugin-policy verification before being scored.","resilient","Observability","cloudwatch")
r(127,"B","secure","Temporary object access","An S3 presigned PUT URL delegates a specific upload operation for a limited time without giving the recipient long-term credentials.",[
"A second bucket and copy/delete automation do not by themselves authorize temporary uploads to selected customers and add unnecessary moving parts.",
"A presigned PUT URL includes a signed bucket/key operation and expiry, allowing an authorized upload without distributing AWS credentials.",
"A custom ECS upload fleet can proxy uploads but adds infrastructure and authorization work that a native presigned operation avoids.",
"SQS messages have size and use-case constraints and are not a substitute for direct image-object uploads."],"presign",note="The URL cannot outlive the signing credentials or restrictive policies. Temporary role credentials may expire before 48 hours; design signing and renewal accordingly, and scope keys/content constraints.")
r(128,"C","performance","Database selection","Store image bodies in S3 and independently indexed image metadata in DynamoDB when low-latency keyed lookup and elastic scale are required.",[
"Redshift is a warehouse for analytical queries, not the simplest low-latency operational metadata lookup store.",
"Glacier is archival object storage and is not an operational queryable metadata database.",
"DynamoDB provides durable managed key-value/document records for timestamps, dimensions and processing status, independent of worker instances.",
"SQS buffers work messages; consumed messages are not a persistent queryable metadata database."],"dynamo s3")
r(129,"D","resilient","Managed application platforms","Elastic Beanstalk automates application-environment provisioning, load balancing and scaling for supported platforms.",[
"Spot instances still require the team to provision/configure the application infrastructure and can be interrupted.",
"Reserved Instances are a billing mechanism, not a managed application provisioning service.",
"Lambda and RDS can support an application architecture, but do not directly deploy the existing platform web/database environment with the requested Beanstalk-style management.",
"Beanstalk deploys supported application platforms and manages the associated provisioning, load balancing and Auto Scaling environment configuration."],"beanstalk",note="For production, decouple database lifecycle from the Beanstalk environment where appropriate. Managed provisioning does not remove responsibility for application configuration and updates.")
r(131,"A","secure","Federated authorization","Successful social sign-in proves identity, not permission to use S3 or DynamoDB. The assumed IAM role's policies determine permitted AWS actions.",[
"Reduced role permissions can deny resource access even while the external identity provider continues authenticating the user successfully.",
"Federation protocols establish/exchange identity; updating them does not fix a role policy that no longer allows resource actions.",
"Federated application users normally assume IAM roles rather than become IAM users assigned to IAM groups.",
"The external provider supplies an identity token; it does not directly grant or revoke permissions to individual AWS resources in the mapped role."],"cognito iam")
h(132,"An encrypted snapshot copy and new encrypted instance/replica are the basic migration path, but the source asks for minimal disruption without a final data synchronization/cutover plan. Option D describes promoting a snapshot copy, which is not a running replica, and B/E substantially overlap. Excluded to avoid teaching a misleading low-downtime sequence.","secure","Database encryption","rdsencrypt")
h(133,"Removing members, deleting the old organization and accepting the new invitation are the conceptual steps. However option A unnecessarily mandates root-user sign-in; authorized IAM principals can perform supported management operations. The exact THREE requirement includes that misleading prerequisite.","secure","Multi-account governance","orgmove")
r(134,"B","secure","Customer identity","Configure an identity-pool role mapping with an appropriate trust policy and least-privilege DynamoDB permissions to issue temporary client credentials.",[
"MFA at an identity provider may strengthen authentication, but does not on its own establish an AWS role or its DynamoDB permissions.",
"The identity pool uses an authorized IAM role for authenticated identities, supplying temporary AWS credentials scoped to the required DynamoDB operations.",
"CloudTrail and GuardDuty audit/detect activity; they do not create the client federation credential flow.",
"Requiring the AWS Console is unnecessary for mobile application identity and is not the intended identity-pool SDK workflow."],"cognito iam")
h(135,"The intended answer is CloudFormation, but the screenshot extraction is missing an answer option. It is kept outside scored exams until the source can be transcribed completely.","resilient","Infrastructure automation","cfn")
r(136,"B","secure","Encryption at rest","SSE-KMS uses envelope encryption for S3 data at rest. Read/write permissions and KMS key authorization remain separate controls.",[
"SSE-KMS is encryption at rest, not a replacement for TLS in transit. Objects stored with it are encrypted on storage.",
"S3 handles object encryption before persistent storage and decryption during authorized retrieval, with KMS protecting the data-encryption keys.",
"Authorized applications and users can use KMS operations and retrieve SSE-KMS objects; permissions are not reserved exclusively for AWS services.",
"KMS does not grant every account in an organization blanket decrypt rights. Key policies, identity policies and other controls must authorize access."],"sse kmspolicy",note="New S3 uploads are encrypted by default with SSE-S3; requiring KMS keys is a stronger, specific requirement. Changing defaults does not retroactively convert all existing objects.")
r(137,"B","resilient","Disaster recovery","Copy usable AMIs and their backing storage to the recovery Region, then recreate compute there. Application data and dependencies need their own recovery plan.",[
"An ELB and EC2 Auto Scaling group are regional resources; one ELB does not span multiple Regions.",
"Copied AMIs provide launchable machine images in the DR Region without keeping a full running compute fleet there.",
"CloudFront caching does not replicate application compute, databases or arbitrary dynamic state into a recovery Region.",
"Snapshots must be restored into volumes; they cannot be directly attached to an instance. The option omits a complete launchable-image/restore workflow."],"dr",note="AMI copies alone do not guarantee a particular RTO/RPO. Replicate data, templates, permissions, configuration and required service dependencies; test recovery.")
r(138,"A","performance","Multi-Region databases","DynamoDB global tables replicate managed table data across selected Regions so clients can use a local regional endpoint.",[
"Adding global-table replica Regions provides the native managed multi-Region replication pattern for local regional access.",
"A normal DynamoDB regional table is already stored across AZs; adding a fictitious Multi-AZ mode does not create cross-Region replicas.",
"CloudFront does not automatically create strongly managed replicas of a DynamoDB table or provide a direct database replication feature.",
"Regional caches can accelerate selected reads, but introduce invalidation and consistency work rather than provide native full-table multi-Region replication."],"globaltable",note="Choose the supported consistency mode and conflict model for the workload/Regions. Multi-Region access patterns still require deliberate read/write and failover design.")
h(139,"With RAM organization sharing enabled, members in the same organization generally do not accept sharing invitations. A/B are the key steps, so the request to choose THREE forces an incorrect invitation step.","cost","Resource sharing","ram")
r(140,"B","cost","Hybrid storage","Cached volumes keep the primary dataset in AWS with a local cache of hot blocks; stored volumes keep the complete primary dataset on premises.",[
"Stored volumes keep all primary data locally, so they do not address running out of on-premises storage capacity.",
"Cached volumes store the primary data in AWS and retain recently accessed blocks locally, reducing the amount of local disk required.",
"Deep Archive has retrieval delays and does not provide transparent low-latency access to the working set.",
"Backup copies support recovery, not a transparent primary storage extension with a local hot-data cache."],"gateway")
h(141,"DynamoDB requires redesign around partition/sort keys and access patterns; preserving arbitrary relational table structures through SCT is not a general supported conversion guarantee. The options omit a defensible mapping and direct DMS DynamoDB-target workflow.","resilient","Database migration","dms dynamo")
h(142,"DataSync plus File Gateway does not automatically turn a failed database into a writable database backed directly by S3 with no code or recovery changes. File-level access and database replication/failover are different guarantees.","resilient","Hybrid recovery","datasync gateway")
r(143,"C","performance","Content delivery","CloudFront caches content near viewers and can use an S3 origin without copying the whole bucket into another Region.",[
"Cross-Region replication is explicitly excluded and does not itself provide a global viewer-facing cache.",
"Transfer Acceleration optimizes S3 transfer paths, but it is not the same as a CDN cache for serving a website to remote viewers.",
"CloudFront provides edge caching in front of the S3 origin; changing DNS directs viewers through the CDN without a full bucket replication.",
"An ALB is not an HTTP cache and cannot simply use an S3 bucket as the proposed caching target."],"cloudfront",note="An S3 website endpoint is configured as a custom origin and does not support OAC. For a private S3 origin with OAC, use the S3 REST endpoint and appropriate website routing.")
r(144,"C","secure","Customer identity","Cognito user pools manage customer sign-up/sign-in and federation; identity pools are needed when the client also requires temporary AWS credentials.",[
"IAM users are not the intended customer user directory, and creating one per application customer adds credential and lifecycle overhead.",
"Separate AWS accounts per customer are unnecessary for consumer authentication and do not provide a practical sign-up service.",
"User pools supply managed application users and social federation; identity pools can additionally issue temporary AWS credentials for permitted client access.",
"Managed Microsoft AD fits enterprise directory integration, not the lightweight consumer/social sign-up workflow requested."],"cognito",note="An identity pool is optional when users only call an authenticated application API and do not need AWS credentials directly.")
r(145,"D","secure","Hybrid connectivity","Site-to-Site VPN can establish managed IPsec connectivity over existing internet links more quickly than provisioning a dedicated physical connection.",[
"Direct Connect provisioning is slower and a dedicated connection is not automatically IPsec-encrypted; the option adds unnecessary infrastructure for a near-term test need.",
"A third-party appliance can work but requires appliance management, configuration and availability planning that a managed VPN avoids.",
"A VPN over Direct Connect can combine private transport and encryption, but waiting for a new physical connection conflicts with the urgent low-cost setup.",
"A managed Site-to-Site VPN connects the corporate network to the VPC using IPsec over existing internet access, fitting the quick setup."],"vpn")
r(146,"B","secure","Customer identity","Cognito identity pools can issue limited guest credentials through an unauthenticated role; keep that role narrowly scoped.",[
"Unauthenticated access is not automatically forbidden; a carefully restricted guest role can expose only intentional public/read-only functions.",
"Identity pools support unauthenticated identities and a limited IAM role, letting the same app offer guest browsing before later sign-in.",
"A second application duplicates functionality and does not provide the integrated guest-to-authenticated flow requested.",
"Removing authentication/authorization globally exposes far more than the intended limited guest feature set."],"cognito iam")
r(147,"A","secure","Customer identity","Cognito user pools support federation with social, OIDC and SAML identity providers while maintaining user-pool profiles.",[
"A user pool can integrate supported social providers, OIDC providers and SAML providers, with attribute mapping into user-pool profiles.",
"User pools support more than social providers; OIDC and SAML federation are supported integration types.",
"Using one provider type does not require configuring all the others. Select the provider integrations the application needs.",
"The supported federation mechanisms avoid a need to move the application directory outside Cognito; effort alone is not a technical limitation."],"cognito")
r(148,"AC","secure","Audit & observability","Capture viewer-request access logs and administrative API audit activity as separate evidence sources; enabling logs alone is not a PCI compliance certification.",[
"CloudFront access logs record viewer requests and help investigate access to the distribution's content.",
"Caching can improve performance but does not create the request or administrative audit trail.",
"CloudTrail records supported CloudFront management API activity so configuration changes can be audited.",
"VPC Flow Logs apply to supported VPC network interfaces, not CloudFront edge viewer requests as a replacement for distribution access logging."],"cloudfront cloudtrail",note="PCI compliance includes many controls beyond these two logging choices. Configure retention, permissions, delivery monitoring and the actual audit requirements.")
r(149,"A","secure","Private service access","Create gateway endpoints and route-table associations in each relevant VPC for private S3 and DynamoDB access. Gateway endpoints are not transitively shared through VPC peering.",[
"Both S3 and DynamoDB support gateway endpoints for the stated VPC access pattern, with endpoint policies and associated route tables.",
"NAT and internet-gateway paths are not the private gateway-endpoint design requested.",
"VPC peering does not extend another VPC's gateway endpoint, and the stated DynamoDB interface-endpoint assumption is not the standard service access model.",
"Peering and public service endpoints do not provide the described endpoint-local private access pattern."],"s3endpoint vpc")
r(150,"B","cost","Centralized egress","A Transit Gateway hub can route multiple VPCs to a dedicated egress VPC. VPC peering does not provide transitive access to another VPC's NAT gateway.",[
"VPC peering does not support using a peer's NAT gateway/Internet Gateway for edge-to-edge transit.",
"Transit Gateway attachments plus a correctly routed egress VPC provide a scalable centralized outbound network with redundant NAT paths.",
"PrivateLink exposes services; it does not transparently expose a NAT gateway as a general consumer-VPC internet route target.",
"VPN attachments are not the native VPC attachment choice for ordinary VPC-to-Transit-Gateway connections and add unnecessary tunnel infrastructure."],"nat vpc",note="Centralization is not automatically cheapest. Include Transit Gateway processing/attachment fees, NAT charges, AZ routing and inspection requirements.")
h(151,"A DLQ applies to supported asynchronous Lambda invocation after failure/retries; the question does not specify the invocation mode. A synchronous timeout is not automatically delivered to a DLQ. The source also has a missing fourth option.","resilient","Serverless failure handling","lambda")
r(152,"B","performance","Compute scaling","Guest memory is not an EC2 default metric. Target tracking needs custom publication/configuration for memory rather than a predefined EC2 memory option.",[
"ASGAverageCPUUtilization is a supported predefined EC2 Auto Scaling target-tracking metric.",
"Memory utilization requires guest-level collection/custom metrics; it is not a built-in predefined EC2 Auto Scaling target-tracking choice.",
"ASGAverageNetworkIn is a predefined target-tracking metric for average incoming network bytes.",
"ASGAverageNetworkOut is a predefined target-tracking metric for average outgoing network bytes."],"as cloudwatch")
r(153,"C","secure","Service authorization","IAM controls who can call DMS management APIs. TLS and KMS protect data, while NACLs filter network traffic.",[
"TLS secures the transport connection but does not grant permission to create, modify or delete DMS resources.",
"KMS encryption protects storage/key operations; it is not the authorization policy for all DMS management actions.",
"IAM policies authorize or deny the relevant dms:* API actions for users and roles, subject to applicable boundaries/organization controls.",
"NACLs filter subnet packets by protocol/address/port. They do not express which IAM principal may delete a DMS task."],"iam dms")
h(154,"S3 File Gateway can expose an NFS share locally, while EFS mount targets can be reached from on premises over private connectivity. The option 'EFS with a VPC endpoint' conflates API endpoints and NFS mount targets; the source does not specify where the share must live.","secure","Hybrid file storage","efs gateway")
r(155,"A","secure","Hybrid connectivity","Direct Connect supplies a dedicated private path; a Site-to-Site VPN over that path supplies the explicitly requested IPsec encryption.",[
"Combining Direct Connect and an appropriately designed Site-to-Site VPN provides private transport plus IPsec encryption.",
"VPN over the public internet supplies IPsec but not the dedicated predictable private transport requested.",
"Direct Connect alone does not inherently supply IPsec encryption, even though it avoids public internet transport.",
"A software VPN alone does not provide a dedicated private circuit and adds appliance operations."],"vpn",note="Validate supported VPN-over-Direct-Connect topology, routing, MTU and per-tunnel throughput. Use sufficient tunnels/capacity for the throughput requirement.")
h(156,"Versioning and least-privilege deletion are sound controls, but both MFA Delete and appropriate Object Lock governance retention can protect versions. The question supplies four potentially relevant controls while demanding exactly three and does not specify retention/operational constraints.","secure","Object protection","s3 iam")
r(157,"A","secure","Least privilege","Least privilege narrows actions, resources and conditions to what a workload/person needs. Monitoring, IP design and elasticity do not replace access control.",[
"Reducing IAM permissions to required actions/resources directly implements the Security pillar's least-privilege access principle.",
"Metrics and dashboards support observability but do not themselves narrow who can access a resource.",
"Non-overlapping address ranges help connectivity planning; they are not a substitute for hardening identity/resource access.",
"Elasticity matches capacity to demand and is primarily a performance/cost design practice, not the direct access-hardening control requested."],"iam")
r(158,"A","cost","Backup cost optimization","Review manual snapshot retention: manual backups persist until explicitly deleted and can continue accumulating storage charges.",[
"Deleting snapshots that are no longer required reduces retained backup storage without stopping or resizing the running cluster.",
"Increasing retention keeps more automated backup data and can increase rather than reduce storage costs.",
"Provisioned Redshift clusters do not become Spot Instance fleets through a purchasing setting.",
"Moving warehouse data to an EC2 instance-store volume is not a supported snapshot-cost configuration and would change the database architecture."],"redshift",note="Confirm recovery and retention requirements before deleting backups; deleting a snapshot removes that recovery point.")
r(159,"C","resilient","Compute availability","A load balancer stops routing to unhealthy targets; Auto Scaling replaces them and restores desired capacity. Health checks alone do not add replacement servers.",[
"Larger servers can add headroom but do not automatically replace a failed instance or maintain the desired fleet size.",
"Flow Logs record network traffic metadata. Monitoring them does not replace failed compute instances.",
"ELB health checks remove unhealthy targets from service, and an appropriately configured Auto Scaling group replaces failed instances to recover capacity.",
"Duplicating the same unmanaged two-instance setup across Regions adds cost and complexity without fixing automatic replacement in each deployment."],"as alb")

r(160,"C","resilient","Hybrid storage","Stored Volume Gateway keeps the complete primary volume on premises and backs it up using durable AWS snapshots.",[
"EBS volumes attach to supported AWS compute in an AZ; they are not directly mounted on-premises block devices.",
"EBS snapshots alone do not supply an on-premises block-storage interface or a managed backup gateway for existing local servers.",
"Stored volumes retain all primary data locally for fast access and asynchronously back up through the Storage Gateway snapshot mechanism.",
"Deep Archive alone provides delayed archive retrieval, not local primary storage with a transparent backup interface."],"gateway")
h(161,"The image's answer labels were not extracted reliably. The relevant concept is API Gateway plus Lambda plus DynamoDB for a serverless transactional API; consult the original screenshot before treating its options as complete.","resilient","Serverless applications","lambda dynamo")
r(162,"A","performance","Data analytics","QuickSight supplies business dashboards and forecasting from supported S3-based datasets without first building a warehouse.",[
"QuickSight can visualize supported S3 data sources and provide built-in forecasting features for suitable time series, minimizing infrastructure management.",
"Redshift is a query warehouse, not by itself an executive dashboard/forecasting interface, and adds the warehouse the question asks to avoid.",
"Copying into DynamoDB adds a separate operational database and does not provide the simplest direct S3-to-dashboard workflow.",
"Copying into RDS adds database provisioning and ingestion work without a stated relational requirement."],"quicksight",note="Use a supported S3 manifest/file format or Athena dataset and sufficient chronological data for forecasting. Forecast quality depends on data and is not guaranteed.")
r(163,"B","resilient","Host observability","The unified CloudWatch agent can append instance/ASG dimensions and publish aggregation dimensions while retaining individual metric series.",[
"Detailed monitoring increases the frequency of selected EC2 metrics; it does not automatically collect arbitrary custom application or guest metrics.",
"With appropriate metric inputs and dimensions, the agent's aggregation_dimensions can roll up by AutoScalingGroupName while preserving per-instance metrics unless deliberately dropped.",
"append-config combines agent configuration files; it is not the metric aggregation dimension setting.",
"A dashboard visualizes already published metrics but does not itself collect or tag custom application metrics."],"cloudwatch",note="Application metrics still need an input such as StatsD/collectd or explicit metric publication. aggregation_dimensions does not discover arbitrary application values automatically.")
r(164,"C","resilient","Compute maintenance","Standby removes an Auto Scaling instance from serving traffic without terminating it, allowing maintenance before returning it to InService.",[
"Hibernation suspends the OS state rather than providing the supported live maintenance/Auto Scaling serving-state workflow.",
"Cooldown affects scaling behavior; it does not isolate one instance from incoming load-balancer requests for maintenance.",
"Standby deregisters the instance from the load balancer and suspends its usual service role while the update is performed, then supports returning it to service.",
"Lifecycle hooks pause launch/termination transitions; they are not the simplest state for maintaining the same already running instance and returning it afterward."],"standby",note="Account for desired-capacity changes, replacement capacity, health checks and connection draining. Enough healthy capacity is required to avoid user impact.")
r(165,"C","resilient","Compute availability","Use health-aware load balancing plus Auto Scaling replacement, with sufficient healthy capacity to absorb a failure.",[
"Upsizing creates more capacity per server but still leaves the fleet unable to automatically replace a failed instance.",
"Flow Logs provide diagnostic network records, not failed-instance replacement or load balancing.",
"Health checks avoid unhealthy targets and Auto Scaling restores desired capacity by replacing failed instances.",
"Duplicating the same setup across Regions adds cost without directly fixing the missing automatic recovery mechanism."],"as alb",note="Configure the group's health checks to include the appropriate ELB/application health signal. Automatic replacement still takes startup and warm-up time.")
r(166,"A","secure","Remote user access","Client VPN is for authenticated individual users; Site-to-Site VPN connects networks, while Direct Connect needs a dedicated connection.",[
"Managed Client VPN supports individual user authentication, routes and authorization rules for the required private resources with no physical circuit to provision.",
"Direct Connect is not the quick, per-user authenticated access choice for a small temporary vendor team.",
"Site-to-Site VPN authenticates network endpoints and requires a suitable customer gateway; it does not supply the same individual-user client access model.",
"A Transit Gateway VPN introduces hub infrastructure appropriate to network interconnection, not the lowest-overhead individual user access pattern here."],"clientvpn",note="Compare actual connection/endpoint charges for usage duration. Limit authorization rules, client routes and destination security groups to the intended resources.")
r(167,"E","resilient","DNS & routing","Route 53 covers registration, DNS routing/traffic steering and health checks. DNS steering is distinct from per-request application load balancing.",[
"Domain registration is one Route 53 capability, but this option lists only one of the supported functions.",
"DNS routing to resources is supported, but it is not the complete list in the question.",
"Route 53 routing policies can distribute DNS answers across geographically distributed endpoints; that is one of the listed functions.",
"Health checks can influence routing for supported targets, but this is only part of the overall feature set.",
"All four statements describe Route 53 capabilities, interpreting 'load-balance' as DNS-level traffic steering rather than an HTTP reverse proxy."],"routing dns")
r(169,"C","secure","Container networking","awsvpc gives each ECS task its own ENI and security-group association, enabling task-level networking and visibility.",[
"Host mode shares the host's network namespace, rather than giving each task an independent ENI/security-group boundary.",
"An ENI per task is not the default behavior of every ECS network mode. The explicit awsvpc setting is required for this design.",
"awsvpc supplies a task ENI, private addressing and security groups so network controls and Flow Logs can distinguish task traffic.",
"Bridge mode uses Docker port mapping on the container instance rather than a separate security-group association for each task."],"ecsnetwork")
h(170,"The intended EC2-on-Outposts answer can place compute on premises, but 'lowest possible latency' depends on the actual client locations, hardware availability, residency and capacity. No location or operational constraints are given to choose uniquely over Local Zones.","performance","Hybrid compute","ecs")
r(171,"A","secure","Private service access","S3 interface endpoints can be reached from on-premises networks over supported private connectivity; S3 gateway endpoints are scoped to their VPC access paths.",[
"DynamoDB's gateway endpoint serves VPC workloads, while an S3 interface endpoint supports the future privately routed on-premises S3 clients.",
"A private NAT gateway translates private addresses for routed private connectivity; it does not itself provide a private S3 service endpoint.",
"A public NAT gateway reaches public endpoints and is not the private endpoint architecture requested.",
"Gateway endpoints work for current VPC-local access, but an on-premises client cannot simply transit a VPN/DX connection to use a VPC's S3 gateway endpoint."],"s3endpoint privatelink",note="For cost, VPC-local S3 traffic may additionally use a gateway endpoint while on-premises DNS resolves to the S3 interface endpoint. Configure private DNS and hybrid routing carefully.")
h(172,"An S3 CORS rule uses AllowedMethods (GET), AllowedOrigins and optionally AllowedHeaders/ExposeHeaders. The options incorrectly present Access-Control-Request-Method as the bucket configuration field and conflate request headers with rule format.","secure","Browser object access","s3")
h(173,"An allow-only bucket policy does not override other identity-based allows, while deny exceptions need carefully scoped Principal/condition handling. Several deny choices can work or misbehave depending on full policy details, permissions boundaries and role sessions; no complete policy is supplied.","secure","Resource policies","iam")
h(174,"The options do not identify whether the team needs CloudWatch metrics, database system views or console query-monitoring views. All require different data sources, so 'build custom queries' plus a console name is insufficiently specified.","performance","Database observability","redshift cloudwatch")
r(175,"A","resilient","Load balancer networking","An internet-facing ALB needs public subnets with a route to an Internet Gateway. Healthy targets do not prove internet reachability of the ALB itself.",[
"Without an Internet Gateway route in the ALB's subnet route table, external clients cannot reach the internet-facing load balancer as intended.",
"Targets can be in public or private subnets with proper connectivity; public target placement alone does not explain failed ALB ingress.",
"An ALB does not require a customer-associated Elastic IP address; it uses its managed DNS endpoint.",
"Cross-zone settings affect target traffic distribution, not a missing internet route to the ALB's public subnet."],"alb vpc")
r(176,"B","performance","Serverless applications","Fargate runs containers without managing EC2 hosts; Aurora Serverless supplies automatically scaling relational compute.",[
"Fargate matches the container requirement, but DynamoDB is non-relational and does not meet the relational database constraint.",
"Fargate removes container-host management and Aurora Serverless v2 adjusts relational database compute capacity within configured limits.",
"The EC2 launch type still requires managing container-instance capacity and its operating environment.",
"This option both retains EC2 host management and chooses a non-relational database instead of the required relational one."],"fargate serverless",note="Configure ECS service autoscaling and task resource limits. Fargate removes host management, but does not automatically choose an arbitrary service's task count without scaling configuration.")
FIXES[177] = {"option": {0: "http://169.254.169.254/latest/meta-data/ami-id", 1: "http://168.254.168.254/latest/metadata/ami-id", 2: "http://169.254.169.254/latest/user-data/ami-id", 3: "http://169.253.169.253/latest/dynamic/ami-id"}}
r(177,"A","secure","Instance metadata","IMDS exposes the launch AMI ID at /latest/meta-data/ami-id. With IMDSv2, first obtain a token and include it on the metadata GET.",[
"This is the standard IPv4 metadata address and the correct AMI metadata path. An IMDSv2 token header is required when v2-only access is enforced.",
"The address and path are wrong: 168.254.168.254 is not the EC2 IPv4 instance metadata endpoint.",
"User data is launch-supplied content; ami-id is part of instance metadata, not nested user data.",
"The endpoint and dynamic path do not identify the AMI metadata field."],"metadata",note="A bare unauthenticated GET is not a complete IMDSv2 request. The example identifies the URL only; use the token exchange and hop-limit settings appropriate to the workload.")
h(178,"Global Accelerator supplies static anycast IPs, but its public internet ingress does not meet 'avoid the public internet for device ingress'. Route 53 private endpoints do not repair that requirement either. The options do not provide a complete private-ingress design.","secure","Private ingress","ga")
h(179,"Native FSx for Lustre S3 integration is valid, but current DataSync support is not interchangeable with every FSx filesystem type. The question forces TWO without establishing a second independently valid Lustre-specific statement; export timing is also misstated.","performance","High-performance file storage","lustre datasync")
r(180,"BC","resilient","Shared file storage","FSx for Windows supports Single-AZ/Multi-AZ deployments and private SMB access from connected networks, subject to routing and AD permissions.",[
"FSx for Windows is a managed filesystem, not an EC2 instance-store cache shared globally across networks.",
"Private network connectivity such as peering, Transit Gateway, VPN or Direct Connect can allow clients in connected networks to reach the filesystem with proper routes, ports and directory access.",
"FSx for Windows provides supported Single-AZ/Multi-AZ and SSD/HDD deployment options, with performance and feature constraints to consider.",
"The listed private connectivity mechanisms are supported ways to provide routed client access; they are not categorically prohibited.",
"FSx for Windows provides Windows/SMB semantics, not a guarantee of a fully POSIX-compliant Linux filesystem."],"fsxwindows")
h(181,"Parallel multipart uploads and a metadata index can help, but Transfer Acceleration benefits depend on geography and are not automatically useful for EC2-to-S3 processing within one Region. The source bundles conditional techniques into one mandatory answer without the relevant network details.","performance","Object storage performance","s3")
h(182,"Neither DynamoDB Streams nor an ordinary mutable database guarantees an immutable transaction ledger. The options omit an explicit append-only/tamper-evident design, so no unique service choice satisfies the requirement as stated.","secure","Immutable data","objectlock dynamostream")
h(183,"Target tracking has different warm-up/scale-in behavior from simple-scaling cooldowns. A wrong metric or suppressed scaling could explain the symptom; a group's min/desired zero is not inherently invalid. Alarm history and policy details are missing.","performance","Compute scaling","as")
r(184,"AC","performance","HPC networking","Cluster placement groups place supported instances close together within one AZ. Instances can change placement groups under supported stop/start rules, but groups cannot be merged.",[
"A cluster placement group in one AZ is the intended low-latency/high-throughput placement strategy when local availability tradeoffs are acceptable.",
"The placement group does not extend its low-latency physical placement guarantee across a Direct Connect link to on-premises hardware.",
"Supported instance placement can be changed using the required stopped-state operations, while separate placement groups themselves cannot be merged.",
"Moving an instance does not create an operation that merges placement groups; that claimed capability is unsupported.",
"Spread placement prioritizes hardware separation for resilience rather than tight physical proximity for the lowest inter-instance latency."],"placement efa")
r(185,"D","performance","Streaming ingestion","Use Video Streams to ingest camera footage. Rekognition analyzes video, while ingestion/storage is a separate responsibility.",[
"Elastic Transcoder is not the live multi-camera ingestion and durable video-stream service.",
"Rekognition Video analyzes video content; it is not the underlying camera-stream ingestion buffer/storage service named in this requirement.",
"SageMaker supports ML workloads, but requires an ingestion/data pipeline rather than replacing the specialized camera video transport.",
"Kinesis Video Streams securely ingests video from distributed cameras and makes it available to downstream analysis consumers."],"video")
r(186,"C","resilient","Content delivery resilience","CloudFront custom error responses map selected origin error codes to a configured page hosted in an accessible origin.",[
"Merely storing an error page does not tell CloudFront which origin status codes should use it; configure the custom error mapping.",
"Chaining distributions is unnecessary and not the supported simple custom-error-response configuration.",
"Host the static error page in S3 or another suitable origin, then configure Custom Error Responses with the desired 5xx code/path and caching behavior.",
"CloudFront is a delivery/cache service, not an object store into which you directly upload a custom page."],"cferror",note="Some CloudFront-generated 5xx conditions are treated differently. Test the origin-error paths, custom response code and error-caching TTL.")
r(187,"B","resilient","Cache freshness","An invalidation removes the cached object path so subsequent requests can fetch the updated origin version. Versioned filenames are useful for future deployments.",[
"Waiting for TTL expiry leaves the known broken configuration in use for up to the remaining cache lifetime.",
"Invalidate the affected path to cause CloudFront to stop using that cached object and fetch the current origin content on a subsequent request.",
"Changing a default TTL is not a reliable immediate removal of an already cached object under existing cache headers/policies.",
"Changing origin headers alone does not proactively remove the stale object that CloudFront already holds."],"cfinvalidate",note="Invalidation propagation is not instantaneous. Browser/client caches may have their own freshness behavior; versioned asset/config paths can avoid repeat stale-cache problems.")
r(188,"D","performance","Load balancing","HTTP Host header conditions require an Application Load Balancer's host-based listener rules, not an NLB's transport-layer listener.",[
"An NLB does not offer an HTTP listener with ALB-style Host header routing rules.",
"TCP listeners do not inspect HTTP URL paths or Host headers for ALB-style content routing.",
"An ALB is appropriate, but path-based routing matches URL paths rather than the required Host header.",
"ALB host-header conditions route the two hostnames to their respective target groups."],"alb")
r(189,"A","resilient","Container load balancing","Both ALB and NLB integrate with ECS dynamic host-port mapping. Classic Load Balancers lack the target-group host-port capability used here.",[
"ECS can register an instance/IP plus dynamically assigned port into the appropriate ALB or NLB target group, allowing multiple tasks per host.",
"ALB supports the feature, but it is not the only listed supported load-balancer family; NLB supports the appropriate integration too.",
"NLB supports the feature, but ALB is also supported, so this option is incomplete.",
"Classic Load Balancers do not supply the dynamic target-group port-mapping model required for this ECS design."],"ecs alb",note="Network mode, target type and security rules must match the service. Permit the actual ephemeral host-port range only from the appropriate load-balancing path.")
r(190,"C","secure","Secret rotation","A custom Secrets Manager rotation Lambda must update the external credential and the stored secret through the rotation stages; storing a value alone cannot rotate a third-party API key.",[
"Parameter Store does not replace Secrets Manager's custom rotation workflow and does not make an external API rotate its key automatically.",
"Putting multiple keys in one secret does not configure an automatic annual rotation against the external API.",
"A custom rotation Lambda can create/update/test the external API key and promote the new secret version according to a configured schedule.",
"Alternating reads between two secrets is not a rotation implementation and does not update the actual API credential."],"secrets",note="The external provider must support a suitable credential rotation API/workflow. Clients should retrieve the current stage and cache carefully through rotation.")
r(191,"D","secure","Configuration compliance","AWS Config can evaluate whether secrets have rotation enabled; a notification integration reports noncompliance. Detection does not itself enable rotation.",[
"There is no universal one-click guarantee that every arbitrary secret has a correct external rotation implementation.",
"Matching every Secrets Manager event is not the same as assessing current rotation configuration and produces irrelevant notifications.",
"GuardDuty detects threats rather than evaluating the requested rotation-enabled configuration rule.",
"A supported Config managed rule can evaluate rotation configuration, with compliance-change notifications routed through a supported event/SNS integration."],"secrets",note="Verify the exact Config managed rule identifier for the Region (for example secretsmanager-rotation-enabled-check) and configure notification/remediation separately.")
r(192,"B","secure","Encrypted analytics","Athena can query SSE-KMS-encrypted S3 objects when the querying identity and service workflow have the necessary S3 and KMS permissions.",[
"KMS private keys are not supplied to Athena. Symmetric KMS protection is used through authorized KMS operations.",
"S3 handles server-side decryption for authorized reads; Athena needs the relevant object/catalog access and kms:Decrypt authorization for the KMS key.",
"Converting to SSE-S3 is unnecessary; SSE-KMS is a supported query input when access is configured correctly.",
"Disabling encryption would weaken the data controls and is not required to create or query the table."],"athena kmspolicy")
r(193,"C","performance","Data catalogs","A Glue crawler inspects a supported data source and creates/updates Data Catalog metadata; a classifier is part of determining data formats/schemas.",[
"A Catalog table stores metadata after it is defined/discovered; the table object itself does not run source discovery.",
"An Athena table is query metadata, not the Glue source-inspection process requested.",
"A crawler traverses the configured supported source, determines schema using appropriate classifiers/connectors and populates the Glue Data Catalog.",
"A classifier helps identify schema/format within the crawling process; it is not the complete scheduled source-discovery/catalog-population component."],"glue")
h(194,"The phrase 'acts as the Organization' is underspecified and a fourth answer is missing. Supported API actions can be audited in CloudTrail and matched through EventBridge for notifications, but the source needs a precise event definition.","secure","Audit & observability","cloudtrail")
r(195,"C","resilient","Stream retention","A consumer must read records before stream retention expires. A two-day batch export can miss data under Kinesis's default 24-hour retention.",[
"Sensor failure is possible in general, but the recurring age-based gap is directly explained by the configured retention and export interval.",
"S3 has no one-day retention limit; objects persist until deleted or expired by applicable lifecycle rules.",
"Default Data Streams retention is 24 hours, so records can age out before an every-other-day exporter reads them.",
"Kinesis is suitable for telemetry. The issue is the retention/read schedule mismatch, not the category of input data."],"kinesis",note="Increase retention appropriately or run a continuous delivery/consumer pipeline with monitored lag; retention is not an archive strategy by itself.")
r(196,"A","resilient","Object protection","S3 Versioning preserves older object versions and uses delete markers for ordinary deletes, allowing recovery when the underlying versions remain.",[
"Versioning retains previous versions and makes many accidental overwrites/deletes recoverable by restoring a version or removing the relevant delete marker.",
"A read-only policy stops legitimate application writes as well and does not provide recovery for already deleted or overwritten data.",
"A lower-cost lifecycle transition changes storage class, not deletion recoverability; expiration rules can instead remove recovery points.",
"Encryption protects confidentiality, not preservation of a deleted version."],"versioning",note="Principals with DeleteObjectVersion can still permanently delete versions unless constrained. Consider least privilege, retention and Object Lock for stronger requirements.")
h(197,"The screenshot contains damaged cryptographic abbreviations and implementation-specific CloudHSM backup internals. Verify the current CloudHSM backup design rather than infer PBK/EBK relationships from the marks; this is outside the high-yield core set.","secure","Hardware key management","kms")
r(198,"B","performance","Data warehousing","Redshift is the analytical SQL warehouse among these services, with JDBC/ODBC ecosystem integration for BI and reporting tools.",[
"DynamoDB is key-value/document operational storage, not the SQL warehouse/BI connection model described.",
"Redshift supports analytical SQL over large datasets and integration with reporting/BI clients through standard connection drivers.",
"Kinesis ingests/processes streams; it is not the general relational analytical warehouse for persistent SQL reporting datasets.",
"SQS is a messaging queue, not a SQL analytical datastore."],"redshift")
r(199,"B","secure","Encryption permissions","KMS key-use permission is different from key administration. An encrypted Kinesis producer needs authorized key operations, not blanket key-administrator power.",[
"Key administration is broader than necessary and does not automatically imply every cryptographic data-use permission.",
"Authorize the producer role for the required KMS data-key operation in the key/identity policy model, scoped to the intended stream/key context.",
"Changing to the AWS-managed key can alter controls but is not the least-privilege fix for the existing customer-key policy requirement.",
"Stream server-side encryption is applied by Kinesis; a producer-library switch does not bypass missing service-side KMS authorization."],"kmspolicy kinesis",note="Producers generally need kms:GenerateDataKey; consumers need kms:Decrypt. Cross-account use and key policies need explicit evaluation.")
r(200,"A","secure","Attribute-based access","Environment tags can drive IAM condition-based access, provided tag modification and resource creation are also controlled.",[
"Tags such as Environment=dev/test/prod can be referenced by applicable IAM condition keys to authorize the intended administration scope.",
"User data configures instance startup and is not the standard IAM resource-tag access-control mechanism.",
"Instance metadata describes the instance to the guest; adding arbitrary metadata does not create IAM policy conditions equivalent to governed resource tags.",
"An Auto Scaling group organizes capacity, but membership alone does not define each administrator's allowed API permissions."],"iam",note="Tag-based policies are only secure when principals cannot freely retag resources into an allowed environment. Validate which actions support the condition keys.")
FIXES[201] = {"option": {0: "ApproximateNumberOfMessagesVisible", 1: "NumberOfMessagesReceived", 2: "NumberOfMessagesDeleted", 3: "ApproximateNumberOfMessagesNotVisible"}}
r(201,"A","performance","Queue-driven scaling","Visible messages are available work waiting in SQS. In-flight and cumulative activity metrics describe different states.",[
"ApproximateNumberOfMessagesVisible measures available queued work and is the direct queue-length signal for worker scaling.",
"NumberOfMessagesReceived is an activity count that can include repeat receives; it is not the current pending backlog.",
"NumberOfMessagesDeleted describes completed/deleted message activity, not the amount of work still waiting.",
"NotVisible messages are in flight under a visibility timeout, not the visible backlog awaiting workers."],"sqs as",note="For target tracking, backlog per worker is often a better proportional metric than absolute queue length. Include acceptable processing latency in the target.")
r(202,"ADE","performance","Database read scaling","Read replicas and caching offload reads; sharding can distribute load across independent databases but requires application/data-model changes.",[
"Routing read-only queries to replicas spreads read load beyond the primary's CPU.",
"Storage Auto Scaling increases allocated storage capacity, not database CPU or read-query execution capacity.",
"Queuing may smooth workload but does not itself add read capacity for synchronous read-heavy database requests.",
"Caching common read results avoids repeated database query execution and reduces primary load.",
"Sharding divides data/work across multiple database instances, increasing aggregate capacity at the cost of application and operational complexity.",
"A traditional RDS MySQL Multi-AZ DB instance standby is for failover, not a readable replica for scaling queries."],"rds aurora",note="Distinguish RDS Multi-AZ DB instances from supported Multi-AZ DB clusters with readable instances. The source describes the traditional instance/standby model.")
r(203,"B","resilient","Messaging & integration","SNS fans a published message out to subscriptions; subscription filters can route categories to dedicated SQS worker queues.",[
"Amazon MQ is for managed message brokers/protocol compatibility, introducing broker operations unnecessary for native SNS-to-SQS routing.",
"SNS supports publish/subscribe delivery to SQS and filter policies that select which requests each worker queue receives.",
"SQS is the queue destination; one queue does not itself provide a topic's publish/subscribe routing across the other queues.",
"Step Functions orchestrates workflows and state transitions, not the simplest topic-based fanout routing layer."],"sns sqs")
h(204,"Lambda request count and allocated memory are relevant, but billed execution duration is also essential and is absent. Timeout is a configured upper bound, not actual billed duration. The exact two-factor phrasing is incomplete for estimating cost.","cost","Serverless pricing","lambda")
r(205,"A","secure","Immutable data","Object Lock applies WORM retention or legal holds to S3 object versions. Versioning alone does not prevent permanent version deletion.",[
"Enable Object Lock and configure appropriate compliance-mode retention or governance controls to protect object versions for the required period.",
"Versioning preserves versions but an authorized principal can still permanently delete a version without an additional retention control.",
"A read-only bucket policy can be changed by authorized administrators and is not an equivalent time-bound WORM retention mechanism.",
"S3 ACLs do not contain a WORM-model setting; retention is an Object Lock feature."],"objectlock",note="Enabling Object Lock alone is not a retention policy. Compliance mode prevents shortening/deletion during retention, while governance mode has authorized bypass behavior. Object Lock can also be enabled on supported existing buckets.")
r(206,"B","cost","Object storage lifecycle","Expire objects when retention ends; transition rules change storage class, while expiration rules remove no-longer-needed data.",[
"S3 storage-class objects are managed with S3 Lifecycle, not an independent Glacier vault rule that places S3 delete markers.",
"An expiration action based on 365 days since creation matches the stated end of retention and removes unnecessary ongoing storage.",
"Cleaning expired delete markers removes markers that no longer have associated versions; it does not define the desired object expiration policy.",
"Deep Archive does not automatically delete an object at one year; expiration still needs a configured lifecycle action."],"s3 versioning",note="For versioned buckets, expiration may create a delete marker; configure noncurrent-version expiration to remove retained versions when policy permits.")
h(207,"Athena is the right cost-conscious S3 log query tool, but the premise registers on-premises NLB targets by instance ID, which is not valid for on-premises addresses; these require IP targets. The source mixes a valid analysis question with an invalid target setup.","performance","Log analytics","athena")
h(208,"The access protocol, sharing scope and meaning of global low latency are unspecified. EFS is regional shared NFS; S3 is globally reachable object storage; neither automatically guarantees low-latency shared filesystem semantics worldwide.","performance","Shared storage","efs s3")
h(209,"Restrict database ingress to the application security group/port is the relevant control, but option A refers only to ports within a security group without specifying the source. Ports alone do not exclude external principals. The exact least-privilege rule is missing.","secure","Network access controls","vpc")
r(210,"C","resilient","Streaming logs","Kinesis Data Streams can buffer live log records for custom near-real-time analysis consumers.",[
"CloudFront delivers/caches HTTP content; it is not an ingestion stream for EC2 log analysis.",
"SQS can queue tasks but does not provide the replayable multi-consumer stream model requested for continuous log analytics.",
"Kinesis Data Streams supports ingestion, retention and independent custom consumers for analyzing streamed log events.",
"SES sends email and is not a log-stream ingestion/retention platform."],"kinesis cloudwatch",note="A collection agent/integration must publish the logs. Kinesis does not automatically discover and tail every file on EC2.")
r(211,"A","secure","Private content delivery","Use signed cookies to authorize multiple private CloudFront resources without modifying their existing URLs.",[
"Signed cookies carry the viewer's policy/signature separately from the URL and can authorize the premium content paths.",
"Signed URLs attach authorization information to each URL, conflicting with keeping current links unchanged across multiple resources.",
"S3 presigned URLs authorize S3 requests rather than provide CloudFront viewer-cookie authorization for the existing content links.",
"Geographic restrictions filter by viewer location, not by whether the viewer has paid for a subscription."],"cloudfront")
r(212,"C","resilient","IP addressing","Stopping an EBS-backed instance preserves its EBS data, but normally releases its auto-assigned public IPv4 address.",[
"An allocated Elastic IP is intended to remain stable until disassociated/released; it is the auto-assigned address that normally changes after stop/start.",
"The instance's security-group associations persist across stop/start and do not need routine reassignment.",
"Restarting after a stop assigns a new ordinary public IPv4 address, so clients/configurations pointing at the old address fail.",
"EBS-backed instances can be stopped; stop is not automatic termination of the instance and attached persistent data."],"publicip ebs")
r(213,"B","resilient","Object storage consistency","After a successful delete, S3 provides strong consistency for subsequent GET/LIST requests against that bucket; geography does not cause an eventual-consistency delay.",[
"A successfully deleted unversioned object should not continue appearing because of an old eventual-consistency assumption.",
"With no versioning or retention protection, a successful delete removes the object, and subsequent list operations reflect that deletion.",
"The API success response establishes the completed operation for S3's strong-consistency model; the given LIST is not expected to randomly show the deleted object.",
"Delete markers are a versioning mechanism; the bucket in this scenario is unversioned."],"consistency versioning")
r(214,"D","resilient","Workflow orchestration","Step Functions supplies explicit workflow state, retries and a graphical execution view for multi-step serverless processing.",[
"SQS decouples tasks but does not provide the requested end-to-end state-machine execution graph on its own.",
"SWF is a different workflow service and is not the straightforward managed visual serverless state-machine solution requested.",
"Independent Lambda triggers do not create the explicit orchestration state/visual workflow for all the processing steps.",
"S3 events can start a Step Functions workflow whose tasks invoke the processing services and update metadata in DynamoDB, with execution state visible in the console."],"steps dynamo",note="Long video transcodes should use an appropriate media/batch service integration; an individual Lambda task cannot run indefinitely.")
r(215,"ACE","secure","Workload IAM roles","Writing logs from a fresh Lambda environment needs log-group creation when absent, log-stream creation and log-event writes.",[
"CreateLogGroup permits creation when a log group has not been provisioned yet.",
"GetLogEvents is a read operation and is not required merely to emit function logs.",
"CreateLogStream permits the runtime to create the stream it writes into.",
"DescribeLogStreams is not one of the three core write-path actions requested.",
"PutLogEvents authorizes sending the function's log records to its stream."],"lambda cloudwatch",note="Scope log actions to the function's groups/streams where the API supports resource-level permissions, with correct creation-time ARN handling.")
h(216,"X-Ray supplies traces/service maps, but an 'enable Insights notifications' setting is not a complete anomaly-to-notification integration. Instrumentation and an EventBridge/SNS or equivalent notification path need explicit configuration.","resilient","Distributed tracing","xray")
r(217,"D","performance","Streaming ingestion","A retained Kinesis stream lets multiple downstream consumers independently process bursty GPS updates.",[
"Firehose specializes in buffered delivery to destinations rather than arbitrary independent consumers with their own replay positions.",
"IoT Core supports device messaging/connectivity, but the data-stream service is the direct match for the retained multi-consumer buffer.",
"Checking batch-job dependencies is unrelated to ingesting and retaining live location events.",
"Kinesis Data Streams supplies a scalable retained event stream suitable for concurrent near-real-time consumer applications."],"kinesis")
h(218,"Textract plus Polly is the intended OCR-to-speech combination, but language support, document layout, handwriting and book-length input constraints must be validated. A proper service-specific review is still needed before scoring this item.","performance","AI service selection")
h(219,"The intended B describes correct response headers, but a cross-origin browser upload must also configure CORS ExposeHeaders to read x-amz-version-id and x-amz-server-side-encryption. Without that omitted step the stated browser requirement is not met.","secure","Browser object access","presign sse")
h(220,"Separate queues/state machines do not automatically prioritize Polly's own asynchronous tasks, and Lambda reserved concurrency does not guarantee Polly scheduling priority or lower off-peak per-request pricing. The compound answer overpromises these properties.","resilient","Workflow orchestration","steps")
r(221,"C","resilient","Hybrid file storage","File Gateway maps NFS/SMB files to S3 objects, so authorized administrators can access the object representation through S3 APIs; Volume Gateway stores block data in a different format.",[
"Cached Volume Gateway exposes block volumes whose AWS storage is not the same directly browsable object/file representation described.",
"Stored Volume Gateway keeps primary block data locally and backs it up as snapshots, not ordinary directly editable file objects in S3.",
"S3 File Gateway exposes file shares with files represented as S3 objects, permitting authorized direct S3 object access by administrators.",
"Tape Gateway presents virtual tape backup interfaces, not a general NFS/SMB file share backed by accessible file objects."],"gateway",note="Do not concurrently modify the same files through both interfaces without a cache-refresh/consistency strategy. Apply IAM/bucket/share controls for application-only and admin exception access.")
h(222,"Snapshot-and-restore is the supported cross-AZ data movement, but it does not by itself guarantee immediate full first-read performance. The choices omit fast snapshot restore or a supported initialization strategy, as well as quiescing data for consistency.","resilient","Block storage migration","ebs")
r(223,"D","resilient","Object storage consistency","S3 has strong read-after-write consistency for successful object writes to the source bucket, including subsequent reads/listing from other client locations.",[
"The old eventual-consistency assumption for newly written S3 objects is incorrect; successful writes are strongly consistent for later reads/listing.",
"The question asks about S3 object availability; this statement about EFS does not answer that requirement.",
"Claiming eventual consistency as the reason for immediate availability is self-contradictory and does not describe the required S3 behavior.",
"A successfully completed S3 PUT is immediately visible to subsequent reads/list operations against that bucket under its strong-consistency model."],"consistency",note="This does not mean cross-Region replication or CDN caches update synchronously. It concerns reads against the bucket where the write completed.")
h(224,"Target tracking and AZ rebalancing can both help, but the source's per-AZ limits and 'without additional scaling costs' guarantee are not well-defined. Rebalancing, warm-up, allocation rules and application routing need concrete configuration.","performance","Compute scaling","as")
r(225,"B","resilient","Cross-Region database recovery","Promote the cross-Region read replica before using it as a writable replacement, then update the application's supported endpoint configuration.",[
"Changing a name for the unavailable primary does not make that original database recover in another Region.",
"Promotion converts the available read replica into an independent writable DB instance; the application can then use its endpoint or a suitable application-controlled alias.",
"The AWS-managed RDS endpoint is not an arbitrary record the customer can edit to point at another instance.",
"A multi-master active/active redesign is not the simple recovery action for the already provisioned active/passive architecture."],"rds dr",note="The replica may lag, promotion takes time, and application DNS/TLS hostname validation and connection refresh need a tested plan. DNS changes alone do not guarantee zero data loss.")

r(242,"D","cost","Archive retrieval","Glacier Flexible Retrieval Standard typically restores in 3–5 hours. Expedited is faster; Bulk takes longer but can be cheaper.",[
"Vault Lock is a retention-policy control in the separate Glacier vault service, not a retrieval speed tier.",
"Expedited is designed for much faster restoration where supported/capacity is available; it is unnecessary if 3–5 hours is acceptable.",
"Flexible Retrieval Bulk generally takes about 5–12 hours, so it can exceed the stated 3–5-hour requirement.",
"Standard is the retrieval option with the typical 3–5-hour restore time matching this requirement."],"s3",note="Typical retrieval times are not a universal hard real-time guarantee. Confirm service terms and the operational SLA before promising a strict maximum.")
r(243,"A","secure","Network access controls","Reference the frontend security group in the backend's port rule to authorize frontend instances even as Auto Scaling replaces their IP addresses.",[
"A security-group source reference authorizes traffic from the intended frontend members on the specified backend port.",
"A subnet CIDR also authorizes unrelated instances sharing that subnet, exceeding the frontend-only requirement.",
"An Auto Scaling group ARN is not an accepted IP/security-group source in a security-group ingress rule.",
"A launch configuration is an instance launch template-like configuration, not a security-group rule source."],"vpc")
r(244,"A","cost","Compute pricing","Use flexible Compute Savings Plans for variable EC2 families, family/Region-bound EC2 Instance Savings Plans for a stable tier, and RDS Reserved Instances for eligible RDS usage.",[
"This aligns the purchase commitments with each tier: flexible compute, stable-family compute, and a database-specific reservation product.",
"EC2 Instance Savings Plans do not discount RDS database usage.",
"The commitments are mismatched to the varying web families, and Compute Savings Plans do not apply to RDS.",
"A family-bound plan reduces web-tier flexibility and leaves the steady eligible RDS usage undiscounted."],"savings",note="Billing commitments do not provide high availability themselves. Keep Multi-AZ architecture, enough capacity and the right reservation attributes independently configured.")
REVIEWS[245] = dict(REVIEWS[212])
r(246,"B","performance","HPC networking","EFA targets low-latency tightly coupled HPC communication on supported EC2 instances and software stacks.",[
"ENA improves standard networking, but EFA's OS-bypass interface is specifically intended for tightly coupled HPC communication.",
"EFA provides the specialized low-latency/high-throughput interface for supported distributed HPC libraries and EC2 instance types.",
"Attaching more ordinary ENIs does not automatically increase the instance's network bandwidth limits or supply an HPC communication fabric.",
"There is no generic Elastic Network setting named here that replaces configuring the supported ENA/EFA hardware interface."],"efa placement")
r(247,"A","performance","Big data processing","Separate durable raw logs in S3 from distributed compute. EMR supplies a managed framework for Spark/Hadoop-style transformations.",[
"S3 provides a durable landing zone and EMR supplies managed distributed processing frameworks suited to large-scale log transformation and analytics.",
"Custom EC2 scripts can process logs but add cluster/framework management compared with the requested managed distributed processing service.",
"Instance-local storage couples data retention to workers and requires durability/replication management the S3 landing zone avoids.",
"DynamoDB is not the simplest raw log landing zone for this analytical batch framework, and custom EC2 scripts retain management overhead."],"emr s3")
r(248,"A","resilient","Object replication","S3 Cross-Region Replication automatically copies eligible new object versions to a configured destination bucket; it is asynchronous.",[
"A CRR rule provides native managed replication to the destination Region once versioning, permissions and the rule are configured.",
"A scheduled script introduces custom retry, change detection and operations that native replication handles.",
"S3 does not expose a generic S3 snapshot feature that creates continuous cross-Region object replication.",
"Versioning preserves versions in a bucket; it does not copy those versions to another Region without a replication rule."],"crr",note="Enable versioning on both buckets and configure the replication role. Existing objects require a separate backfill/Batch Replication strategy; 'automatic' does not mean synchronous.")
r(249,"B","cost","Object storage lifecycle","Frequently accessed short-lived objects fit S3 Standard plus Lifecycle expiration, avoiding archive minimum-retention and retrieval penalties.",[
"EBS and a custom deletion script require volume sizing, a running host and maintenance rather than native object lifecycle management.",
"S3 can serve the hot video objects and expire them automatically after 30 days through a managed lifecycle rule.",
"Archive classes do not fit heavily accessed hot content and can incur retrieval delays/charges and minimum storage-duration charges.",
"Stored Volume Gateway is a hybrid block-storage service and adds infrastructure unrelated to native web object retention."],"s3 versioning",note="In versioned buckets, configure noncurrent-version expiration as appropriate; a delete marker alone does not remove all billed versions.")
r(250,"D","secure","Audit integrity","CloudTrail log file integrity validation uses signed digest files to detect changes/removal. Encryption protects confidentiality, not proof of log-file history.",[
"SSE-S3 encrypts stored data but does not create CloudTrail's signed digest chain for integrity validation.",
"SSE-KMS adds key controls/auditing but does not substitute for log-file integrity validation.",
"Access restriction reduces tampering opportunities but is not cryptographic evidence that delivered logs remain unchanged.",
"Integrity validation delivers signed digests that can be used to verify the integrity of subsequently delivered log files."],"trailvalidation",note="Enabling the feature now does not retroactively generate validation digests for logs delivered last year. Actually run validation and retain/protect the necessary digest files.")
r(251,"B","secure","Workload IAM roles","An EC2 instance profile delivers temporary role credentials to the workload, avoiding stored long-term keys.",[
"Embedding an access key in code creates a long-lived secret and complicates rotation and containment.",
"Attach an appropriately scoped IAM role through an instance profile, letting the SDK retrieve managed temporary credentials for the required S3 operations.",
"A repository is not a safe storage/delivery mechanism for long-term production access keys.",
"User data is not a secret vault and can expose credentials through launch configuration or instance access."],"iam metadata")
h(252,"The generic source/destination rules are correct at workload subnets, but Transit Gateway attachment-subnet NACL evaluation has direction-specific exceptions. The source needs the exact subnet/direction identified before it can be scored without teaching an overbroad rule.","secure","Network access controls","vpc")
r(253,"B","resilient","Compute lifecycle","A termination lifecycle hook pauses an Auto Scaling transition so an external action can drain, checkpoint or copy state before completion.",[
"Cooldown changes scaling timing, not a per-instance pause for custom termination cleanup.",
"A terminating lifecycle hook moves the instance into a wait state, allowing cleanup/checkpoint automation before completing the transition.",
"A termination policy chooses which instance to remove; it does not execute the cleanup workload itself.",
"Suspending termination prevents normal scale-in broadly rather than running cleanup and then continuing each termination."],"hooks",note="Lifecycle hooks have timeouts/default results; they are not a durability guarantee. Stateful database data should also have a sound replication/backup architecture.")
r(254,"DE","resilient","Availability capacity planning","To survive any one AZ loss with six running instances, subtract the largest AZ's allocation and check that at least six remain.",[
"2+2+2 leaves only four after losing any AZ, below the six-instance requirement.",
"3+3+0 leaves only three if either populated AZ fails.",
"4+2+2 leaves only four if the four-instance AZ fails, so it does not survive every single-AZ failure.",
"6+6+0 leaves six if either populated AZ fails and twelve if the unused AZ fails, meeting the requirement.",
"3+3+3 leaves six after any one AZ fails, meeting the requirement with nine total instances."],"as dr")
r(255,"D","cost","Event-driven processing","Upload large files to S3 and invoke short-lived metadata work from object events. Pass object references, not 25-GB bodies, into messaging/compute triggers.",[
"Firehose is not intended to ingest individual 25-GB records/files as a message and then run the proposed metadata transform.",
"A queued EC2 worker fleet can work if messages reference files, but introduces worker capacity and startup/idle overhead for a few-second metadata task.",
"One EBS volume/instance couples ingestion to one host and does not provide the requested durable elastic event-driven object workflow.",
"S3 handles the large object upload, and a completion event invokes Lambda to read required metadata without paying for idle worker hosts."],"s3events lambda",note="S3 notifications are at-least-once; make metadata writes idempotent. Do not download a 25-GB file into Lambda merely to read object headers; use event/HeadObject data where sufficient.")
r(256,"C","resilient","Global network performance","Global Accelerator uses stable anycast ingress and health-based endpoint routing, reducing dependence on client DNS-cache refresh during failover.",[
"Geolocation DNS routing chooses location-based answers and remains subject to resolver/client caching; it does not guarantee seconds-level propagation to every user.",
"WAF filters web requests; it is not a CDN or global traffic acceleration/failover service.",
"Global Accelerator sends users through the AWS global network to healthy regional endpoints behind stable anycast addresses.",
"Direct Connect serves dedicated hybrid network connectivity, not general internet users scattered worldwide."],"ga",note="Application state, endpoint support, health checks and client protocols still determine end-to-end recovery. Accelerator routing alone cannot guarantee an application-wide RTO.")
HOLDS[257] = dict(HOLDS[104])
h(258,"The workload omits the actual throughput/IOPS target and uses a small capacity whose supported sc1 minimum must be checked against the current service version. Lowest storage price alone does not prove the burst requirement is met.","cost","Block storage","ebs")
r(259,"D","cost","Compute purchasing","Keep a non-interruptible On-Demand baseline and diversify interruptible burst capacity with a mixed instances policy where the workload tolerates replacement.",[
"Arbitrarily switching every instance to t2.micro can underprovision CPU/memory and does not establish performance suitability.",
"All On-Demand preserves capacity behavior but forgoes the proposed lower-cost interruptible burst capacity.",
"All Spot can be interrupted and removes the explicit stable baseline the application requires.",
"A mixed policy can maintain two On-Demand baseline instances and use a chosen mix above that baseline, reducing burst costs with controlled Spot exposure."],"spot",note="Spot is only appropriate for interruption-tolerant, recoverable instances. Use diverse instance pools, capacity-aware allocation and graceful draining; the policy alone cannot guarantee performance.")
r(260,"D","secure","Remote administration","A classic bastion pattern places the reachable jump host in a public subnet and allows narrowly scoped SSH from it to private targets.",[
"A private-subnet bastion is not directly reachable from the internet without a separate access path, contrary to this specified jump-host design.",
"A NAT instance in a private subnet does not supply the required internet-reachable administration jump host.",
"A NAT instance provides address translation; it is not the purpose-built administration host and credential/session workflow requested.",
"A hardened public-subnet bastion can accept restricted administrator access and connect to private database servers under scoped security-group rules."],"vpc sessionmanager",note="The question explicitly requires a jump host. If that restriction can change, Session Manager often removes the need for public SSH infrastructure.")
r(261,"B","resilient","Infrastructure drift","CloudFormation drift detection compares supported properties explicitly specified in the template, not every implicit service default.",[
"Running at individual-resource scope does not make unspecified default property values become part of the template comparison.",
"Explicitly declaring the relevant supported property gives CloudFormation an expected value to compare during drift detection.",
"Manual review remains useful, but it is not necessary to give up automated comparison for a supported property that can be specified in the template.",
"Read permissions matter for detection generally, but do not solve an absent expected value for an implicit default."],"cfnDrift")
r(262,"A","resilient","Object replication","Live CRR covers eligible new versions; S3 Batch Replication backfills eligible existing objects. Track replication status for evidence.",[
"Configure CRR for ongoing writes and Batch Replication for the existing dataset, with versioning/roles and status reporting appropriately configured.",
"Transfer Acceleration improves transfer paths and does not automatically maintain a destination-Region copy.",
"Lifecycle transitions change storage class/retention, not the object's AWS Region.",
"CloudFront edge caching is not a compliance-controlled complete replica of every retained object version in a specified destination bucket."],"crr",note="Use appropriate Inventory/status/metrics evidence and define handling for failures, deleted versions, encrypted objects and replication timing.")
r(263,"BC","secure","Network segmentation","Instance security groups isolate each tier without changing subnet-wide NACL behavior for unrelated applications.",[
"A subnet NACL affects every resource in that subnet and is broader than the targeted web-tier control requested.",
"A web-tier SG allowing only the required HTTPS internet ingress implements the first requirement without modifying other instances' subnet rules.",
"A DB SG that permits MySQL only from the web-tier SG limits database ingress to the intended tier.",
"A deny-all outbound NACL blocks required stateless response traffic and changes the whole shared subnet's behavior.",
"HTTPS is not the MySQL database port; the DB must accept the required database protocol from the frontend tier."],"vpc")
r(264,"AB","resilient","Highly available migration","Preserve the MySQL application interface with RDS MySQL Multi-AZ, and spread automatically replaced web capacity across AZs.",[
"RDS MySQL retains the engine interface while Multi-AZ supplies managed standby/failover for the database.",
"A multi-AZ EC2 Auto Scaling web tier provides distributed capacity and automatic instance replacement, preserving the server-based application model.",
"S3 is object storage, not a MySQL database with relational read replicas.",
"DynamoDB requires a different API/data model and a caching layer is a separate design; this is not minimal-change migration.",
"Aurora can be compatible with MySQL, but 'drop-in' is not guaranteed and Serverless alone is not the explicit Multi-AZ MySQL solution requested."],"rds as")
r(265,"A","performance","Multi-Region databases","Global tables provide managed multi-Region local access and replication with defined conflict/consistency behavior; cross-Region RDS replicas are not active-active writers.",[
"DynamoDB global tables support multi-Region replication and local reads/writes with service-defined conflict/consistency behavior, rather than custom replication code.",
"Aurora cross-Region read replicas normally replicate from a primary writer and do not supply independent active-active writes in each Region.",
"Traditional RDS Multi-AZ is regional availability/failover, not multi-Region active-active writing.",
"S3 CRR copies objects asynchronously; it is not a millisecond-latency transactional multi-Region database."],"globaltable",note="For eventually consistent global tables, conflicting writes use a defined last-writer-wins model that may not meet all business semantics. Select a supported consistency mode and validate requirements explicitly.")
h(266,"RDS MySQL and Beanstalk are the intended managed services, but the source calls a multi-node database/web application 'single-tier' and does not specify database clustering/write topology. Arbitrary multi-node MySQL deployments are not automatically rehosted into one RDS instance without changes.","resilient","Managed migration","rds beanstalk")
r(268,"A","secure","Encryption & key management","KMS exposes managed cryptographic APIs with centrally controlled key policies, supported rotation and CloudTrail audit integration.",[
"KMS provides the central key-management and cryptographic API service, with permissions, supported automatic key-material rotation and auditable use.",
"ACM manages certificates for TLS integrations; it is not a general data-encryption/decryption API.",
"API Gateway and STS provide APIs/temporary credentials, not the requested centrally managed cryptographic-key service.",
"IAM access keys authenticate AWS API requests; they are not the data-encryption keys or rotation service."],"kms kmspolicy",note="Automatic rotation depends on the KMS key type/origin and changes key material, not existing ciphertext or an application's data-encryption key automatically.")
r(269,"C","cost","Object storage classes","Intelligent-Tiering moves eligible objects among access tiers according to usage, while its non-archive tiers retain millisecond access.",[
"One Zone-IA stores in one AZ and has retrieval charges; fixed infrequent-access placement does not adapt to changing hot/cold patterns.",
"Standard-IA does not automatically promote hot objects or change tiers to match unpredictable access and charges for retrieval.",
"Intelligent-Tiering automatically adjusts eligible object access tiers, fitting uncertain patterns without application-level classification.",
"Analytics and lifecycle rules require choosing transition rules and do not provide the same automatic access-responsive tier changes."],"s3",note="Do not enable optional asynchronous Archive Access tiers when millisecond retrieval is required. Account for object monitoring fees and the sub-128-KB monitoring threshold.")
r(270,"B","performance","HPC networking","A cluster placement group trades AZ/hardware separation for tight placement intended for high-throughput low-latency inter-instance traffic.",[
"Partition placement separates groups onto different hardware partitions for resilience; it is not the most tightly colocated low-latency placement choice.",
"Cluster placement places supported instances close together within one AZ to optimize tightly coupled communication.",
"Spread placement separates instances across distinct hardware, prioritizing fault isolation over closest physical placement.",
"Enhanced networking is an instance/network-interface capability, not a placement group strategy type."],"placement efa")
r(271,"BD","performance","Session state storage","Externalize session state so web/app instances can scale independently. DynamoDB provides durable keyed records; ElastiCache provides low-latency in-memory access with appropriate availability design.",[
"CloudWatch is for monitoring/logs, not the application's scalable session-state datastore.",
"DynamoDB can store keyed session/cart records with managed scale, durability and expiration through an appropriate TTL design.",
"A load balancer can distribute or stick requests, but is not itself the shared persistent session datastore.",
"ElastiCache can supply very low-latency shared state, with supported replication/serverless scaling/availability configured for the requirements.",
"Storage Gateway bridges hybrid storage interfaces, not a purpose-built application session key-value store."],"dynamo",note="An evictable cache should not be the sole durable record for critical shopping-cart data unless the selected design explicitly meets its persistence/recovery needs.")
h(272,"The question relies on legacy cross-account object ownership/ACL assumptions and asks for exactly two choices despite incomplete object-owner permissions. Modern bucket-owner-enforced ownership disables ACLs. A private S3 origin with CloudFront/OAC is a more controlled public-delivery design.","secure","Object ownership","s3 cloudfront")
r(273,"C","resilient","Shared file storage","FSx for Windows provides a native managed Windows filesystem with SMB/AD features for Windows application migration.",[
"WorkSpaces provides managed desktops, not the managed shared Windows filesystem service.",
"EFS exposes NFS semantics and is not native Windows File Server/SMB replacement storage.",
"FSx for Windows supplies managed native Windows file storage, retaining the expected SMB/Windows application interface.",
"File Gateway can expose SMB over S3-backed files, but is not a full equivalent of the managed native Windows filesystem and its features."],"fsxwindows gateway")
r(274,"C","cost","Multi-account billing","Organizations consolidated billing centralizes payment while retaining account-level usage/cost attribution and supported allocation/reporting mechanisms.",[
"A VPC is a networking boundary, not a separate billing account or consolidated-payer mechanism.",
"Control Tower helps establish/govern a landing zone, but Organizations consolidated billing is the underlying payment arrangement requested.",
"Consolidated billing combines payment and eligible discounts while member accounts remain individually identifiable for cost analysis and reporting.",
"Cost Explorer visualizes allocated costs; it does not itself create a consolidated account-payment relationship."],"orgbilling")
r(275,"A","performance","High-performance file storage","Managed FSx for Lustre combines a parallel POSIX-oriented HPC filesystem with S3 data repository integration.",[
"FSx for Lustre is the managed parallel filesystem with native S3 import/export integration targeted by the HPC dataset requirements.",
"A self-managed Lustre-on-EBS stack leaves cluster/filesystem operations to the team rather than meeting the fully managed requirement.",
"Combining EBS volumes does not on its own supply a managed shared parallel filesystem or S3 repository integration.",
"A Marketplace AMI can install software but still requires managing the filesystem servers and availability."],"lustre")
r(276,"AB","secure","Private content delivery","Protect the origin and the viewer independently: OAC authorizes CloudFront-to-S3; signed URLs/cookies authorize paying viewers to CloudFront.",[
"OAC with a scoped S3 bucket policy prevents direct public origin access while allowing the intended CloudFront distribution.",
"Signed URLs/cookies grant time-limited viewer access after the application verifies purchase entitlement.",
"Direct S3 presigned URLs can authorize downloads but skip the requested low-latency global CDN caching layer.",
"Making the bucket public permits bypassing the premium content authorization architecture and does not keep the origin private.",
"Global Accelerator is not a direct front end for an S3 website endpoint and does not supply this CDN private-content authorization model."],"cloudfront",note="OAC uses the S3 REST origin, not an S3 static website endpoint. Neither OAC nor signed cookies independently implements application subscription billing/authentication.")
r(277,"A","cost","Private network connectivity","For two non-overlapping VPCs with no transitive-routing requirement, peering is a direct private connectivity option without a Transit Gateway hub.",[
"VPC peering provides direct private routing between the two VPCs; update routes and access controls on both sides.",
"Transit Gateway is useful for a larger hub-and-spoke network, but adds attachment/processing infrastructure and cost for only this pair.",
"VPN tunneling adds gateways, tunnel management and processing for connectivity available natively through peering.",
"NAT translates addresses and does not establish the required bidirectional private peering relationship by itself."],"peering",note="Peering requires non-overlapping address ranges and is not transitive. Cross-account acceptance, DNS resolution settings and both VPCs' routes/security controls need configuration.")
r(279,"AC","performance","Global object delivery","CloudFront optimizes viewer downloads with edge caching, while S3 Transfer Acceleration can improve long-distance direct object transfer paths.",[
"CloudFront caches popular video content close to viewers and reduces repeated long-distance origin downloads.",
"VPC endpoints are for private service access, not global public-client CDN acceleration across Regions.",
"Transfer Acceleration uses accelerated edge paths for S3 transfers, useful for suitable distant upload/download clients after testing.",
"Larger application EC2 instances do not fix client-to-S3 geographic latency, especially when transfers are directly to S3.",
"Cross-Region replication adds replication, routing and consistency considerations instead of the minimal-change CDN/acceleration combination offered."],"cloudfront transferaccel",note="Benchmark Transfer Acceleration for actual client locations and file sizes and account for its additional charges; it is not always faster or cheaper.")
r(280,"C","resilient","Network availability","A single zonal NAT gateway can make all AZs' outbound access depend on the gateway's AZ even when the application fleet is multi-AZ.",[
"Instances in unaffected AZs are stated to remain healthy; their loss of egress follows the shared route target.",
"The ALB handles inbound application requests and does not provide the private instances' outbound NAT path.",
"All private routes depend on the one zonal NAT gateway in us-east-1a, so that AZ failure removes outbound connectivity for the other AZs too.",
"Auto Scaling manages compute capacity, not replacement of the shared NAT gateway route target during this network failure."],"nat")
r(281,"A","performance","Compute scaling","Target tracking manages scaling to keep a proportional metric such as average CPU near the chosen target value.",[
"Target tracking fits 'maintain average CPU at 60%' and manages the associated scaling decisions around that target.",
"Step scaling maps alarm breach sizes to chosen capacity changes; it does not directly express one utilization target in the same way.",
"Simple scaling applies a configured adjustment on an alarm and cooldown; it is not the most direct target-maintenance policy.",
"Scheduled scaling follows time-based actions rather than continuously reacting to actual CPU utilization."],"tracking")
r(282,"B","cost","Compute scaling","A predictable daily load window is a good fit for scheduled scale-out before the window and scale-in after it.",[
"Migrating an existing EC2 application to Lambda is a separate redesign and not necessary to implement the known daily capacity schedule.",
"Scheduled actions adjust capacity ahead of the known promotion and afterward without a daily manual operation.",
"High CPU thresholds react after load increases, potentially leaving users waiting during new-instance startup.",
"A daily manual DesiredCapacity change is operationally fragile and unnecessary when a native schedule is available."],"scheduled")
r(283,"B","resilient","Cross-Region backups","An EBS snapshot is regional; copy it into the destination Region using the native snapshot-copy operation to establish an independent recovery artifact.",[
"A source volume snapshot is first created in the volume's Region; a cross-Region copy is the native way to place a copy elsewhere.",
"Copying the snapshot directly to ap-south-1 supplies the required additional regional copy without launching compute.",
"EBS-managed snapshot storage is not a customer S3 bucket on which you configure S3 CRR rules.",
"Launching a new instance adds cost and an unnecessary recovery/re-snapshot sequence when direct snapshot copy is supported."],"ebs",note="Encrypted copies require a usable destination-Region KMS key and appropriate permissions. Monitor copy completion and retention in both Regions.")
r(284,"ACD","resilient","Monitoring & alerting","Use ALB CloudWatch metrics for request volume and target-response latency, with SNS alarm actions for notification.",[
"Two metric alarms and an SNS action implement native threshold detection and notification without writing a custom log scanner.",
"Polling access logs introduces delayed delivery, custom code and extra processing when the needed managed metrics are already available.",
"Use RequestCount with the appropriate Sum statistic over 60 seconds to detect more than 1,000 requests per minute.",
"Use TargetResponseTime with the required statistic (Average for this wording) and threshold to detect backend response latency.",
"CloudTrail audits management API calls, not every ALB viewer request or the target response-time metric."],"cloudwatch alb",note="Choose periods/evaluation windows deliberately. CloudWatch alarms are near-real-time operational signals, not a guarantee of instantaneous notification.")
h(285,"Deleting the current delete marker restores the previous version as the current object; a version-specific GET can also retrieve existing data. Because the source asks for one action but also offers that valid retrieval statement, its wording needs a clearer restore-versus-download distinction.","resilient","Object recovery","versioning")
r(286,"D","resilient","DNS failover","A regional ALB cannot front another Region. Use Route 53 health-aware failover between independent regional deployments.",[
"One ALB is regional and does not route directly across regional ALB deployments as a global failover controller.",
"Multi-AZ routing inside one Region does not satisfy recovery from loss of the entire primary Region.",
"Creating backup resources in another AZ still leaves the system dependent on the same Region and does not implement global traffic switching.",
"Route 53 failover records with appropriate health checks switch DNS answers to the healthy secondary regional endpoint."],"routing dr",note="Client DNS caches, application state and regional readiness affect the real recovery time. Test failover and failback instead of assuming DNS policy alone is sufficient.")
h(287,"Presigning individual multipart UploadPart operations is the right concept, but a presigned POST/PUT URL does not have a switch that enables the multipart protocol. The backend must create the upload, sign part requests and complete/abort it. The offered option conflates distinct upload methods.","secure","Direct object uploads","presign s3limits")
h(288,"A Cognito authorizer validates tokens, but group claims alone do not automatically implement per-method authorization. Supported scopes/resource-server configuration or additional authorization logic is needed; that missing step matters for the promised fine-grained policy.","secure","API authorization","cognito")
h(289,"SNS-to-SQS plus per-queue DLQs is a good design, but EventBridge-to-SQS plus those DLQs can also meet these requirements. The exact TWO formulation leaves an additional valid routing alternative.","resilient","Messaging & integration","sns sqs")
r(290,"A","secure","Remote administration","Session Manager provides an interactive managed channel without opening inbound SSH or running a public bastion, with supported session auditing/logging configuration.",[
"Session Manager uses the SSM agent and authorized service channel, supporting shell access without inbound port 22 and optional CloudWatch/S3 session logging.",
"A public bastion adds public infrastructure and still relies on an SSH path to targets, contrary to the stated constraints.",
"Pushing temporary SSH keys does not remove the requirement for an SSH network path/port to the instance.",
"Moving SSH to another port does not remove inbound remote-shell exposure and is not equivalent to an auditable managed SSM session."],"sessionmanager",note="Install/configure the SSM agent, instance role, network endpoints and logging permissions. SSH/port-forwarding sessions through SSM do not provide the same command-content logging as ordinary supported shell sessions.")
h(291,"This upload shows DNS dashboard records rather than an exam question. It is preserved as a source attachment and excluded from the study pool.","performance","Source attachment","dns")
r(292,"C","resilient","Infrastructure automation","CloudFormation supplies declarative versionable templates, change sets and stack lifecycle management across supported AWS resources.",[
"Beanstalk manages application environments, but CloudFormation is the general infrastructure template/change-set service for the listed resource types.",
"An AMI captures a machine image, not the complete VPC, database, IAM and load-balancer resource stack.",
"CloudFormation declares the infrastructure and exposes stack/change-set operations for repeatable deployments and review of planned changes.",
"An EBS snapshot captures block data, not the complete application infrastructure configuration."],"cfnfull",note="Rollback behavior depends on operation/resource state and retention policies; test deployment recovery and avoid assuming every external side effect is reversible.")
FIXES[294] = {"option": {2: "Use curl with an IMDSv2 token to query instance metadata at http://169.254.169.254/latest/meta-data/."}}
r(294,"C","secure","Instance metadata","Instance metadata exposes local-ipv4 and, when assigned, public-ipv4. Query it with IMDSv2 token authentication rather than assuming the OS NIC sees the public NAT-mapped address.",[
"OS interface tools show guest interface addresses but do not reliably expose the externally mapped public IPv4 address.",
"CloudTrail records API activity; it is not the low-overhead per-instance metadata lookup endpoint.",
"The metadata service provides the instance's local/public address fields; use the correct path and an IMDSv2 token header.",
"User data contains launch-supplied bootstrap data, not the standard live instance address metadata fields."],"metadata publicip")
r(295,"C","resilient","Infrastructure automation","CloudFormation Outputs exposes values such as an ALB DNSName for humans, exports and downstream automation after stack operations.",[
"Resources declares what to create; it does not by itself expose selected values as stack outputs.",
"Parameters are inputs supplied to a stack, not the computed return values from created resources.",
"Declare an output value using the ALB DNSName attribute so stack outputs expose the resulting endpoint.",
"Mappings are static lookup tables used by a template, not the section for publishing created resource attributes."],"cfnoutputs")
